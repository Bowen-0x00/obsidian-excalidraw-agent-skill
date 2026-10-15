// Compile only: upstream Engines are never executed on a GitHub runner.
import fs from 'node:fs';
import path from 'node:path';

const root = process.argv[2] || '.';
const manifest = JSON.parse(fs.readFileSync(path.join(root, 'bridge/shared-scripts.json'), 'utf8'));
const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;
for (const file of manifest.files) {
  const source = fs.readFileSync(path.join(root, file.target), 'utf8');
  const body = source.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '');
  try {
    new AsyncFunction('ea', 'utils', body);
  } catch (error) {
    throw new Error(`${file.target}: ${error.message}`);
  }
}
console.log(`Syntax checked ${manifest.files.length} declared shared Engines without executing them.`);
