# Scientific cover illustration

The approved transparent image is `../figures/cover-porphine-gaussians.png`.
It shows selected normalized real Gaussian basis functions on porphine, not
computed occupied molecular orbitals. The cover image is unchanged by the
post-submission cleanup.

Each function is `N P(x,y,z) exp(-alpha r^2)` in local atom-centered
coordinates. The homogeneous angular polynomials are harmonic; `N` gives
unit integral of the squared function over three-dimensional space.

| Type | Polynomial P | PubChem atom ID | alpha (inverse square angstrom) |
| --- | --- | --- | --- |
| s | 1 | C14 | 2.0 |
| p_z | z | C8 | 3.0 |
| d_xy | xy | C19 | 3.0 |
| f_z(x2-y2) | z(x^2-y^2) | C5 | 4.2 |
| g_xy(x2-y2) | xy(x^2-y^2) | C21 | 5.2 |

Green and amber denote positive and negative values. Atom identifiers refer
to the archived PubChem data, not chemical nomenclature. Exponents are chosen
for legibility; no named contracted basis or orbital occupation is implied.

Geometry, atomic identities, connectivity and bond orders come from
[PubChem CID 66868](https://pubchem.ncbi.nlm.nih.gov/compound/66868), porphine,
C20H14N4. The 3D record downloaded on 15 October 2026 is preserved unchanged
in [`porphine-pubchem-3d.json`](porphine-pubchem-3d.json). The conformer is
recentered and rigidly rotated into its best-fit heavy-atom plane; it is not
claimed to be HF optimized. The stored
[`06-porphine-exact-gaussians.json`](06-porphine-exact-gaussians.json) retains
the approved render's normalization constants, exponents, centers, isovalues,
mesh counts and numerical residuals.

The procedural source is `../../scripts/render_basis_cover.py`. It reconstructs
the molecule and meshes from these data; the old generated Blender scene and
duplicate renders are not required. From the repository root, using Blender
4.5 and its bundled NumPy:

    blender --background --python scripts/render_basis_cover.py

Use `-- --quick` for a faster render or `-- --opaque-preview` for a separate
light-background review image. New PNG, Blender scene and metadata outputs go
to `chapter/build/cover/`, without overwriting the approved chapter graphic.
No image-generation model is used by this renderer.

Numerical checks can run without Blender, using a NumPy-enabled Python:

    python3 scripts/render_basis_cover.py -- --check

Checks cover harmonic polynomials, unit norms by independent Gauss-Hermite
quadrature and selected nodal planes. Full rendering also checks closed mesh
topology, expected lobe counts, sampling boundaries and relative vertex
isovalue residuals below 1e-8. Surfaces use 20% of each function's maximum
absolute sampled amplitude on an 89-cubed grid over [-2,2] angstrom.

Earlier design studies and the original editable scene remain recoverable
at Git revision `b6c7763` under `archive/drafts/cover-studies/`.
