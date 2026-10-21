# Many Electrons, One Determinant

**Hartree–Fock Theory, Basis Sets, and Molecular Integrals**

The chapter has been submitted to arXiv; its public identifier is not yet available. This directory contains the complete editable source and all compilation inputs. Repository cleanup does not alter the submitted chapter text or scientific illustrations.

## Source and build

Edit `ESQC_Loos_HF_BF_chapter.tex`: it contains the complete chapter, title page, historical panels, and native diagram/table definitions. There are no local TeX inputs. The bibliography is in `ESQC_Loos_HF_BF_chapter.bib`; `chapter-unsrtnat.bst` makes reference titles hyperlinks. Required graphics are in `figures/`.

With TeX Live and latexmk, run from the repository root:

```sh
sh scripts/build_chapter.sh
```

Or, from this directory:

```sh
latexmk -pdf -outdir=build -interaction=nonstopmode -halt-on-error ESQC_Loos_HF_BF_chapter.tex
```

The PDF and auxiliary files are placed in `build/`, which is not tracked. Latexmk runs BibTeX and repeats LaTeX to resolve references and the historical-panel contents list. No image-generation service or Blender installation is needed to compile.

## Source package for future revisions

After a successful build, run from the repository root:

```sh
python3 scripts/package_chapter.py
```

This generates `submission.zip` and a matching `submission/` directory, with exactly one `.tex`, the bibliography and style, the generated `.bbl`, and only the graphics actually used. The repository licence and citation metadata accompany the sources. Commented-out illustrations are excluded. Both outputs are ignored by Git; the script does not upload anything.

## Verification

From the repository root:

```sh
python3 scripts/test_chapter_paths.py
python3 scripts/check_chapter_source.py
python3 scripts/check_chapter_layout.py
python3 scripts/check_chapter_notation.py
python3 scripts/check_chapter_references.py --check-bbl
python3 scripts/check_chapter_assets.py
python3 scripts/check_chapter_hf_algebra.py
python3 scripts/check_chapter_integrals.py
python3 scripts/check_chapter_mp2.py
```

The rendered-reference check requires a successful build. These are source-consistency and targeted numerical checks, not a substitute for scientific review.

## Credits and reproducibility

[`records/`](records/) retains reference-verification data, [portrait source credits](records/portrait-sources.md), [sketch prompts and provenance](records/portrait-sketches.md), and [cover definitions and molecular data](records/cover-illustration.md). Original photographs and development drafts are recoverable at Git revision `b6c7763`; they are not compilation inputs.

The approved cover can be regenerated with `scripts/render_basis_cover.py` and Blender. Regenerated scenes, metadata and previews are written to `build/cover/`, not to the source tree. See the [cover record](records/cover-illustration.md) for commands and numerical checks.
