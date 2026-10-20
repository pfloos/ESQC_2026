# Chapter audit

## Hyperlinked reference titles (19 October 2026)

- Pulled main before editing; baseline `ed884d7` was current. Added the
  local, licensed `chapter-unsrtnat.bst` derivative of natbib's unsrtnat
  style: titles link to DOI targets, falling back to stored publisher URLs,
  rather than appending visible DOI/URL text to each entry. The style is
  committed source, so the normal BibTeX/latexmk workflow reproduces it.
- Kept all existing DOI fields and bibliographic metadata. Added verified
  publisher URLs only for the three books without stored DOIs; provenance
  and the limited Dover page extraction are recorded in the reference audit.
- Extended the reference check with `--check-bbl`, verifying one correctly
  targeted hyperlink per rendered reference title and no separate DOI/URL
  blocks. All 85 references pass; their 82 DOI and three publisher targets
  are also present as PDF link annotations. An exact normalized comparison
  retains every title, author, publication detail, and citation order after
  stripping only the link wrappers and previous standalone DOI blocks.
- All seven checks pass, with all 637 displays, all 30 figure/table callouts,
  all six table styles, the author's MOM correction, and Further reading
  unchanged. Compilation succeeds to 135 pages without undefined references
  or citations, BibTeX warnings, or overfull boxes. The PDF skill guided
  targeted rendered bibliography checks and verification of link annotations;
  no full-document visual review was undertaken.

## Approved chapter title (19 October 2026)

- Pulled main before editing; baseline `39405c2` was current. Applied the
  author-approved main title, "Many Electrons, One Determinant", with
  "Hartree--Fock Theory, Basis Sets, and Molecular Integrals" as the subtitle.
  Updated the cover, LaTeX title declaration, and PDF title metadata.
- Retained the cover illustration, dark-green palette, author information,
  ESQC branding, and "Hartree--Fock Theory" running headers. The complete
  chapter body after begin-document is byte-for-byte unchanged.
- All seven checks pass; all 637 displays and Further reading are unchanged.
  Compilation succeeds to 135 pages without undefined citations/references,
  BibTeX warnings, or overfull boxes. The PDF skill guided a rendered cover
  check and verification of the new PDF metadata; no body layout audit.

## Table styling and abstract refresh (19 October 2026)

- Pulled main before editing; baseline `15aa52b` was current. Harmonized
  all six numbered tables using the notation glossary as the visual model:
  dark-green bold headings, pale-green logical group bands, a shared small
  body font, and booktabs horizontal rules without vertical borders.
  Introduced shared table-style commands so future tables can reuse this
  design. The glossary keeps its existing appearance and repeated headings.
- Moved table captions above their entries, retaining their exact text,
  citations, labels, and numbers. Added RHF/UHF/GHF group bands to the
  classification table and augmentation bands to the shell-content table.
  Retained the red/orange operator distinction in the screening table.
  Made the shell-content table a normal float so its caption cannot be left
  behind on a different page. Paragraph boundaries around two other floats
  keep sentences from being interrupted by a table.
- Refreshed the colored abstract to reflect the current ESQC doctoral-level
  chapter, including SCF convergence/stability, overlap-based occupation
  selection, the MP2/AO-to-MO connection, and the expanded worked exercises.
  No removed MP2 Laplace material was restored. The cover and title are
  unchanged; alternative titles are proposed to the author in conversation.
- Extended the layout check to verify the shared headings/rules in all six
  tables, expand the included coefficient tables, and require captions above
  entries in each non-longtable table. Independent source comparisons retain
  all table mathematics, numerical rows, shell counts, contraction data,
  and caption/attribution text exactly.
- All seven checks pass. All 637 displays are retained in order, with zero
  notation or mathematical-token changes; all 30 figure/table callouts,
  85 cited references, the author's MOM correction, and Further reading
  are preserved. Compilation succeeds to 135 pages without undefined
  citations/references, BibTeX warnings, or overfull boxes. The PDF skill
  guided checks of the abstract and affected tables, not a full visual audit.

## Epsilon-matrix notation and acronym glossary (19 October 2026)

- Pulled through the author's `360be9d` before editing. Retained the
  corrected MOM overlap matrix, bold capital O rather than the bold zero
  command, and the author's other glossary edits. Integrated the concurrent
  `2cd42bb` glossary simplifications after the first push was safely rejected;
  both deleted caveats remain deleted.
- Defined the canonical chapter command `\beps` as bold epsilon. Replaced
  rendered `\bE` and `\bepsilon` uses, including the occupied blocks, UHF
  spin sectors, and SCF/DIIS/MOM flowcharts. The GHF spinor energy matrix
  also uses `\beps` rather than a separate calligraphic E. Original unused
  slide-compatible command declarations are retained in the preamble.
- Corrected the symbol-table entries to distinguish occupied-space
  multipliers before canonicalization from the canonical diagonal orbital
  energies, and to specify RHF/GHF dimensions and occupied/virtual/spin blocks.
- Extended the same table with a separate alphabetized group of 48 acronyms
  and abbreviations already used in the chapter. Retained its table number,
  label, repeated headings, and dark-green color scheme; no new topic or
  bibliography item was introduced.
