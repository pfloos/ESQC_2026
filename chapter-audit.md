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

The remaining passes will be recorded here as they are completed.
