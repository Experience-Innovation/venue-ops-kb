---
title: "Session 18 Operational Plan — CI / Enrichment Cycle"
session: S18
date: 2026-04-05
lifecycle: active
machine: "MacBook Air (bubblegumpshrimpco)"
branch: "session-18/ci-enrichment-cycle"
initiative: "Academic Rigor Initiative Phase B.5 Session 3"
---

# Session 18 Operational Plan

## §1. Session Declaration

| Field | Value |
|---|---|
| Session | S18 |
| Date | 2026-04-05 |
| Machine | MacBook Air (bubblegumpshrimpco) |
| Branch | session-18/ci-enrichment-cycle |
| Base commit | 3c11584 (main @ PR #7 merge) |
| Operator | Claude Opus 4.6 (ESC persona v2.1) |
| Reviewer | Alex Jackson |
| Initiative | Academic Rigor Initiative Phase B.5 Session 3 |
| Phase | CI / Enrichment Cycle |
| Lineage | S17 → S18 (A-04 Part 1 CONDITIONAL PASS → DR remediation + bibliographic enrichment) |

**Session objective:** Process 5 targeted DR remediation files to resolve 5 HIGH-severity traceability gaps (DELTA-007 through DELTA-011), execute DELTA-004 bibliographic enrichment across 260 source notes, and resolve 11 MED-severity traceability gaps (DELTA-012) if budget permits.

**Binary success test:** DELTA-007-011 resolved + DELTA-004 resolved (or partially resolved with documented scope) + validation report filed + PR opened.

---

## §2. Brigade Roster

| Role | Assignment | Tool Access |
|---|---|---|
| **ESC (primary)** | Orchestration, planning, quality gates, concept enrichment, delta register maintenance | All |
| **Explore agents** | Source note metadata extraction (Track B batched grep operations) | Read-only |

**Dispatch estimate:** Low agent count session. Track A is sequential enrichment work (read DR → extract URLs → create source notes → enrich concepts). Track B uses grep-based batch extraction — may dispatch 2-3 Explore agents for parallel source_type cluster analysis. Track C is manual wikilink resolution.

**Tier level:** Tier 1 (< 3 agent dispatches expected). Escalate to Tier 2 only if Track B requires parallel agent batches.

---

## §3. GLRC Framework

### Governance
- All new source notes validated against SCHEMA.yaml before writing
- All enriched concept notes re-validated after modification
- Terminology scan before every commit
- Frontmatter Field Conventions enforced (status: on content notes, lifecycle: on governance artifacts, audit_outcome: on validation reports)

### Lineage
- Session branch: session-18/ci-enrichment-cycle
- All DR remediation file URLs verified verbatim (S15 URL-verbatim standard)
- Source notes carry research_batch tag (new batch ID for DR remediation files)
- Commit messages with full narrative per feedback_commit-message-standard

### Reconciliation
- Delta register metrics reconciled at session close
- Source note count: 260 (pre-session) → 260 + N (post-Track A)
- DELTA-004 progress tracked: X/260 enriched with author/publication/publish_date
- Concept enrichment tracked: 5 concepts × sources[] additions

### Compliance
- Hard Rule #1: Zero fabrication — author/publication/publish_date null if not inferable
- Hard Rule #4: CS/BMO Centre exemplar-only (tag cs_exemplar: true if applicable)
- Hard Rule #9: All wikilinks quoted in frontmatter
- Hard Rule #12: Source notes before concept enrichment
- S15 URL-verbatim standard: every URL grep-verified against DR file text

---

## §4. Phase Definitions

### Phase 1: DR File Registration + Rename (~5K tokens)
**Owner:** ESC
**Duration:** Minimal
**Steps:**
1. Rename 5 DR files to pipeline convention (DR-Remediation-*.md)
2. Register in pipeline-state.json as new batch (batch-13-dr-remediation)
3. Log in progress.md
**Exit:** 5 files registered, pipeline-state.json updated

### Phase 2: Track A — DR Remediation Intake (5 files × 5-stage pipeline) (~120K tokens)
**Owner:** ESC
**Duration:** Major phase
**Steps per file:**
1. **Rinse:** Read DR file, identify all footnote URLs, strip any non-factual content
2. **Ready:** Map URLs to source_type, build extraction manifest (which URLs → which source notes)
3. **Route:** Create source notes (Source-0261+) with full frontmatter
4. **Enrich:** Update target concept note — add new sources[] wikilinks, enrich body text with claim-backing inline citations
5. **Validate:** 34 pre-write checks on all new/modified notes
**Gate:** Each concept note passes schema validation + has claim-to-source traceability for all body claims
**Exit:** 5 concept notes enriched, ~25-35 new source notes created, DELTA-007-011 resolvable

### Phase 3: Track B — DELTA-004 Bibliographic Enrichment (~150K tokens)
**Owner:** ESC (with Explore agents for grep extraction)
**Duration:** Major phase — centerpiece
**Steps:**
1. Count current source notes by source_type using grep
2. For each source_type cluster, extract description fields in bulk
3. Derive author/publication/publish_date from description + URL pattern:
   - regulatory-document → author = issuing agency (NFPA, FDA, OSHA, etc.)
   - deep-research → author = null (extraction_model already captured)
   - industry-publication → author from description byline
   - trade-association → author = association name
   - vendor-documentation → author = vendor name
   - academic-paper → author from description
   - news-article → author from byline in description
   - conference-proceedings → author from description
4. Write enrichments in batches (edit frontmatter, add author/publication/publish_date)
5. Track progress: X/260 enriched per cluster
**Gate:** No fabricated metadata. Null where not inferable.
**Exit:** DELTA-004 resolved or partially resolved with documented remaining scope

### Phase 4: Track C — DELTA-012 MED-Severity Resolution (~30K tokens, if budget permits)
**Owner:** ESC
**Duration:** Minor phase
**Steps:**
1. Read audit report per-concept MED gap list
2. For each of 11 concepts, identify existing source notes in 06_Sources/ that cover the unsourced claims
3. Add supplementary source wikilinks to concept frontmatter sources[]
4. Add inline citations in body text where gap was identified
**Exit:** DELTA-012 partially or fully resolved

### Phase 5: Validation + Delta Register (~15K tokens)
**Owner:** ESC
**Steps:**
1. Run terminology scan on all modified files
2. Write validation report: _Pipeline/Validation/session-18-ci-enrichment-validation.md
3. Update delta register: DELTA-004, DELTA-007-011 status → resolved with resolution_evidence
4. If Track C executed: update DELTA-012
5. Reconcile metrics
**Exit:** Validation report filed, delta register current

### Phase 6: Session Close-Out (~30K tokens)
**Owner:** ESC
**Steps:**
1. Update progress.md with session work
2. Update pipeline-state.json
3. Git commit with full narrative
4. Push branch, create PR via gh pr create
5. Retro conversation with Alex
6. Handoff + pass-forward document
**Exit:** PR opened, close-out complete

---

## §5. Batch Definitions

### Batch 13: DR Remediation Intake

| Sub-batch | DR File | Target Concept | Target DELTA | Est. Source Notes |
|---|---|---|---|---|
| 13a | DR-Remediation-Gender-Inclusive-Facilities.md | Inclusivity-And-Accessibility-Gender-Inclusive-Facilities | DELTA-007 | 5-8 |
| 13b | DR-Remediation-Indigenous-Reconciliation.md | Inclusivity-And-Accessibility-Indigenous-Cultural-Programming | DELTA-008 | 4-6 |
| 13c | DR-Remediation-Liquor-Licensing.md | Legal-Compliance-And-Licensing-Liquor-Licensing-Venues | DELTA-009 | 5-8 |
| 13d | DR-Remediation-Responsible-Beverage-Service.md | Legal-Compliance-And-Licensing-Responsible-Beverage-Service | DELTA-010 | 6-8 |
| 13e | DR-Remediation-Trademark-Naming-Rights.md | Legal-Compliance-And-Licensing-Naming-Rights | DELTA-011 | 4-6 |

**Total estimated source notes:** 24-36 (Source-0261 through ~Source-0296)
**Source selection criteria:** Primary authoritative URLs that directly back claims in concept body text. Not all 384 unique URLs in DR files — select the sources that resolve the identified traceability gaps.

### Batch 14: DELTA-004 Bibliographic Enrichment

| Cluster | source_type | Est. Count | Approach |
|---|---|---|---|
| 14a | regulatory-document | ~60 | author = issuing agency from description |
| 14b | deep-research | ~40 | author = null (DR output, not original author) |
| 14c | industry-publication | ~50 | author from description byline pattern |
| 14d | trade-association | ~40 | author = association name from description |
| 14e | vendor-documentation | ~30 | author = vendor name from description |
| 14f | academic-paper | ~15 | author from description |
| 14g | news-article | ~15 | author from byline in description |
| 14h | conference-proceedings | ~10 | author from description |

**Note:** Counts are estimates. Actual distribution to be confirmed via grep count at Phase 3 start.

---

## §6. Delta Register State (Pre-Session)

| ID | Category | Severity | Status | S18 Action |
|---|---|---|---|---|
| DELTA-001 | vocabulary | low | resolved-inline (S16) | No action |
| DELTA-002 | vocabulary | low | resolved-inline (S16) | No action |
| DELTA-003 | vocabulary | low | resolved-inline (S16) | No action |
| DELTA-004 | citation | medium | **deferred → S18 target** | **Track B: resolve** |
| DELTA-005 | citation | low | resolved-inline (S16) | No action |
| DELTA-006 | obsidian | medium | resolved-inline (S17) | No action |
| DELTA-007 | traceability | **high** | **deferred → S18 target** | **Track A: resolve** |
| DELTA-008 | traceability | **high** | **deferred → S18 target** | **Track A: resolve** |
| DELTA-009 | traceability | **high** | **deferred → S18 target** | **Track A: resolve** |
| DELTA-010 | traceability | **high** | **deferred → S18 target** | **Track A: resolve** |
| DELTA-011 | traceability | **high** | **deferred → S18 target** | **Track A: resolve** |
| DELTA-012 | traceability | medium | **deferred → S18 if budget** | **Track C: attempt** |
| DELTA-013 | traceability | low | deferred (S18-S20) | No action (polish) |

**S18 targets:** 6 entries (DELTA-004, 007-011) mandatory. DELTA-012 stretch goal.

---

## §7. Kanban

| Status | Tasks |
|---|---|
| **Done** | ✅ Orientation (MFA 1-9), ✅ DR file verification (GATE passed) |
| **In Progress** | 📝 Operational plan (this document) |
| **Ready** | Phase 1: DR registration + rename |
| **Backlog** | Phase 2: Track A (DR intake), Phase 3: Track B (DELTA-004), Phase 4: Track C (DELTA-012), Phase 5: Validation, Phase 6: Close-out |

---

## §8. Token Budget

| Phase | Est. Tokens | Cumulative |
|---|---|---|
| Orientation + planning | ~120K | 120K |
| Phase 1: DR registration | ~5K | 125K |
| Phase 2: Track A (5 DR files) | ~120K | 245K |
| Phase 3: Track B (260 source notes) | ~150K | 395K |
| Phase 4: Track C (11 concepts) | ~30K | 425K |
| Phase 5: Validation + delta register | ~15K | 440K |
| Phase 6: Close-out | ~30K | 470K |
| **Buffer (compaction, retries)** | ~30K | **500K** |

**Soft target:** 500K
**Hard cap:** 750K
**Risk:** Track B (260 source notes × 3 fields) is volume work. If grep-based batch approach works cleanly, stays within estimate. If individual file reads required for ambiguous cases, could expand to ~200K. Mitigation: batch aggressively by source_type, accept null for ambiguous cases rather than over-reading.

---

## VOCABULARY.yaml Addition Required

The 5 DR remediation files need a `research_batch` identifier. The current VOCABULARY.yaml does not include a batch ID for targeted remediation DR. Options:

1. **Add `dr-remediation-s18`** as a new research_batch value
2. **Reuse existing batch IDs** based on original concept extraction batch

**Recommendation:** Add `dr-remediation-s18` — these are targeted remediation research runs, distinct from the original v2.0 prompts. This maintains clean provenance lineage.

**Requires Alex alignment before Phase 2 execution.**

---

*Experience Innovation Inc. | VEP KB Session 18 Operational Plan | Academic Rigor Initiative Phase B.5 Session 3 | 2026-04-05*