- Extended the notation guard and its documented alias comparison. All 637
  displays are retained in order against `2cd42bb`; 17 have notation-only
  spelling changes. An exact comparison of the entire scientific body,
  including MOM, permits only these matrix-name replacements. No factor,
  sign, index, contraction, prose passage, or Further reading was changed.
- All seven checks pass, with all 30 figure/table callouts and 85 cited
  bibliography entries retained. Compilation succeeds to 135 pages without
  undefined citations/references, BibTeX warnings, or overfull boxes. The
  expanded glossary occupies four pages; a small row-spacing adjustment
  avoids a nearly empty fifth glossary page. Only affected glossary pages are
  rendered for a focused PDF check, not a full-document visual review.

## Three supplementary exercises (19 October 2026)

- Pulled main before editing; the current baseline was `33b38c4`. Added
  exactly the three exercises selected by the author, each with a complete
  solution in the existing exercise/solution colors and no new subsection.
- After the closed-shell AO energy: Hermiticity, electron counting from
  real-space integration, single-spin metric idempotency, the RHF factor of
  two, and the occupied-space projector acting on AO coefficient vectors.
  Single-spin populations consistently use N^sigma; the general open-shell
  charge density is explicitly distinguished from the RHF case.
- After SCF convergence criteria: derive the residual from the occupied
  Roothaan--Hall equations and their adjoint, transform it to the MO basis,
  and identify its occupied--virtual factors and signs. Explain energy
  plateaus, the mixed-iteration zero produced by one diagonalization, the
  need for a density-consistent Fock matrix (including after DIIS), and the
  distinction between stationarity, local stability, and global optimality.
- After the Gaussian product theorem: normalize an s primitive, derive the
  overlap of two normalized primitives, examine coincident centers, unequal
  exponents, equal exponents, and infinite separation, and evaluate a
  fully specified unequal-exponent example (overlap 0.4700). Calligraphic
  N denotes the local primitive normalization factor, not a spin population.
- Extended the independent HF-algebra checks to complex nonorthogonal AOs,
  both density normalizations, unequal spin populations, coefficient-space
  projection, MO residual blocks, mixed iterations, and stable/unstable
  stationary examples. Added 27 independent Cartesian numerical overlap
  quadratures and the Gaussian limiting cases to the integral checks.
- All seven checks pass. The layout comparison preserves all 607 existing
  displays in order and Further reading. Removing only the three addition
  blocks recovers both baseline chapter sources byte for byte: no existing
  prose, equation, figure, bibliography, or author MP2 edit was changed.
  There are now 17 exercises; all 30 figure/table callouts and 85 cited
  bibliography entries are retained. Compilation succeeds to 134 pages
  without undefined references/citations, BibTeX warnings, or overfull boxes.
  Following the PDF skill, checked one rendered solution page per added
  exercise; no full-document visual review was undertaken.

## Chapter-wide notation pass and author synchronization (18 October 2026)

- Integrated the author's commits through `fe1d3c7` while preserving the
  separate superscript-spin-count change. The revised MP2 section and
  revised stationarity exercise are byte-for-byte identical to that author
  baseline; the removed MP2 Laplace section and illustration stay removed.
- `chapter-notation-audit.md` records the review of all notation families.
  Standardized spin-component C superscripts, AO core matrix bH, UHF operator
  hats/commands, introductory spin-operator commands, the spatial HOMO name,
  and ECP operator hats. The two general AO exercises now explicitly name
  spin-AO functions chi_mu^AO rather than extending spatial phi to spin space.
- Updated the glossary for barred spin partners, AO versus MO Fock matrices,
  MOM's local overlap matrix, the author's E_H notation, and the retained
  density conventions. GHF's half-charge block is not conflated with the
  full spinor or RHF/UHF charge density.
- Removed the orphan positive-gap glossary entry and now-uncited Almlof
  reference after the author's Laplace removal. The retained bibliography
  has 85 cited entries (81 audited articles/contributed chapters).
- Added `scripts/check_chapter_notation.py`. Its comparison against
  `fe1d3c7` retains all 607 displays in order and permits only the 11
  explicitly documented notation-only display updates. All other factors,
  signs, indices, contractions, and Further reading are unchanged. The
  lexical guard keeps the classification table's two-spin block subscripts
  distinct from single-spin coefficient-matrix labels.
- All seven checks pass, including all 30 figure/table callouts. Compilation
  succeeds to 128 PDF pages without undefined citations/references, BibTeX
  warnings, or overfull boxes. The glossary remains three pages. The PDF
  skill guided targeted checks of the glossary, explicit spin-AO expansion,
  and UHF/GHF operator/matrix passages, not a full visual audit.

## Superscript spin-population convention (18 October 2026)

- Pulled main through `10cd1aa`. Checked both chapter sources, biography
  source, and chapter-figure LaTeX assets: the equations already use
  N^alpha/N^beta and the generic N^sigma consistently. Removed the glossary's
  contradictory allowance for subscript spin counts and explicitly fixed
  the superscript convention, including its generic sigma form.
