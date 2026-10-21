#!/bin/sh
# Build only inside chapter/build; no generated files in the repository root.
set -eu
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$script_dir/../chapter"
latexmk -pdf -outdir=build -interaction=nonstopmode -halt-on-error ESQC_Loos_HF_BF_chapter.tex
