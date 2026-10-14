# Chapter audit

This record concerns the chapter, not modifications to the lecture decks.
The active frames of `ESQC_Loos_HF.tex` and `ESQC_Loos_BF.tex` are the
coverage baseline. Commented-out frames are not additional required material.

## Pass 1: scientific questions in the integral section

- Corrected both OS vertical-recurrence product-center signs. Differentiating
  the Boys function gives a minus sign; the slide equations have plus signs.
  The chapter includes a short derivative check so the correction is explicit.
- Checked the bra lowering term, ket lowering term, and mixed bra/ket term
  against independent quadrature of Gaussian conditional moments.
- Clarified that the recurrence formulas apply to unnormalized primitives and
  that the combined VRR/HRR late-contraction strategy is Head--Gordon--Pople.
- Made the real-function assumption and auxiliary-metric invertibility explicit
  in RI. Added residual orthogonality and the equality of fitting one or both
  densities, connecting the least-squares derivation to the factorization.
- Numerical verification: `python3 scripts/check_chapter_integrals.py`.
  The script also checks RI projection and contraction in a nonorthogonal,
  incomplete auxiliary space.

## Pass 2: equations, notation, and physics-package conventions

- Restored explicit `\cdot` in the remaining matrix products, including
  the orthogonalization derivation and its intermediate normalization steps.
- Removed sentence-ending periods, commas, and semicolons from displayed
  equations. Mathematical separators in tuples and sets are retained.
  Invisible `\left.`/`\right.` delimiters remain where a multirow expression
  requires them.
- Converted applicable paired delimiters to `\qty`, explicit matrices to
  `\pmqty`, determinants to `\mdet`, derivatives to `\dv`, and the
  commutator to `\comm`. Existing `\pdv`, `\fdv`, `\dd`, `\abs`, `\norm`,
  `\Tr`, and bra–ket commands are retained. The slides' custom paired
  integral commands are preserved. Delimiters split across alignment rows
  remain explicit because a single `\qty` argument cannot span those rows.
- Restored missing `\quad`/`\qquad` commands and corrected the cc-pVTZ
  shell decomposition's `2s` transcription to `2d`.
- Corrected the STO derivative to include its value at the nucleus, and
  distinguished a cusp-shaped exponential from satisfaction of the actual
  point-nucleus cusp condition.
- Corrected the Boys localization optimization direction and explained
  why minimizing the two spread expressions maximizes centroid separation.
- Verification: source-convention check and full LaTeX/BibTeX compilation.

## Pass 3: fidelity to both lecture presentations

- Reviewed all 100 active HF frame blocks and all 48 active basis/integral
  frame blocks; their chapter destinations are recorded individually in
  `chapter-slide-coverage.md`. Commented-out frames and presentation
  scaffolding are distinguished from the scientific content.
- Checked the normalization, one- and two-electron, spin-to-spatial, and
  atomic worked examples; all Slater--Condon cases; spin adaptation and
  contamination; Koopmans IP/EA energy decompositions; canonicalization;
  AO Fock/energy contractions; SCF, DIIS, and MOM stages; properties;
  localization; UHF/H2; and GHF/classification.
- Checked the basis-family comparisons, shell counts, contraction example,
  ECP operators and families, Gaussian product and one-electron formulas,
  Laplace-transform stages of the ssss derivation, Boys limits/recurrences,
  VRR/HRR stages, numerical screening table, direct SCF, and RI/CD.
- Restored the ghost-basis diagram, the integral-recipe diagram, the explicit
  ten-primitive carbon contraction, and the Gaussian-basis remarks on Pulay
  terms, all-electron practicality, and locality.
- Restored physicists' brackets on the plane-wave ERI derivation, matching
  the slides' actual index grouping. Explained the periodic Coulomb kernel,
  reciprocal-vector relabeling, and the excluded zero-transfer term.
- Corrected DIIS's history sum to contain exactly m stored iterations.
- Corrected GHF's spin/AO tensor-factor ordering and exchange contraction for
  complex density matrices; an independent numerical kernel check verifies
  the latter. Distinguished the half-charge GHF block from the full density.