- Extended the source-convention check to reject unbraced/braced subscript
  alpha/beta/sigma population counts in those chapter sources. It ignores
  comments and leaves unrelated subscripts (shell counts, significant
  integrals, grid points, core-electron counts, etc.) untouched.
- No equation, derivation step, reference, or lecture deck was changed.

## Compact notation glossary (18 October 2026)

- Pulled the current main branch (`d83c46b`) before editing. Expanded the
  existing notation table, retaining its label and number, into a three-page
  glossary with repeated column headings and the existing dark-green palette.
  Topic groups cover particles/indices, operators/energies, integral brackets,
  AO matrices/densities, numerical parameters, Gaussian basis/integral symbols,
  and RI/local symbol reuses.
- Made spin-orbital versus spatial sums, RHF/UHF/GHF density normalization,
  the half-charge GHF block, physicists'/chemists'/antisymmetrized brackets,
  real-orbital ERI symmetry, MP2 denominator/gap signs, and overloaded symbols
  explicit. No chapter notation or derivation was changed.
- Added longtable for one multipage table rather than adding numbered tables.
  Extended the existing label/callout check to recognize longtable, preserving
  its normal verification requirements.
- All six checks pass. All 613 existing displays, all 31 figure/table prose
  callouts, and Further reading are preserved. A separate exact source
  comparison confirms that the chapter body after the glossary is unchanged;
  the only preamble change is loading longtable.
- Full compilation succeeds (130 PDF pages), without undefined citations,
  cross-references, BibTeX warnings, or overfull boxes. The PDF skill guided
  targeted verification of the three glossary pages only; the rest of the
  document was not subjected to a new visual audit.

## MP2, AO-to-MO transformation, and Laplace narrative (17 October 2026)

- Expanded section 1.7.6 in place, following PDF slides 45--53 of the
  author's specified post-HF lecture. `chapter-posthf-coverage.md` records
  every slide's destination, source hashes, notation decisions, and image
  provenance. The original direct/exchange illustration is retained and
  called out in prose; no replacement illustration was designed.
- Connected the second-order spin-orbital expression to the RHF spin sum,
  explained direct/exchange contributions and the factor of one quarter,
  and separated quartic energy accumulation from the conventional
  fifth-order transformation cost. Included the naive eighth-order method,
  all four one-index contractions, initialization/buffer reuse, work/storage
  accounting, and the occupied--virtual integral block needed for MP2.
- Made the Laplace slide's sign correction explicit: the excitation gap
  D=-Delta is positive, the energy has a minus prefactor, occupied dressing
  uses +epsilon*t/2 and virtual dressing uses -epsilon*t/2. Included the
  quadrature and the original links to locality, RI, and stochastic sampling,
  without claiming automatic lower scaling from a bare Laplace transform.
- Retained chapter notation (N electrons, K spatial basis functions), physics
  commands, semantic colors, standalone align/equation-split conventions,
  and absence of sentence punctuation in displays. Further reading is unchanged.
- Added the two original algorithm references identified in the slides,
  verified against publisher-deposited DOI metadata. There are now 86 cited
  references, including 82 audited articles/contributed chapters.
- Added `scripts/check_chapter_mp2.py`. All 256 transformed integrals agree
  between naive and four-stage evaluation; spin-orbital, ordered-pair, and
  RHF MP2 energies agree; Laplace integration agrees within 9.66e-15.
- All six checks pass. The 583 displays present after the approved equation
  corrections remain in order; there are 30 added displays across the new
  exercise and MP2 discussion. All 31 figures/tables have prose callouts.
  Existing exercise/solution and scientific illustration environments are
  also retained exactly relative to `d19d2af`.
- Full compilation succeeds (128 pages) without undefined citations,
  cross-references, or BibTeX warnings. Targeted rendered-page checks cover
  the new exercise, energy/diagram, four transformations, Laplace formulas,
  and corrected AO-energy bra. No full-document visual audit was performed.

## Detailed HF-stationarity exercise (17 October 2026)

- Added an exercise/solution immediately after the existing Fock-operator
  derivation, without shortening or moving that derivation. The solution
  expands the energy in coordinates, differentiates each conjugate occurrence
  in the Coulomb and exchange terms, derives the constraints and Hermitian
  multiplier matrix, and obtains the occupied--virtual gradient and
  Brillouin condition. It distinguishes stationarity from stability.
- Extended the independent algebra check with 48 central finite-difference
  checks of the separate one-electron, Coulomb, and exchange derivatives
  along real and imaginary orbital variations.
- The source-layout comparison against `d19d2af` preserves all 583 existing
  displays and Further reading; the new equations are additions. Source
  conventions and compilation pass.

## Approved equation corrections (17 October 2026)

- Applied the author's explicit approval of M1--M3 in the scientific audit:
  removed three redundant coefficient conjugations inside AO-energy bras,
  replaced AO-style phi by spatial-MO psi in the singlet/triplet spatial
  factors (and their introductory sentence), and restored both explicit
  matrix-product dots in the transformed eigenvalue equation.
- Final energy/density contractions, spin factors, relative signs, and all
  intervening derivation steps are unchanged. The audit report records the
  approval while retaining the original findings as a historical record.

