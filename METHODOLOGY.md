# Methodology — Venue Operations Knowledge Base

**Version:** 1.0
**Published:** 2026-04-05 (Session 16, Academic Rigor Initiative Phase B.5)
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

1. Read deep research (DR) outputs from Perplexity Pro and Gemini DR (~15K-80K words each, 31 files total)
2. Extracted concepts, identified sources, mapped to 26-domain taxonomy
3. Created concept notes, source notes, domain overviews, MOCs with structured frontmatter
4. Cross-linked using 7-type relationship taxonomy (parent_of/child_of, implements, governed_by, supported_by, related_to, varies_by, scales_with)
5. Validated every note against 34 pre-write checks
6. Ran audits for provenance completeness, vocabulary enforcement, citation standardization
7. Maintained a machine-readable delta register of findings and deferrals

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

## 5. Vault Statistics (as of Session 16)

| Metric | Value |
|---|:-:|
| **Total notes** | 482 |
| Domain overviews | 26 / 26 (100%) |
| Concept notes | 169 |
| Source notes | 260 |
| MOC notes (navigation layer) | 27 (26 domain + 1 master) |
| Validation reports | 15+ |
| **Research batches processed** | 11 (batches 00-10) |
| **DR files processed** | 28 processable / 31 total |
| **Domains at authoritative (15+)** | 4 |
| **Domains at working depth (8+)** | 6 |
| **Domains at minimum viable (3+)** | 11 |
| **Domains at scaffolded (1-2)** | 2 |
| **Domains at empty (0)** | 3 (data-and-analytics, booking-and-sales, tenant-and-partner-relations) |

**Coverage distribution:** 21 of 26 domains (81%) at minimum viable or deeper; 3 of 26 (12%) empty pending fresh DR research.

---

## 6. GLRC Compliance Status (Session 16)

Provenance chain completeness (audit A-01, Session 16):

| Field | Coverage |
|---|:-:|
| ai_disclosure | 482 / 482 (100%) |
| extraction_model | 482 / 482 (100%) |
| research_batch (applicable notes) | 429 / 429 concepts + sources (100%) |

Vocabulary compliance (audit A-02, Session 16):

| Check | Status |
|---|:-:|
| Old domain slugs in vault content | 0 violations |
| note_type values | 100% from VOCABULARY.yaml |
| status values (vault content) | 100% `draft` |
| extraction_model values | 100% valid |

Citation format (audit A-03, Session 16):

| Field | Coverage |
|---|:-:|
| Required (source_type, url, accessed, description) | 100% |
| Optional (author, publication, publish_date) | 0% — deferred to S18 enrichment |

---

## 7. Known Limitations

**Content-level limitations:**

1. **3 empty domains.** `data-and-analytics`, `booking-and-sales`, `tenant-and-partner-relations` have 0 concepts. DR corpus exhausted for these topics; fresh research required.
2. **No non-concept notes yet.** Standards (`02_Standards/`), Technology (`03_Technology/`), Organizations (`04_Organizations/`), People (`05_People/`) folders are empty by design — enrichment pass deferred to post-v1.0 (Phase E of initiative roadmap).
3. **All notes at `status: draft`.** No notes have undergone formal human review + promotion to `reviewed` or `canonical`. This represents a multi-session effort ahead.
4. **Bibliographic metadata gaps.** 260 source notes carry required citation fields (url, accessed, description, source_type) but optional fields (author, publication, publish_date) are not yet populated. Enrichment scheduled for Session 18.
5. **Claim-to-source traceability not yet inline-audited.** Every concept note cites sources in frontmatter, but body-text claim-to-source inline verification is deferred to Sessions 17-18 (audit A-04).

**Methodological limitations:**

1. **Human review not yet applied.** Notes are AI-generated with automated validation. The progression from `draft` → `reviewed` (human verification) → `canonical` (authoritative reference) is ahead of us, not behind us.
2. **No peer review.** This is a draft academic resource. Peer review by industry professionals is planned but not yet executed.
3. **Geography.** Content is North America-focused (US/Canada jurisdictions dominant). International applicability is limited.
4. **Recency.** Content extraction from DR completed April 2026. Some data (technology platforms, regulations, certifications) will drift over time.
5. **AI fabrication risk.** While the pipeline includes hard rules against fabrication and a URL-verbatim-quote enforcement standard (established Session 15), AI-extraction risk is non-zero. Human review stage exists to catch residual errors.

**Delta register (machine-readable backlog):** open findings tracked in `_Pipeline/delta-register.yaml`. Zero-open at v1.0 release.

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

### Audit History

| Session | Audits | Outcome |
|---|---|---|
| S16 | A-01 provenance, A-02 vocabulary, A-03 citation | PASS / 4 delta entries |
| S17-S18 | A-04 claim-to-source traceability, A-05 consistency | Planned |
| S19 | A-06 confidence tier defensibility, delta register sweep | Planned |
| S20 | A-07 final validation, v1.0 tag | Planned |

### Session History

All 15+ sessions documented with handoffs in `_sessions/session-NN-handoff.md`. Processing log in `_sessions/progress.md`. Initiative roadmap in `_sessions/vep-kb-initiative-roadmap.md` v1.1.

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

---

*AI Disclosure: Drafted by Claude (Anthropic, Opus 4.6). Reviewed and approved by Alex Jackson, Experience Innovation Inc. This methodology statement itself is subject to the same provenance and transparency discipline it describes.*