- Qualified monotonic basis improvement to nested variational spaces and
  corrected the claim that all basis parameters are necessarily empirical.
- Made the positive-quadratic-coefficient condition explicit in the H2
  stationary-point discussion. These changes clarify or correct existing
  material; no additional electronic-structure topic was introduced.
- Preserved the slides' mathematical command vocabulary, colors with local
  semantic roles, numerical tables, and individual steps of the derivations.
  Physics-package commands implement equivalent delimiter/matrix notation.

## Pass 4: references and source attribution

- Checked every retained article/contributed-chapter identity against
  publisher-deposited DOI metadata or the publisher's article page.
  chapter-reference-audit.md records the sources and incomplete-metadata cases.
- Removed the false Schwarz screening entry: its DOI resolves to an unrelated
  histology article. The inequality is now named mathematically; practical
  screening is cited to the genuine Häser–Ahlrichs paper.
- Corrected the Edmiston–Ruedenberg page range, author initials/suffixes, and
  German title capitalization. Book editions were checked separately.
- Added targeted references for Slater–Condon rules, the MP partition,
  symmetric/canonical orthogonalization, population analysis, IMOM, Basis Set
  Exchange, diffuse/core–valence bases, both existing extrapolation formulas,
  the existing ECP families, late contraction, and Coulomb-fitting bases.
- Kept citations distinct from numerical/illustration provenance: the retained
  screening data and course diagrams are from the slides, not assigned to an
  unverified journal article.
- Made every bibliography DOI a direct clickable DOI link.
- Verification: offline citation/DOI-audit consistency check, source check, and
  complete LaTeX/BibTeX compilation with no unresolved citations.

## Pass 5: prose, navigation, and standalone-document presentation

- Changed the single-chapter document from book to article, with a title page,
  roman-numbered contents, and ordinary section/subsection/subsubsection
  numbering. Preserved the entire color palette and dark green heading scheme.
- Removed the duplicated chapter heading and used a short, stable running
  title instead of a book-style chapter mark.
- Added a linked section roadmap and targeted references between finite-basis
  HF, basis design, Gaussian products, Boys functions, recurrences, and RI.
- Replaced remaining conversion-process wording with explanatory prose,
  retaining the equations and every intermediate derivation step.
- Added a numbered caption and source description to the numerical screening
  table, and corrected the molecule-name typo dodecaexaene to dodecahexaene.
- Expanded the README with chapter sources, bibliography, build instructions,
  audit records, and verification commands. Generated chapter PDFs and build
  auxiliaries are not committed; narrowly scoped ignore rules leave the existing
  lecture PDFs tracked. Changing class requires clearing the old generated
  book-class table of contents before rebuilding.
- Verification: all three source/reference/numerical checks and complete
  LaTeX/BibTeX compilation, with resolved citations and cross-references.
  Visual appearance and overflow were intentionally not audited, as requested.

## Reader-oriented editorial pass

- Read the narrative continuously across the HF, basis-set, and integral
  sections, with the displayed derivations retained in their original order.
- Tightened repeated introductory and concluding prose without removing
  worked examples, scientific remarks, or intermediate derivation steps.
- Clarified the exact/trial wavefunction and electronic-Hamiltonian
  conventions, forward use of Slater–Condon rules and the Fock operator,
  density conventions, and the relationship between stored-integral SCF
  and direct SCF.
- Defined method abbreviations, DIIS iteration/residual notation, H2 overlap
  notation, Pauli/tensor-product notation, spinor matrices, and the local
  meanings of the classification-table operators.
- Clarified basis exponents and angular-momentum labels, primitive versus
  contracted function labels, extrapolation parameters, ECP charges, Gaussian
  product centers, Boys orders, Cartesian unit vectors, and RI fitting indices.
- The author confirmed that the screening benchmark's size variable counts
  basis functions. Changed that formula and the corresponding table heading
  from N to K; all numerical values are unchanged.
- Kept the section hierarchy, figures, custom notation commands, colors,
  bibliography, and scientific scope unchanged. All other displayed
  mathematical expressions are unchanged.