## Scientific consistency and editorial continuity (17 October 2026)

- Pulled the author's changes through `faf8986` ("up to 2") and used that
  revision as the preservation baseline. The new MP2/AO-to-MO backlog items
  are outside this audit/editorial request and were not added.
- Recorded a cross-chapter scientific review in `chapter-scientific-audit.md`.
  Three displayed-equation changes are explicitly proposed for approval:
  double conjugation in the intermediate AO-energy bra expansion, spatial-MO
  symbols in two spin-adaptation displays, and two missing matrix-product
  dots. No displayed mathematical expression was changed in this pass.
- Clarified existing assumptions in prose: BO derivative terms, constant
  exchange phase, real-orbital ERI symmetry, spin-including versus spatial
  AO labels, Koopmans relaxation bounds, reference versus auxiliary-ground
  eigenvalues, unitary phase invariance, real population/direct-SCF formulas,
  H2 nuclear constants and finite-overlap localization, primitive
  normalization, ECP local-channel corrections, and screening accuracy.
- Smoothed transitions at changes of representation, reduced repeated
  introductory summaries, distinguished the two existing CBS extrapolations,
  and qualified what Aufbau/MOM procedures actually guarantee. Section
  ordering, examples, exercises/solutions, illustrations, colors, cover,
  biographies, bibliography, and Further reading are preserved.
- Added `scripts/check_chapter_hf_algebra.py`: determinant norms, RHF spin
  factors, Li/B pair counts, IP/EA signs and decompositions, orbital-energy
  double counting, complex trace order, spin-adaptation phases, H2 curvature,
  and counterexamples documenting the two complex-orbital issues.
- All five checks pass; all 583 baseline displays and Further reading are
  preserved, all 30 figures/tables are called out, and all 84 bibliography
  entries remain cited. A separate exact comparison preserves all exercise,
  solution, figure, table, and TikZ environments.
- Full compilation succeeds (122 pages), with no undefined citations or
  references and no BibTeX warnings. The PDF skill guided targeted checks of
  the revised H2 and Gaussian-contraction passages, not a full visual audit.

## Systematic equation highlights and alignment convention (16 October 2026)

- Retained the author's four existing boxed takeaway statements and added
  43 targeted highlights across HF, basis functions, and molecular integrals.
  The chapter now has 47 uses of `\boxed`: principal defining/working
  equations and conceptual takeaways are highlighted; intermediate algebra
  and repeated formulas are not. In multiline derivations, only the final
  expression is boxed. No extra frame is added inside a colored theorem box,
  and existing exercise/solution styling and semantic colors are unchanged.
- Highlights cover the determinant ansatz, orbital expansion, HF energies,
  integral notation, Fock operator, canonical and matrix equations,
  orthogonalization, IP/EA corrections, density, SCF/DIIS/MOM working results,
  Pople--Nesbet equations, GHF spinors and variational hierarchy, plane waves,
  primitive/contracted Gaussians, CBS extrapolation, counterpoise correction,
  fundamental ERIs, Boys functions, contracted HRRs, screening, and RI.
- At the author's clarification, replaced all 41 equation/aligned groups:
  40 parallel groups now use standalone align; the continued UHF energy
  expression uses equation/split. The paired boxed Pople--Nesbet equations
  use two native align rows. No notag or nonumber commands were introduced.
  Equation numbers and existing references update automatically.
- Updated the equation formatter and layout checks to enforce this convention
  and prevent redundant boxed equations inside theorem panels. Content
  comparison ignores only the balanced outer boxing delimiters, in addition
  to the existing layout tokens: all 594 displays from `0682a1e` are preserved
  in order. Mathematical expressions, derivation steps, explicit matrix dots,
  notation commands, prose, bibliography, cover, and Further reading remain
  unchanged.
- Full compilation succeeds (115 pages). All four chapter checks pass, with
  no undefined citations/references or BibTeX warnings. The PDF skill was used
  for targeted checks of the new highlights, including determinant, density/
  Fock, Pople--Nesbet, and integral/Boys-function results; no full-chapter
  layout audit was undertaken.

## Author-requested presentation revision (16 October 2026)

- Pulled the author's updates through `0a74b5c` before editing. Retained the
  new spin material, notation changes, and removal of the old closed-shell
  hydrogen occupation figure. The approved cover remains unchanged.
- Added a gold abstract box identifying ESQC 2026, the doctoral audience,
  and the scope of the two lecture presentations.
- Completed prose callouts for every existing figure/table. Added captions
  and labels in place to nine previously unnumbered scientific diagrams and
  the correlation-consistent shell-content table. The resulting 29 numbered
  figures/tables all have prose references. The Further reading book images,
  ESQC group photograph, cover, and inline theorem portraits are not numbered
  scientific figures.
- Replaced all 108 top-level align environments by equation/split or, for
  genuinely parallel columns, equation/aligned. Removed all notag/nonumber
  commands. Independent formulas formerly separated by manual quad spacing
  use aligned rows/columns; logical arrows and mathematical enumerations
  retain appropriate spacing. Equation numbers and cross-references update
  automatically. Explicit matrix multiplication dots are preserved.
