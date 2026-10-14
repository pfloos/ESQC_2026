# Electronic Structure Quantum Chemistry — [ESQC 2026](https://www.esqc.org)

<p align="center">
  <img src="fig/front.png" alt="Electronic-structure illustration used on the title slide" width="760">
</p>

<p align="center">
  Lecture material on <strong>Hartree–Fock theory, basis sets, and molecular integrals</strong><br>
  for the 20th European Summer School in Quantum Chemistry (ESQC).<br>
  <sub>6–19 September 2026 · Hotel Torre Normanna, near Palermo, Sicily, Italy</sub>
</p>

## About these lectures

This repository contains the material for Pierre-François Loos's four lectures on Hartree–Fock theory at ESQC 2026. The course develops the theoretical foundations of Hartree–Fock theory and connects them to the finite-basis and self-consistent-field algorithms used in practical electronic-structure calculations.

The material is divided into two complementary slide decks. Most students will only need the PDF files; the LaTeX sources are included for reference.

| Lecture material | Slides | Source | Topics covered |
| --- | --- | --- | --- |
| **Hartree–Fock Theory** | [PDF](ESQC_Loos_HF.pdf) | [LaTeX](ESQC_Loos_HF.tex) | Electronic Hamiltonian and Born–Oppenheimer approximation; antisymmetry and Slater determinants; Hartree–Fock energy; Slater–Condon rules; Fock operator; Roothaan–Hall equations; SCF and DIIS; excited-state SCF and MOM; Koopmans' and Brillouin's theorems; molecular properties; unrestricted Hartree–Fock |
| **Basis Sets & Integrals** | [PDF](ESQC_Loos_BF.pdf) | [LaTeX](ESQC_Loos_BF.tex) | Molecular-orbital expansions; plane-wave, Slater-type, and Gaussian basis functions; common Gaussian basis-set families; basis-set superposition error; effective core potentials; one- and two-electron integrals; Boys functions and recurrence relations; integral screening; direct SCF; resolution of the identity |

Shared illustrations and diagrams are stored in [`fig/`](fig/).

## The textbook chapter

The material from both presentations is also developed as a standalone,
PhD-level textbook chapter, with full sentences, intermediate derivation
steps, worked examples, computational remarks, and the scientific figure
content from the slides, including author-approved native redraws. It uses
the article class, dark green headings, and the
slides' notation and custom commands. Equation punctuation is omitted;
mathematical separators and explicit matrix-multiplication dots are retained.

The main source is [ESQC_Loos_HF_BF_chapter.tex](ESQC_Loos_HF_BF_chapter.tex).
It includes [ESQC_Loos_BF_chapter_content.tex](ESQC_Loos_BF_chapter_content.tex)
and uses [ESQC_Loos_HF_BF_chapter.bib](ESQC_Loos_HF_BF_chapter.bib) for the
bibliography. These files should remain together in the repository root.
The approved editable figure and table fragments are in
[`chapter-figures/`](chapter-figures/); retain that directory when compiling.
The dark-green vector cover is defined in
[`chapter-titlepage.tex`](chapter-titlepage.tex), which must also remain
alongside the main source. It requires no external artwork or new packages.
The bibliography has direct DOI links; article identities and verification
exceptions are recorded in [the reference audit](chapter-reference-audit.md).

### Building the chapter

With TeX Live and latexmk installed, run this from the repository root:

    latexmk -pdf -interaction=nonstopmode -halt-on-error ESQC_Loos_HF_BF_chapter.tex

latexmk runs BibTeX and repeats LaTeX as needed to resolve citations and
cross-references. The resulting PDF is generated locally and is not tracked
in Git. The chapter uses the same scientific/font packages as the slides,
with article-layout packages and natbib for citations; it does not need Beamer.
If a local build still has auxiliary files from the former book class,
remove those with the cleanup command below before rebuilding.

To remove auxiliary build files while retaining the PDF:

    latexmk -c ESQC_Loos_HF_BF_chapter.tex

### Chapter verification records

[The five-pass audit](chapter-audit.md) describes scientific corrections and
editorial decisions. [The slide coverage index](chapter-slide-coverage.md)
maps every active frame of both presentations to the chapter.
Corrections in the chapter do not silently modify the original slides.

The following checks run with Python's standard library from the repository root:

    python3 scripts/check_chapter_source.py
    python3 scripts/check_chapter_references.py
    python3 scripts/check_chapter_integrals.py

They check displayed-equation punctuation, citation/DOI-audit consistency,
and independent numerical tests of OS recurrences, RI projection, and GHF
matrix conventions. The reference script is an offline consistency check,
not an automated test that a publication exists or supports a claim.
Compilation checks supplement these tests; visual/overflow review remains
a separate editorial task.

## Building the slides

You need a reasonably complete [TeX Live](https://tug.org/texlive/) installation with `latexmk`. From the repository root, run:

```bash
latexmk -pdf ESQC_Loos_HF.tex
latexmk -pdf ESQC_Loos_BF.tex
```

The resulting files, `ESQC_Loos_HF.pdf` and `ESQC_Loos_BF.pdf`, are created in the repository root.

To remove the auxiliary files generated during compilation:

```bash
latexmk -c ESQC_Loos_HF.tex
latexmk -c ESQC_Loos_BF.tex
```

The sources use Beamer and several common scientific LaTeX packages, including `amsmath`, `physics`, `mhchem`, `tikz`, `pgfplots`, `libertine`, `newtxmath`, and `algorithmicx`.

## Repository contents

```text
ESQC_2026/
├── ESQC_Loos_HF.pdf   # Hartree–Fock theory slides
├── ESQC_Loos_HF.tex   # Corresponding LaTeX source
├── ESQC_Loos_BF.pdf   # Basis sets and molecular integrals slides
├── ESQC_Loos_BF.tex   # Corresponding LaTeX source
├── ESQC_Loos_HF_BF_chapter.tex       # Standalone chapter main source
├── ESQC_Loos_BF_chapter_content.tex  # Included basis/integral material
├── ESQC_Loos_HF_BF_chapter.bib       # Chapter bibliography
├── chapter-audit.md                  # Five-pass audit record
├── chapter-slide-coverage.md         # Active-slide coverage index
├── chapter-reference-audit.md        # Verified article identities
├── scripts/           # Chapter consistency and numerical checks
├── fig/               # Figures shared by the presentations and chapter
└── README.md           # Course and build information
```

## Feedback

Questions, corrections, and suggestions are welcome. Please [open an issue](https://github.com/pfloos/ESQC_2026/issues) so that they can be tracked and discussed.

## Author

[**Pierre-François Loos**](https://pfloos.github.io/WEB_LOOS)<br>
Laboratoire de Chimie et Physique Quantiques (UMR 5626)<br>
Université de Toulouse, CNRS, UPS — Toulouse, France

The slides and chapter are teaching material and remain under active development.
