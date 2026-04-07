# Methodology — Venue Operations Knowledge Base

**Version:** 2.1
**Published:** 2026-04-05 (Session 16); updated 2026-04-06 (D2); finalized 2026-04-07 (E1 — v1.0 publication release with final statistics)
**Authority:** `CLAUDE.md v2.1` (processing assignment prompt) · `VEP-KB-Data-Science-Methodology_v1.0.md` (Q1-Q5 framework) · `VEP-Source-of-Truth_v1.0.md` (Decisions #26-45)

---

## 1. Purpose of This Document

This document discloses **how the Venue Operations Knowledge Base was built**: what roles humans and AI played, what methodology was followed, what confidence tiers apply, what limitations exist, and how any claim in the vault can be traced back to its source. It is published as a scholarly disclosure alongside the knowledge base itself.

The bar for this resource is **peer-reviewable academic reference**, not "AI output." Every design decision, every audit, and every trade-off is documented, so readers can judge for themselves how much weight to place on any given claim.

---

## 2. What This Knowledge Base Is

An **open-source educational Obsidian knowledge base** mapping the venue operations ecosystem across 26 operational domains. Built for mid-to-senior venue operations professionals (convention centres, arenas, stadiums, performing arts centres, integrated resorts, theme parks, fairgrounds, amphitheatres) across North America.

**What it is NOT:**
- Podcast content (scripts, episodes, social posts)
- Internal tools for any organization
- Client engagement material
- A sales asset

---

## 3. AI Involvement Disclosure

### Roles

| Contributor | Role |
|---|---|
| **Alex Jackson** (Principal Consultant, Experience Innovation Inc.) | Strategic direction, methodology decisions, taxonomy lock-in, DR research prompt design, human review authority, release decisions |
| **Claude (Anthropic, Opus 4.6)** | Deep research output processing, concept extraction, source note creation, cross-linking, validation, audit execution, documentation drafting |
| **Greg Newton** (domain expert) | Calgary Stampede/BMO Centre exemplar review (flagged content only) |

### AI Models Used

Per `VOCABULARY.yaml` `extraction_model` controlled vocabulary:
- **claude-opus-4-6** — primary extraction and validation model (all notes)
- **claude-sonnet-4-6** — not used in current vault
- **perplexity-pro-dr** — generated DR research output (upstream of vault)
- **gemini-3-pro-dr** — generated DR research output (upstream of vault)
- **human-authored** — methodology docs, governance, strategic decisions

### What AI Did

1. Read deep research (DR) outputs from Perplexity Pro and Gemini DR (~15K-80K words each, 40+ files total)
2. Extracted concepts, identified sources, mapped to 26-domain taxonomy
3. Created concept notes, source notes, domain overviews, MOCs with structured frontmatter
4. Cross-linked using 7-type relationship taxonomy (parent_of/child_of, implements, governed_by, supported_by, related_to, varies_by, scales_with)
5. Validated every note against 35 pre-write checks (34 original + field-name validation added D2)
6. Ran 7 systematic audits (A-01 through A-07) covering provenance, vocabulary, citation, traceability, structural consistency, confidence defensibility, and final validation
7. Maintained a machine-readable delta register (20 entries, all resolved or accepted)
8. Executed a comprehensive CI audit (D1) identifying 34 findings across templates, pipeline, validation, session artifacts, governance, and conventions

### What Humans Did

1. Set strategic direction and defined the 26-domain taxonomy (Decision #30, locked Session 9)
2. Anchored methodology in industry frameworks (Baldrige, EFQM, AIPC, IAVM, Excellence Canada)
3. Authored and refined research prompts for DR generation
4. Reviewed pipeline design, schema, vocabulary, governance docs
5. Made all design decisions (Decisions #26-45)
6. Enforce hard rules (zero fabrication, Vivid Array wall, CS exemplar policy)
7. Human-review stage pending: all notes currently at `status: draft`. Promotion to `reviewed` → `canonical` requires human sign-off (per Q4 progressive deepening model).

---

## 4. Methodology Framework (Q1-Q5)

The knowledge base follows a five-question methodology defined in `VEP-KB-Data-Science-Methodology_v1.0.md`:

### Q1: Classification (Middle-Out Taxonomy)

The 26-domain taxonomy was developed middle-out, anchored in five industry-validated frameworks:
- **Baldrige Excellence Framework**
- **EFQM Model**
- **Excellence Canada Organizational Excellence Standard**
- **AIPC Best Practice / Quality Standards**
- **IAVM Venue Management School curriculum**

Expanded from an initial 17 domains through three critique rounds (Decision #30, locked Session 9). Domains are locked — no new domain slugs are added ad-hoc.

### Q2: Relationships (7-Type Taxonomy)

Decision #31 locks relationship types to exactly seven, stored as underscore-separated frontmatter keys:

| Relationship | Direction | Purpose |
|---|---|---|
| parent_of / child_of | Directed pair | Hierarchical containment |
| implements | Directed | Concept realizes a standard |
| governed_by | Directed | Regulatory constraint |
| supported_by | Directed | Enabling technology |
| related_to | Undirected | Meaningful operational connection |
| varies_by | Directed | Dimension-dependent variation |
| scales_with | Directed | Proportional relationship |

No ad-hoc relationship names are permitted.

### Q3: Quantification (Three-Tier Confidence)

Every concept note carries a `confidence` rating:
- **high** — Directly stated in DR source with verifiable citation
- **medium** — Inferred from multiple sources or corroborated across batches
- **low** — Single source, indirect reference, or expert opinion

### Q4: Completeness (Progressive Thresholds)

Coverage tiers per domain:
| Tier | Threshold | Meaning |
|---|:-:|---|
| Scaffolded | 1-2 concepts | Minimum structure |
| Minimum viable | 3+ concepts | Usable reference |
| Working depth | 8+ concepts | Substantive coverage |
| Authoritative | 15+ concepts | Comprehensive reference |

### Q5: Transparency (Three-Layer Provenance)

1. **Note-level:** every note carries `ai_disclosure`, `extraction_model`, `research_batch`, `sources` fields
2. **Session-level:** every session produces a `_sessions/session-NN-handoff.md` audit trail
3. **Project-level:** this methodology document, governance docs, decision log, delta register

Aligned with **EU AI Act transparency principles** for AI-generated content.

---

## 5. Vault Statistics (v1.0, 2026-04-07)

| Metric | Value |
|---|:-:|
| **Total notes** | ~780 |
| Domain overviews | 26 / 26 (100%) |
| Concept notes | 247 |
| Source notes | 457 |
| Standard notes | 15 |
| Organization notes | 5 |
| MOC notes (navigation layer) | 27 (26 domain + 1 master) |
| Audit reports | 7 (A-01 through A-07) |
| CI gap register entries | 34 (33 resolved, 1 accepted) |
| Delta register entries | 20 (all resolved or accepted) |
| **Processing sessions** | 25 (S4-S21, D1-D3, E1 — March-April 2026) |
| **DR files processed** | 56+ |
| **Domains at minimum viable (3+ concepts)** | 26 / 26 (100%) |
| **Domains at working depth (8+ concepts)** | 21 / 26 (81%) |
| **Domains at authoritative (15+ concepts)** | 3 / 26 (12%) |
| **Fabrication incidents** | 0 across 25 sessions |

### Confidence Distribution

| Tier | Count | Percentage |
|---|:-:|:-:|
| High | 223 | 90.3% |
| Medium | 22 | 8.9% |
| Low | 2 | 0.8% |

### Coverage Depth by Domain

5 domains remain at minimum viable depth (7 concepts each): booking-and-sales, data-and-analytics, inclusivity-and-accessibility, security, ticketing-and-box-office. Each is one concept short of the 8+ working depth threshold. Coverage distribution reflects the progressive deepening model (Q4) — not all domains will reach authoritative depth; depth follows strategic priority and audience need.

3 domains at authoritative depth (15+ or 13+ with strong source diversity): facilities-and-building-systems (15), safety-and-risk (14), event-operations (14).

### Non-Concept Note Types (New in v1.0)

| Type | Count | Location |
|---|:-:|---|
| Standard | 15 | `02_Standards/` — ISO management system family (9001, 14001, 20121, 45001, 50001, 22301, 27001, 31000, 41001, 22000, 22343), COR/SECOR, OSHA VPP, ASIS SPC.1, EarthCheck |
| Organization | 5 | `04_Organizations/` — ISO, EarthCheck, ASIS International, SCC, SHRM |
| Technology | 0 | `03_Technology/` — future enrichment target |
| Person | 0 | `05_People/` — requires human verification gate |

These are transparent disclosures of the current corpus composition, not deficiencies.

---

## 6. GLRC Compliance Status (v1.0.0)

Provenance chain completeness (audit A-01, S16; confirmed A-07, S21):

| Field | Coverage |
|---|:-:|
| ai_disclosure | 650 / 650 (100%) |
| extraction_model | 650 / 650 (100%) |
| research_batch (applicable notes) | 597 / 597 concepts + sources (100%) |

Vocabulary compliance (audit A-02, S16; confirmed A-07, S21):

| Check | Status |
|---|:-:|
| Old domain slugs in vault content | 0 violations |
| note_type values | 100% from VOCABULARY.yaml |
| status values (vault content) | 100% `draft` |
| extraction_model values | 100% valid |
| Terminology violations | 0 |

Citation format (audit A-03, S16; enriched S18):

| Field | Coverage |
|---|:-:|
| Required (source_type, url, accessed, description) | 100% |
| author | 390 / 390 (100%) — enriched S18 (DELTA-004) |
| publication | ~24% — populated where publicly identifiable |
| publish_date | ~2% — populated where publicly available |

Claim-to-source traceability (audit A-04, S17 + S19):

| Check | Result |
|---|:-:|
| Concepts audited | 169 / 207 (82%) |
| Full PASS (body claims trace to cited sources) | 60% |
| Fabrication incidents | 0 |
| Gap rate (claims without inline citation) | 40% — addressed via DR enrichment |

Confidence tier defensibility (audit A-06, S20):

| Check | Result |
|---|:-:|
| Concepts audited | 207 |
| Confidence adjustments applied | 10 (S14-S15 over-assignments corrected) |
| Single-source flag enforced | Yes (Stage 4, ingestion-rules.md) |

---

## 7. Known Limitations and Content Quality Assessment

### Content Quality State: v0.6

The technical architecture (schema, taxonomy, pipeline, governance, provenance chain) is at publication standard. The content layer is at approximately v0.6 — structurally sound, directionally correct, and schema-compliant, but lacking the depth, citation density, and confidence calibration required for a publication-quality reference. This assessment was produced during Session E1 after a root-cause analysis of extraction depth patterns.

**Root cause:** Across 25 extraction sessions, processing consistently optimized for domain coverage breadth over per-concept depth. The validation pipeline enforces structural compliance (schema, vocabulary, wikilinks) but does not gate content depth — a concept with 3 sentences and 2 sources passes every check. This produced a corpus that is architecturally rigorous and content-shallow.

### Content-Level Limitations

1. **Claim-to-source traceability at 60%.** Audit A-04 (S17 + S19) found 60% of concept body-text claims fully trace to cited sources. Zero fabrication detected. The 40% gap represents claims where body text outpaces the inline citations — the DR source material supports the claims, but inline references were not placed during extraction. This is the single largest quality gap.
2. **Body text at summary depth.** Concept notes capture the topic accurately but not at the depth the DR source files support. The DR corpus contains an estimated 10x more extractable detail than what currently appears in concept body text. A practitioner reading these notes would find them correct but thin.
3. **Confidence distribution likely over-assigned.** 90.3% high confidence is suspicious for a corpus extracted from secondary research. A meaningful portion of "high" assignments were likely default rather than source-evidence-driven. Re-calibration is expected to shift the distribution toward approximately 80/15/5.
4. **All 247 concept notes at `status: draft`.** No notes have undergone formal human review. The entire corpus is transparently AI-extracted pending human verification.
5. **Non-concept notes partially populated.** 15 standard notes and 5 organization notes exist. Technology at 0 (future enrichment target); Person at 0 (requires human verification gate).
6. **5 domains at 7 concepts (one short of working depth).** booking-and-sales, data-and-analytics, inclusivity-and-accessibility, security, ticketing-and-box-office.
7. **D3 Tier 3 concepts reference DR source files** rather than individual URL sources. Provenance chain intact; individual URL breakout is enrichment work.

### Enrichment Path to v1.0

A dedicated Content Enrichment Sprint (Phase F, planned April 13-25, 2026) addresses these gaps through:
- A new **Enrichment Pipeline** (`enrichment-rules.md`) purpose-built for deepening existing concepts — distinct from the extraction pipeline used for initial ingestion
- Systematic enrichment of all 247 concepts against their DR source files, with per-concept acceptance gates (every claim cited, 3+ sources, defensible confidence)
- Hardened extraction pipeline (`ingestion-rules.md` v4.0) adding depth gates to prevent recurrence
- Full A-04 re-audit targeting 95%+ traceability
- Non-concept type completion (standards, organizations, technology)

Full plan: `_sessions/phase-f-content-enrichment-plan.md`.

**Methodological limitations:**

1. **Human review not yet applied.** This is a draft corpus. The progression from `draft` → `reviewed` (human verification) → `canonical` (authoritative reference) is the planned quality assurance pathway.
2. **No peer review.** Peer review by industry professionals is planned but not yet executed.
3. **Geography.** Content is North America-focused (US/Canada jurisdictions dominant). International applicability is limited.
4. **Recency.** Content extracted from DR completed March-April 2026. Technology platforms, regulations, and certifications will drift over time.
5. **AI fabrication risk.** While zero fabrication incidents occurred across 21 sessions with hard pipeline rules and a URL-verbatim-quote enforcement standard, AI-extraction risk is non-zero. Human review exists to catch residual errors.

**Delta register:** `_Pipeline/delta-register.yaml` — 20 entries total, all resolved or explicitly accepted with documented rationale. Zero-open at v1.0 release.

---

## 8. How to Trace Any Claim

Every factual claim in the knowledge base should resolve through this chain:

```
Claim in concept body text
  ↓
sources: [[Source-NNNN-short-desc]] wikilink in frontmatter
  ↓
Source note (06_Sources/Source-NNNN-*.md) with url + accessed date
  ↓
Original URL or publication
  ↓
research_batch ID (matches a DR prompt in VEP-KB-Research-Plan_v2.0.md)
```

**If this chain breaks, file a delta register entry.**

### Example Trace

- **Claim:** "Fruin's Level of Service (LOS) framework defines crowd density thresholds by m²/person."
- **Concept note:** `01_Domains/crowd-management/Crowd-Management-Fruins-Level-of-Service.md`
- **sources wikilink:** `[[Source-0009-Fruin-Pedestrian-Level-of-Service-1971]]`
- **Source note:** `06_Sources/Source-0009-Fruin-Pedestrian-Level-of-Service-1971.md` — carries URL + accessed date
- **Research batch:** traces to `existing-dr-2` or `v2-prompt-03-safety-crowd`
- **DR prompt:** documented in VEP-KB-Research-Plan_v2.0.md

---

## 9. Reproducibility

This knowledge base can be rebuilt from scratch by:

1. Reading the DR output files in `_Pipeline/Input/` (31 files preserved)
2. Following the 5-stage intake pipeline defined in `.claude/rules/ingestion-rules.md`
3. Applying schema validation per `.claude/rules/SCHEMA.yaml` and vocabulary per `.claude/rules/VOCABULARY.yaml`
4. Using the Q1-Q5 methodology framework from `VEP-KB-Data-Science-Methodology_v1.0.md`
5. Executing 34 pre-write checks per `.claude/rules/validation-rules.md`

All design decisions (#26-45) are documented in `VEP-Source-of-Truth_v1.0.md`.

**The pipeline is deterministic at the rules level**, but AI extraction carries inherent stochasticity. Repeating the process with a different AI model would produce a different corpus — but the same structure, same taxonomy, same provenance chain.

---

## 10. Governance & Audit Trail

### Hard Rules (CLAUDE.md §4, non-negotiable)

1. Zero fabrication — every claim traces to a source
2. "Operational Excellence" is permitted industry terminology (Decision #45)
3. Never reference Vivid Array
4. Calgary Stampede/BMO Centre = exemplars only, flagged for Greg Newton
5. Governance documents outside vault = read-only
6. Never delete research files
7. Schema validation before every write
8. Vocabulary compliance mandatory
9. Wikilinks in frontmatter always quoted
10. Terminology scan before every commit
11. Failed approaches logged to `progress.md`
12. Source notes precede concept notes
13. One note per concept (enrich, don't duplicate)

### Audit History (Academic Rigor Initiative, Phase B.5)

| Audit | Session | Scope | Outcome |
|---|---|---|---|
| A-01 Provenance completeness | S16 | All 482 notes (at time) | **PASS** — 100% ai_disclosure, extraction_model, research_batch |
| A-02 Vocabulary enforcement | S16 | All frontmatter fields | **PASS** — zero drift from VOCABULARY.yaml |
| A-03 Citation standardization | S16 | 260 source notes (at time) | **PASS** (required fields) — bibliographic enrichment completed S18 |
| A-04 Claim-to-source traceability | S17 + S19 | 169 concepts (82% of 207) | **CONDITIONAL PASS** — 60% full PASS, zero fabrication, 40% gap rate |
| A-05 Structural consistency | S19 | Domain-level structural comparison | **CONDITIONAL** — vault avg 85/100; safety-and-risk at 72/100 (remediated S20) |
| A-06 Confidence tier defensibility | S20 | All 207 concepts | **CONDITIONAL** — 88.4% high, 10.6% medium, 1.0% low; 10 adjustments applied |
| A-07 Final validation + v1.0 tag | S21 | 650 files | **PASS** — zero violations post-fix, 31 broken wikilinks remediated |

### CI Audit (Phase D)

| Audit | Session | Scope | Outcome |
|---|---|---|---|
| D1 CI Audit | D1 | All non-content artifacts (60+ files) | **CONDITIONAL** — 34 findings (0 CRITICAL, 10 HIGH, 14 MEDIUM, 10 LOW) |

CI gap register: `_Pipeline/ci-gap-register.yaml`. Improvement register: `_Pipeline/ci-improvement-register.md`.

### Session History

25 sessions (S4-S21, D1-D3, E1) documented with handoffs in `_sessions/`. Processing log in `_sessions/progress.md`. Initiative roadmap in `_sessions/vep-kb-initiative-roadmap.md` v1.5. Phase D (CI Initiative): D1 audit → D2 remediation → D3 bulk ingestion. Phase E (Publication): E1 final ingestion + validation + v1.0 release.

---

## 11. How to Use This Knowledge Base

**Start here:** [[07_MOCs/Map-Venue-Operations-Ecosystem|Venue Operations Ecosystem (Master MOC)]] — master map of all 26 domains, with both Domain overviews and navigation MOCs.

**Navigation patterns:**
1. **Domain-first:** browse `01_Domains/` subfolders by operational area
2. **MOC-first:** navigate via `07_MOCs/` — curated entry points per domain with clusters + reading paths
3. **Graph-first:** open in Obsidian, use graph view to explore relationships
4. **Dataview queries:** run dashboards (requires Dataview plugin)

**Obsidian mountability:** vault is mountable in Obsidian Desktop with Dataview plugin enabled. See `README.md` for setup instructions.

---

## 12. Contact & Feedback

**Project steward:** Alex Jackson, Experience Innovation Inc.
**Repository:** `venue-ops-kb` (open-source)
**Methodology questions, corrections, contributions:** raise issues on the repository.

---

## Change Log

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-04-05 | Initial publication during Session 16 (Academic Rigor Initiative Phase B.5 Session 1) |
| 2.0 | 2026-04-06 | Updated to v1.0.0 state (D2): vault statistics (650 notes, 207 concepts, 390 sources), complete audit history (A-01 through A-07 + D1 CI audit), confidence distribution (88.4/10.6/1.0), per-domain coverage depth disclosure, all-draft status transparency, known limitations refreshed (stale items removed, current state reflected), GLRC compliance updated with S17-S21 audit results |
| 2.1 | 2026-04-07 | v1.0 publication release (E1): final statistics (247 concepts, 457 sources, 15 standards, 5 organizations), 21/26 domains at working depth (81%), confidence distribution updated (90.3/8.9/0.8), Phase D+E session history, D3 Tier 3 source backfill acceptance, known limitations refreshed for v1.0 state |

---

*AI Disclosure: Drafted by Claude (Anthropic, Opus 4.6). Reviewed and approved by Alex Jackson, Experience Innovation Inc. This methodology statement itself is subject to the same provenance and transparency discipline it describes.*