- Added blue boxes for Pauli exclusion, Brillouin, Koopmans, variational
  bounds, and the Gaussian product theorem, distinct from violet exercises
  and green solutions. Authenticated historical portraits accompany the
  three named results; printed credit/license links and asset provenance are
  recorded in `chapter-figures/portraits.md`. Full derivations, including the
  exact IP/EA decompositions, remain outside or inside their original context.
- Systematized numbered headings, with separate subsections for Slater--Condon
  rules and spin symmetry, and subsubsections for major SCF, orbital-analysis,
  dissociation, and integral topics. Derivation cases remain paragraphs.
  No existing prose or illustration was reordered.
- Added four DOI-verified correlated-method references at the relevant CI,
  coupled-cluster, and MP passages. Further reading is byte-for-byte unchanged.
- `scripts/check_chapter_layout.py --compare-math 0a74b5c` verifies that all
  593 original displays remain in order, modulo layout-only tokens, while
  allowing the new Koopmans summary. It also checks labels, callouts,
  unresolved references, and the absence of legacy equation environments.
  The source-convention, reference, and numerical integral/RI/GHF checks pass.
- Full compilation succeeds (114 pages), with no undefined citations or
  cross-references and no BibTeX warnings. The PDF skill was used for targeted
  checks of the abstract, five theorem-box designs, new inline captions/table,
  and added bibliography entries, not a full-chapter overflow audit.

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

### Gaussian cover illustration review

- Prepared a separate one-page preview of the author's selected overlapping
  Gaussian concept: three analytic Gaussian profiles with translucent green
  fills, replacing only the decorative motif in a draft cover variant.
- Preserved all title-page typography and wording. The profiles are decorative,
  with arbitrary scales, rather than a normalized basis-set specification.
- Compiled the preview and inspected its rendered page using the PDF skill.
  The active cover and all chapter sources remain unchanged pending approval.

#### Different exponents, colors, and a 3D surface

- Revised the preview to the sum of two two-dimensional Gaussian functions,
  shown in perspective. Exponents 2.0 and 0.5 in arbitrary display units
  distinguish a narrower and broader contribution. Green/blue surface colors
  encode their relative weights, with a fine mesh to clarify the 3D shape.
- Kept this revision in the separate review document, leaving the current
  chapter cover unchanged. The preview compiles and its rendered page was
  inspected using the PDF skill.

#### Separated Gaussians and their product

- Replaced the combined-sum preview with three separate smooth surfaces:
  a green Gaussian, a broader blue Gaussian, and their amber pointwise product.
  Increased center separation to 2.8 display units; exponents are 0.6 and 0.3.
- Removed the mesh and used transparent fills. Kept unit peaks for the original
  Gaussians and the true unscaled product height (about 0.2085), centered at
  x = -0.4667, consistent with the Gaussian product theorem. Tails below 0.008
  are omitted for clean decorative outlines.
- Verified the direct product against its completed-square form at 18 points.
  Preview compilation and PDF-skill visual inspection pass. Cover wording and
  typography are preserved; the active cover remains unchanged pending approval.

#### One-dimensional Gaussian product cover preview

- At the author's request, returned the illustration to 1D: two separated
  green/blue Gaussian curves with different exponents and their amber product,
  with translucent fills. Retained the exact functions and unscaled product
  from the preceding design, evaluated along y=0 over [-6,6].
- Removed the 3D plotting dependency from the preview; the illustration is
  native TikZ. All cover wording and typography remain identical.
- Compiled the review PDF, verified the product identity and unchanged cover
  text, and inspected the rendered page using the PDF skill. The active cover
  remains unchanged pending approval.

#### Approved 1D cover incorporation (14 October 2026)

- Incorporated the author-approved 1D Gaussian/product design into the active
  `chapter-titlepage.tex`, without changing its curves, colors, transparency,
  typography, or wording. Retained the separate review as an approval record.
- Verified the active cover against the approved draft, compiled the full
  chapter, ran the existing source/reference checks, and inspected the compiled
  title page using the PDF skill. Chapter content and scientific figures are
  unchanged.

## Figure captions, labels, running head, and STO-3G presentation

- Expanded Figure 1's caption to define the particle labels, common origin,
  absolute position vectors, relative displacements and their directions,
  and the corresponding distances. Retained its textbook acknowledgment.
- Fixed the UHF alpha/beta labels in Figure 2 by anchoring them above the
  first orbital boxes. In Figure 6's Schmidt panel, replaced the duplicate
  first-vector labels with the explicit equality phi_1 = phi'_1.
- Shortened the running head to `Hartree--Fock Theory` without changing the
  document title or cover. All chapter derivations are unchanged.
- Converted the hydrogen STO-3G excerpt into a native table (Table 3), keeping
  every digit of its three exponents and coefficients. All six values match
  the Basis Set Exchange STO-3G hydrogen JSON definition exactly. The original
  STO/STO-3G plot is retained as a numbered figure (Figure 13), with a caption
  identifying the STO, contraction, and weighted primitive Gaussian curves.
