---
type: operational-plan
lifecycle: active
created: 2026-04-06
session: D3
branch: session-d3/ingestion
machine: MacBook Air (bubblegumpshrimpco)
initiative: Phase D CI Initiative
---

# Session D3 Operational Plan — DR Ingestion + Publication-Ready

**Session:** D3 (Phase D, Session 3)
**Date:** 2026-04-06
**Predecessor:** D2 (PR #13 merged)
**Operator:** Claude (Opus 4.6, 1M context)

---

## §1. Context & Scope

**Inherited state:**
- 207 concepts, 390 sources, 26 domain overviews, 27 MOCs
- CI gap register: 8 open (CI-GAP-012, 016, 022, 023, 028, 030, 031, 032)
- D2 completed: SCHEMA v3.0, templates standardized, METHODOLOGY v2.0, LICENSE, 22/34 CI gaps resolved
- 16 domains below working depth (8+); 6 HIGH-priority domains at 3-5 concepts
- 4 non-concept note type folders empty (02-05)
- All governance infrastructure complete — ready for bulk ingestion

**New inputs (this session):**
- 16 DR output files (R-11 through R-25, with R-11 in two versions) totaling ~1.3MB
- Files staged in `_Pipeline/Input/` with standardized naming (DR-RNN-description.md)
- D2 DR prompts R-11–R-19 designed by Claude, executed by Alex in Perplexity Pro
- R-20–R-25 are Alex-authored prompts covering innovation, ISO standards, university venues, specialty venues, legal liability, and venue-community relations

**Scope decisions:**
1. **PRIMARY:** Ingest all 16 DR files through the 5-stage pipeline — concepts, sources, cross-links
2. **SECONDARY:** Extract non-concept notes (standards, organizations, technologies) from R-21 (ISO Standards) and across ingested corpus
3. **TERTIARY:** Resolve all D3-targeted CI gaps (012, 016, 022, 023, 028, 030, 031)
4. **GATE:** Final validation pass, METHODOLOGY update, README update, publication gate check
5. **Processing order:** HIGH priority domains first (R-11/R-12/R-13), then MEDIUM (R-14–R-19), then NEW (R-20–R-25)

**Scope exclusions:**
- Person notes (lowest yield, highest verification cost — per enrichment backlog §3)
- Full DELTA-018/019 enrichment (addressed partially through R-11 ingestion; remaining items are Phase E)
- CI-GAP-032 full resolution (non-concept extraction is started this session, not completed)

---

## §2. Brigade Roster

| Role | Owner | Responsibility | Batch Size |
|------|-------|---------------|------------|
| **ESC** | Claude (primary) | Orchestration, pipeline execution, QA gates, governance | All phases |
| **Explore agents** | Subagents | DR file spot-checks, duplicate verification | Ad hoc |

**Agent dispatch standards:** This session is primarily direct execution (reading, writing notes). No large-scale agent dispatches needed — the ESC handles ingestion directly. Explore agents used only for parallel spot-checks.

---

## §3. GLRC Framework

| Dimension | Checkpoint | When | Evidence |
|-----------|-----------|------|----------|
| **Governance** | Operational plan aligned with Alex | Pre-execution | This document |
| **Governance** | VOCABULARY.yaml updated with new research_batch entries | Phase 1 | Controlled vocabulary current |
| **Lineage** | ai_disclosure + extraction_model + research_batch on every note | Every note write | Frontmatter validation |
| **Lineage** | Source notes created before concept notes | Every batch | Processing workflow compliance |
| **Reconciliation** | Wikilink integrity check (Step 5b) | Every batch | Zero broken links |
| **Reconciliation** | Deduplication check before every concept creation | Every concept | No duplicate notes |
| **Compliance** | Schema validation (35 rules) per note | Every note write | Validation report per batch |
| **Compliance** | Terminology scan pre-commit | Session close | Zero forbidden terms |

---

## §4. Phase Definitions

### Phase 1: Setup + VOCABULARY Update (~20K tokens)

**Owner:** ESC
**Objective:** Register all 16 DR files, update VOCABULARY.yaml with new research_batch entries, update pipeline-state.json.

**Workflow:**
1. Add research_batch entries for R-20 through R-25 to VOCABULARY.yaml
2. Register all files in pipeline-state.json
3. Log receipt in progress.md

**Exit criteria:**
- All 16 files registered
- VOCABULARY.yaml has entries for all research batches
- pipeline-state.json updated

### Phase 2: Batch A — HIGH Priority (R-11, R-12, R-13) (~150K tokens)

**Owner:** ESC
**Objective:** Ingest the 3 highest-priority DR outputs targeting the weakest domains.

**Targets:**
| DR File | Domain | Current | Target |
|---------|--------|:-------:|:------:|
| R-11 (both versions) | people-and-culture | 7 | 10+ |
| R-12 | logistics-and-warehouse | 3 | 8+ |
| R-13 | financial-operations | 4 | 8+ |

**Workflow per file:**
1. Read DR file (Stage 2: Register)
2. Rinse: strip marketing, identify entities, note source URLs
3. Ready: map concepts to domains, assign confidence, build extraction manifest
4. Present manifest (internal gate — validate against VOCABULARY.yaml)
5. Create source notes (Stage 5: Route — sources first)
6. Create/enrich concept notes
7. Cross-link (Step 4)
8. Validate (Step 5 + 5b)

**Exit criteria:**
- logistics-and-warehouse at 8+ concepts (working depth)
- financial-operations at 8+ concepts (working depth)
- people-and-culture enriched with workforce/labor content
- All source notes created with URLs
- Zero broken wikilinks

### Phase 3: Batch B — MEDIUM Priority Core (R-14, R-15, R-16) (~120K tokens)

**Owner:** ESC
**Objective:** Deepen crowd-management, supply-chain, and guest-experience domains.

**Targets:**
| DR File | Domain | Current | Target |
|---------|--------|:-------:|:------:|
| R-14 | crowd-management | 4 | 8+ |
| R-15 | supply-chain-and-procurement | 4 | 8+ |
| R-16 | guest-experience | 5 | 8+ |

**Exit criteria:**
- All 3 domains at working depth (8+)
- CI-GAP-028 addressed (cross-batch corroboration for single-batch domains)
- CI-GAP-030 addressed (logistics confidence enrichment via related supply-chain content)

### Phase 4: Batch C — MEDIUM Priority Digital (R-17, R-18, R-19) (~100K tokens)

**Owner:** ESC
**Objective:** Deepen marketing, technology, and parking (confidence enrichment).

**Targets:**
| DR File | Domain | Current | Target |
|---------|--------|:-------:|:------:|
| R-17 | marketing-and-communications | 5 | 8+ |
| R-18 | technology-and-digital | 5 | 8+ |
| R-19 | parking-and-transportation | 10 | 10 (confidence enrichment) |

**Exit criteria:**
- marketing-and-communications at working depth
- technology-and-digital at working depth
- CI-GAP-031 addressed (parking independent source enrichment)

### Phase 5: Batch D — NEW Coverage (R-20 through R-25) (~200K tokens)

**Owner:** ESC
**Objective:** Process 6 additional DR outputs covering innovation, ISO standards, university venues, specialty venues, legal liability, and venue-community relations.

**Sub-batches:**
| DR File | Primary Domains | Key Value |
|---------|----------------|-----------|
| R-20 Innovation | technology-and-digital, strategy-and-governance | Future-facing concepts, AI/ML venue applications |
| R-21 ISO Standards | quality-and-continuous-improvement, ALL | **Non-concept extraction target** — standards notes for 02_Standards/ |
| R-22 University/Small Venue | multiple | Fills venue_scale: small/medium gap across corpus |
| R-23 Emerging/Specialty Pt 2 | multiple | Specialty venue type coverage |
| R-24 Legal Liability | legal-compliance-and-licensing | Deepens regulatory landscape, addresses case law |
| R-25 Venue-Community | strategy-and-governance | Government relations, community benefit agreements |

**Exit criteria:**
- New concepts extracted from all 6 files
- R-21 produces first standard notes in 02_Standards/
- Organization notes extracted where clearly identified
- Technology notes extracted where clearly identified

### Phase 6: Non-Concept Note Extraction (~50K tokens)

**Owner:** ESC
**Objective:** Extract standards, organizations, and technology notes from the full session corpus. First content in 02_Standards/, 03_Technology/, 04_Organizations/.

**Approach:** Per enrichment backlog §3 — Standards first (highest yield), then Organizations, then Technology.

**Exit criteria:**
- At least 15 standard notes in 02_Standards/
- At least 10 organization notes in 04_Organizations/
- At least 5 technology notes in 03_Technology/
- CI-GAP-032 partially addressed (non-concept extraction started)

### Phase 7: CI Gap Resolution + Documentation (~30K tokens)

**Owner:** ESC
**Objective:** Close all D3-targeted CI gaps.

| Gap | Action |
|-----|--------|
| CI-GAP-012 | Document S18 validation report variance as acceptable |
| CI-GAP-016 | Add minimal frontmatter to progress.md (already resolved in D2 per handoff) |
| CI-GAP-022 | Document batch numbering convention in ingestion-rules.md |
| CI-GAP-023 | Document DR input file naming convention |
| CI-GAP-028 | Verify cross-batch corroboration achieved through DR ingestion |
| CI-GAP-030 | Verify logistics confidence improved through R-12 |
| CI-GAP-031 | Verify parking confidence improved through R-19 |

**Exit criteria:**
- All D3-targeted CI gaps resolved or documented
- ci-gap-register.yaml updated

### Phase 8: Final Validation + Publication Gate (~40K tokens)

**Owner:** ESC
**Objective:** Zero-error vault validation, statistics update, publication readiness check.

**Workflow:**
1. Full schema validation sweep
2. Terminology scan
3. Wikilink integrity check
4. Orphan detection
5. Domain coverage table (all 26 domains)
6. METHODOLOGY.md final update with post-D3 statistics
7. README.md updated with final counts
8. Validation report written

**Exit criteria:**
- Zero schema violations
- Zero broken wikilinks
- Zero orphans
- All 26 domains at minimum viable (3+)
- 22+ domains at working depth (8+)
- METHODOLOGY.md current
- README.md current

### Phase 9: QA/QC + Remediation (~20K tokens)

**Owner:** ESC
**Objective:** Self-audit all Phase 2-8 outputs. Fix issues found.

### Phase 10: PM/GLRC Delta Analysis + Session Close-Out (~40K tokens)

**Owner:** ESC + Alex
**Objective:** Mandatory close-out per protocol.

**Sub-phase 10a — PM/GLRC Delta Analysis:**

| Artifact | Check |
|----------|-------|
| Initiative roadmap | D3 items marked complete, gate criteria updated |
| CI gap register | All D3 gaps resolved, metrics updated |
| Progress.md | D3 session entry complete |
| Pipeline-state.json | Status current, batch entries added |
| Domain overviews | node_count fields accurate for all enriched domains |
| VOCABULARY.yaml | New research_batch entries present |
| Enrichment backlog | Updated with D3 outcomes |

**Sub-phase 10b — Standard Close-Out:**
1. Session accounting (work product inventory + OIR)
2. Retro conversation with Alex
3. Handoff + pass-forward
4. Git commit + push + PR

---

## §5. Batch Definitions

| Batch | Scope | DR Files | Est. New Concepts | Est. New Sources |
|-------|-------|----------|:-----------------:|:----------------:|
| batch-19-workforce-labor | R-11 (2 versions) | 2 | 5-8 | 20-30 |
| batch-20-logistics | R-12 | 1 | 5-8 | 15-25 |
| batch-21-financial | R-13 | 1 | 4-6 | 15-20 |
| batch-22-crowd-mgmt | R-14 | 1 | 4-6 | 15-20 |
| batch-23-supply-chain | R-15 | 1 | 4-6 | 15-20 |
| batch-24-guest-experience | R-16 | 1 | 4-6 | 15-25 |
| batch-25-marketing | R-17 | 1 | 4-6 | 15-20 |
| batch-26-technology | R-18 | 1 | 4-6 | 15-20 |
| batch-27-parking-enrich | R-19 | 1 | 0-2 (enrichment) | 10-15 |
| batch-28-innovation | R-20 | 1 | 4-8 | 15-25 |
| batch-29-iso-standards | R-21 | 1 | 3-5 + 15-25 standards | 15-25 |
| batch-30-university-venue | R-22 | 1 | 5-10 | 15-25 |
| batch-31-specialty-venues | R-23 | 1 | 3-5 | 10-15 |
| batch-32-legal-liability | R-24 | 1 | 4-8 | 15-25 |
| batch-33-venue-community | R-25 | 1 | 4-8 | 15-25 |
| batch-34-non-concept | Cross-corpus | — | 30-50 (std/org/tech) | 0 |

**Totals estimated:** 85-160 new concept notes, 30-50 non-concept notes, 200-350 new source notes

---

## §6. Binary Success Criteria

| # | Criterion | How Measured |
|---|-----------|-------------|
| 1 | HIGH priority DR ingested (R-11, R-12, R-13) | logistics ≥8, financial-ops ≥8, people-and-culture enriched |
| 2 | MEDIUM priority DR ingested (R-14–R-19) | crowd-mgmt ≥8, supply-chain ≥8, guest-exp ≥8, marketing ≥8, tech ≥8 |
| 3 | Additional DR ingested (R-20–R-25) | Concepts extracted from all 6 files |
| 4 | Non-concept notes extracted | ≥15 standards, ≥10 organizations, ≥5 technologies |
| 5 | Zero D3-targeted CI gaps remaining | ci-gap-register.yaml shows 0 D3 open |
| 6 | Final validation pass clean | Zero schema violations, zero broken wikilinks, zero orphans |
| 7 | METHODOLOGY + README current | Post-D3 statistics reflected |
| 8 | PR opened | `gh pr create` successful |

---

## §7. Risk Register

| Risk | Severity | Mitigation |
|------|----------|------------|
| Token budget exceeded before all DR processed | HIGH | Process HIGH priority first; if budget tight, defer R-23 (smallest file, 35K) and non-concept extraction to follow-up session |
| Context compaction loses extraction manifest | MEDIUM | Write manifests to Processing/ before creating notes; log progress after each batch |
| Duplicate concept creation across DR files | MEDIUM | Deduplication check before every concept (filename + title search); enrich existing notes |
| R-21 through R-25 prompt number assignment incorrect | LOW | Content verified via headers; cross-reference with Alex if any prompt purpose seems misaligned |
| Source URL fabrication in DR outputs | LOW | Perplexity Pro inline citations verified in prior sessions (S20); spot-check 3 URLs per batch |

---

## §8. Token Budget

| Phase | Estimated Tokens | Cumulative |
|-------|:----------------:|:----------:|
| Session start + scan | 50K | 50K |
| Phase 1: Setup | 20K | 70K |
| Phase 2: Batch A (HIGH) | 150K | 220K |
| Phase 3: Batch B (MEDIUM core) | 120K | 340K |
| Phase 4: Batch C (MEDIUM digital) | 100K | 440K |
| Phase 5: Batch D (NEW coverage) | 200K | 640K |
| Phase 6: Non-concept extraction | 50K | 690K |
| Phase 7: CI gap resolution | 30K | 720K |
| Phase 8: Final validation | 40K | 760K |
| Phase 9: QA/QC | 20K | 780K |
| Phase 10: Close-out | 40K | 820K |
| **Total estimated** | **820K** | |
| **Budget ceiling** | **1,000K** | |
| **Buffer** | **180K** | |

**Risk mitigation:** If approaching 700K before Phase 5 completes, consolidate Phases 6-7 and reduce Phase 8 scope. HIGH priority DR (Phase 2) is the minimum viable session output.

---

*AI Disclosure: Operational plan co-produced by Claude (Anthropic) and Alex Jackson, 2026-04-06.*
