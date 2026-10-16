#!/usr/bin/env python3
"""Print a layout-only apply_patch for the chapter's display equations.

Derivations use equation/split; genuine multi-column comparisons use aligned.
Independent formulae separated by manual spacing become aligned rows.
Spacing around logical arrows, prose, and enumerations is intentional.
"""

import difflib
from pathlib import Path
import re

from check_chapter_layout import FILES, ROOT, DISPLAY


def outer_tokens(body):
    """Find alignment tabs, row breaks, spacers, and relations outside groups."""
    pattern = re.compile(
        r"\\(?:begin|end)\{[^}]+\}|\\\\(?:\[[^]]*\])?|"
        r"\\(?:qquad|quad|leq|geq|neq|approx|equiv|propto|rightarrow|in)\b|"
        r"\\[{}]|[{}&=]"
    )
    depth, environments, result = 0, 0, []
    for match in pattern.finditer(body):
        token = match[0]
        if token.startswith(r"\begin"):
            environments += 1
        elif token.startswith(r"\end"):
            environments -= 1
        elif token == "{":
            depth += 1
        elif token == "}":
            depth -= 1
        elif depth == 0 and environments == 0:
            result.append(match)
    return result


def align_relation(body):
    relations = [m for m in outer_tokens(body) if m[0] not in {r"\quad", r"\qquad", "&", r"\\"}]
    position = relations[0].start() if relations else 0
    return body[:position] + "&" + body[position:]


def convert(match):
    kind, body = match[1], match[2]
    body = re.sub(r"\\(?:notag|nonumber)\b", "", body)
    # Alignment already supplies the indentation of continuation lines.
    body = re.sub(r"(&\s*)\\q(?:quad|uad)\b\s*", r"\1", body)
    if kind.startswith("align"):
        tabs, maximum = 0, 0
        for token in outer_tokens(body):
            if token[0] == "&":
                tabs += 1
                maximum = max(maximum, tabs)
            elif token[0].startswith(r"\\"):
                tabs = 0
        inner = "aligned" if maximum > 1 else "split"
        outer = "equation*" if kind.endswith("*") else "equation"
        return f"\\begin{{{outer}}}\n\\begin{{{inner}}}" + body + f"\\end{{{inner}}}\n\\end{{{outer}}}"
    if kind.startswith("equation"):
        tokens = outer_tokens(body)
        spacers = [m for m in tokens if m[0] in {r"\qquad", r"\quad"}]
        # No conversion of logical chains or inline explanatory connectors.
        connector = r"\\(?:[a-zA-Z]*[Aa]rrow|Longleftrightarrow|longleftrightarrow|equiv|neq|text|green)\b|[+]"
        chunks = re.split(r"\\(?:qquad|quad)\b", body) if spacers else []
        independent = chunks and all(
            any(m[0] not in {"&", r"\\", r"\quad", r"\qquad"} for m in outer_tokens(chunk))
            for chunk in chunks
        )
        if independent and all(
            not re.match(connector, body[m.end():].lstrip())
            and not re.search(r"\\(?:[a-zA-Z]*[Aa]rrow|Longleftrightarrow|longleftrightarrow|equiv|neq)\s*$", body[:m.start()])
            for m in spacers
        ) and not any(m[0] in {"&", r"\\"} for m in tokens):
            label = re.search(r"\\label\{[^}]+\}", body)
            suffix = "\n  " + label[0] if label else ""
            body = re.sub(r"\\label\{[^}]+\}", "", body)
            chunks = re.split(r"\\(?:qquad|quad)\b", body)
            rows = "\n  \\\\\n  ".join(align_relation(chunk.strip()) for chunk in chunks)
            return f"\\begin{{{kind}}}\n\\begin{{split}}\n  " + rows + "\n\\end{split}" + suffix + f"\n\\end{{{kind}}}"
    return match[0].replace(match[2], body)


def main():
    patch = ["*** Begin Patch"]
    for name in FILES:
        original = (ROOT / name).read_text()
        revised = DISPLAY.sub(convert, original)
        diff = list(difflib.unified_diff(original.splitlines(), revised.splitlines(), n=3, lineterm=""))
        if diff:
            patch.append(f"*** Update File: {ROOT / name}")
            patch += ["@@" if line.startswith("@@") else line for line in diff[2:]]
    patch.append("*** End Patch")
    print("\n".join(patch))


if __name__ == "__main__":
    main()
