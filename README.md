# Electronic Structure Quantum Chemistry — ESQC 2026

<p align="center">
  <img src="fig/front.png" alt="Electronic-structure illustration used on the title slide" width="760">
</p>

<p align="center">
  Lecture slides on <strong>Hartree–Fock theory, basis sets, and molecular integrals</strong><br>
  prepared for the 2026 European Summer School in Quantum Chemistry (ESQC).<br>
  <sub>6–19 September 2026 · Hotel Torre Normanna, near Palermo, Sicily, Italy</sub>
</p>

## Lecture material

The repository contains two complementary Beamer presentations:

| Lecture | Source | Main topics |
| --- | --- | --- |
| **Hartree–Fock Theory** | [`ESQC_Loos_HF.tex`](ESQC_Loos_HF.tex) | The electronic problem, antisymmetry, Slater determinants, the Hartree–Fock energy, Slater–Condon rules, the Fock operator, Roothaan–Hall equations, SCF, Koopmans' theorem, and unrestricted Hartree–Fock |
| **Basis Sets & Integrals** | [`ESQC_Loos_BF.tex`](ESQC_Loos_BF.tex) | Molecular-orbital expansions, Gaussian and plane-wave basis sets, one- and two-electron integrals, Boys functions, ERI screening and recurrence relations, and resolution-of-the-identity techniques |

The shared illustrations and diagrams are stored in [`fig/`](fig/).

## Building the slides

A reasonably complete TeX Live installation is recommended. From the repository root, build either deck with `latexmk`:

```bash
latexmk -pdf ESQC_Loos_HF.tex
latexmk -pdf ESQC_Loos_BF.tex
```

To remove the auxiliary files generated during compilation:

```bash
latexmk -c ESQC_Loos_HF.tex
latexmk -c ESQC_Loos_BF.tex
```

The sources use Beamer together with standard scientific LaTeX packages, including `amsmath`, `physics`, `mhchem`, `tikz`, `libertine`, `newtxmath`, and `algorithmicx`.

## Repository structure

```text
ESQC_2026/
├── ESQC_Loos_HF.tex   # Hartree–Fock theory
├── ESQC_Loos_BF.tex   # Basis sets and molecular integrals
├── fig/               # Figures used by both presentations
└── README.md
```

## Author

**Pierre-François Loos**<br>
Laboratoire de Chimie et Physique Quantiques (UMR 5626)<br>
Université de Toulouse, CNRS, UPS — Toulouse, France

These slides are teaching material and remain under active development. Corrections and suggestions are welcome through the repository's issue tracker.
