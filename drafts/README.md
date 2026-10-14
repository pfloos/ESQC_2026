# Figure and table designs awaiting approval

None of these proposed replacements is included in the active chapter.
Current figure numbers refer to the chapter before any replacement is made.
The active chapter has received source credits only.

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
image files. Their captions will retain the sources of the scientific content
if the author approves incorporation. Recoloring an existing image alone is
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

Approval may be given separately for each page. Figures remain untouched
until approved; the carbon table will become a numbered chapter table only
after approval, and later figure/table numbers will then change naturally.
