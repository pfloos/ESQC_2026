#!/usr/bin/env python3
"""Offline checks for float callouts, equation layout, and content preservation.

Use --compare-math REF to check that every display in a Git revision is still
present, in order, modulo layout-only changes. New theorem statements may add
displays, but may not replace or shorten existing derivations.
"""

import argparse
from collections import Counter
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FILES = ("ESQC_Loos_HF_BF_chapter.tex", "ESQC_Loos_BF_chapter_content.tex")
FLOAT = re.compile(r"\\begin\{(figure|table)\*?\}.*?\\end\{\1\*?\}", re.S)
CENTER = re.compile(r"\\begin\{center\}.*?\\end\{center\}", re.S)
DISPLAY = re.compile(
    r"\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}(.*?)\\end\{\1\}", re.S
)


def uncomment(text):
    return re.sub(r"(?<!\\)%[^\n]*", "", text)


def math_tokens(text):
    text = uncomment(text)
    # A box changes emphasis, not the mathematical statement. Remove only
    # its own balanced argument delimiters, never braces belonging to math.
    while match := re.search(r"\\boxed\s*\{", text):
        depth, end = 1, match.end()
        while depth and end < len(text):
            if text[end] in "{}" and text[end - 1] != "\\":
                depth += 1 if text[end] == "{" else -1
            end += 1
        if depth:
            raise ValueError("Unbalanced boxed expression")
        text = text[:match.start()] + text[match.end():end - 1] + text[end:]
    text = re.sub(r"\\label\{[^}]*\}", "", text)
    text = re.sub(r"\\(?:begin|end)\{(?:split|aligned|gathered)\}", "", text)
    text = re.sub(r"\\(?:notag|nonumber|qquad|quad)\b", "", text)
    text = re.sub(r"\\\\(?:\[[^]]*\])?", "", text)
    return re.sub(r"[\s&]+", "", text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compare-math", metavar="REF")
    parser.add_argument("--allow-old-equations", action="store_true")
    args = parser.parse_args()
    sources = {name: uncomment((ROOT / name).read_text()) for name in FILES}
    joined = "\n".join(sources.values())
    floats = [m[0] for m in FLOAT.finditer(joined)]
    inline = [m[0] for m in CENTER.finditer(joined) if r"\captionof{" in m[0]]
    prose = FLOAT.sub("", joined)
    for block in inline:
        prose = prose.replace(block, "")
    errors = []
    for block in floats + inline:
        labels = re.findall(r"\\label\{([^}]+)\}", block)
        if len(labels) != 1:
            errors.append(f"Figure/table needs exactly one label: {labels}")
        elif not re.search(r"\\(?:ref|autoref|cref|Cref)\{" + re.escape(labels[0]) + r"\}", prose):
            errors.append(f"No text callout outside floats: {labels[0]}")
    for match in CENTER.finditer(joined):
        if (r"\begin{tikzpicture}" in match[0] or r"\HtwoOrbitalPlot" in match[0]
                or r"\begin{tabular}" in match[0]) and r"\captionof{" not in match[0]:
            errors.append("Scientific inline diagram/table has no caption")
    labels = Counter(re.findall(r"\\label\{([^}]+)\}", joined))
    errors += [f"Duplicate label: {key}" for key, n in labels.items() if n > 1]
    for key in re.findall(r"\\(?:eqref|ref|autoref)\{([^}]+)\}", joined):
        if key not in labels:
            errors.append(f"Unresolved source label: {key}")
    if not args.allow_old_equations:
        for name, source in sources.items():
            if re.search(r"\\begin\{aligned\}|\\(?:notag|nonumber)\b", source):
                errors.append(f"Legacy equation layout in {name}")
    preserved = 0
    if args.compare_math:
        for name in FILES:
            previous = subprocess.check_output(
                ["git", "show", f"{args.compare_math}:{name}"], cwd=ROOT, text=True
            )
            old = [math_tokens(m[2]) for m in DISPLAY.finditer(uncomment(previous))]
            new = [math_tokens(m[2]) for m in DISPLAY.finditer(sources[name])]
            position = 0
            for index, expression in enumerate(old, 1):
                while position < len(new) and new[position] != expression:
                    position += 1
                if position == len(new):
                    errors.append(f"Display {index} changed or missing in {name}: {expression[:90]}")
                    break
                position += 1
                preserved += 1
            if name == FILES[0]:
                pattern = r"\\section\*\{Further reading\}.*?(?=\\section|\Z)"
                if re.search(pattern, previous, re.S)[0] != re.search(pattern, (ROOT / name).read_text(), re.S)[0]:
                    errors.append("Further reading has changed")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Layout checks passed: {len(floats) + len(inline)} figures/tables labeled and cited in prose")
    if args.compare_math:
        print(f"Preserved all {preserved} original displays and Further reading from {args.compare_math}")


if __name__ == "__main__":
    main()
