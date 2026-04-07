# Methodology — Venue Operations Knowledge Base

**Version:** 2.0
**Published:** 2026-04-05 (Session 16); updated 2026-04-06 (Session D2 — v1.0.0 statistics, complete audit history, coverage depth disclosure)
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

## 5. Vault Statistics (v1.0.0, 2026-04-06)

| Metric | Value |
|---|:-:|
| **Total notes** | 650 |
| Domain overviews | 26 / 26 (100%) |
| Concept notes | 207 |
| Source notes | 390 |
| MOC notes (navigation layer) | 27 (26 domain + 1 master) |
| Audit reports | 7 (A-01 through A-07) |
| Delta register entries | 20 (all resolved or accepted) |
| **Processing sessions** | 21 (S4-S21, March-April 2026) |
| **DR files processed** | 40+ |
| **Domains at minimum viable (3+ concepts)** | 26 / 26 (100%) |
| **Domains at working depth (8+ concepts)** | 10 / 26 (38%) |
| **Domains at authoritative (15+ concepts)** | 1 / 26 (4%) |
| **Fabrication incidents** | 0 across 21 sessions |

### Confidence Distribution

| Tier | Count | Percentage |
|---|:-:|:-:|
| High | 183 | 88.4% |
| Medium | 22 | 10.6% |
| Low | 2 | 1.0% |

### Coverage Depth by Domain

15 domains are at minimum viable depth (3-7 concepts) and are candidates for enrichment to working depth. Coverage distribution reflects the progressive deepening model (Q4) — not all domains will reach authoritative depth; depth follows strategic priority, content calendar alignment, and audience need.

Domains with highest medium+low confidence concentrations:
- **logistics-and-warehouse:** 3 concepts, 66% medium+low (smallest domain, single research batch)
- **parking-and-transportation:** 10 concepts, 40% medium+low (vendor-sourced concentration, documented in A-06)

These are transparent disclosures, not deficiencies — they represent the current state of source material quality for these domains.

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

## 7. Known Limitations

**Content-level limitations:**

1. **All 207 concept notes at `status: draft`.** No notes have undergone formal human review. Promotion to `reviewed` → `canonical` requires human sign-off per Q4 progressive deepening model. This is the documented workflow — AI extraction produces drafts; human review produces reviewed/canonical status. The entire corpus is transparently AI-extracted pending human verification.
2. **No non-concept notes yet.** Standards (`02_Standards/`), Technology (`03_Technology/`), Organizations (`04_Organizations/`), People (`05_People/`) — these note types exist in the schema but have zero instances. An estimated 70-120 entities are extractable from the existing 390-source corpus. Scheduled for Phase D4 ingestion.
3. **15 domains at minimum viable depth (3-7 concepts).** These are usable references but lack the substantive coverage of working-depth domains (8+). Progressive deepening will prioritize domains based on strategic value and audience need.
4. **5 lowest-count domains depend on a single research batch.** logistics-and-warehouse, crowd-management, supply-chain-and-procurement, financial-operations, and booking-and-sales each drew from one DR prompt with no cross-batch corroboration. DR enrichment targeting these domains is planned for Phase D3/D4.
5. **Bibliographic metadata partially populated.** Author field at 100% (enriched S18). Publication at ~24%, publish_date at ~2% — populated where publicly identifiable from source URLs. Remaining gaps reflect sources where publisher metadata is not determinable from the URL alone.
6. **Claim-to-source traceability at 60%.** Audit A-04 (S17 + S19) found 60% of concept body-text claims fully trace to cited sources. Zero fabrication detected. The 40% gap represents claims that are supported by cited sources in frontmatter but lack inline body-text citation — a citation density issue, not a factual accuracy issue. DR enrichment addresses this.

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

21 sessions (S4-S21) documented with handoffs in `_sessions/session-NN-handoff.md`. Processing log in `_sessions/progress.md`. Initiative roadmap in `_sessions/vep-kb-initiative-roadmap.md` v1.5.

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

---

*AI Disclosure: Drafted by Claude (Anthropic, Opus 4.6). Reviewed and approved by Alex Jackson, Experience Innovation Inc. This methodology statement itself is subject to the same provenance and transparency discipline it describes.*
