# Chapter reference verification

## Five further historical perspectives (21 October 2026)

Added the four primary articles below for William Hartree, Bertha Swirles,
and Dirac. Author lists, titles, years, volumes, issues, page ranges, and DOIs
were checked against publisher-deposited Crossref records on 20 October.
The archive records and MacTutor biography confirm that the published
W. Hartree is William, Douglas's father, not another Hartree namesake.
The journal name for Dirac's paper retains its historical Proceedings title,
rather than the publisher database's modern Mathematical Proceedings name.

Dirac's original 1930 text was consulted through the Cambridge-hosted PDF,
including its discussion of the density matrix and orbital-transformation
invariance. The two Royal Society source records for Swirles's work were
also checked; no claim of unrestricted full-text access to those papers is
made. Relativistic SCF and configuration superposition are identified as
extensions beyond the ordinary non-relativistic single-determinant model.
McWeeny (1960) and Boys--Bernardi (1970) are retained existing citations,
not newly attributed discoveries or duplicate bibliography entries.

Biographical sources are linked in each historical panel: Hill's first-hand
William Hartree obituary, the St Andrews biographies, Girton's John Davies
tribute, the IAQMS obituary by Sutcliffe and Robb, and Bernardi's author
profile in the 1996 Chemical Society Reviews article. The indexed author
profile identifies his Cambridge period as 1969--1971; unverified lifespan
dates have not been supplied. Access to the Bernardi source image was
unsuccessful and no substitute/generated likeness is used.

The bibliography now contains 92 cited entries: 88 audited articles/contributed
chapters and four books. Further reading is unchanged.

