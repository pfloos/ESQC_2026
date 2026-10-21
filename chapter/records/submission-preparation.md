# Source consolidation and submission preparation — 21 October 2026

Baseline: the author's latest reviewed revision, `46578db`, pulled before
editing. The original slide sources, slide PDFs, shared `fig/` directory and
repository licence are unchanged.

## Organisation

- `chapter/ESQC_Loos_HF_BF_chapter.tex` is the one editable chapter source.
  Fourteen distinct former TeX source files are incorporated recursively:
  the main chapter, basis/integral material, historical panels, title page,
  and native figure/table/style fragments. Incorporation markers preserve
  their origins; the redundant fragments remain recoverable through Git.
- Bibliography/style and required graphics are local to `chapter/`.
  Seven chapter-used slide assets are copied without changing slide originals.
- Audits and coverage records are in `chapter/records/`.
- Earlier designs/review documents and the superseded photographs/provenance
  are in `archive/`. Local preview intermediates and the pre-consolidation
  PDF are also retained there but not tracked. Nothing unique was discarded.
- An unused MP2 illustration is preserved in `archive/drafts/figures/`, not
  included in the active chapter graphics or submission package.

## Preservation checks

The legacy-aware comparison tools expand sources directly from Git. Against
`46578db`, all **654 displays** retain the same mathematical tokens in the
same order; Further reading is unchanged. The source checks retain all
18 exercise/solution pairs, 31 cited scientific figures/tables, six tables
using the shared style, 26 historical-panel entries and 110 reference keys.
Whitespace-only cleanup removes trailing spaces, not paragraph breaks.
Photograph credits and permission-pending notices are retained for the
reference-based sketch adaptations; see `portrait-sketches.md`.

## Reproducibility

`scripts/build_chapter.sh` isolates generated files in `chapter/build/`.
`scripts/package_chapter.py` creates a generated `chapter/submission.zip`
containing exactly one `.tex`, the `.bib`, `.bst`, generated `.bbl`, and
39 required graphics, with no dependence on the slide or archive directories.
`scripts/check_chapter_assets.py` verifies the exact active graphics set,
portrait provenance, RGBA PNG headers, dimensions and checksums.

This is technical submission preparation, not an arXiv upload or a clearance
of third-party portrait permissions. Licence selection and final public
distribution remain the author's decisions.
