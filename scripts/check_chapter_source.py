"""Check chapter source conventions; --patch prints an apply_patch correction.

Only sentence punctuation at the ends of display lines is removed. Commas in
tuples, argument lists, and the Cartesian-component enumeration are retained.
"""

import argparse
import difflib
import re
from pathlib import Path

FILES = ("ESQC_Loos_HF_BF_chapter.tex", "ESQC_Loos_BF_chapter_content.tex")
DISPLAY = re.compile(r"\\(begin|end)\{(equation\*?|align\*?|gather\*?|multline\*?|displaymath)\}")
SPIN_SUBSCRIPT = re.compile(
    r"(?<![A-Za-z\\])N\s*_\s*(?:\{\s*)?"
    r"(?:\\(?:mathrm|text)\s*\{\s*)?\\(?:alpha|beta|sigma)\b"
)


def spin_population_subscripts(source):
    """Return lines with subscript spin counts; unrelated N subscripts stay valid."""
    source = re.sub(r"(?<!\\)%[^\n]*", "", source)
    return [source.count("\n", 0, match.start()) + 1
            for match in SPIN_SUBSCRIPT.finditer(source)]


def normalized(source):
    lines, display, brace_depth = [], 0, 0
    for line in source.splitlines(keepends=True):
        events = list(DISPLAY.finditer(line))
        if any(m[1] == "begin" for m in events):
            display += sum(m[1] == "begin" for m in events)
        if display and not events:
            depth = brace_depth
            depths = []
            for index, character in enumerate(line):
                depths.append(depth)
                if index and line[index-1] == "\\":
                    continue
                if character == "{":
                    depth += 1
                elif character == "}":
                    depth -= 1
            brace_depth = depth
            # A component tuple followed by a comma continues the enumeration.
            tuple_list = re.search(r"\([^()]*,[^()]*\),\s*\\\\", line)
            if not tuple_list:
                matches = list(re.finditer(r"(?<!\\)[.,;](?=\s*(?:\\(?:notag|nonumber)\s*)?(?:\\\\(?:\[[^]]*\])?)?\s*$)", line))
                for match in reversed(matches):
                    invisible = re.search(r"\\(?:left|right|big|Big|bigg|Bigg)[lr]?$", line[:match.start()])
                    if depths[match.start()] == 0 and not invisible:
                        line = line[:match.start()] + line[match.end():]
        if any(m[1] == "end" for m in events):
            display -= sum(m[1] == "end" for m in events)
        lines.append(line)
    return "".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--patch", action="store_true")
    parser.add_argument("--physics-patch", action="store_true")
    args = parser.parse_args()
    patches = []
    for filename in FILES:
        original = Path(filename).read_text()
        revised = physics_notation(original) if args.physics_patch else normalized(original)
        if original != revised:
            diff = list(difflib.unified_diff(original.splitlines(), revised.splitlines(), n=3, lineterm=""))
            hunks = ["@@" if line.startswith("@@") else line for line in diff[2:]]
            patches.extend([f"*** Update File: {Path(filename).resolve()}", *hunks])
    if args.patch or args.physics_patch:
        if patches:
            print("\n".join(["*** Begin Patch", *patches, "*** End Patch"]))
    elif patches:
        raise SystemExit("Chapter source needs display-punctuation corrections")
    else:
        sources = [Path(name) for name in FILES]
        sources += [Path("chapter-biographies.tex")]
        sources += sorted(Path("chapter-figures").rglob("*.tex"))
        errors = [f"{path}:{line}: use N^alpha/N^beta/N^sigma, not subscript spin counts"
                  for path in sources if path.is_file()
                  for line in spin_population_subscripts(path.read_text())]
        if errors:
            raise SystemExit("\n".join(errors))
        print("Chapter display-punctuation and superscript spin-population conventions passed")


def physics_notation(source):
    # Package matrix commands preserve the original matrix delimiters exactly.
    source = source.replace(r"\begin{pmatrix}", r"\pmqty{")
    source = source.replace(r"\end{pmatrix}", "}")
    source = source.replace(r"\begin{vmatrix}", r"\mdet{")
    source = source.replace(r"\end{vmatrix}", "}")
    tokens = list(re.finditer(r"\\(left|right)(\\[{}]|[()[\].|])", source))
    stack, replacements = [], []
    delimiters = {"(": ")", "[": "]", r"\{": r"\}", "|": "|"}
    for token in tokens:
        if token[1] == "left":
            stack.append(token)
        elif stack:
            opening = stack.pop()
            body = source[opening.end():token.start()]
            # Multirow split delimiters require left/right: a qty argument
            # cannot contain a top-level alignment tab or row boundary.
            if delimiters.get(opening[2]) != token[2] or "&" in body or r"\\" in body:
                continue
            left = "{" if opening[2] == r"\{" else opening[2]
            right = "}" if token[2] == r"\}" else token[2]
            replacements += [(opening.start(), opening.end(), r"\qty" + left),
                             (token.start(), token.end(), right)]
    for begin, end, replacement in sorted(replacements, reverse=True):
        source = source[:begin] + replacement + source[end:]
    return source


if __name__ == "__main__":
    main()
