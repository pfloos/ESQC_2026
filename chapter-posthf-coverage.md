# Post-HF slide additions

17 October 2026. Added at the author's explicit request to section 1.7.6,
"Connection with many-body perturbation theory". The nine selected slides
are narrated in their original order, without extending into coupled cluster
or the other post-HF topics outside the requested range.

Sources retrieved from the author's teaching repository on this date:

- [LaTeX source](https://github.com/pfloos/teaching/blob/main/postHF/ISTPC_Loos_postHF.tex)
- [Compiled slides](https://github.com/pfloos/teaching/blob/main/postHF/ISTPC_Loos_postHF.pdf)

SHA-256 of the retrieved LaTeX:
`845ce46bc6e74a0abacf8ea658534fdc207c5e66eae3e32394630dd1f3f60ea8`.
SHA-256 of the retrieved PDF:
`d051ba7ba3fb6b209870b762011e877c6f947c0b7841e75a3d0f690ef85089d9`.

| PDF slide | Source title | Chapter destination |
| --- | --- | --- |
| 45 | MP2 correlation energy | Spin-orbital origin, RHF spin sum, direct/exchange decomposition, retained original illustration (`fig:mp2-direct-exchange`) |
| 46 | Computing the MP2 correlation energy | Initialization, four occupied/virtual loops, denominator and accumulation step, O-squared V-squared work |
| 47 | AO to MO transformation (Take 1) | Four-coefficient expansion, free versus summed indices, eight-loop K-to-the-eighth cost |
| 48 | AO to MO transformation (Take 2) | Exact reordering as four successive one-index contractions |
| 49 | Semi-direct algorithm: Step 1 | `eq:ao-mo-quarter-one`, I allocation/initialization, fifth-order work and quartic storage |
| 50 | Semi-direct algorithm: Step 2 | `eq:ao-mo-quarter-two`, J allocation/initialization, fifth-order work and quartic storage |
| 51 | Semi-direct algorithm: Step 3 | `eq:ao-mo-quarter-three`, cleared/reused I buffer, fifth-order work without another temporary buffer |
| 52 | Semi-direct algorithm: Step 4 | `eq:ao-mo-quarter-four`, output MO tensor, fifth-order work, total storage accounting |
| 53 | Laplace transform | Positive-gap identity, exponential separation, dressed orbitals, finite quadrature, and the slide's links to localization, RI, stochastic sampling, and quadrature |

## Explicit notation and sign decisions

- The chapter retains N for electrons and K for spatial basis functions,
  rather than importing the algorithm slides' generic size symbol N.
  Spatial occupied/virtual counts are O=N/2 and V=K-O. Their switch back to
  spin-orbital indices for the Laplace expression is explicit.
- Existing chapter commands and colors are retained. The four transformation
  stages use the slides' local violet/orange/blue/red sequence; occupied and
  virtual labels otherwise retain the chapter's green/red convention.
- The spin-orbital numerator is an absolute square, allowing complex
  canonical orbitals. The spatial and transformation formulas explicitly
  specialize to real orbitals, as in the slides.
- Only AO labels are summed in each quarter transformation. MO labels on
  its left-hand side remain free; the source's schematic nested summation
  subscripts including output MO labels are not copied literally.
- The Laplace slide writes a negative MP2 denominator in an exponential
  identity requiring a positive argument. The chapter explicitly introduces
  D=-Delta>0 and retains the minus sign before the integral/quadrature.
  Without this change the integral diverges and the MP2 energy sign is wrong.
  Occupied dressing is exp(+epsilon_i t/2), virtual dressing
  exp(-epsilon_a t/2); their squared integral gives exp(-D t).
- A bare Laplace transformation is not claimed to reduce the scaling by
  itself. Its benefit is denominator separation, enabling the additional
  strategies listed in the slide.

## Illustration provenance

`chapter-figures/mp2-direct-exchange.png` is the original 1084-by-402 image
embedded as Im18 on PDF page 45, extracted without cropping or redrawing.
The caption credits the author's lecture and explains its labels. The slide
does not identify a separate original publication for the image; none has
been invented. This record does not assert a new reproduction license.

## Checks

`scripts/check_chapter_mp2.py` compares all full four-index transformed
integrals with the four quarter transformations on a small deterministic
tensor. It also compares spin-orbital and spin-summed RHF energies, checks
the direct/exchange index conversion, verifies the dressed-integral
exponents, and integrates the Laplace form independently of the reciprocal
denominator expression. The source-layout comparison against `d19d2af`
requires every corrected pre-existing display to remain in order, while
allowing the new stationarity and MP2 displays.

All six chapter checks pass. The original 583 corrected displays remain in
order, all 31 scientific figures/tables have prose callouts, and Further
reading is unchanged. Complete compilation succeeds (128 pages), with no
undefined references or citations and no BibTeX warnings. Targeted rendered
checks cover the new MP2 energy/diagram, quarter transformations, and Laplace
equations. The numerical Laplace-energy agreement is within 9.66e-15.
