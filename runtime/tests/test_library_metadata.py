"""Metadata edits preserve drawing data and reject stale or ambiguous updates."""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from library_metadata import apply_descriptions


class LibraryMetadataTests(unittest.TestCase):
    def source(self, directory):
        path = Path(directory) / "symbols.excalidrawlib"
        document = {"type": "excalidrawlib", "version": 2, "source": "user", "userNote": "preserve",
                    "files": {"image": {"dataURL": "data:image/png;base64,cHJlc2VydmU="}},
                    "libraryItems": [{"id": "first", "name": "NAND", "created": 1, "status": "published",
                                      "elements": [{"id": "a", "type": "line", "x": -12.25, "points": [[0, 0], [-22.12345, 19]],
                                                    "customData": {"svgPathShape": "M 0 0 L 2 3", "gradient": "user rendering source"}}]},
                                     {"id": "second", "name": "NAND", "created": 2, "status": "unpublished",
                                      "description": "human annotation", "elements": [{"id": "b", "type": "rectangle"}]}]}
        path.write_text(json.dumps(document), encoding="utf-8")
        original = path.read_bytes()
        return path, document, original, hashlib.sha256(original).hexdigest()

    def test_exact_id_update_preserves_every_non_description_field(self):
        with tempfile.TemporaryDirectory() as directory:
            path, original_document, raw, digest = self.source(directory)
            receipt = apply_descriptions(path, {"description": "Logic gate symbols",
                                               "items": [{"id": "first", "description": "NAND with a distinct visual outline"}]}, digest)
            updated = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(updated["libraryItems"][0]["description"], "NAND with a distinct visual outline")
            self.assertEqual(updated["libraryItems"][1]["description"], "human annotation")
            updated.pop("description")
            updated["libraryItems"][0].pop("description")
            self.assertEqual(updated, original_document)
            self.assertEqual(Path(receipt["backup"]).read_bytes(), raw)

    def test_stale_source_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path, _, _, digest = self.source(directory)
            path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            latest = path.read_bytes()
            with self.assertRaises(ValueError):
                apply_descriptions(path, {"items": [{"id": "first", "description": "new"}]}, digest)
            self.assertEqual(path.read_bytes(), latest)
            self.assertEqual(list(path.parent.glob("*.metadata-backup")), [])

    def test_name_is_not_an_identity_and_geometry_edits_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path, _, raw, digest = self.source(directory)
            for proposal in [{"items": [{"id": "NAND", "description": "ambiguous"}]},
                             {"items": [{"id": "first", "description": "new", "elements": []}]},
                             {"items": [{"id": "first", "description": "one"}, {"id": "first", "description": "two"}]}]:
                with self.subTest(proposal=proposal), self.assertRaises(ValueError):
                    apply_descriptions(path, proposal, digest)
                self.assertEqual(path.read_bytes(), raw)

    def test_legacy_arrays_are_not_silently_migrated(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "legacy.excalidrawlib"
            path.write_text(json.dumps({"type": "excalidrawlib", "version": 1, "library": [[{"id": "a", "type": "rectangle"}]]}), encoding="utf-8")
            raw = path.read_bytes()
            with self.assertRaises(ValueError):
                apply_descriptions(path, {"items": []}, hashlib.sha256(raw).hexdigest())
            self.assertEqual(path.read_bytes(), raw)


if __name__ == "__main__":
    unittest.main()
