# Approved figure and table design review

The [cover illustration studies](cover-studies/README.md) record the design
iterations of 15 October 2026. The author approved the final mathematically
rendered porphine design (study 6), now incorporated in the chapter cover.
The earlier alternatives remain archived and are not active.

All six design pages were approved by the author and incorporated on
14 October 2026. The comparison PDF is retained as the archived approval
record; its pending-approval banners describe the earlier review stage.

Figure numbers in that review refer to the chapter before incorporation.
Active, editable illustrations and the table are in
[`chapter-figures/`](../chapter-figures/), separate from these review drafts.

The [six-page comparison PDF](../output/pdf/chapter-figure-design-review.pdf)
shows the current illustration and a proposed replacement on each page:

1. Figure 1: separate absolute-position and relative-displacement panels.
2. Figure 2: orbital-sharing cards for RHF, ROHF, and UHF, retaining the
   singlet/doublet examples. This alternative emphasizes spatial constraints,
   rather than the original energy-level ordering.
3. Figures 3-5: a coordinated occupation-map design for the reference, singles,
   doubles, and the closed-shell H2 occupation equivalence.
4. Figure 6: parallel Schmidt, symmetric, and canonical orthogonalization
   panels, with original and orthonormal functions distinguished by line style.
5. Figure 10: an eight-class constraint matrix and a separate list preserving
   all eleven constraint-release connections in the current graph.
6. Figure 12: a native table of the ten primitive exponents and coefficients
   in the carbon cc-pVTZ contraction excerpt.

The designs are newly authored LaTeX/TikZ layouts, not edits to the borrowed
image files. Their chapter captions retain the sources of the scientific content.
Recoloring an existing image alone is
not being presented as an original design, and no reuse-permission claim is made.

The table is provided as a separate
[editable fragment](carbon-contraction-tabular.tex). Its values were checked
against the Basis Set Exchange cc-pVTZ carbon definition and the source image.
Every displayed digit is preserved; only the D-format scientific notation is
reformatted. The incomplete next shell visible at the image's bottom edge is
not reconstructed or guessed.

The [preview source](../output/pdf/chapter-figure-design-review.tex) can be
compiled from the repository root with:

    latexmk -pdf -outdir=output/pdf output/pdf/chapter-figure-design-review.tex

The former Figure 12 is now Table 2. Later figure/table numbers have changed
naturally. The reference and excited-determinant maps remain at their separate
chapter locations, using the approved common design. The original image files
remain available to the slide decks; they have not been overwritten or deleted.

## Approved Gaussian cover illustration review

The author selected the overlapping-Gaussian concept as a replacement for
the decorative cover contours. The new
[single-page cover preview](../output/pdf/chapter-titlepage-gaussian-review.pdf)
shows two spatially separated one-dimensional Gaussians and their exact
pointwise product. The narrow Gaussian is green, the broader Gaussian blue,
and the product amber, with smooth curves and translucent fills.
Exponents are 0.6 and 0.3, centers are -1.4 and 1.4, and
both original peaks are unity, in arbitrary display units. The product is not
rescaled: its peak is exp(-1.568), about 0.2085, at -0.4667.
Curves are drawn over the display interval [-6,6]. This is not a normalized basis-set
specification. There are no axes or labels, and all cover typography and
wording are unchanged.
The author approved this 1D design on 14 October 2026. It was incorporated
at that time, then superseded by the approved porphine design on 15 October
2026. This separate PDF and draft source are retained as the archived
design-review record.

The editable cover variant is `chapter-titlepage-gaussians.tex`. Compile its
review document from the repository root with:

    latexmk -pdf -outdir=output/pdf output/pdf/chapter-titlepage-gaussian-review.tex

## Archived orbital-atlas cover proposal (not selected)

The [new single-page preview](../output/pdf/chapter-titlepage-orbital-atlas-review.pdf)
offers a richer, original contour illustration while retaining the active
cover's typography, wording, and dark-green framing. Teal and amber contours
show opposite signs of an illustrative linear combination of six Gaussian
functions; the pale-blue contours provide a broader Gaussian envelope.
This is schematic artwork, not a calculated HF orbital, an electron density,
or an identified molecule. It contains no scientific labels or quantitative
claims. The saved artwork consists of editable native TikZ paths.

This proposal was not selected. The active chapter now uses the approved
porphine rendering instead. The archived proposal's editable
layout is `chapter-titlepage-orbital-atlas.tex`, with contours in
`cover-orbital-contours.tex`. Compile the standalone preview from the
repository root with:

    latexmk -pdf -outdir=output/pdf output/pdf/chapter-titlepage-orbital-atlas-review.tex

Compiling the saved artwork does not require Python. Optional regeneration
uses `scripts/generate_cover_orbital_art.py` with NumPy and contourpy installed;
the script prints the TikZ paths to standard output without modifying files.