- Verification: full 106-page compilation and all three existing checks pass;
  displayed derivations match the preceding commit. The PDF skill was used
  to inspect only the changed figure/table pages. No full-chapter layout audit
  was performed. The active Gaussian cover remains unchanged.

## Author revision and exercise/solution boxes (15 October 2026)

- Fast-forwarded to the author's five new commits through `59f942d` and read
  the changes before editing. Preserved the new mean-field illustration,
  anyon discussion, ESQC photograph, acknowledgements, revised notation,
  and prose/section adjustments.
- Framed all 13 existing worked-example statements and their full solutions
  with distinct violet exercise and dark-green solution boxes. Long solutions
  can break across pages, with repeated identifying continuation headings.
  Ordinary explanatory prose remains outside the boxes. No exercises or
  derivation steps have been removed or added.
- Kept the text width effectively unchanged inside the frames to preserve
  the mathematical layout. Every displayed derivation matches the user's
  pushed version exactly; all 13 statement/solution pairs are balanced.
- Full compilation and existing source/reference checks pass. The PDF skill
  was used to inspect representative short, long, and continued solution
  boxes, not to perform a full-chapter layout audit.

## Historical-reference expansion (15 October 2026)

- Added 16 verified primary sources, bringing the bibliography to 70 cited
  entries (66 articles/contributed chapters and four books). Added citations
  beside their relevant discussions, with brief historical context for the
  original HF construction and the development of Gaussian basis functions.
- Covered Pauli's exclusion principle and spin-statistics theorem, Dirac's
  fermionic wavefunctions, Slater's 1930 HF note and screened orbitals,
  Brillouin's original article, open-shell SCF, density-matrix theory,
  HF stability, Gaussian expansions/contraction, and density fitting/RI.
  Added the original Leinaas--Myrheim and Wilczek sources for the author's
  new anyon discussion.
- Checked publication identity and complete author lists against publisher-
  deposited DOI metadata; clarified DOI details and recorded all additions
  in `chapter-reference-audit.md`. No unverified references were retained.
- Full compilation resolves citations and cross-references. All three checks
  pass. The PDF skill was used to inspect representative new bibliography
  pages and confirm accent/math typography.
- At the author's explicit direction, retained the normalized determinant
  relation in Eq. `eq:hf-determinant` and changed the antisymmetrizer's
  coefficient from 1/N! to 1/sqrt(N!). Clarified that this normalization-
  weighted convention is not the idempotent projector convention. This is
  the sole change to a displayed derivation relative to the author's pushed
  version; all other displayed mathematics is preserved.

## Original cover proposal (15 October 2026; awaiting approval)

- Created a separate orbital-atlas cover preview with a six-center Gaussian
  combination, contrasting teal/amber phase contours, and a pale-blue
  envelope. This is original schematic art, not a computed HF orbital,
  electron density, or identified molecule. The vector paths and generator
  remain editable; the saved preview compiles without Python dependencies.
- Preserved the active cover's wording, typography, and dark-green palette.
  Compiled and visually inspected the standalone one-page PDF. The PDF skill
  informed this targeted preview review, not a full-chapter layout audit.
- The active `chapter-titlepage.tex` remains unchanged. The proposal is
  explicitly marked as awaiting author approval before incorporation.

## Approved porphine cover integration (15 October 2026)

- Incorporated the author's approved mathematical porphine rendering in
  `chapter-titlepage.tex`, replacing only the previous Gaussian-product art.
  The image is an unmodified copy of the approved transparent render in
  `chapter-figures/cover-porphine-gaussians.png`. Earlier cover alternatives
  remain archived; no original assets have been deleted.
- Preserved all title-page wording, text positions, font sizes, author and
  affiliation details, ESQC 2026 branding, footer, and dark-green framing.
  The image's transparent margins allow it to sit above the author block
  without overlap. Chapter text, equations, and bibliography are unchanged.
- The illustration contains normalized real s/p/d/f/g Gaussian functions
  on PubChem porphine coordinates. Formulae, exponents, source data,
  signed-isosurface checks, and the native editable scene remain documented
  in `drafts/cover-studies/06-porphine-exact-gaussians.md`.
- Full compilation succeeds (110 pages) with resolved citations and
  cross-references; all three chapter checks pass. The PDF skill was used
  for a targeted inspection of the changed cover page, not a full-chapter
  layout/overflow audit. Chapter compilation requires only the saved PNG,
  not Blender or NumPy.

## Uniform white cover background (15 October 2026)

- At the author's request, removed the pale-green lower-page panel from
  the active cover. The existing illustration already has a genuine alpha
  channel; no image replacement, recoloring, or background removal was needed.
- Retained the approved illustration, its placement, all cover typography,
  the dark-green side stripe, rules, and wording. Chapter content is unchanged.
- Full 110-page compilation and all three chapter checks pass. The PDF skill
  was used to inspect only the updated cover; pixel samples confirm the same
  white background above, beside, and through the transparent image regions.

## Targeted reference additions (16 October 2026)

- Added the ten author-approved references: Lowdin (1959), Lehtola (2019),
  Saunders--Hillier (1973), Fukutome (1981), Payne et al. (1992), Krishnan
  et al. (1980), Clark et al. (1983), Frisch et al. (1984), Gill (1994),
  and Weigend (2002). Each is cited at the existing relevant passage;
  the Fukutome designations receive a short explicit attribution.
