"""Install a headless drawing client and isolate an SSH reverse tunnel."""
from __future__ import annotations

import base64
import hashlib
import io
import json
import os
import re
import shlex
import subprocess
import sys
import tomllib
import urllib.parse
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "runtime"))
from runtime_config import load_connection, state_directory
from setup_connection import _bridge_probe, _private_write

# Executed by the user's remote Python interpreter; all payloads, including
# credentials, arrive over SSH stdin, never as command arguments.
REMOTE_INSTALL = r'''
import base64,hashlib,io,json,os,pathlib,subprocess,sys,zipfile
payload=json.load(sys.stdin)
home=pathlib.Path.home()
base=home/'.local/share/obsidian-excalidraw-agent-remote'
state=base/'state'; package=base/'package'; record_path=state/'installation.json'
agent=pathlib.Path(os.environ.get('PI_CODING_AGENT_DIR',str(home/'.omp/agent'))).expanduser()
record=json.loads(record_path.read_text()) if record_path.is_file() else {}
def private_write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
    temporary=path.with_name(path.name+'.tmp')
    fd=os.open(temporary,os.O_WRONLY|os.O_CREAT|os.O_TRUNC,0o600)
    with os.fdopen(fd,'w',encoding='utf-8') as output:
        json.dump(value,output,ensure_ascii=False,indent=2);output.write('\n')
    temporary.chmod(0o600);temporary.replace(path)
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
archive=zipfile.ZipFile(io.BytesIO(base64.b64decode(payload['package'])))
files={}
for entry in archive.infolist():
    relative=pathlib.PurePosixPath(entry.filename)
    if relative.is_absolute() or '..' in relative.parts or ':' in entry.filename or entry.is_dir():
        raise ValueError('Invalid package member')
    files[entry.filename]=archive.read(entry)
old_files=record.get('package_files',{})
for relative,content in files.items():
    target=package/relative
    if target.is_file() and target.read_bytes()!=content and old_files.get(relative)!=digest(target):
        raise ValueError('Refusing to overwrite a modified managed runtime: '+relative)
    if target.exists() and not target.is_file():raise ValueError('Runtime destination is not a file')
skill=agent/'skills/obsidian-excalidraw'
skill_files={key[len('skills/obsidian-excalidraw/'):]:value for key,value in files.items() if key.startswith('skills/obsidian-excalidraw/')}
for relative,content in skill_files.items():
    target=skill/relative
    if target.is_file() and target.read_bytes()!=content and record.get('skill_files',{}).get(relative)!=digest(target):
        raise ValueError('Refusing to overwrite a customized or unmanaged Skill: '+relative)
mcp_path=agent/'mcp.json'
mcp=json.loads(mcp_path.read_text()) if mcp_path.is_file() else {'mcpServers':{}}
if not isinstance(mcp,dict) or not isinstance(mcp.get('mcpServers',{}),dict):raise ValueError('Invalid existing MCP configuration')
existing=mcp.get('mcpServers',{}).get('excalidraw-local')
if existing is not None and existing!=record.get('mcp_entry'):
    raise ValueError('Refusing to replace an unmanaged excalidraw-local server entry')
state.mkdir(parents=True,exist_ok=True,mode=0o700)
package.mkdir(parents=True,exist_ok=True,mode=0o700)
for relative,content in files.items():
    target=package/relative;target.parent.mkdir(parents=True,exist_ok=True)
    temporary=target.with_name(target.name+'.tmp');temporary.write_bytes(content);temporary.replace(target)
# Record ownership before dependency installation so a failed pip download can
# be retried without treating our partially installed package as user edits.
partial=dict(record)
partial['package_files']={key:hashlib.sha256(value).hexdigest() for key,value in files.items()}
private_write(record_path,partial)
venv=base/'venv'; python=venv/'bin/python'
if not python.is_file():subprocess.run([sys.executable,'-m','venv',str(venv)],check=True,stdout=sys.stderr)
subprocess.run([str(python),'-m','pip','install','--disable-pip-version-check','--index-url','https://pypi.org/simple',*payload['dependencies']],check=True,stdout=sys.stderr)
connection=payload['connection']
private_write(state/'connection.json',connection)
for relative,content in skill_files.items():
    target=skill/relative;target.parent.mkdir(parents=True,exist_ok=True)
    temporary=target.with_name(target.name+'.tmp');temporary.write_bytes(content);temporary.replace(target)
entry={'type':'stdio','command':str(python),'args':[str(package/'launcher.py'),'serve'],
       'env':{'PYTHONUTF8':'1','EXCALIDRAW_AGENT_STATE_DIR':str(state)},'timeout':180000}
mcp.setdefault('mcpServers',{})['excalidraw-local']=entry
private_write(mcp_path,mcp)
private_write(record_path,{'version':payload['version'],'package_files':{k:hashlib.sha256(v).hexdigest()for k,v in files.items()},
    'skill_files':{k:hashlib.sha256(v).hexdigest()for k,v in skill_files.items()},'mcp_entry':entry})
print(json.dumps({'installed':True,'version':payload['version'],'package_path':str(package),'state_path':str(state),
    'python':str(python),'mcp_path':str(mcp_path),'skill_path':str(skill),'server_name':'excalidraw-local',
    'rendering_location':'host','remote_port':payload['remote_port'],'token_disclosed':False},ensure_ascii=False))
'''


