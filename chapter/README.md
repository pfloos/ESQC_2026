# Many Electrons, One Determinant

The standalone ESQC chapter lives entirely in this directory. Edit
`ESQC_Loos_HF_BF_chapter.tex`: it contains the complete chapter, title page,
historical panels, and native diagram/table definitions. There are no local
TeX inputs or included chapter fragments. The original scientific notation,
derivation steps, exercises, and Further reading are retained.

The bibliography remains editable in `ESQC_Loos_HF_BF_chapter.bib`; the local
`chapter-unsrtnat.bst` makes reference titles hyperlinks. Raster/PDF figures
remain separate files in `figures/`, as required by LaTeX. A single TeX source
does not mean that these graphics can be omitted from a source submission.

## Build

With TeX Live and latexmk, run from the repository root:

    sh scripts/build_chapter.sh

Or from this directory:

    latexmk -pdf -outdir=build -interaction=nonstopmode -halt-on-error ESQC_Loos_HF_BF_chapter.tex

The PDF and all auxiliary files are placed in `build/`, which is not tracked.
The historical-panel contents list may require several LaTeX passes; latexmk
handles these automatically. No image-generation service is needed to build.

## Prepare source submission

After a successful build, run from the repository root:

    python3 scripts/package_chapter.py

This produces `submission.zip` and a matching `submission/` directory, each
with exactly one `.tex` file, the bibliography and style, a generated `.bbl`,
and only the graphics actually used. Drafts, original photographs, build
artifacts, audit records, and the compiled PDF are excluded. Both outputs are
generated locally and ignored by Git. The script does not upload anything or
choose a distribution licence. Review third-party artwork and the chosen
submission licence before posting.

## Checks and records

From the repository root:

    python3 scripts/check_chapter_source.py
    python3 scripts/check_chapter_layout.py
    python3 scripts/check_chapter_notation.py
    python3 scripts/check_chapter_references.py --check-bbl
    python3 scripts/check_chapter_assets.py
    python3 scripts/check_chapter_hf_algebra.py
    python3 scripts/check_chapter_integrals.py
    python3 scripts/check_chapter_mp2.py

`records/` retains the scientific, notation, coverage and reference audits.
Historical paths in earlier records describe the repository at the time of
the audit. Their former `.tex` inputs now appear inline in the single source,
between incorporation markers. [Portrait illustration documentation](records/portrait-sketches.md)
records the modern AI-assisted sketches; these are not archival photographs.
Superseded photographs and their original provenance are preserved outside
this directory in `../archive/photographic-portraits/`.
