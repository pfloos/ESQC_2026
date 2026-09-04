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
├── fig/               # Figures shared by the presentations
└── README.md           # Course and build information
```

## Feedback

Questions, corrections, and suggestions are welcome. Please [open an issue](https://github.com/pfloos/ESQC_2026/issues) so that they can be tracked and discussed.

## Author

[**Pierre-François Loos**](https://pfloos.github.io/WEB_LOOS)<br>
Laboratoire de Chimie et Physique Quantiques (UMR 5626)<br>
Université de Toulouse, CNRS, UPS — Toulouse, France

These slides are teaching material and remain under active development.
