# Hartree–Fock Theory, Basis Sets, and Molecular Integrals — ESQC 2026

<p align="center">
  <img src="fig/front.png" alt="Electronic-structure illustration used on the title slide" width="760">
</p>

Lecture slides and a companion textbook chapter by **Pierre-François Loos** for the [20th European Summer School in Quantum Chemistry (ESQC)](https://www.esqc.org), held on 6–19 September 2026 near Palermo, Sicily, Italy.

## Downloads

The [latest release](https://github.com/pfloos/ESQC_2026/releases/latest) provides the compiled chapter, a self-contained chapter source bundle, both slide decks and checksums.

| Material | Download |
| --- | --- |
| Complete chapter | [PDF](https://github.com/pfloos/ESQC_2026/releases/latest/download/Many_Electrons_One_Determinant.pdf) |
| Standalone chapter sources | [ZIP](https://github.com/pfloos/ESQC_2026/releases/latest/download/ESQC_2026_chapter_source.zip) |
| Hartree–Fock slides | [PDF](https://github.com/pfloos/ESQC_2026/releases/latest/download/ESQC_Loos_HF.pdf) |
| Basis sets and integrals slides | [PDF](https://github.com/pfloos/ESQC_2026/releases/latest/download/ESQC_Loos_BF.pdf) |

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

### Reuse for research and teaching

These materials are shared to support **research and teaching**. You are welcome to reuse and adapt the original text, diagrams and lecture materials under the repository's [GNU GPL v3 licence](LICENSE). Please credit Pierre-François Loos and cite the chapter when using the materials.

Third-party images, reproduced material and portrait adaptations remain subject to the individual licences and permissions recorded in the chapter and its [provenance records](chapter/records/). Permission-pending notices are not grants of permission. This reuse invitation does not override third-party terms.

### Citation

Use GitHub's **Cite this repository** button or [CITATION.cff](CITATION.cff) for the preferred chapter citation. The arXiv identifier will be added once available.

> Loos, P.-F. (2026). *Many Electrons, One Determinant: Hartree–Fock Theory, Basis Sets, and Molecular Integrals*. ESQC 2026. [Version 1.0.0](https://github.com/pfloos/ESQC_2026/releases/tag/v1.0.0).

Corrections and suggestions are welcome through [GitHub issues](https://github.com/pfloos/ESQC_2026/issues).

[**Pierre-François Loos**](https://pfloos.github.io/WEB_LOOS)<br>
Laboratoire de Chimie et Physique Quantiques (UMR 5626)<br>
Université de Toulouse, CNRS, UPS — Toulouse, France
