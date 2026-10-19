# Chapter-wide notation consistency

18 October 2026. Baseline for the mathematical comparison: the author's
`fe1d3c7`, including the revised MP2 exposition, removal of the MP2 Laplace
subsection/illustration, and E_H for the Hartree energy in the stationarity
exercise. Those author changes were integrated before continuing this pass.

This is a notation pass, not a new scientific rewrite. It covers both chapter
sources, the glossary, biography source, and LaTeX figure assets. Lecture decks
are reference material and are not edited.

## Convention review

| Family | Chapter convention and action |
| --- | --- |
| Electron/basis counts | N counts electrons and K spatial basis functions; the spin basis has 2K functions. N^alpha/N^beta and the generic N^sigma use superscripts consistently. Unrelated subscripts such as N_sig and core counts are retained. |
| Orbitals and basis functions | phi denotes spatial basis functions, psi spatial MOs, and chi spin orbitals. Made the already spin-including basis in the two general AO exercises explicit as chi_mu^AO; their closed-shell specialization returns to phi_mu. Changed the STO-like HOMO symbol from phi to psi. |
| Spin components | C^sigma now consistently denotes a spin-dependent coefficient matrix. Its adjoint is written with parentheses so that the dagger applies to the entire matrix. Superscript spin labels on spatial orbitals, densities, and orbital energies are retained. |
| Operators versus matrix elements | The UHF equations now use the same hh/hf/chJ/chK hatted commands as the general derivation. Scalar h_ij, J_ij, K_ij remain matrix elements, not operators. The introductory spin operators use chS. Direction hats on unit vectors are not operator hats and are unchanged. |
| AO versus MO matrices | The AO core-Hamiltonian matrix is bH in every formulation, including GHF. F_{mu nu}/bF are AO Fock representations; f_pq/bff are MO representations. The latter distinction is added to the glossary. |
| Orbital energies and multipliers | epsilon_p is a canonical orbital energy. The Hermitian occupied-space multiplier matrix bepsilon becomes diagonal under canonicalization; bE is the full diagonal orbital-energy matrix in the finite-basis equations. These defined roles are retained rather than conflated. |
| RHF/UHF/GHF densities | RHF P is spin summed; UHF P^alpha/P^beta count each occupied spin orbital once, and their sum/difference are P^T/P^S. GHF's full spinor density is mathcal P; its Pauli charge block P is half the spin-summed charge density. No density or factor of two is renamed or altered. |
| Integral conventions | Physicists' <ij|kl> and chemists' (ik|jl) retain their exact index conversion. Antisymmetrized double bars retain the direct-minus-exchange definition. Primitive square and contracted round brackets retain their Gaussian-integral context. Real-orbital versus complex-orbital symmetries are unchanged. |
| Conjugation and determinant phases | A star means conjugation; dagger means Hermitian adjoint. Barred psi is the beta-spin partner, not conjugation; the glossary now states this. Fermionic substitution phases and all signs are unchanged. |
| Energies and particle labels | Electronic HF energies exclude the nuclear constant unless explicitly stated. IP/EA signs and electron-number superscripts are retained. The author's new E_H Hartree contribution is distinguished from the isolated-H energy E_H in the dissociation example by context in the glossary. |
| SCF, DIIS, MOM | Iteration and history indices remain local. MOM's bO is explicitly an overlap matrix, not the zero block bO elsewhere; the glossary now includes that exception. Overlap weights are not orbital energies. |
| Gaussian functions and recurrences | Exponents, product centers, Cartesian power vectors, shell labels, primitive counts, Boys orders, and recurrence-direction indices retain their stated meanings. K in a local contraction sum counts primitives; this is explicitly scoped. |
| ECPs | The effective potential operator has a hat consistently, both in the one-electron Hamiltonian and its semilocal decomposition. Radial channel functions U_l remain scalar functions. Core charge Q_A remains distinct from atomic population charge q_A. |
| RI and Cholesky | Auxiliary labels, coefficients, metric, and low-rank factors are distinct from orbital coefficients and densities. The full AO-pair ERI matrix and auxiliary metric share V only in their separately stated contexts. Their contractions and indices are unchanged. |

## Author's MP2 removal

No removed MP2 Laplace expression or illustration is restored. Removed the
leftover positive-gap D entry from the glossary and the now-uncited Almlof
reference from the retained bibliography and DOI table. The current MP2
denominator is Delta_{ij}^{ab}=epsilon_i+epsilon_j-epsilon_a-epsilon_b.
The Gaussian ERI derivation still uses its unrelated Laplace representation
of the Coulomb kernel; that original basis/integral material is preserved.

## Verification and limits

`python3 scripts/check_chapter_notation.py --compare-math fe1d3c7` compares
every displayed equation in order against the author's updated baseline.
It permits only the explicit notation equivalences recorded above (operator
hats/commands, bH, spin-component C, the spin-AO name, and the HOMO name).
It does not ignore factors, signs, indices, contractions, or density changes.
The source check separately rejects subscript spin counts, and the notation
check guards against the concrete spelling variants corrected in this pass.
These are lexical safeguards, not a proof that every possible future symbol
change has the intended mathematical meaning.

All other chapter checks remain applicable: float callouts, display/source
conventions, DOI/citation consistency, HF algebra, integral recurrences,
RI/GHF contractions, and MP2 transformations. The existing MP2 numerical
script also retains an independent legacy Laplace-identity test; it does not
insert that material into the chapter. Further reading is unchanged.

Completed results: all seven checks pass; all 607 displays remain in order,
with 11 documented notation-only changes and no other mathematical-token
changes. All 30 figure/table callouts resolve, and all 85 bibliography entries
are cited. The author's MP2 section and stationarity exercise are retained
byte for byte. Full compilation succeeds to 128 pages; the glossary occupies
three pages. Targeted rendered checks cover the glossary and the changed
spin-AO/UHF/GHF passages. No full-document layout audit was undertaken.

## Subsequent exercise additions (19 October 2026)

The author requested three additional exercises after this notation pass.
They add displays without changing any existing chapter text or mathematics.
The equal-display-count comparison against `fe1d3c7` above documents the
18 October checkpoint; it is not the appropriate preservation check for
this expanded chapter. Use `python3 scripts/check_chapter_notation.py` for
the current canonical-notation guard and
`python3 scripts/check_chapter_layout.py --compare-math 33b38c4` to verify
that all 607 pre-exercise displays remain in order and Further reading is
unchanged. A separate exact comparison confirms that removing only the
three exercise addition blocks recovers both `33b38c4` chapter sources
byte for byte, including the author's MP2 and stationarity revisions.
