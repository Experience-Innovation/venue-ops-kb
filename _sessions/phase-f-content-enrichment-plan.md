---
type: operational-plan
lifecycle: active
created: 2026-04-07
session: E1
purpose: "Comprehensive plan for content enrichment sprint bringing the venue-ops-kb from v0.6 content quality to v1.0 publication-ready. Resumption April 13, 2026."
---

# Phase F: Infrastructure Evolution + Content Enrichment Sprint — v1.0 Publication-Ready

**Created:** E1 (2026-04-07)
**Resumption:** April 13, 2026 (Monday)
**Target completion:** April 25, 2026 (Friday)
**Model strategy:** Opus for infrastructure build + pipeline design + QA; Sonnet for systematic enrichment execution
**Governing principle:** Quality out of the gate. No more breadth-over-depth.

---

## §0. Infrastructure Evolution (Added E1 Retro)

### SQLite as Source of Truth

The vault migrates from a flat-file metadata model (YAML frontmatter in 780+ .md files) to a three-layer architecture:

| Layer | Owns | Format |
|---|---|---|
| **SQLite** (SOT) | All metadata — frontmatter fields, relationships, confidence, sources, pipeline state, enrichment tracking, validation results | `.db` file with WAL mode |
| **Markdown** (publication) | Body text content — what practitioners read in Obsidian | `.md` files in vault |
| **JSON** (pipeline config) | Pipeline definitions, schema, vocabulary, acceptance criteria | `.json` files in `.claude/rules/` |

**Data flow:** Agents write metadata to SQLite → sync process generates .md frontmatter from SQLite → Obsidian reads .md files. Body text is written directly to .md. Metadata changes go through SQLite only.

**SQLite schema (core tables):**
- `concepts` — all concept metadata (247 rows), with constraints: `body_word_count >= 500`, `inline_citation_count >= 3`, `source_count >= 3`
- `sources` — all source metadata (457 rows)
- `standards`, `organizations`, `technology`, `people` — non-concept note types
- `domains` — 26 domains with coverage metrics
- `pipeline_state` — batch tracking (replaces pipeline-state.json)
- `enrichment_tracking` — per-concept, per-pass tracking with timestamps and model used
- `validation_results` — every validation run with findings
- `ci_gaps`, `delta_entries` — issue tracking (replaces YAML registers)
- `relationships` — all cross-note relationships as a queryable graph

**What this enables:**
- Validation via SQL constraints at write time, not grep-based scanning after the fact
- Enrichment progress queryable: `SELECT * FROM concepts WHERE enrichment_pass < 3`
- Coverage dashboards from SQL, not Dataview (which requires Obsidian open)
- Agent dispatch driven by queries: "next 10 unenriched concepts in crowd-management"
- ACID integrity on all operational state

### Pipeline Configuration Migration

Pipeline rules migrate from prose .md to machine-parseable JSON:
- `ingestion-pipeline.json` — replaces ingestion-rules.md for agent execution (md retained as human-readable companion)
- `enrichment-pipeline.json` — new, defines the 4-pass enrichment workflow
- `validation-rules.json` — replaces validation-rules.md for programmatic validation
- `schema.json` — replaces SCHEMA.yaml
- `vocabulary.json` — replaces VOCABULARY.yaml

### Build Sequence

This infrastructure is F1 scope (April 13, Opus):
1. SQLite schema design and creation
2. Migration script: extract frontmatter from all .md files → insert into SQLite
3. Sync script: read SQLite record → update .md frontmatter
4. JSON pipeline definitions (ingestion + enrichment)
5. Validate round-trip: .md → SQLite → .md produces identical frontmatter
6. Pilot enrichment of 10 concepts using the new infrastructure

---

## §1. Problem Statement

E1 identified a systemic content quality gap across the vault. The technical architecture (schema, taxonomy, pipeline, governance, provenance) is at v1.0 standard. The content layer is at approximately v0.6:

| Quality Dimension | Current State | v1.0 Target |
|---|---|---|
| Claim-to-source traceability | 60% (A-04 audit) | 95%+ |
| Body text depth | Summary-level (3-5 paragraphs) | Reference-level (practitioner learns something new) |
| Confidence calibration | 90.3% high — likely over-assigned | Defensible per-concept with source evidence |
| Inline citation density | Sparse — many claims unsourced in body | Every factual claim cites a source |
| Non-concept types | 20 notes (15 standards, 5 orgs) | 50+ (standards, orgs, technology) |
| Source depth per concept | Many at 1-2 sources | 3+ with diverse source types |

**Root cause:** Every extraction session optimized for domain coverage breadth over per-concept depth. The validation pipeline measures structural compliance (schema, vocabulary, wikilinks), not content depth. Concepts that pass all 35 checks can still be shallow.

---

## §2. Pipeline Evolution — Two Distinct Workflows

### 2.1 Extraction Pipeline (existing, to be refined)

**Purpose:** Processing new DR files into new notes.
**When used:** Future DR research rounds.
**Key change:** Add a depth gate at Stage 4 (Ready):

- Extraction manifest must include a **claim-count estimate** per concept
- Body text must carry **inline citations at the point of creation**, not as backfill
- New Stage 4 rule: "No concept note shall be created with fewer than 3 inline source citations in body text. If the DR file does not contain sufficient evidence for 3+ citations, the concept is flagged as `confidence: low` with a single-source flag."
- Minimum body text length: 500 words for working-depth domains, 300 words for minimum-viable domains

**Codification:** Update `ingestion-rules.md` to v4.0 with these gates.

### 2.2 Enrichment Pipeline (new)

**Purpose:** Deepening existing concepts to publication quality.
**When used:** Phase F enrichment sprint and any future quality passes.
**Model:** Sonnet (structured execution against defined quality standard).
**Unit of work:** One concept note at a time.

**Six-step enrichment workflow per concept:**

```
STEP 1 — READ CONCEPT
  Read the existing concept note. List every factual claim in the body text.
  Classify each claim: CITED (has inline wikilink/reference) or UNCITED.

STEP 2 — READ DR SOURCE
  Identify the DR file(s) tagged to this concept's research_batch.
  Read the sections relevant to this concept's topic.
  Note all source URLs cited in those DR sections.

STEP 3 — DEEPEN BODY TEXT
  For each UNCITED claim: locate the supporting passage in the DR file.
  If evidence found: add inline citation and expand the claim with DR detail.
  If no evidence found: flag the claim for removal or downgrade to "reported but unverified."
  Add new content from DR sections that the original extraction missed.
  Target: body text reads as a reference article, not a summary.

STEP 4 — SOURCE AUDIT
  For each source URL in the DR file's References section that supports this concept:
  Check if a source note exists in 06_Sources/.
  If not: create source note (or flag for batch creation).
  Update concept sources: field with all supporting source wikilinks.
  Target: 3+ sources per concept minimum.

STEP 5 — CONFIDENCE RE-ASSESSMENT
  Re-evaluate confidence tier against actual source evidence:
  - HIGH: 3+ independent sources directly stating the claim, verifiable URLs
  - MEDIUM: 2 sources, or sources that infer rather than state directly
  - LOW: single source, indirect reference, or industry knowledge without citation
  Document the rationale if confidence changes from the original assignment.

STEP 6 — VALIDATE
  Run all 35 pre-write validation checks.
  Verify zero broken wikilinks.
  Verify inline citations resolve to source notes.
  Log enrichment in progress record.
```

**Acceptance gate per concept:** Every factual claim in body text has an inline citation OR is explicitly marked as editorial synthesis. Confidence tier is defensible. 3+ sources in frontmatter.

**Codification:** Create `enrichment-rules.md` in `.claude/rules/` as a peer to `ingestion-rules.md`.

---

## §3. Enrichment Scope — What Gets Enriched

### 3.1 Concept Notes (247 total)

**Priority tiers for enrichment order:**

| Tier | Criteria | Count | Rationale |
|---|---|---|---|
| P1 | DELTA-flagged concepts (DELTA-013, 016, 018, 019) | 31 | Known quality gaps documented in delta register |
| P2 | v2-prompt batch concepts (earliest extractions) | ~140 | First-pass extractions from original 13 prompts — highest likelihood of shallow treatment |
| P3 | dr-s20 batch concepts | ~38 | Second generation — moderate enrichment needed |
| P4 | dr-d2/d3 batch concepts (D3+E1) | ~36 | Most recent — least enrichment needed but still should meet the standard |

