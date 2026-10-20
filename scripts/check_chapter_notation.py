#!/usr/bin/env python3
"""Check canonical notation and, optionally, the documented notation-only diff.

This is a lexical safeguard, not a semantic proof of every equation. The
equivalences below are limited to the explicit changes recorded in the
18--19 October notation audit; they do not identify different density conventions
or interchange physicists'/chemists' integral indices.
"""

import argparse
import re
import subprocess

from check_chapter_layout import DISPLAY, FILES, ROOT, math_tokens, uncomment
from check_chapter_source import spin_population_subscripts


def equivalent_tokens(expression):
    # The author requested one epsilon-matrix command for multipliers,
    # canonical energies, and the GHF spinor energy matrix. This renames
    # those matrices only; their dimensions, blocks, and factors are retained.
    expression = re.sub(r"\\(?:bE|bepsilon)(?![A-Za-z])", lambda _: r"\beps", expression)
    text = math_tokens(expression)
    text = text.replace(r"\boldsymbol{\mathcalE}", r"\beps")
    # One AO core matrix throughout, including the GHF blocks.
    text = text.replace(r"\bh", r"\bH")
    # C_sigma and C^sigma name the same spin-dependent coefficient matrix.
    text = text.replace(r"\qty(\bC^\sigma)^\dagger", r"\bC_\sigma^\dagger")
    text = text.replace(r"\bC^\sigma", r"\bC_\sigma")
    # The old exercises explicitly included spin in phi's local meaning.
    # Their new chi^AO spelling makes that spin basis explicit, without
    # changing coefficients, contraction indices, or the occupied sum.
    for index in (r"\mu", r"\nu", r"\lambda", r"\sigma"):
        text = text.replace(r"\chi_" + index + r"^{\text{AO}*}", r"\phi_" + index + "^*")
        text = text.replace(r"\chi_" + index + r"^\text{AO}", r"\phi_" + index)
    text = text.replace(r"\psi_\text{HOMO}", r"\phi_\text{HOMO}")
    # Operator hats/macros do not change their explicitly defined actions.
    text = re.sub(r"(?<![A-Za-z\\])f\^(\\(?:alpha|beta))",
                  lambda m: r"\hf^" + m[1], text)
    text = re.sub(r"(?<![A-Za-z\\])h(?=\(\\br_1\))", lambda _: r"\hh", text)
    text = text.replace("}{h}{", r"}{\hh}{")
    for symbol in ("J", "K"):
        text = re.sub(r"(?<![A-Za-z\\])" + symbol + r"_i\^(\\(?:alpha|beta|sigma))",
                      lambda m: r"\ch" + symbol + "_i^" + m[1], text)
    text = text.replace(r"\hatU_A", r"\Hat{U}_A")
    text = re.sub(r"(?<![A-Za-z\\])U\^\\text\{ECP\}",
                  lambda _: r"\Hat{U}^\text{ECP}", text)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compare-math", metavar="REF")
    args = parser.parse_args()
    paths = [ROOT / name for name in FILES]
    paths += [ROOT / "chapter-biographies.tex"]
    paths += sorted((ROOT / "chapter-figures").rglob("*.tex"))
    rules = (
        (r"\\bC_\s*(?:\\(?:alpha|beta|sigma)\b|\{\s*\\(?:alpha|beta|sigma)\s*\})",
         "use superscript spin labels on C"),
        (r"\\bh\b", "use bH for the AO core-Hamiltonian matrix"),
        (r"\\hat\s+S(?:_z|\^2)", "use the chapter's chS spin-operator command"),
        (r"\\phi_\\text\{HOMO\}", "use psi for a molecular orbital"),
        (r"\\varepsilon\b", "use epsilon for orbital energies"),
        (r"\\(?:bE|bepsilon)(?![A-Za-z])|\\boldsymbol\s*\{\s*\\mathcal\s*E\s*\}",
         "use beps for multiplier and orbital-energy matrices"),
        (r"(?<![A-Za-z\\])f\^\\(?:alpha|beta)\b", "use hf for a Fock operator"),
        (r"(?<![A-Za-z\\])h\(\\br_1\)", "use hh for the core operator"),
        (r"(?<![A-Za-z\\])[JK]_i\^\\(?:alpha|beta|sigma)\b", "use chJ/chK for orbital operators"),
    )
    errors = []
    for path in paths:
        source = uncomment(path.read_text())
        # Keep unused slide-compatible macro declarations; audit rendered text.
        if r"\begin{document}" in source:
            source = source.split(r"\begin{document}", 1)[1]
        for line in spin_population_subscripts(source):
            errors.append(f"{path.name}: subscript spin population near body line {line}")
        for pattern, message in rules:
            if re.search(pattern, source):
                errors.append(f"{path.name}: {message}")

    checked = changed = 0
    if args.compare_math:
        for name in FILES:
            before = subprocess.check_output(["git", "show", f"{args.compare_math}:{name}"],
                                             cwd=ROOT, text=True)
            after = (ROOT / name).read_text()
            old = [m[2] for m in DISPLAY.finditer(uncomment(before))]
            new = [m[2] for m in DISPLAY.finditer(uncomment(after))]
            if len(old) != len(new):
                errors.append(f"{name}: display count changed ({len(old)} -> {len(new)})")
                continue
            for n, (a, b) in enumerate(zip(old, new), 1):
                checked += 1
                changed += math_tokens(a) != math_tokens(b)
                if equivalent_tokens(a) != equivalent_tokens(b):
                    errors.append(f"{name}: display {n} has a change beyond the documented notation aliases")
            if name == FILES[0]:
                pattern = r"\\section\*\{Further reading\}.*?(?=\\section|\Z)"
                if re.search(pattern, before, re.S)[0] != re.search(pattern, after, re.S)[0]:
                    errors.append("Further reading changed")
    if errors:
        raise SystemExit("\n".join(errors))
    print("Canonical notation checks passed across chapter, biographies, and figure sources")
    if args.compare_math:
        print(f"All {checked} displays retained in order; {changed} use documented notation-only changes")
        print(f"Other mathematical tokens and Further reading are unchanged from {args.compare_math}")


if __name__ == "__main__":
    main()
