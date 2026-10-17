# Scientific consistency and editorial audit

17 October 2026. Baseline: author's `faf8986` ("up to 2").

## Scope and preservation

This pass covers the existing HF, basis-set, and integral material. It does
not add the MP2 or AO-to-MO sections mentioned in the author's backlog.
All derivations, examples, exercise/solution pairs, illustrations, and
numerical tables are retained. Further reading, biographies, bibliography,
cover, and semantic color conventions are unchanged. Substantive displayed
mathematics is not corrected silently: the proposed replacements below await
the author's approval. Prose can clarify the assumptions of an unchanged
formula without introducing a new topic.

The source-preservation check counts 583 equation/align displays in the two
chapter sources at this baseline. Numerical tests below exercise selected
identities independently; they are not a proof of every displayed equation
or a new set of ab initio molecular calculations.

## Review coverage

| Material | Checks and outcome |
| --- | --- |
| Clamped nuclei and Born--Oppenheimer separation | Electronic versus total energy; fixed-geometry convention; omitted derivative terms. Nuclear equation assumes omission of the diagonal derivative correction as well as inter-state coupling. |
| Antisymmetry and determinants | Normalization-weighted antisymmetrizer matches the author's requested normalized determinant, and is correctly distinguished from an idempotent projector. Equal coordinate probabilities alone do not establish a constant exchange phase; the state-ray assumption needs explicit wording. |
| Energy functional and few-electron examples | Pair counting, same-spin self-interaction cancellation, spin selection, RHF factors of two, and Li/B occupation patterns are consistent. |
| Integral notation and Slater--Condon rules | Physicists'/chemists' index conversion and complex conjugation; excitation phases and nonzero matrix elements. Eightfold symmetry requires real orbitals, not just real numerical integral values. |
| Spin symmetry and spin-adapted singles | Spin-contamination convention and the relative signs of the singlet/triplet combinations checked. The two-open-shell-electron picture suppresses the common closed-shell core. Local spatial-MO symbols should be regularized: proposal M2. |
| Variation, canonicalization, orbital energies | Constrained versus unrestricted stationarity; occupied-space unitary invariance is invariance of the physical state, not of its arbitrary overall phase. Orbital-energy double counting is consistent. |
| Koopmans and MP partition | Removal/attachment signs and both exact relaxation/correlation decompositions checked. Relaxation inequalities require a variational space containing the frozen determinant. The auxiliary reference eigenvalue is a ground-state eigenvalue only for appropriate Aufbau occupation. |
| Finite basis and AO contractions | Overlap metric, density trace order, RHF exchange factor, and electronic-energy trace checked. The general spin-orbital exercise needs its spin-including basis scope stated. An intermediate bra expansion has a double conjugation: M1. A remaining omitted matrix dot is M3. |
| SCF, DIIS, MOM | Fixed-point versus stability distinction, DIIS constraint/signs/history count, and MOM overlap weights checked. Aufbau ordering alone does not guarantee convergence or a global minimum; MOM is an occupation-following procedure, not a guarantee of a higher state. |
| Properties and localization | Density normalization and trace contraction, population conventions, occupied-space invariance, and directions of localization optimizations checked. Complex extensions of the printed Mulliken formulas need care; the population/localization formulas are presented for real AOs and coefficients. |
| UHF, H2, GHF, classification | Same/opposite-spin pair counts, Pople--Nesbet contractions, H2 curvature and spin contamination, spin/AO block ordering, and nested-space variational inequalities checked. Angle-dependent H2 energies omit the nuclear constant, unlike the preceding total RHF expression. GHF's charge block is half the spin-summed density, as already stated. |
| Basis sets, extrapolation, counterpoise, ECPs | Primitive/contraction counts, Cartesian/spherical shell counts, nested-space assumptions, HF versus correlation extrapolation, ghost-basis inequalities, and ECP charge/core counts checked. Angular ECP corrections must be understood relative to the local channel. Counterpoise removes a basis imbalance, not every interaction-energy error. |
| Gaussian integrals, screening, RI/CD | Product centers/prefactors, one-electron formulas, Laplace reduction, Boys orders/limits, VRR signs, HRR/contraction sequence, real-AO scope, Coulomb metric and rank assumptions checked. Screening thresholds control discarded contributions; an integral threshold alone is not a bound on accumulated energy error. |

## Proposed displayed-equation corrections — awaiting approval

### M1. AO-energy derivation: conjugation inside a bra

Location: solution **AO Hartree--Fock energy**, the expansion immediately
before `eq:hf-energy-matrix` in `ESQC_Loos_HF_BF_chapter.tex`.

The first argument of `\mel{...}{...}{...}` denotes a ket whose adjoint is
taken to form the bra. Therefore

```latex
\mel{\sum_\mu C_{\mu i}^*\phi_\mu}{\hh}
    {\sum_\nu C_{\nu i}\phi_\nu}
```

conjugates the first coefficient twice. Proposed replacement:

```latex
\mel{\sum_\mu C_{\mu i}\phi_\mu}{\hh}
    {\sum_\nu C_{\nu i}\phi_\nu}
```

Likewise remove the stars from the two coefficients **inside the bra
argument only** in the next two-electron expansion. Keep the stars in
explicit scalar contractions and density definitions. Keep every intervening
step. The final density-trace formula is already correct.