**Estimated enrichment rate:** 15-20 concepts per hour with Sonnet (read concept + read DR excerpt + enrich + validate). 247 concepts ÷ 17.5/hr = ~14 hours of enrichment execution across sessions.

### 3.2 Non-Concept Notes

| Type | Current | Target | Source |
|---|---|---|---|
| Standards (02_Standards/) | 15 | 30+ | R-21 has 15+ more extractable; existing concept `implements:` and `governed_by:` fields reference standards not yet in 02_Standards/ |
| Organizations (04_Organizations/) | 5 | 15+ | Source note `author:` fields for corporate authors; concept body text references to IAVM, NFPA, PCMA, AIPC, etc. |
| Technology (03_Technology/) | 0 | 15+ | Concept `supported_by:` fields; body text platform references (Momentus, AXS, Ticketmaster, UKG, etc.) |
| Person (05_People/) | 0 | 0 (deferred) | Requires human verification — not a Sonnet task. Accepted at 0 for v1.0. |

### 3.3 Domain Coverage Gap-Close

5 domains at 7 concepts need +1 each to reach working depth (8+):
- booking-and-sales, data-and-analytics, inclusivity-and-accessibility, security, ticketing-and-box-office
- These can be extracted from existing DR files during the enrichment pass — look for concepts that were identified but not created in original extraction.

---

## §4. Session Schedule (April 13-25)

### Week 1: Pipeline Design + Pilot + Begin Enrichment

| Session | Date | Model | Scope | Deliverables |
|---|---|---|---|---|
| **F1** | Apr 13 (Mon) | Opus | Infrastructure build + pipeline design + pilot | SQLite schema + migration; JSON pipeline definitions; `enrichment-pipeline.json`; `ingestion-pipeline.json` v4.0 with depth gates; sync scripts; pilot enrichment of 10 P1 concepts against new infrastructure; enrichment manifest |
| **F2** | Apr 14 (Tue) | Sonnet | P1 enrichment (DELTA-flagged) | 31 DELTA-flagged concepts enriched to v1.0 standard; A-04 spot-check on completed batch |
| **F3** | Apr 15–16 | Sonnet | P2 enrichment batch 1 (v2-prompt 01-04) | ~60 concepts enriched; non-concept extraction from relevant DR files |
| **F4** | Apr 17–18 | Sonnet | P2 enrichment batch 2 (v2-prompt 05-11) | ~80 concepts enriched; non-concept extraction continues |

### Week 2: Complete Enrichment + QA + Publication

| Session | Date | Model | Scope | Deliverables |
|---|---|---|---|---|
| **F5** | Apr 21–22 | Sonnet | P3+P4 enrichment (S20 + D2/D3 batches) + domain gap-close | ~76 concepts enriched; 5 new concepts for gap-close; non-concept extraction complete |
| **F6** | Apr 23 | Opus | Full QA/QC — A-04 re-audit + confidence re-calibration | A-04 re-audit targeting 95%+ traceability; confidence distribution audit; wikilink integrity; editorial consistency spot-check |
| **F7** | Apr 24–25 | Opus | Publication artifacts + close-out | METHODOLOGY v3.0 (final statistics); README update; validation report; PR; tag v1.0.0 |

**Total estimated sessions:** 7 (2 Opus, 5 Sonnet)
**Total estimated enrichment execution:** ~14 hours across F2-F5

---

## §5. Quality Gates

### Per-Concept Gate (applied during F2-F5)

Every enriched concept must pass before being marked complete:
- [ ] Every factual claim in body text has an inline citation
- [ ] 3+ source notes in frontmatter `sources:` field
- [ ] Confidence tier is defensible with documented rationale if changed
- [ ] Body text is reference-depth (practitioner would learn something)
- [ ] All 35 pre-write validation checks pass
- [ ] No broken wikilinks

### Per-Session Gate (applied at end of each enrichment session)

- [ ] Enrichment count matches plan
- [ ] Spot-check: random 5 concepts re-audited for traceability
- [ ] No new broken wikilinks introduced
- [ ] Progress logged

