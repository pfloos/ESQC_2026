# Approved native chapter illustrations

These LaTeX/TikZ fragments implement the six-page design review approved by
the author on 14 October 2026. They are included by the chapter and compiled
with its notation, fonts, physics package, and dark-green palette.

- `coordinates.tex`: Figure 1, absolute and relative coordinate panels.
- `orbital-sharing.tex`: Figure 2, RHF/ROHF/UHF spatial-orbital sharing.
- The approved closed-shell H2 equivalence is typeset directly in Figure 3.
- `reference-occupation.tex` and `excited-occupations.tex`: Figures 4 and 5,
  selected columns of the approved common occupation map, retained at the
  original separate chapter locations.
- `orthogonalization.tex`: Figure 6, three method panels and transformation
  rules, including explicit matrix multiplication dots.
- `symmetry-classes.tex`: Figure 10, eight classes and all eleven release
  connections. The separate reproduced classification Table 1 is unchanged.
- `carbon-contraction-tabular.tex`: Table 2, replacing former Figure 12,
  with all twenty numeric entries preserved exactly from the approved draft.
- `hydrogen-sto3g-tabular.tex`: native table of the three hydrogen STO-3G
  exponents and coefficients, transcribed exactly from the lecture image and
  verified against Basis Set Exchange. The original `fig/STO.pdf` comparison
  plot is now included as a separately captioned chapter figure.

`styles.tex` is included within local groups, so figure styles do not affect
other chapter illustrations. Source credits remain in the chapter captions.
Original borrowed images are not modified or deleted and remain available to
the slides. The archived comparison PDF in `output/pdf/` records the design
approval stage; it is not an input to the chapter build.

## Approved cover illustration (15 October 2026)

`cover-porphine-gaussians.png` is the approved transparent cover artwork,
included by `chapter-titlepage.tex`. Keep this image with the chapter sources.
It is an unmodified copy of the approved 2400-by-1650 scientific render:
normalized real s/p/d/f/g Gaussian functions on a PubChem porphine framework.
The signs are consistently green (positive) and amber (negative).

[Function definitions, exponents, source coordinates, verification, and
editable scene](../drafts/cover-studies/06-porphine-exact-gaussians.md)
are archived with the approval record. Compiling the chapter uses only the
saved PNG; Blender and NumPy are optional regeneration dependencies.