| BibTeX key | Publication title | DOI record |
| --- | --- | --- |
| `HartreeHartree1935` | Self-consistent field, with exchange, for beryllium | [10.1098/rspa.1935.0085](https://doi.org/10.1098/rspa.1935.0085) |
| `Swirles1935` | The relativistic self-consistent field | [10.1098/rspa.1935.0211](https://doi.org/10.1098/rspa.1935.0211) |
| `HartreeHartreeSwirles1939` | Self-consistent field, including exchange and superposition of configurations, with some results for oxygen | [10.1098/rsta.1939.0008](https://doi.org/10.1098/rsta.1939.0008) |
| `Dirac1930` | Note on Exchange Phenomena in the Thomas Atom | [10.1017/S0305004100016108](https://doi.org/10.1017/S0305004100016108) |

## Berthier's independent UHF contribution (20 October 2026)

Added Berthier's original 1954 paper beside Pople and Nesbet's existing
reference and in his new historical box. Author, title and subtitle, year,
journal, volume, pages, and DOI were verified against
[EDP Sciences-deposited Crossref metadata](https://api.crossref.org/works/10.1051/jcp/1954510363).
The publisher landing page and full text were access-restricted; no full-text
inspection is claimed. The 1954 UHF contribution, later work with Bernard
Levy, dates, and role in the French theoretical-chemistry community were
checked against [Yves Ellinger's first-hand obituary for the Societe Francaise
d'Exobiologie](https://exobiologie.fr/deces-de-gaston-berthier/).
The independent 1954 contributions are credited through the chapter's
Pople--Nesbet--Berthier terminology, without asserting an exact priority date.
The bibliography now contains 88 cited entries: 84 audited articles/contributed
chapters and the four retained books. Further reading is unchanged.

| BibTeX key | Publication title | DOI record |
| --- | --- | --- |
| `Berthier1954` | Configurations electroniques incompletes: Partie I. La Methode du Champ Moleculaire Self-Consistent et l'Etude des Etats a Couches Incompletes | [10.1051/jcp/1954510363](https://doi.org/10.1051/jcp/1954510363) |

## Title hyperlinks (19 October 2026)

The chapter's local `chapter-unsrtnat.bst` is a renamed, documented derivative
of Patrick W. Daly's natbib `unsrtnat.bst` 1.93, retaining its original license
and attribution. It preserves the citation-order reference format and links
each title to its DOI resolver target, with a URL fallback. Standalone DOI
and URL text is omitted; no existing DOI field or bibliographic metadata
has been removed or changed.

Added publisher URLs for the three books with no DOI in the existing file:

- `Jensen2017`: [Wiley-VCH publisher record](https://www.wiley-vch.de/en/areas-interest/natural-sciences/introduction-to-computational-chemistry-978-1-118-82599-0), identifying Frank Jensen, third edition, February 2017, ISBN 978-1-118-82599-0.
- `Cramer2004`: [Wiley-VCH publisher record](https://www.wiley-vch.de/en/areas-interest/natural-sciences/essentials-of-computational-chemistry-978-0-470-09182-1), identifying Christopher J. Cramer, second edition, September 2004, ISBN 978-0-470-09182-1.
- `SzaboOstlund1996`: [Dover publisher record](https://store.doverpublications.com/products/9780486691862), whose current page identifies Modern Quantum Chemistry and ISBN/SKU 9780486691862. The original author/year metadata is retained, not inferred from the limited extracted product-page text.

All 85 rendered reference titles have exactly one link to their stored
target: 82 DOI links and three publisher URLs. All targets are present in
the compiled PDF's link annotations. Removing only the hyperlink wrappers
and the former standalone DOI blocks recovers every original reference's
title, authors, publication details, and order. The source check can repeat
the rendered-link verification with
`python3 scripts/check_chapter_references.py --check-bbl` after compilation.
The count of audited articles/contributed chapters remains 81; no source has
been added or removed, and Further reading is unchanged.

## Author's MP2 revision (18 October 2026)

The author removed the MP2 Laplace subsection in `fe1d3c7`. Its now-uncited
Almlof (1991) entry has therefore been removed from the retained bibliography
and DOI table. The previous verification remains historical evidence, not
an active chapter citation. Frisch--Head-Gordon--Pople (1990) remains cited
for the retained AO-to-MO algorithm. The current bibliography contains
85 cited entries: 81 audited articles/contributed chapters and four books.
Further reading is unchanged.

## MP2 algorithm additions (17 October 2026)

Added the two original algorithm papers identified in the author's post-HF
slides: Frisch, Head-Gordon, and Pople for the semi-direct AO-to-MO
transformation, and Almlof for the Laplace representation. Author lists,
titles, years, volumes, issues, and page ranges were verified against
Elsevier-deposited metadata from the Crossref works API on this date.
Publisher search records independently confirm both article identities;
full publisher pages returned access errors, so no claim of full-text
verification is made. The mathematical exposition follows the author's
source slides and is independently checked numerically. The bibliography
now contains 86 cited entries, including 82 audited articles/contributed
chapters and the four retained books. Further reading is unchanged.

| BibTeX key | Publication title | DOI record |
| --- | --- | --- |
| `FrischHeadGordonPople1990` | Semi-direct algorithms for the MP2 energy and gradient | [10.1016/0009-2614(90)80030-H](https://doi.org/10.1016/0009-2614(90)80030-H) |

## Correlated-method additions (16 October 2026)

Added four references at the existing discussions of correlated wavefunction
methods, without expanding the chapter into a treatment of those methods:

- Shavitt (1998): CI and the historical development of determinant expansions.
- Cizek (1966): the original molecular coupled-cluster formulation.
- Bartlett and Musial (2007): the modern coupled-cluster review.
- Cremer (2011): the MP perturbation-theory review, alongside the retained
  original Moller--Plesset (1934) reference.

All four author lists, titles, years, volumes, issues, and page ranges were
checked against publisher-deposited DOI metadata by content negotiation.
The APS article page and the Cremer review were also consulted. Shavitt's
DOI record lists `10.1080/00268979809482290` as an alias of the retained
`10.1080/002689798168303`, not a separate article. The bibliography now has
84 cited entries: 80 audited articles/contributed chapters and four books.
Further reading is unchanged.

## Original full-bibliography audit

Verification date: 13 October 2026. This is a bibliography audit, not a
claim that every cited article has been reproduced or independently rederived.
Publisher-deposited DOI metadata was retrieved through DOI content negotiation
(`Accept: application/vnd.citationstyles.csl+json`) and compared with the
bibliography's author lists, titles, publication years, journal or book names,
volumes, and page ranges or article numbers. Publisher pages and author-hosted
papers were used to clarify incomplete metadata and citation relevance.

## Corrections and verification limits

- Removed the invalid `Schwarz1978` entry. Its DOI, `10.1007/BF00549033`,
  belongs to a 1970 histology paper by T. J. Flórez-Cossio, not an ERI paper.
  The mathematical bound is now attributed to the Cauchy–Schwarz inequality;
  the discussion of practical screening cites Häser and Ahlrichs (1989).
- Corrected Edmiston–Ruedenberg's pages from 457–465 to **457–464**.
- Replaced the unconfirmed given name of Korsell with the published initial,
  and restored the bibliographic suffix Jr. for Fægri and Dunning.
- Protected German title capitalization and mathematical/chemical abbreviations.
- The DOI resolver rate-limited Coulson–Fischer during this audit; its
  [publisher article page](https://doi.org/10.1080/14786444908521726) separately
  confirms the title, authors, volume 40, issue 303, and pages 386–393 (1949).
- The Löwdin 1970 DOI record omits the author and volume. The
  [Elsevier chapter page](https://www.sciencedirect.com/science/article/pii/S0065327608603391)
  identifies Per-Olov Löwdin, volume 5, and pages 185–199.
- RSC DOI metadata reports only the first page for the two Weigend articles;
  the publisher/author-institution records confirm 3297–3305 (2005) and
  1057–1065 (2006). AIP articles use article numbers rather than page ranges.
- IMOM is cited to Barca, Gilbert, and Gill (2018), whose
  [author-hosted paper](https://rsc.anu.edu.au/~pgill/papers/184_IMOM.pdf)
  explicitly describes the fixed-initial-reference variant. The original MOM
  citation remains Gilbert, Besley, and Gill (2008).
- Screening citations support the method, not the numerical screening table.
  That table's data and the retained illustrations come from the course slides;
  no unverified journal provenance has been assigned to them.
- DOI links are clickable in the compiled bibliography. A link establishes
  article identity, not open-access availability or permission to reuse figures.

## Verified article and contributed-chapter identities

Every retained article or contributed chapter is listed below. The bibliography
contains the full author lists and journal details; links identify the actual
publication, rather than a search-results page.

| BibTeX key | Publication title | DOI record |
| --- | --- | --- |
| `Shavitt1998` | The history and evolution of configuration interaction | [10.1080/002689798168303](https://doi.org/10.1080/002689798168303) |
| `Cizek1966` | On the Correlation Problem in Atomic and Molecular Systems. Calculation of Wavefunction Components in Ursell-Type Expansion Using Quantum-Field Theoretical Methods | [10.1063/1.1727484](https://doi.org/10.1063/1.1727484) |
| `BartlettMusial2007` | Coupled-cluster theory in quantum chemistry | [10.1103/RevModPhys.79.291](https://doi.org/10.1103/RevModPhys.79.291) |
| `Cremer2011` | Moller--Plesset perturbation theory: from small molecule methods to methods for thousands of atoms | [10.1002/wcms.58](https://doi.org/10.1002/wcms.58) |
| `Almlof1982` | Principles for a direct SCF approach to LICAO–MOab‐initio calculations | [10.1002/jcc.540030314](https://doi.org/10.1002/jcc.540030314) |
| `Barca2018` | Simple Models for Difficult Electronic Excitations | [10.1021/acs.jctc.7b00994](https://doi.org/10.1021/acs.jctc.7b00994) |
| `BeebeLinderberg1977` | Simplifications in the generation and transformation of two‐electron integrals in molecular calculations | [10.1002/qua.560120408](https://doi.org/10.1002/qua.560120408) |
| `Bennett2017` | A new generation of effective core potentials for correlated calculations | [10.1063/1.4995643](https://doi.org/10.1063/1.4995643) |
| `Bergner1993` | Ab initio energy-adjusted pseudopotentials for elements of groups 13–17 | [10.1080/00268979300103121](https://doi.org/10.1080/00268979300103121) |
| `BornOppenheimer1927` | Zur Quantentheorie der Molekeln | [10.1002/andp.19273892002](https://doi.org/10.1002/andp.19273892002) |
| `Boys1950` | Electronic wave functions - I. A general method of calculation for the stationary states of any molecular system | [10.1098/rspa.1950.0036](https://doi.org/10.1098/rspa.1950.0036) |
| `BoysBernardi1970` | The calculation of small molecular interactions by the differences of separate total energies. Some procedures with reduced errors | [10.1080/00268977000101561](https://doi.org/10.1080/00268977000101561) |
| `Burkatzki2007` | Energy-consistent pseudopotentials for quantum Monte Carlo calculations | [10.1063/1.2741534](https://doi.org/10.1063/1.2741534) |
| `Condon1930` | The Theory of Complex Spectra | [10.1103/PhysRev.36.1121](https://doi.org/10.1103/PhysRev.36.1121) |
| `CoulsonFischer1949` | Notes on the Molecular Orbital Treatment of the Hydrogen Molecule | [10.1080/14786444908521726](https://doi.org/10.1080/14786444908521726) |
| `Dunning1989` | Gaussian basis sets for use in correlated molecular calculations. I. The atoms boron through neon and hydrogen | [10.1063/1.456153](https://doi.org/10.1063/1.456153) |
| `EdmistonRuedenberg1963` | Localized Atomic and Molecular Orbitals | [10.1103/RevModPhys.35.457](https://doi.org/10.1103/RevModPhys.35.457) |
| `Fock1930` | Näherungsmethode zur Lösung des quantenmechanischen Mehrkörperproblems | [10.1007/BF01340294](https://doi.org/10.1007/BF01340294) |
| `FosterBoys1960` | Canonical Configurational Interaction Procedure | [10.1103/RevModPhys.32.300](https://doi.org/10.1103/RevModPhys.32.300) |
| `Gilbert2008` | Self-Consistent Field Calculations of Excited States Using the Maximum Overlap Method (MOM) | [10.1021/jp801738f](https://doi.org/10.1021/jp801738f) |
| `Hall1951` | The molecular orbital theory of chemical valency VIII. A method of calculating ionization potentials | [10.1098/rspa.1951.0048](https://doi.org/10.1098/rspa.1951.0048) |
| `Hartree1928` | The Wave Mechanics of an Atom with a Non-Coulomb Central Field. Part I. Theory and Methods | [10.1017/S0305004100011919](https://doi.org/10.1017/S0305004100011919) |
| `HaserAhlrichs1989` | Improvements on the direct SCF method | [10.1002/jcc.540100111](https://doi.org/10.1002/jcc.540100111) |
| `HeadGordonPople1988` | A method for two-electron Gaussian integral and integral derivative evaluation using recurrence relations | [10.1063/1.455553](https://doi.org/10.1063/1.455553) |
| `Hehre1969` | Self-Consistent Molecular-Orbital Methods. I. Use of Gaussian Expansions of Slater-Type Atomic Orbitals | [10.1063/1.1672392](https://doi.org/10.1063/1.1672392) |
| `Hehre1972` | Self—Consistent Molecular Orbital Methods. XII. Further Extensions of Gaussian—Type Basis Sets for Use in Molecular Orbital Studies of Organic Molecules | [10.1063/1.1677527](https://doi.org/10.1063/1.1677527) |
| `Helgaker1997` | Basis-set convergence of correlated calculations on water | [10.1063/1.473863](https://doi.org/10.1063/1.473863) |
| `Jensen2001` | Polarization consistent basis sets: Principles | [10.1063/1.1413524](https://doi.org/10.1063/1.1413524) |
| `Jensen2005` | Estimating the Hartree—Fock limit from finite basis set calculations | [10.1007/s00214-005-0635-2](https://doi.org/10.1007/s00214-005-0635-2) |
| `Kato1957` | On the eigenfunctions of many‐particle systems in quantum mechanics | [10.1002/cpa.3160100201](https://doi.org/10.1002/cpa.3160100201) |
| `Kendall1992` | Electron affinities of the first-row atoms revisited. Systematic basis sets and wave functions | [10.1063/1.462569](https://doi.org/10.1063/1.462569) |
| `Koopmans1934` | Über die Zuordnung von Wellenfunktionen und Eigenwerten zu den Einzelnen Elektronen Eines Atoms | [10.1016/S0031-8914(34)90011-2](https://doi.org/10.1016/S0031-8914(34)90011-2) |
| `Lowdin1950` | On the Non-Orthogonality Problem Connected with the Use of Atomic Wave Functions in the Theory of Molecules and Crystals | [10.1063/1.1747632](https://doi.org/10.1063/1.1747632) |
| `Lowdin1970` | On the Nonorthogonality Problem | [10.1016/S0065-3276(08)60339-1](https://doi.org/10.1016/S0065-3276(08)60339-1) |
| `MollerPlesset1934` | Note on an Approximation Treatment for Many-Electron Systems | [10.1103/PhysRev.46.618](https://doi.org/10.1103/PhysRev.46.618) |
| `Mulliken1955` | Electronic Population Analysis on LCAO–MO Molecular Wave Functions. I | [10.1063/1.1740588](https://doi.org/10.1063/1.1740588) |
| `ObaraSaika1986` | Efficient recursive computation of molecular integrals over Cartesian Gaussian functions | [10.1063/1.450106](https://doi.org/10.1063/1.450106) |
| `Peterson2002` | Accurate correlation consistent basis sets for molecular core–valence correlation effects: The second row atoms Al–Ar, and the first row atoms B–Ne revisited | [10.1063/1.1520138](https://doi.org/10.1063/1.1520138) |
| `PipekMezey1989` | A fast intrinsic localization procedure applicable for a b i n i t i o and semiempirical linear combination of atomic orbital wave functions | [10.1063/1.456588](https://doi.org/10.1063/1.456588) |
| `PopleNesbet1954` | Self-Consistent Orbitals for Radicals | [10.1063/1.1740120](https://doi.org/10.1063/1.1740120) |
| `Pritchard2019` | New Basis Set Exchange: An Open, Up-to-Date Resource for the Molecular Sciences Community | [10.1021/acs.jcim.9b00725](https://doi.org/10.1021/acs.jcim.9b00725) |
| `Pulay1980` | Convergence acceleration of iterative sequences. the case of scf iteration | [10.1016/0009-2614(80)80396-4](https://doi.org/10.1016/0009-2614(80)80396-4) |
| `Pulay1982` | Improved SCF convergence acceleration | [10.1002/jcc.540030413](https://doi.org/10.1002/jcc.540030413) |
| `Roothaan1951` | New Developments in Molecular Orbital Theory | [10.1103/RevModPhys.23.69](https://doi.org/10.1103/RevModPhys.23.69) |
| `Slater1929` | The Theory of Complex Spectra | [10.1103/PhysRev.34.1293](https://doi.org/10.1103/PhysRev.34.1293) |
| `Stevens1992` | Relativistic compact effective potentials and efficient, shared-exponent basis sets for the third-, fourth-, and fifth-row atoms | [10.1139/v92-085](https://doi.org/10.1139/v92-085) |
| `StuberPaldus2003` | Symmetry Breaking in the Independent Particle Model | [10.1007/978-94-010-0113-7_5](https://doi.org/10.1007/978-94-010-0113-7_5) |
| `WadtHay1985` | Ab initio effective core potentials for molecular calculations. Potentials for main group elements Na to Bi | [10.1063/1.448800](https://doi.org/10.1063/1.448800) |
| `Weigend2006` | Accurate Coulomb-fitting basis sets for H to Rn | [10.1039/B515623H](https://doi.org/10.1039/B515623H) |
| `WeigendAhlrichs2005` | Balanced basis sets of split valence, triple zeta valence and quadruple zeta valence quality for H to Rn: Design and assessment of accuracy | [10.1039/B508541A](https://doi.org/10.1039/B508541A) |
| `Whitten1973` | Coulombic potential energy integrals and approximations | [10.1063/1.1679012](https://doi.org/10.1063/1.1679012) |
| `Woon1995` | Gaussian basis sets for use in correlated molecular calculations. V. Core-valence basis sets for boron through neon | [10.1063/1.470645](https://doi.org/10.1063/1.470645) |

## Figure and table sources confirmed by the author

The author identified the book origins of Figures 1-6. Captions now credit
Szabo and Ostlund for Figure 1, the determinant/occupation diagrams, and
Figure 6, and Jensen for Figure 2. Specific book figure/page numbers have not
been assumed. The author-approved native redraws now replace these images in
the chapter, retaining the book credits. Original image files remain unchanged
for the slide decks.

Table 1 matches the orbital-coefficient columns of Table I in Henderson,
Jiménez-Hoyos, and Scuseria (2018); the density-matrix columns of that source
are not present in this chapter. The caption therefore says reproduced in
part, with the omission and notation adjustment stated explicitly. The source
table was checked in the [author preprint](https://arxiv.org/pdf/1710.00932).

Figure 10 uses the approved constraint-matrix and release-map layout, based on
Figure 1 of Burton, Thom, and Loos (2019), as
confirmed by the author and the [author preprint](https://arxiv.org/html/1903.08489v2).
Both new publication records were checked against publisher-deposited DOI
metadata and published journal issue details. Henderson's article appeared
online in December 2017 but belongs to volume 14, issue 2 (2018).

The carbon-contraction image (formerly Figure 12) is now native Table 2.
All ten exponents and ten coefficients preserve the approved transcription
exactly, including the negative ninth coefficient. The caption credits the
cc-pVTZ family to Dunning (1989) and the Basis Set Exchange data source to
Pritchard and coworkers (2019). Table 1 remains the separately acknowledged
partial reproduction from Henderson, Jiménez-Hoyos, and Scuseria.

The hydrogen STO-3G data excerpt is now a native coefficient/exponent table.
All six numbers are transcribed exactly from `fig/STO-3G.png` and independently
matched as decimal values against the
[Basis Set Exchange STO-3G hydrogen definition](https://www.basissetexchange.org/api/basis/sto-3g/format/json/?elements=1).
The table cites Hehre, Stewart, and Pople (1969) and Pritchard and coworkers
(2019). The original comparison plot is retained as a numbered figure, with
its STO, contracted STO-3G, and weighted primitive curves identified in the caption.

| BibTeX key | Publication title | DOI record |
| --- | --- | --- |
| `Henderson2018` | Magnetic Structure of Density Matrices | [10.1021/acs.jctc.7b01016](https://doi.org/10.1021/acs.jctc.7b01016) |
| `BurtonThomLoos2019` | Parity-Time Symmetry in Hartree-Fock Theory | [10.1021/acs.jctc.9b00289](https://doi.org/10.1021/acs.jctc.9b00289) |

## General books

These are textbooks, not journal articles. Editions and publication years were
checked separately against publisher/catalogue records.

- Jensen (2017), third edition: [Wiley-VCH publisher record](https://www.wiley-vch.de/en/areas-interest/natural-sciences/chemistry-11ch/computational-chemistry-molecular-modeling-11chd/introduction-to-computational-chemistry-978-1-118-82599-0).
- Cramer (2004), second edition: [Wiley-VCH publisher record](https://www.wiley-vch.de/en/areas-interest/natural-sciences/essentials-of-computational-chemistry-978-0-470-09182-1).
- Szabo and Ostlund (1996), Dover republication: ISBN 9780486691862;
  distinguished from the original McGraw–Hill publication.
- Helgaker, Jørgensen, and Olsen (2000): [Wiley book DOI](https://doi.org/10.1002/9781119019572).

## Historical and foundational reference extension (15 October 2026)

Added the following primary sources at the passages they support, rather than
as uncited bibliography padding. Publisher-deposited DOI metadata confirms each
identity, author list, year, volume, issue, and page range. Some Crossref REST
requests were rate-limited; DOI content negotiation supplied the remaining
records, with publisher pages and available abstracts used for relevance.
Slater's Hartree-method note has DOI suffix `35.210.2`, not `35.210`;
Brillouin's original article is issue 9 with DOI ending `0309037300`.

| BibTeX key | Publication title | DOI record |
| --- | --- | --- |
| `Pauli1925` | Über den Zusammenhang des Abschlusses der Elektronengruppen im Atom mit der Komplexstruktur der Spektren | [10.1007/bf02980631](https://doi.org/10.1007/bf02980631) |
| `Dirac1926` | On the theory of quantum mechanics | [10.1098/rspa.1926.0133](https://doi.org/10.1098/rspa.1926.0133) |
| `Pauli1940` | The Connection Between Spin and Statistics | [10.1103/physrev.58.716](https://doi.org/10.1103/physrev.58.716) |
| `Slater1930` | Note on Hartree's Method | [10.1103/PhysRev.35.210.2](https://doi.org/10.1103/PhysRev.35.210.2) |
| `Slater1930Orbitals` | Atomic Shielding Constants | [10.1103/PhysRev.36.57](https://doi.org/10.1103/PhysRev.36.57) |
| `Brillouin1932` | Les problèmes de perturbations et les champs self-consistents | [10.1051/jphysrad:0193200309037300](https://doi.org/10.1051/jphysrad:0193200309037300) |
| `Roothaan1960` | Self-Consistent Field Theory for Open Shells of Electronic Systems | [10.1103/revmodphys.32.179](https://doi.org/10.1103/revmodphys.32.179) |
| `McWeeny1960` | Some Recent Advances in Density Matrix Theory | [10.1103/RevModPhys.32.335](https://doi.org/10.1103/RevModPhys.32.335) |
| `Thouless1960` | Stability conditions and nuclear rotations in the Hartree-Fock theory | [10.1016/0029-5582(60)90048-1](https://doi.org/10.1016/0029-5582(60)90048-1) |
| `SeegerPople1977` | Self-consistent molecular orbital methods. XVIII. Constraints and stability in Hartree–Fock theory | [10.1063/1.434318](https://doi.org/10.1063/1.434318) |
| `Huzinaga1965` | Gaussian-Type Functions for Polyatomic Systems. I | [10.1063/1.1696113](https://doi.org/10.1063/1.1696113) |
| `Raffenetti1973` | General contraction of Gaussian atomic orbitals: Core, valence, polarization, and diffuse basis sets; Molecular integral evaluation | [10.1063/1.1679007](https://doi.org/10.1063/1.1679007) |
| `LeinaasMyrheim1977` | On the theory of identical particles | [10.1007/BF02727953](https://doi.org/10.1007/BF02727953) |
| `Wilczek1982` | Quantum Mechanics of Fractional-Spin Particles | [10.1103/physrevlett.49.957](https://doi.org/10.1103/physrevlett.49.957) |
| `Dunlap1979` | On some approximations in applications of Xα theory | [10.1063/1.438728](https://doi.org/10.1063/1.438728) |
| `Vahtras1993` | Integral approximations for LCAO-SCF calculations | [10.1016/0009-2614(93)89151-7](https://doi.org/10.1016/0009-2614(93)89151-7) |

## Targeted additions approved by the author (16 October 2026)

Added the ten sources proposed in the preceding recommendation, at the
existing passages they support. The optional Lehtola--Blockhuys--Van Alsenoy
(2020) review was not added: the author explicitly requested that Further
reading remain unchanged. Existing figure/table provenance citations are
retained, including Henderson's Table I credit.

Publication identities and author lists were checked against publisher pages
and publisher-deposited DOI metadata during the recommendation pass.
Löwdin (1959) and Gill (1994) are contributed review chapters, not standalone
journal articles. Gill's author-hosted full text confirms the interpolation
and downward-recursion discussion (printed pages 167 and 182).

Löwdin's digitized DOI record reports January 1958, but the
[publisher's volume page](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470143483)
also gives copyright 1959, and the
[author's published bibliography](https://onlinelibrary.wiley.com/doi/10.1002/qua.10096)
lists this contribution as volume 2, pages 207--322 (1959). The entry therefore
retains the conventional 1959 citation rather than silently adopting the
inconsistent digitized date.

Payne et al. support the plane-wave representation and computational context,
not a derivation of molecular HF. Clark et al. support diffuse augmentation;
Krishnan et al. support the 6-311G contraction; Frisch et al. support the
supplementary-function discussion. Saunders--Hillier is attached specifically
to level shifting, not DIIS. Fukutome is cited for the designations in the
classification discussion without replacing the reproduced-table credit.
Weigend (2002) is an implementation-level RI-HF reference, complementary to
the existing Weigend (2006) Coulomb-fitting citation.

| BibTeX key | Publication title | DOI record |
| --- | --- | --- |
| `Lowdin1959` | Correlation Problem in Many-Electron Quantum Mechanics I. Review of Different Approaches and Discussion of Some Current Ideas | [10.1002/9780470143483.ch7](https://doi.org/10.1002/9780470143483.ch7) |
| `Lehtola2019` | Assessment of Initial Guesses for Self-Consistent Field Calculations. Superposition of Atomic Potentials: Simple yet Efficient | [10.1021/acs.jctc.8b01089](https://doi.org/10.1021/acs.jctc.8b01089) |
| `SaundersHillier1973` | A Level-Shifting Method for Converging Closed Shell Hartree-Fock Wave Functions | [10.1002/qua.560070407](https://doi.org/10.1002/qua.560070407) |
| `Fukutome1981` | Unrestricted Hartree-Fock Theory and Its Applications to Molecules and Chemical Reactions | [10.1002/qua.560200502](https://doi.org/10.1002/qua.560200502) |
| `Payne1992` | Iterative Minimization Techniques for Ab Initio Total-Energy Calculations: Molecular Dynamics and Conjugate Gradients | [10.1103/RevModPhys.64.1045](https://doi.org/10.1103/RevModPhys.64.1045) |
| `Krishnan1980` | Self-Consistent Molecular Orbital Methods. XX. A Basis Set for Correlated Wave Functions | [10.1063/1.438955](https://doi.org/10.1063/1.438955) |
| `Clark1983` | Efficient Diffuse Function-Augmented Basis Sets for Anion Calculations. III. The 3-21+G Basis Set for First-Row Elements, Li-F | [10.1002/jcc.540040303](https://doi.org/10.1002/jcc.540040303) |
| `Frisch1984` | Self-Consistent Molecular Orbital Methods 25. Supplementary Functions for Gaussian Basis Sets | [10.1063/1.447079](https://doi.org/10.1063/1.447079) |
| `Gill1994` | Molecular Integrals over Gaussian Basis Functions | [10.1016/S0065-3276(08)60019-2](https://doi.org/10.1016/S0065-3276(08)60019-2) |
| `Weigend2002` | A Fully Direct RI-HF Algorithm: Implementation, Optimised Auxiliary Basis Sets, Demonstration of Accuracy and Efficiency | [10.1039/B204199P](https://doi.org/10.1039/B204199P) |

## Aufbau occupation and open-shell spatial-orbital ordering (20 October 2026)

Verified the theorem in the [original Bach et al. manuscript](https://arxiv.org/abs/cond-mat/9307066)
and its [APS record](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.72.2981).
Its unconstrained spin-orbital minimization is not an assertion about a
single common ordering of UHF spatial orbitals.

For the author's TEMPO suggestion, verified the primary
[Kusamoto--Kume--Nishihara study](https://pubs.acs.org/doi/10.1021/ja805751h),
including its [PubMed metadata and abstract](https://pubmed.ncbi.nlm.nih.gov/18821762/).
The documented example is a TEMPO-derived dithiolate Pt(II) complex, not
bare TEMPO. Its spatial SOMO--HOMO inversion does not by itself demonstrate
an inverted occupied/virtual gap within one self-consistent HF spin channel.
No new HF calculation or unsupported claim for bare TEMPO is presented.
The ACS landing page was access-restricted; the original author abstract and
bibliographic metadata were checked through PubMed and the
[author's institutional publication record](https://tus.elsevierpure.com/en/publications/realization-of-somo-homo-level-conversion-for-a-tempo-dithiolate-/).

| BibTeX key | Publication title | DOI record |
| --- | --- | --- |
| `Bach1994` | There Are No Unfilled Shells in Unrestricted Hartree-Fock Theory | [10.1103/PhysRevLett.72.2981](https://doi.org/10.1103/PhysRevLett.72.2981) |
| `Kusamoto2008` | Realization of SOMO-HOMO Level Conversion for a TEMPO-Dithiolate Ligand by Coordination to Platinum(II) | [10.1021/ja805751h](https://doi.org/10.1021/ja805751h) |