### Publication Gate (F6-F7)

- [ ] A-04 re-audit: 95%+ claim-to-source traceability (up from 60%)
- [ ] Confidence distribution is defensible (expect shift from 90/9/1 toward 80/15/5 or similar)
- [ ] 26/26 domains at working depth (8+)
- [ ] Non-concept types: 30+ standards, 15+ organizations, 15+ technology
- [ ] Zero broken wikilinks
- [ ] Zero forbidden terminology
- [ ] METHODOLOGY.md reflects final state
- [ ] README.md reflects final state
- [ ] Obsidian mounts cleanly

---

## §6. Sonnet Enrichment Prompt Architecture

Each Sonnet enrichment session receives:

**System prompt:** Enrichment rules, schema, vocabulary, quality standard, per-concept acceptance criteria.

**Per-concept context package:**
1. The existing concept note (full frontmatter + body)
2. Relevant DR file excerpt (pre-extracted section — not the full 600-1000 line DR file)
3. Existing source notes referenced by the concept (frontmatter only — for citation verification)

**Task instruction:** "Enrich this concept to publication quality following the 6-step enrichment workflow. Return the complete updated note."

**Why this works for Sonnet:**
- All architectural decisions are made (taxonomy, schema, relationships locked)
- Each unit of work is self-contained (one concept at a time)
- The quality standard is explicit and measurable (inline citations, 3+ sources, confidence rationale)
- No judgment calls on taxonomy, relationship types, or governance — pure structured execution
- Opus handles pipeline design, QA/QC, and anything requiring cross-corpus judgment

**Prep work for Sonnet sessions (done by Opus in F1):**
- Build concept-to-DR-section mapping manifest
- Pre-extract relevant DR sections per concept into a structured format
- Define the exact system prompt and per-concept template
- Validate the approach on 10 pilot concepts

---

## §7. Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Sonnet enrichment quality below standard | Medium | High | Opus QA spot-checks after each batch; pilot 10 concepts in F1 to calibrate prompt |
| DR file sections insufficient for deep enrichment on some concepts | Medium | Medium | Flag concepts where DR evidence is thin; accept at `confidence: low` with documented rationale rather than padding |
| Token budget exceeded on enrichment sessions | Low | Medium | Sonnet cost is ~5x lower than Opus; 14 hours of Sonnet execution is economically feasible |
| Schedule slip beyond April 25 | Medium | Low | The content is usable now; the enrichment improves it. A few days of slip doesn't change the outcome. |
| Enrichment introduces new errors | Low | High | Full validation after every concept; A-04 re-audit in F6 catches anything missed |

---

## §8. Success Criteria for Phase F

| # | Criterion | Measurement |
|---|---|---|
| 1 | 95%+ claim-to-source traceability | A-04 re-audit across full corpus |
| 2 | Every concept at reference depth | Body text depth spot-check (min 500 words for working-depth domains) |
| 3 | Confidence distribution defensible | Re-calibration audit with per-concept rationale |
| 4 | 26/26 domains at working depth | Domain coverage table |
| 5 | 50+ non-concept notes | Standards + Organizations + Technology count |
| 6 | Enrichment pipeline codified | `enrichment-rules.md` in `.claude/rules/` |
| 7 | Ingestion pipeline hardened | `ingestion-rules.md` v4.0 with depth gates |
| 8 | v1.0 tag on main | `gh pr create` + merge + `git tag v1.0.0` |

---

## §9. What "Done" Looks Like

A venue operations professional opens this KB in Obsidian. They navigate to a concept — say, Crowd-Management-Flow-Management-Crush-Prevention. The body text reads like a reference article: specific, cited, deep enough that they learn something they didn't know. Every claim links to a source. The confidence rating is justified. The cross-domain links lead to related concepts that are equally substantive. The standards folder has the NFPA and ISO standards referenced in the concept. The organizations folder has the IAVM and NFPA entries.

They trust it because they can trace any claim. They use it because the depth is there.

That's v1.0.

---

*AI Disclosure: Plan co-produced by Claude (Anthropic) and Alex Jackson, 2026-04-07.*
