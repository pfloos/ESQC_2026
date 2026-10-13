# Chapter audit

This record concerns the chapter, not modifications to the lecture decks.
The active frames of `ESQC_Loos_HF.tex` and `ESQC_Loos_BF.tex` are the
coverage baseline. Commented-out frames are not additional required material.

## Pass 1: scientific questions in the integral section

- Corrected both OS vertical-recurrence product-center signs. Differentiating
  the Boys function gives a minus sign; the slide equations have plus signs.
  The chapter includes a short derivative check so the correction is explicit.
- Checked the bra lowering term, ket lowering term, and mixed bra/ket term
  against independent quadrature of Gaussian conditional moments.
- Clarified that the recurrence formulas apply to unnormalized primitives and
  that the combined VRR/HRR late-contraction strategy is Head--Gordon--Pople.
- Made the real-function assumption and auxiliary-metric invertibility explicit
  in RI. Added residual orthogonality and the equality of fitting one or both
  densities, connecting the least-squares derivation to the factorization.
- Numerical verification: `python3 scripts/check_chapter_integrals.py`.
  The script also checks RI projection and contraction in a nonorthogonal,
  incomplete auxiliary space.

## Pass 2: equations, notation, and physics-package conventions

- Restored explicit `\cdot` in the remaining matrix products, including
  the orthogonalization derivation and its intermediate normalization steps.
- Removed sentence-ending periods, commas, and semicolons from displayed
  equations. Mathematical separators in tuples and sets are retained.
  Invisible `\left.`/`\right.` delimiters remain where a multirow expression
  requires them.
- Converted applicable paired delimiters to `\qty`, explicit matrices to
  `\pmqty`, determinants to `\mdet`, derivatives to `\dv`, and the
  commutator to `\comm`. Existing `\pdv`, `\fdv`, `\dd`, `\abs`, `\norm`,
  `\Tr`, and bra–ket commands are retained. The slides' custom paired
  integral commands are preserved. Delimiters split across alignment rows
  remain explicit because a single `\qty` argument cannot span those rows.
- Restored missing `\quad`/`\qquad` commands and corrected the cc-pVTZ
  shell decomposition's `2s` transcription to `2d`.
- Corrected the STO derivative to include its value at the nucleus, and
  distinguished a cusp-shaped exponential from satisfaction of the actual
  point-nucleus cusp condition.
- Corrected the Boys localization optimization direction and explained
  why minimizing the two spread expressions maximizes centroid separation.
- Verification: source-convention check and full LaTeX/BibTeX compilation.

## Pass 3: fidelity to both lecture presentations

- Reviewed all 100 active HF frame blocks and all 48 active basis/integral
  frame blocks; their chapter destinations are recorded individually in
  `chapter-slide-coverage.md`. Commented-out frames and presentation
  scaffolding are distinguished from the scientific content.
- Checked the normalization, one- and two-electron, spin-to-spatial, and
  atomic worked examples; all Slater--Condon cases; spin adaptation and
  contamination; Koopmans IP/EA energy decompositions; canonicalization;
  AO Fock/energy contractions; SCF, DIIS, and MOM stages; properties;
  localization; UHF/H2; and GHF/classification.
- Checked the basis-family comparisons, shell counts, contraction example,
  ECP operators and families, Gaussian product and one-electron formulas,
  Laplace-transform stages of the ssss derivation, Boys limits/recurrences,
  VRR/HRR stages, numerical screening table, direct SCF, and RI/CD.
- Restored the ghost-basis diagram, the integral-recipe diagram, the explicit
  ten-primitive carbon contraction, and the Gaussian-basis remarks on Pulay
  terms, all-electron practicality, and locality.
- Restored physicists' brackets on the plane-wave ERI derivation, matching
  the slides' actual index grouping. Explained the periodic Coulomb kernel,
  reciprocal-vector relabeling, and the excluded zero-transfer term.
- Corrected DIIS's history sum to contain exactly m stored iterations.
- Corrected GHF's spin/AO tensor-factor ordering and exchange contraction for
  complex density matrices; an independent numerical kernel check verifies
  the latter. Distinguished the half-charge GHF block from the full density.
- Qualified monotonic basis improvement to nested variational spaces and
  corrected the claim that all basis parameters are necessarily empirical.
- Made the positive-quadratic-coefficient condition explicit in the H2
  stationary-point discussion. These changes clarify or correct existing
  material; no additional electronic-structure topic was introduced.
- Preserved the slides' mathematical command vocabulary, colors with local
  semantic roles, numerical tables, and individual steps of the derivations.
  Physics-package commands implement equivalent delimiter/matrix notation.

## Pass 4: references and source attribution

- Checked every retained article/contributed-chapter identity against
  publisher-deposited DOI metadata or the publisher's article page.
  chapter-reference-audit.md records the sources and incomplete-metadata cases.
- Removed the false Schwarz screening entry: its DOI resolves to an unrelated
  histology article. The inequality is now named mathematically; practical
  screening is cited to the genuine Häser–Ahlrichs paper.
- Corrected the Edmiston–Ruedenberg page range, author initials/suffixes, and
  German title capitalization. Book editions were checked separately.
- Added targeted references for Slater–Condon rules, the MP partition,
  symmetric/canonical orthogonalization, population analysis, IMOM, Basis Set
  Exchange, diffuse/core–valence bases, both existing extrapolation formulas,
  the existing ECP families, late contraction, and Coulomb-fitting bases.
- Kept citations distinct from numerical/illustration provenance: the retained
  screening data and course diagrams are from the slides, not assigned to an
  unverified journal article.
- Made every bibliography DOI a direct clickable DOI link.
- Verification: offline citation/DOI-audit consistency check, source check, and
  complete LaTeX/BibTeX compilation with no unresolved citations.

The final pass will be recorded here when it is completed.