Evidence: for the normalized complex vector used by
`scripts/check_chapter_hf_algebra.py`, the Hermitian expectation is
`-0.29012215`, whereas the double-conjugated expression gives
`-0.42292741 + 0.28391233 i`. The independent trace contraction agrees with
the correct expectation. This is an actual error for complex coefficients,
not merely a stylistic preference. The developers'
[PySCF HF implementation](https://pyscf.org/_modules/pyscf/scf/hf.html) supplies a separate primary
implementation check of the density/energy contraction convention.

### M2. Spatial molecular-orbital symbols in the spin-adaptation illustration

Location: paragraph **Spatial and spin symmetry** in the spin-adapted-singles
subsection. The singlet and triplet two-electron factors use `\phi_i` and
`\phi_a`, although the chapter reserves `\phi_\mu` for AOs and `\psi_p`
for spatial MOs. Proposed replacement: use `\psi_i` and `\psi_a` in these
two displays, without changing normalization, signs, or the suppressed-core
convention. This is notation regularization, not a change to spin adaptation.
For now, the prose explicitly identifies these as spatial MOs.

### M3. Explicit matrix multiplication dots

Location: **Reduction to an ordinary eigenvalue problem**, the intermediate
equation containing `\bF'\bC' = \bC'\bE`.
Proposed replacement: `\bF'\cdot\bC' = \bC'\cdot\bE`.
This restores the author's requested explicit matrix-product notation and
does not alter the algebra. It is listed rather than applied here so that
the unchanged-display baseline remains exact during this audit.

## Prose clarifications and continuity pass

The accompanying editorial revision makes the assumptions in the coverage
table explicit, adds short bridges at changes of representation, and removes
unnecessary repetition in narrative summaries. It does not reorder sections
or remove derivation steps. Specific safeguards include:

- The exchange-phase argument states the pure-state-ray assumption before
  the unchanged implication; probability equality alone would permit a
  coordinate-dependent phase. Pauli's own
  [Nobel lecture](https://www.nobelprize.org/prizes/physics/1945/pauli/lecture/) is primary
  historical context for the symmetry assumption, not a derivation from
  equal coordinate probabilities.
- Real-*orbital* eightfold symmetry is distinguished from real integral
  *values*. The chapter's own periodic plane-wave expression supplies a
  counterexample: with momenta `(0,3;1,2)` the scaled physicists' ERI is 1,
  but the extra permutation `(1,3;0,2)` is zero. Both values are real.
- The AO spin-orbital exercise temporarily includes spin in its basis label;
  the later RHF formulas return to the spin-summed spatial density. The
  separately derived GHF notation remains unchanged.
- Phase-invariance statements refer to the physical state. Koopmans
  comparisons keep the geometry and one-electron space fixed and identify
  the variational assumption behind relaxation bounds.
- The MP zeroth-order eigenvalue is described as the reference eigenvalue;
  an Aufbau qualification separates it from non-Aufbau/MOM solutions. The
  [original Moller--Plesset paper](https://doi.org/10.1103/PhysRev.46.618)
  remains the existing chapter reference; no MP2 section is added here.
- H2's rotation polynomial is explicitly electronic; the common `1/R`
  constant is restored when total-energy curves are compared. The separated
  atomic energy is understood in the same finite basis.
- Real-function assumptions delimit Gaussian screening/direct-SCF and
  population/localization formulas; complex spinor densities remain allowed
  in the separately specified GHF contractions. ECP radial channel terms
  are corrections to the local channel in the printed semilocal convention.

## Reproducible checks

Run from the repository root:

```text
python3 scripts/check_chapter_hf_algebra.py
python3 scripts/check_chapter_integrals.py
python3 scripts/check_chapter_layout.py --compare-math faf8986
python3 scripts/check_chapter_source.py
python3 scripts/check_chapter_references.py
latexmk -pdf -interaction=nonstopmode -halt-on-error ESQC_Loos_HF_BF_chapter.tex
git diff --check
```

The new standard-library algebra check covers determinant norms for 2--4
electrons; RHF spin summation; Li/B pair counts; frozen IP/EA signs and exact
decompositions; orbital-energy double counting; complex density trace order;
the two counterexamples above; fermionic phases in the `S^2` matrix of
spin-adapted singles; and H2 curvature/spin contamination. The existing
integral check independently covers 540 recurrence cases, RI projection and
contraction, and complex-density GHF exchange/tensor ordering.

The layout comparison verifies preservation in order of all baseline
equation/align displays and byte-for-byte preservation of Further reading.
It does not certify the scientific correctness of a preserved formula, which
is why M1--M3 remain explicitly listed above.

### Completed verification

All five source/reference/algebra/integral checks above pass. The display
comparison preserves all 583 original displays, and all 30 numbered figures
and tables have prose callouts. All 84 bibliography entries are cited, with
80 audited article/contributed-chapter identities retained. A separate
comparison also confirms that the exercise and solution environments and
figure/table/TikZ environments are unchanged from the baseline.

Full LaTeX/BibTeX compilation succeeds: 122 PDF pages, no undefined citations
or cross-references, and no BibTeX warnings. Targeted rendered-page checks
cover the H2 electronic-versus-total-energy clarification and the Gaussian
normalization/contraction clarification. This was not a full-document
overflow or visual audit. M1--M3 remain proposals, not applied corrections.