- The bibliography now contains 80 cited entries: 76 audited articles or
  contributed chapters and four books. Recorded publication provenance,
  placement rationale, and Lowdin's digitized-date discrepancy in
  `chapter-reference-audit.md`. Existing figure/table credits are unchanged.
- Preserved Further reading byte-for-byte, including all four book citations
  and images. Did not add the optional Lehtola et al. (2020) review. All
  522 main-text and 87 basis/integral displayed derivations are unchanged;
  other existing prose differs only by the inserted citations.
- Integrated the author's newer remote commit `bc323cc` before pushing,
  retaining its starred `physics` overlap command. Rechecked preservation
  against that latest remote version, including Further reading and all
  displayed derivations.
- Full compilation succeeds (110 pages); all ten additions appear in the
  compiled bibliography, with no undefined citations or references and no
  BibTeX warnings. All three chapter checks pass. The PDF skill was used
  for a targeted check of the bibliography pages containing the additions,
  not a full-chapter layout/overflow audit. The cover is unchanged.

## Historical biographies (17 October 2026)

- Pulled the author's `ddf6742` changes before editing. Preserved the moved
  Pauli theorem panel, revised spin discussion, equation layouts, and prose.
- Added eleven short biographies near their relevant discussions: Hartree,
  Fock, Pauli, Slater, Condon, Brillouin, Koopmans, Roothaan, Hall, Lowdin,
  and Boys. Warm terracotta boxes distinguish historical context from blue
  theorems, violet exercises, and green solutions. Box definitions and text
  are kept separately in `chapter-biographies.tex` for easy author editing.
- Included eight authentic archival portraits, with institutional biography
  links, photo credits, and reuse statements. Roothaan and Slater use the
  Chicago archive's educational/scholarly permission, not a CC license;
  commercial publication will need separate permission. Fock, Hall, and Boys
  currently have linked institutional portrait sources only, because their
  reproduction permissions are not specified. Full provenance and this
  remaining task are recorded in `chapter-figures/portraits.md` and `todo.md`.
- Existing chapter text and all 584 displayed equations are preserved, as is
  Further reading byte-for-byte. The citation checker now reads the new
  biography file; all 84 bibliography entries remain cited and verified.
- The complete chapter compiles to 117 pages without undefined citations or
  references. All four source/reference/layout/integral checks pass. The PDF
  skill was used for a targeted inspection of the new biography boxes, not
  a full-chapter visual or overflow audit. The approved cover is untouched.

## Author-approved draft portraits (17 October 2026)

- Pulled before editing; the remote was up to date at `4d7a1db`.
- At the author's explicit request, added the IAQMS portraits of Fock, Hall,
  and Boys as credited draft reproductions. Each box prints a bold
  "Draft reproduction: permission pending" warning. No reuse license,
  photographer identity, or image date is invented. Provenance records the
  original image URLs and the need for rights clearance before final publication.
- All eleven biographies now have portraits. The three biography texts,
  existing chapter text, 584 displayed equations, and Further reading are
  unchanged. The cover and bibliography are untouched.
- Full compilation succeeds at 117 pages. All four chapter checks pass,
  with no undefined citations or references. The PDF skill was used only for
  targeted review of the three updated biography boxes and their notices.

## Notation reference and concluding synthesis (17 October 2026)

- Pulled before editing; the remote was up to date at `04246c6`.
- Added a one-page "Notation and conventions" reference after the contents,
  retaining Roman front-matter numbering. Its numbered, labeled table is
  explicitly cited and reuses the chapter's symbols, custom macros, physics
  commands, and AO/MO/spin-orbital colors. It distinguishes occupation
  conventions and contextual reuse of symbols, notably the density matrix
  and Gaussian product center. Both new headings appear in the contents.
- Added a short concluding perspective connecting the HF variational space,
  orbital-basis incompleteness, integral evaluation and approximations, and
  SCF convergence. Cross-references point back to the relevant derivations;
  no new scientific topics or bibliography entries were introduced.
- Preserved all existing chapter prose, examples, illustrations, and 584
  displayed equations. Further reading is byte-for-byte unchanged, as are
  the approved cover and biography boxes.
- Full compilation succeeds at 119 pages, without undefined references or
  citations. All four chapter checks pass; 30 figures/tables are labeled and
  cited in prose. The PDF skill guided targeted inspection of the two new
  additions only, not a full-chapter layout audit.

## Additional historical perspectives (17 October 2026)

- Pulled before editing; the remote was up to date at `ffb2f8d`.
- Integrated the author's newer `be397cf` commit before pushing, preserving
  its full-width Basis Set Exchange figure. Repeated the source-preservation,
  equation, reference, and compilation checks against that newer baseline.
- Added all eight proposed perspectives: Born/Oppenheimer, Mulliken,
  Coulson/Fischer-Hjalmars, Pople/Nesbet, Pulay, Moller/Plesset, Huzinaga,
  and Dunning. There are now 23 people in 19 historical boxes. Each member
  of a pair has a separately identified portrait and biographical paragraph.
