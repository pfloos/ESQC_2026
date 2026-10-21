#!/usr/bin/env python3
"""Create a minimal, one-TeX submission bundle from the compiled chapter.

No upload is performed. Existing unrelated files are never deleted.
The generated .bbl is included so that the submitted bibliography is stable.
The repository licence and citation metadata accompany redistributed sources.
"""
from pathlib import Path
import re
import shutil
import zipfile

from chapter_paths import ROOT, CHAPTER, STEM, required_assets


def main():
    source = CHAPTER / f"{STEM}.tex"
    text = source.read_text()
    if re.search(r"\\(?:input|include)\s*\{", text):
        raise SystemExit("Submission requires a single self-contained TeX source")
    bbl = CHAPTER / "build" / f"{STEM}.bbl"
    if not bbl.is_file():
        raise SystemExit("Build the chapter before packaging it")
    files = [source, CHAPTER / f"{STEM}.bib", CHAPTER / "chapter-unsrtnat.bst", bbl]
    files.extend(required_assets())
    files.append(ROOT / "LICENSE")
    if (ROOT / "CITATION.cff").is_file():
        files.append(ROOT / "CITATION.cff")
    target = CHAPTER / "submission"
    target.mkdir(exist_ok=True)
    expected = set()
    with zipfile.ZipFile(CHAPTER / "submission.zip", "w", zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in files:
            relative = (Path(path.name) if path == bbl or path.parent == ROOT
                        else path.relative_to(CHAPTER))
            expected.add(relative.as_posix())
            output = target / relative
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, output)
            bundle.write(path, relative.as_posix())
    # Fail loudly rather than silently deleting somebody's additions.
    extra = {p.relative_to(target).as_posix() for p in target.rglob("*") if p.is_file()} - expected
    if extra:
        raise SystemExit(f"Unexpected files in generated submission directory: {sorted(extra)}")
    assert len(list(target.rglob("*.tex"))) == 1
    print(f"Prepared {len(files)} files, exactly one TeX source: {CHAPTER / 'submission.zip'}")
    print(f"Archive size: {(CHAPTER / 'submission.zip').stat().st_size / 1024**2:.1f} MiB")


if __name__ == "__main__":
    main()
