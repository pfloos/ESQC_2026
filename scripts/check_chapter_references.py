#!/usr/bin/env python3
"""Check citation keys and DOI coverage against the manually verified audit.

This is an offline consistency check, not a substitute for checking a DOI's
publisher metadata or reading the source for relevance.
"""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def main():
    bib = (ROOT / "ESQC_Loos_HF_BF_chapter.bib").read_text()
    audit = (ROOT / "chapter-reference-audit.md").read_text()
    sources = [
        ROOT / "ESQC_Loos_HF_BF_chapter.tex",
        ROOT / "ESQC_Loos_BF_chapter_content.tex",
    ]
    errors = []
    entries = {}
    for match in re.finditer(r"@(\w+)\s*\{([^,]+),(.*?)(?=\n@|\Z)", bib, re.S):
        kind, key, body = match.groups()
        if key in entries:
            errors.append(f"Duplicate bibliography key: {key}")
        doi = re.search(r"\bdoi\s*=\s*\{([^}]+)\}", body)
        entries[key] = (kind.lower(), doi.group(1) if doi else None)

    cited = set()
    for source in sources:
        # Ignore LaTeX comments, but retain escaped percent signs.
        text = re.sub(r"(?<!\\)%[^\n]*", "", source.read_text())
        for match in re.finditer(
            r"\\cite\w*\*?(?:\[[^]]*\])*\s*\{([^}]+)\}", text
        ):
            cited.update(key.strip() for key in match.group(1).split(","))
    for key in sorted(cited - entries.keys()):
        errors.append(f"Citation has no bibliography entry: {key}")
    for key in sorted(entries.keys() - cited):
        errors.append(f"Uncited bibliography entry: {key}")

    verified = {}
    for key, doi in re.findall(
        r"^\| \x60([^\x60]+)\x60 \|.*?\| \[[^]]+\]\(https://doi\.org/(.+)\) \|$",
        audit,
        re.M,
    ):
        verified[key] = doi.lower()
    seen_dois = set()
    for key, (kind, doi) in entries.items():
        if kind not in {"article", "incollection"}:
            continue
        if not doi:
            errors.append(f"Article/contributed chapter lacks a DOI: {key}")
            continue
        if verified.get(key) != doi.lower():
            errors.append(f"DOI differs from, or is absent in, audit: {key}")
        if doi.lower() in seen_dois:
            errors.append(f"Repeated article DOI: {doi}")
        seen_dois.add(doi.lower())
    for key in sorted(verified.keys() - entries.keys()):
        errors.append(f"Audit record has no retained bibliography entry: {key}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        f"Reference consistency passed: {len(cited)} cited entries, "
        f"{len(verified)} audited articles/contributed chapters"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