- Placed the boxes beside the relevant existing topics: separation of nuclear
  and electronic motion, population analysis, hydrogen dissociation, UHF matrix
  equations, DIIS, the perturbation partition, Gaussian basis construction,
  and correlation-consistent basis sets. The earlier eleven biographies and
  all pre-existing chapter prose remain unchanged.
- Verified institutional biographies and original papers; in particular, the
  Coulson--Fischer publication date follows the 1949 original rather than the
  inconsistent date in a retrospective obituary. Omitted Huzinaga's birth year
  instead of resolving conflicting secondary birthday accounts by guesswork.
- Located an explicitly labeled Huzinaga portrait in a Yamada Science
  Foundation report and a labeled Nesbet portrait in an author profile.
  The Huzinaga source page retains its original three image streams
  byte-for-byte; only malformed invisible OCR and unused font resources were
  removed to avoid PDF-reader warnings. No likenesses were generated.
- Recorded all twelve portrait sources, credits, and reuse terms in
  `chapter-figures/portraits.md`. Seven new portraits use the author-approved
  draft policy with explicit permission-pending notices, in addition to the
  previous three. Open-license portraits retain their license links and credits.
- Preserved all 584 displayed equations, the notation reference, conclusion,
  approved cover, and Further reading. No bibliography entries were added;
  all 84 retained entries remain cited and the reference check passes.
- Full compilation succeeds at 121 pages, without undefined citations or
  references. All four chapter checks pass. The PDF skill guided targeted
  inspection of the eight new boxes, not a full-chapter visual audit.
## Paragraph-flow harmonization (20 October 2026)

- Pulled the author's latest revisions through `40ab2e4` before editing.
  Preserved the main source byte-for-byte up to the SCF-algorithm subsection,
  including all newly revised equations and highlights.
- Removed 38 unnecessary paragraph boundaries in the later HF discussion and
  28 in the basis-set/integral material. Related explanations now continue
  across displays and short figure/table introductions without artificial
  paragraph breaks. Retained meaningful topic changes and exercise/solution
  boundaries; did not rewrap source lines or alter mathematical alignment.
- Every nonblank source line is byte-for-byte identical to the author baseline.
  All 633 displays, derivation steps, figures, tables, headings, citations,
  historical boxes, and Further reading are unchanged.
- All seven chapter checks pass, including baseline mathematical preservation
  and the 85 hyperlinked reference titles. Full compilation succeeds at 134
  pages, with no undefined citations/references or overfull-box warnings.
  The PDF skill guided a targeted check of the initial-guess/convergence and
  plane-wave pages only, not a full visual audit.

## Numbered SCF algorithm summary (20 October 2026)

- Pulled before editing; the author's remote was unchanged at `d980bab`.
- Added Algorithm 1 beside the RHF SCF discussion: an editable, one-page
  dark-green card with colored numbered badges, separate setup/iteration/output
  bands, and eight referenceable steps. The existing flow diagram is retained.
  The orthogonalization, initial-guess, convergence, and DIIS explanations now
  refer to the relevant step numbers through clickable cross-references.
- The summary states the closed-shell spin-summed density convention, keeps
  every matrix-product dot, distinguishes the physical Fock build from the
  matrix used for DIIS orbital generation, and tests a matched density/Fock
  pair only after an orbital update. It separates electronic energy from
  nuclear repulsion and stationarity from stability.
- All 633 existing displays and Further reading are unchanged. All seven
  chapter checks pass; no undefined references/citations, duplicate labels,
  oversized floats, or overfull-box warnings are reported. Compilation succeeds
  at 135 pages. Verified all eight step numbers and distinct hyperlink targets.
- The PDF skill guided targeted rendering of the complete algorithm card on
  printed page 72 (PDF page 79); it fits on one page without clipping.

## Matching unrestricted SCF summary (20 October 2026)

- Pulled the author's `fa5ce38` revision before editing, preserving its
  orthogonalization-figure changes. The approved RHF panel is unchanged.
- Reused the same algorithm-card environment for Algorithm 2, with the same
  eight steps, green setup/output bands, blue iteration band, and numbered
  badges. Added linked step references in the unrestricted SCF discussion.
- The UHF card specifies fixed superscript spin populations, a common AO
  metric, two coupled physical Fock builds, the spin-resolved energy trace,
  both commutator residuals, separate orbital occupations, and spin densities
  without an RHF factor of two. The physical density/Fock pairs remain distinct
  from DIIS working matrices. Output distinguishes electronic and total
  molecular energies and includes the spin expectation value.
- Extended the independent algebra checks with the UHF half-trace energy
  identity for three spin occupations and an AO-metric counterexample in
  which the alpha residual vanishes while the beta residual does not.
- All seven chapter checks pass. All 633 existing displays, the basis/integral
  material, bibliography, and Further reading are unchanged. Compilation
  succeeds at 136 pages, with no undefined citations/references, duplicate
  labels, oversized floats, or overfull-box warnings.
- The PDF skill guided targeted review of the complete UHF card on printed
  page 89 (PDF page 96). It fits on one page; verified all eight step numbers
  and their distinct hyperlink targets.