def _host_connection() -> dict[str, Any]:
    connection = load_connection()
    if connection.get("mode") == "remote":
        raise ValueError("Run remote deployment/tunnel on the graphical host, not on the headless client")
    if not _bridge_probe(connection).get("connected"):
        raise ValueError("Start the connected host Obsidian Bridge before deploying remote drawing")
    token = connection.get("bridge_token", "")
    if not re.fullmatch(r"[0-9a-f]{64}", token, flags=re.IGNORECASE):
        raise ValueError("Host Bridge credentials must be generated by drawing_setup connect")
    return connection


def _port(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 1024 <= value <= 65535:
        raise ValueError("Remote port must be an integer between 1024 and 65535")
    return value


def _ssh_config(host: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", host):
        raise ValueError("Use an existing safe SSH host alias")
    resolved = subprocess.run(["ssh", "-G", host], capture_output=True, text=True, check=True)
    fields: dict[str, list[str]] = {}
    for line in resolved.stdout.splitlines():
        parts = line.split(" ", 1)
        if len(parts) == 2:
            fields.setdefault(parts[0], []).append(parts[1])
    destination = state_directory() / "remote" / host / "ssh_config"
    destination.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    lines = ["Host target"]
    mappings = {"hostname": "HostName", "user": "User", "port": "Port",
                "identityfile": "IdentityFile", "proxyjump": "ProxyJump", "proxycommand": "ProxyCommand",
                "hostkeyalias": "HostKeyAlias", "userknownhostsfile": "UserKnownHostsFile"}
    for key, spelling in mappings.items():
        for value in fields.get(key, []):
            if value == "none":
                continue
            if "\n" in value or "\r" in value:
                raise ValueError("Invalid SSH configuration field")
            if key == "identityfile":
                value = '"' + value.replace('"', '\\"') + '"'
            lines.append(f"    {spelling} {value}")
    lines += ["    BatchMode yes", "    ForwardX11 no", "    ExitOnForwardFailure yes",
              "    ServerAliveInterval 30", "    ServerAliveCountMax 3", "    StrictHostKeyChecking yes",
              "    RequestTTY no", "    ControlMaster no"]
    fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as output:
        output.write("\n".join(lines) + "\n")
    return destination


def tunnel_command(host: str, remote_port: int | None = None) -> list[str]:
    """Return a foreground reverse tunnel command without touching user forwards."""
    connection = _host_connection()
    local_port = urllib.parse.urlsplit(connection["bridge_url"]).port
    if local_port is None:
        raise ValueError("Host Bridge URL must include its port")
    port = _port(remote_port if remote_port is not None else local_port)
    config = _ssh_config(host)
    return ["ssh", "-F", str(config), "-N", "-T", "-R",
            f"127.0.0.1:{port}:127.0.0.1:{local_port}", "target"]


def _package_archive() -> bytes:
    paths = [ROOT / name for name in ("launcher.py", "setup_connection.py", "remote_control.py", "pyproject.toml", "uv.lock")]
    paths += [path for folder in ("runtime", "skills/obsidian-excalidraw") for path in (ROOT / folder).rglob("*")
              if path.is_file() and "__pycache__" not in path.parts and path.suffix in (".py", ".md")]
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in paths:
            archive.writestr(path.relative_to(ROOT).as_posix(), path.read_bytes())
    return stream.getvalue()


def deploy_remote(host: str, remote_port: int | None = None) -> dict[str, Any]:
    """Provision a remote headless MCP and full Skill; never expose host credentials."""
    connection = _host_connection()
    tunnel = tunnel_command(host, remote_port)
    port = int(tunnel[-2].split(":")[1])
    dependencies = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]["dependencies"]
    remote_connection = {"mode": "remote", "bridge_url": f"http://127.0.0.1:{port}",
                         "bridge_token": connection["bridge_token"], "bridge_timeout": 180,
                         "vault_name": connection.get("vault_name"), "host_vault_path": connection.get("vault_path"),
                         "bridge_script": connection.get("bridge_script"), "remote_host": host}
    payload = {"version": "0.8.0", "package": base64.b64encode(_package_archive()).decode("ascii"),
               "dependencies": dependencies, "connection": remote_connection, "remote_port": port}
    config_path = tunnel[2]
    command = "python3 -c " + shlex.quote(REMOTE_INSTALL)
    result = subprocess.run(["ssh", "-F", config_path, "-T", "target", command],
                            input=json.dumps(payload), capture_output=True, text=True, timeout=600)
    if result.returncode:
        # stderr may include remote interpreter traces; redact the token before reporting.
        detail = result.stderr.replace(connection["bridge_token"], "[REDACTED]")[-3000:]
        raise RuntimeError(f"Remote installation failed ({result.returncode}); package/dependencies may have been partially installed. {detail}")
    receipt = json.loads(result.stdout)
    _private_write(state_directory() / "remote" / host / "deployment.json", receipt)
    return {**receipt, "ssh_host": host, "tunnel_command": tunnel,
            "next": "Run remote-tunnel on this host, then start/reload remote OMP and use excalidraw-local."}
