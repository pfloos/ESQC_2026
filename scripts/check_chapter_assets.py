#!/usr/bin/env python3
"""Check the consolidated source, minimal figure set and sketch provenance."""
import hashlib
import json
import re
import struct

from chapter_paths import CHAPTER, STEM, required_assets


def main():
    source = CHAPTER / f"{STEM}.tex"
    assert list(CHAPTER.glob("*.tex")) == [source], "Expected one editable chapter TeX source"
    assert not re.search(r"\\(?:input|include)\s*\{", source.read_text()), "Unmerged chapter input"
    used = set(required_assets())
    actual = {p for p in (CHAPTER / "figures").iterdir() if p.is_file()
              and not p.name.startswith(".") and p.name != "README.md"}
    assert used == actual, f"Missing/unused chapter graphics: {used ^ actual}"
    records = json.loads((CHAPTER / "records/portrait-sketch-prompts.json").read_text())
    sketches = {p for p in used if p.name.startswith("sketch-")}
    assert len(records) == len(sketches) == 29, "Expected 29 portrait replacements"
    assert {CHAPTER / item["file"] for item in records} == sketches
    for item in records:
        path = CHAPTER / item["file"]
        data = path.read_bytes()
        assert hashlib.sha256(data).hexdigest() == item["sha256"], path
        assert data[:8] == b"\x89PNG\r\n\x1a\n" and data[25] == 6, f"Not RGBA PNG: {path}"
        assert list(struct.unpack(">II", data[16:24])) == item["dimensions"], path
        assert max(item["dimensions"]) == 600, path
        # Superseded photographs live in Git history, not in the active source
        # tree. Keep an explicit immutable provenance pointer; a source checkout
        # need not contain photographic originals or the full Git history.
        reference = item["reference_source"].split(" (", 1)[0]
        assert reference.startswith("archive/photographic-portraits/"), reference
        assert ".." not in reference.split("/"), reference
        assert re.fullmatch(r"[0-9a-f]{40}", item["reference_revision"]), reference
    print(f"Assets passed: one merged TeX source, {len(used)} required graphics, 29 RGBA sketches with provenance/checksums")


if __name__ == "__main__":
    main()
