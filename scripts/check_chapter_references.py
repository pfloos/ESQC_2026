#!/usr/bin/env python3
"""Check citation keys and DOI coverage against the manually verified audit.

This is an offline consistency check, not a substitute for checking a DOI's
publisher metadata or reading the source for relevance.
Use --check-bbl after compilation to verify title links and hidden DOI/URL text.
"""

import argparse
from pathlib import Path
import re
import sys


from chapter_paths import ROOT, CHAPTER, STEM, FILES


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-bbl", action="store_true",
                        help="after compilation, verify every rendered title link")
    args = parser.parse_args()
    bib = (CHAPTER / f"{STEM}.bib").read_text()
    audit = (CHAPTER / "records/chapter-reference-audit.md").read_text()
    sources = [ROOT / name for name in FILES]
    errors = []
    entries = {}
    for match in re.finditer(r"@(\w+)\s*\{([^,]+),(.*?)(?=\n@|\Z)", bib, re.S):
        kind, key, body = match.groups()
        if key in entries:
            errors.append(f"Duplicate bibliography key: {key}")
        doi = re.search(r"\bdoi\s*=\s*\{([^}]+)\}", body)
        url = re.search(r"\burl\s*=\s*\{([^}]+)\}", body)
        entries[key] = (kind.lower(), doi.group(1) if doi else None,
                        url.group(1) if url else None)

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
    for key, (kind, doi, url) in entries.items():
        if not doi and not url:
            errors.append(f"Reference title has no DOI/URL link target: {key}")
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

    if args.check_bbl:
        path = CHAPTER / "build" / f"{STEM}.bbl"
        if not path.exists():
            errors.append("Compile the chapter before checking rendered title links")
        else:
            items = re.findall(
                r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}(.*?)"
                r"(?=\\bibitem|\\end\{thebibliography\})", path.read_text(), re.S)
            rendered = dict(items)
            if len(items) != len(rendered):
                errors.append("Repeated key in the rendered bibliography")
            if set(rendered) != cited:
                errors.append("Rendered bibliography keys differ from the chapter citations")
            for key, block in rendered.items():
                if key not in entries:
                    continue
                _, doi, url = entries[key]
                target = f"https://doi.org/{doi}" if doi else url
                title = block.split(r"\newblock", 1)[-1].lstrip()
                expected = r"\href{" + (target or "") + "}{"
                if not title.startswith(expected) or block.count(r"\href{") != 1:
                    errors.append(f"Expected exactly one title hyperlink to {target}: {key}")
                if re.search(r"\\(?:doi|url)\{|\\newblock\s+(?:doi:|URL\b)", block):
                    errors.append(f"Standalone DOI/URL remains in reference: {key}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        f"Reference consistency passed: {len(cited)} cited entries, "
        f"{len(verified)} audited articles/contributed chapters"
    )
    if args.check_bbl:
        print(f"Rendered references passed: {len(rendered)} linked titles, no standalone DOI/URL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
