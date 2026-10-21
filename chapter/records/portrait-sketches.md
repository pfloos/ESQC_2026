# Modern portrait illustrations

All 29 photographic portraits formerly used in the historical panels have
been replaced with individual, transparent-background graphite-style sketches.
The Pauli, Brillouin and Koopmans theorem panels reuse the corresponding new
sketches. Bernardi's historical panel remains text-only: no authenticated
portrait was available, and no new portrait has been added to that panel.

The final illustrations were made on 21 October 2026 using the built-in
`image_gen` tool in reference-image editing mode, one call per subject.
Each uses the corresponding existing photograph as a likeness reference;
the two PDF portraits were rendered to PNG first. They are modern sketch
adaptations, **not archival drawings**, and are labelled as adaptations in
the chapter.

The common brief requested a faithful head-and-shoulders graphite/fine-pen
sketch retaining the actual face, age, hair, spectacles, facial hair, clothing
and orientation, with restrained cross-hatching, a transparent background,
and no labels or signatures. The complete
individual prompts, final image dimensions and SHA-256 checksums are in
[`portrait-sketch-prompts.json`](portrait-sketch-prompts.json). These prompts
are generation records, not biographical sources.

For reproducible small-panel delivery, the saved PNGs were proportionally
downsampled to a 600-pixel maximum edge with macOS `sips`; alpha transparency
was checked for every file. The generated full-resolution originals remain
in the image-generation output directory on the author's computer. The
chapter builds from the committed PNGs without any image-generation service.

Biographical links, original photographic attributions, source-licence links
and permission-pending notices have all been retained in the historical and
theorem boxes. Applicable attribution/share-alike requirements are not
superseded by the repository's general licence. Several source portraits
remain subject to permission checks: these adaptations are **not a rights
clearance or a workaround for unresolved photographic reuse permissions**.
The complete original credit/permission record is preserved in
[`portrait-sources.md`](portrait-sources.md). Superseded photographs remain
recoverable at Git revision `b6c7763c15e4ffeb00e2aa7951902aa33209245d` under
`archive/photographic-portraits/`; each prompt record includes that immutable
reference revision. They are not needed in the active working tree or a
submission bundle. Replacing the old photographs does not remove the need
to resolve the rights of adapted source portraits before public distribution
under a licence that requires those rights.