- Verification: compared displays, figure/table/algorithm contents, heading
  order, and the preamble against the preceding commit, allowing only the
  approved screening-variable rename. All three existing verification scripts
  pass, and full compilation resolves citations and cross-references.
  Visual/overflow review remains excluded as requested.

## Figure and table source acknowledgments

- Added the author's source identifications to the captions: Szabo and Ostlund
  for Figures 1, 3-6; Jensen for Figure 2; Burton, Thom, and Loos (2019),
  Figure 1, for the chapter's Figure 10.
- Credited Table 1 as reproduced in part from Henderson, Jiménez-Hoyos, and
  Scuseria (2018), Table I. Explicitly noted that the density-matrix columns
  are omitted and the notation is adjusted.
- Verified both new paper records and checked the classification-table match
  against the author preprint. Existing book references are used without
  inventing source page/figure numbers.
- No illustrations have been replaced. The author requested approval of
  alternative designs before incorporation, including the proposed table
  replacing the current carbon-contraction image (Figure 12).
- Verification: chapter compilation and source/reference consistency checks.

## Pending design review

- Prepared a separate six-page PDF showing current and proposed designs for
  Figures 1, 2, 3-5, 6, 10, and a table replacing Figure 12.
- Kept all proposals outside the chapter, with editable LaTeX/TikZ source and
  an independent table fragment. Approval can be given page by page.
- Preserved all eight symmetry classes and all eleven constraint-release
  connections in the alternative classification layout.
- Transcribed the ten-row carbon contraction and compared all twenty numeric
  entries exactly with the Basis Set Exchange cc-pVTZ carbon definition.
- Compiled the review PDF and visually inspected all six pages, repairing
  label/spacing collisions before delivery. Full-chapter visual review was
  not performed.
- Newly drawn layouts retain scientific source attribution. No source-credit
  removal or reuse-permission assertion is implied by a redesign.

## Approved figure and table incorporation (14 October 2026)

- Incorporated all six approved design-review pages as native LaTeX/TikZ
  material in the dark-green chapter scheme. Figure and table source credits
  remain in the captions; Figure 10 now describes its layout as based on the
  cited paper, rather than extracted from it.
- Kept Figures 1-6 and 10 at their existing source locations, with the
  reference and excitation maps remaining separate figures. The H2
  spin-orbital/spatial-orbital equivalence uses the approved display schematic.
- Replaced former Figure 12 with Table 2, preserving all ten exponents and
  coefficients exactly, including the negative ninth coefficient and shell
  scale. Subsequent figure/table numbering updates automatically.
- Kept the partial reproduction and acknowledgment in Table 1 unchanged.
  Figure 10 retains all eight classes and eleven constraint-release connections.
- Active fragments are in `chapter-figures/`. The comparison PDF remains an
  archived approval record; original images and both slide decks are untouched.
- Verification: full 106-page chapter compiles with citations and references
  resolved; all three existing verification scripts pass. Compared both chapter
  sources against the preceding commit after excluding figure/table blocks:
  all remaining text, equations, derivation steps, and section order are identical.
- The PDF skill was used to inspect only the changed illustrations and table
  in their compiled chapter context. No full-chapter layout/overflow audit was
  performed, in accordance with the author's earlier preference.

## Title-page redesign (14 October 2026)

- Replaced the default article title page with a native, page-relative TikZ
  cover: a dark-green accent band, large left-aligned title, pale-green lower
  panel, decorative orbital-inspired contours, and separated author/conference
  details. Retained the author name, affiliation, title topics, and ESQC year.
- The cover is isolated in `chapter-titlepage.tex` and reuses the existing
  typography, colors, and TikZ package. No external artwork is required.
- The PDF skill was used to inspect the rendered cover. Chapter content,
  scientific figures, equations, citations, and page-numbering setup are
  unchanged. Full compilation and existing source/reference checks pass.

### Cover typography refinement

- Set `ESQC 2026` on a single line at the upper right and added `(ESQC)`
  after the conference name in the footer, as requested by the author.
- Left the decorative illustration unchanged pending selection of an
  alternative design. Verified full compilation and inspected the revised
  cover using the PDF skill; no chapter content was altered.
