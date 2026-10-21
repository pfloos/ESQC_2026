# Hartree–Fock Theory, Basis Sets, and Molecular Integrals — ESQC 2026

<p align="center">
  <img src="fig/front.png" alt="Electronic-structure illustration used on the title slide" width="760">
</p>

Lecture slides and a companion textbook chapter by **Pierre-François Loos** for the [20th European Summer School in Quantum Chemistry (ESQC)](https://www.esqc.org), held on 6–19 September 2026 near Palermo, Sicily, Italy.

## Companion chapter

**Many Electrons, One Determinant: Hartree–Fock Theory, Basis Sets, and Molecular Integrals**

The chapter has been submitted to arXiv. Its public link will be added once available.

This PhD-level introduction develops Hartree–Fock theory, finite-basis formulations, self-consistent-field algorithms, basis sets, and molecular integrals. It includes detailed derivations, historical perspectives, computational remarks, and exercises with worked solutions.

- [Complete LaTeX source](chapter/ESQC_Loos_HF_BF_chapter.tex)
- [Bibliography](chapter/ESQC_Loos_HF_BF_chapter.bib)
- [Chapter build and verification instructions](chapter/README.md)
- [Illustration credits and provenance](chapter/records/)

The chapter uses one editable `.tex` file. Its bibliography, reference style and required graphics are contained in [`chapter/`](chapter/); the slide sources are not needed to compile it.

## Lecture slides

| Presentation | Slides | LaTeX source |
| --- | --- | --- |
| Hartree–Fock Theory | [PDF](ESQC_Loos_HF.pdf) | [Source](ESQC_Loos_HF.tex) |
| Basis Sets & Integrals | [PDF](ESQC_Loos_BF.pdf) | [Source](ESQC_Loos_BF.tex) |

The first presentation covers the electronic Hamiltonian, determinants, Hartree–Fock energy and equations, SCF algorithms, excited-state SCF, molecular properties, and unrestricted formulations. The second covers orbital basis families, basis-set superposition error, effective core potentials, molecular integrals, recurrence relations, screening, direct SCF, and resolution of the identity.

Original slide illustrations and editable figure sources remain in [`fig/`](fig/).

## Build locally

A reasonably complete [TeX Live](https://tug.org/texlive/) installation with `latexmk` is required. Run these commands from the repository root.

For the chapter:

```sh
sh scripts/build_chapter.sh
```

The compiled chapter and auxiliary files are generated in `chapter/build/` and are not tracked in Git. To prepare a source package for a future revision, build first and then run:

```sh
python3 scripts/package_chapter.py
```

For the slides:

```sh
latexmk -pdf ESQC_Loos_HF.tex
latexmk -pdf ESQC_Loos_BF.tex
```

The slide PDFs are stored at the repository root. Remove their auxiliary files, while retaining the PDFs, with:

```sh
latexmk -c ESQC_Loos_HF.tex
latexmk -c ESQC_Loos_BF.tex
```

## Repository layout

```text
ESQC_2026/
├── ESQC_Loos_HF.tex / .pdf   # Hartree–Fock slides
├── ESQC_Loos_BF.tex / .pdf   # Basis-set and integral slides
├── chapter/                 # Single-source chapter, bibliography and style
│   ├── figures/             # Required illustrations and portrait sketches
│   └── records/             # Reference verification and illustration provenance
├── fig/                     # Original slide assets
└── scripts/                 # Build, packaging, checks and cover regeneration
```

Development drafts, superseded photographs and earlier review files have been removed from the working tree; they remain recoverable through Git history. Current credits, portrait-generation records and scientific cover data are retained.

## Credits and feedback

See [LICENSE](LICENSE) and the individual third-party credits recorded in the chapter and its [provenance records](chapter/records/). This cleanup does not change those credits or permission statuses.

Corrections and suggestions are welcome through [GitHub issues](https://github.com/pfloos/ESQC_2026/issues).

[**Pierre-François Loos**](https://pfloos.github.io/WEB_LOOS)<br>
Laboratoire de Chimie et Physique Quantiques (UMR 5626)<br>
Université de Toulouse, CNRS, UPS — Toulouse, France
