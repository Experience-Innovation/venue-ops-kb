# Session 15 — Operational Plan
**Date:** 2026-04-05
**Machine:** MacBook Air (bubblegumpshrimpco)
**Branch:** session-15/batch-processing (worktree)
**Base commit:** 5ee694f (S14 close-out cherry-picked)
**Owner:** Alex Jackson, Principal Consultant — EXi
**Operator:** Claude Opus 4.6 (ESC persona)

---

## 1. Session Context & Scope

### What happened before
Session 14 completed batches 05-08 (64 concepts, 110 sources) but the close-out commit was pushed AFTER PR #4 was merged, leaving D#45 and session artifacts stranded on the remote branch. Session 15 opened with a delta audit, recovered the S14 close-out via cherry-pick, and remediated 5 additional gaps (see `session-15-delta-analysis.md`).

### Session 15 scope
- **Primary:** batch-09-existing-dr — extract venue ops intelligence from 5 original v1.0 DR reports
- **Secondary:** batch-10-cross-linking — vault-wide orphan detection, relationship density audit
- **Closeout:** Full 5-phase GLRC sequence

### Strategic intent
Bring 4 remaining zero-concept domains (data-and-analytics, financial-operations, booking-and-sales, tenant-and-partner-relations) to at least scaffolded status. Advance strategy-and-governance, quality-and-continuous-improvement, technology-and-digital, people-and-culture from minimum viable toward working depth.

### Out of scope
- batch-11-mocs (MOC generation) — deferred to future session
- batch-12-final-validation — deferred to future session
- Standard/Technology/Organization/Person note types — deferred per design (S14 OIR items #2-#4)
- Any VEP-Client repo work

---

## 2. Brigade Roster (R&R per role)

| Role | Staffing | R&R | When Activated |
|------|----------|-----|----------------|
| **Executive Sous Chef (ESC)** | Claude Opus 4.6 (primary context) | Brigade leader, dispatch planner, QA authority, personally accountable for completion. Writes dispatch plans, enforces output schemas, runs terminology scans, makes GO/NO-GO calls at every gate. | Entire session |
| **Recon Agent (Rinse stage)** | Explore subagent | Reads each DR file, extracts venue-ops concepts only (filtering out podcast strategy, GTM, competitive positioning, EXi business content). Returns extraction manifest with concept name, target domain, confidence tier, source URLs. | batch-09 Stage 3 (Rinse) |
| **Source Builder Agent (Route stage, sources)** | Explore subagent | Creates source notes in 06_Sources/ per extraction manifest. Follows Source-NNNN-description.md naming, populates required frontmatter fields. | batch-09 Stage 5 (after Ready gate) |
| **Concept Builder Agent (Route stage, concepts)** | Explore subagent | Creates concept notes in 01_Domains/{slug}/ per extraction manifest. Links to source notes, parent domain overview, related concepts. Applies cross-cutting dimensions. | batch-09 Stage 5 (after sources written) |
| **QA Auditor Agent (Post-batch gate)** | Explore subagent | Runs 6-dimension QA: terminology, schema, wikilinks, link integrity, orphans (vault-wide), vocabulary. Includes source notes in terminology scan per S14 retro. | batch-09 gate, batch-10 final gate |
| **Orphan Resolver Agent (batch-10)** | Explore subagent | Vault-wide orphan detection across all 01_Domains/. Proposes related_to links to resolve each orphan. Returns link mapping for ESC approval. | batch-10 primary task |

**Batch sizing:** 1-file batches get 10-15 concepts. 5-file cross-domain enrichment = 10-20 concepts total. Recon agent handles all 5 files in one dispatch (parallel extraction). Concept builders cap at 8-10 notes per agent for dense content.

**Dispatch guardrails (per CLAUDE.md ESC persona):**
- Pre-extract binary content before dispatching (N/A for batch-09 — all markdown)
- Never dispatch agents for Bash-heavy work
- Never use bypassPermissions for Agent SDK agents
- All dispatch prompts include 7 required fields (objective, output format, tool/source guidance, task boundaries, success criteria, constraints, escalation)

---

## 3. GLRC Framework (per phase)

| Phase | Governance | Lineage | Reconciliation | Compliance |
|-------|-----------|---------|----------------|-----------|
| **Phase 0: Delta Audit** | ESC owns gate decisions; human-reviewable delta table | S14 artifacts traced via git log; cherry-pick commit recorded | Pipeline-state, progress.md, domain counts verified against actual files | D#45 scope verified across 3 files (CLAUDE.md, validation-rules.md) |
| **Phase 1: Operational Plan** | This document; Alex GL required before execution | Plan links to predecessor session (S14 handoff, delta analysis) | Plan scope reconciled with pipeline-state.json pending batches | Plan conforms to 8-section standard |
| **Phase 2: batch-09 Receive/Register** | Input files accessed from worktree path only | pipeline-state.json updated with file registration | Word counts verified against pass-forward | All 5 input files present per OIR |
| **Phase 3: batch-09 Rinse (Recon)** | Recon agent dispatch plan logged; output schema enforced | Extraction manifest traces each concept to source DR file | Manifest count reconciled against concept targeting | Podcast/GTM/EXi content filtered out (audit trail) |
| **Phase 4: batch-09 Ready (Gate)** | ESC validates manifest against VOCABULARY.yaml before Route | Every manifest entry has target domain, confidence tier | Manifest duplicates checked against existing 152 concepts | All domain slugs from 26-domain taxonomy |
| **Phase 5: batch-09 Route (Sources)** | Source Builder agent dispatch plan logged | Source-0231+ numbering sequential; DR file → source lineage | Source count matches manifest URL count | ai_disclosure, research_batch, extraction_model on every note |
| **Phase 6: batch-09 Route (Concepts)** | Concept Builder agent dispatch plan logged | Concept → source → DR file chain complete | Domain node_counts updated in overview files | All 34 pre-write checks pass per schema |
| **Phase 7: batch-09 QA Gate** | 6-dimension scan results logged | Orphan list + resolution links recorded | batch-09 metrics match pipeline-state.json targets | Zero terminology violations (concept + source notes) |
| **Phase 8: batch-10 Cross-Linking** | Orphan Resolver dispatch plan logged | All new related_to links trace to semantic justification | Every concept has ≥1 related_to post-pass | Density targets met per validation-rules.md |
| **Phase 9: Session Closeout** | Handoff, delta analysis, OIR, retro | Full session audit trail in progress.md | All metrics updated (vault stats, domain table, pipeline state) | GLRC provenance verified on all new notes |

---

## 4. Phase Definitions

### Phase 2: batch-09 Receive/Register (ESC, ~10 min)
**Owner:** ESC
**Steps:**
1. Verify all 5 batch-09 input files accessible from worktree
2. Log registration in progress.md: filename, batch ID, word count, date
3. Check for duplicate content against existing source notes (Source-0001 through Source-0230)
**QA Gate:** All 5 files readable, word counts logged, no duplicates found
**Exit criteria:** Registration entries committed to progress.md

### Phase 3: batch-09 Rinse (Recon Agent, ~20 min)
**Owner:** Recon Agent, ESC reviews
**Steps:**
1. Dispatch Recon agent with all 5 DR files, extraction constraints, output schema
2. Agent strips podcast strategy, GTM tactics, competitive positioning, EXi business content
3. Agent identifies venue-ops concepts, standards, technologies, organizations, people, URLs
4. Agent returns structured extraction manifest per file
**QA Gate:** ESC reviews manifest for (a) no podcast/GTM content, (b) no EXi/Vivid Array/CS leakage, (c) all concepts map to 26-domain taxonomy
**Exit criteria:** Clean extraction manifest aligned with batch-09 primary domains

### Phase 4: batch-09 Ready (ESC, ~10 min)
**Owner:** ESC
**Steps:**
1. Map each concept to primary domain
2. Assign confidence tier (high/medium/low) per Q3
3. Validate manifest against VOCABULARY.yaml (domain, venue_type, vef_alignment values)
4. Check for duplicates against existing 152 concept notes
5. Assign source note numbers (Source-0231+)
**QA Gate (CRITICAL):** Manifest fully validated against VOCABULARY.yaml — no invalid values proceed to Stage 5
**Exit criteria:** Signed-off manifest ready for Route dispatch

### Phase 5: batch-09 Route — Sources (Source Builder Agent, ~15 min)
**Owner:** Source Builder Agent, ESC reviews
**Steps:**
1. Dispatch Source Builder with manifest + Source-0231 starting number
2. Agent creates one Source-NNNN-description.md per cited URL
3. Agent populates: source_type, url, accessed (2026-04-05), description, research_batch
**QA Gate:** Sequential numbering, frontmatter complete, all from controlled vocabulary
**Exit criteria:** All source notes written before any concept note creation

### Phase 6: batch-09 Route — Concepts (Concept Builder Agent, ~25 min)
**Owner:** Concept Builder Agent, ESC reviews
**Steps:**
1. Dispatch Concept Builder with manifest + completed source note list
2. Agent creates concept notes in 01_Domains/{slug}/
3. Agent applies forward-reference constraint: only links to notes that already exist
4. Agent populates frontmatter including child_of (parent domain), sources, research_batch
5. Agent updates domain overview node_counts
**QA Gate:** All wikilinks resolve, all schema required fields present, filenames follow pattern
**Exit criteria:** All concept notes written, domain overviews updated

### Phase 7: batch-09 QA Gate (QA Auditor Agent, ~15 min)
**Owner:** QA Auditor Agent, ESC owns gate decision
**Steps:**
1. Dispatch QA Auditor with 6-dimension scope: terminology (concept+source), schema, wikilinks, link integrity, orphans (vault-wide), vocabulary
2. Agent returns findings report
3. ESC remediates any issues surfaced
4. Write batch-09-validation.md to _Pipeline/Validation/
**QA Gate:** Zero violations across all 6 dimensions
**Exit criteria:** GREEN gate, validation report written, pipeline-state.json updated

### Phase 8: batch-10 Cross-Linking (Orphan Resolver Agent, ~20 min)
**Owner:** Orphan Resolver Agent, ESC reviews
**Steps:**
1. Dispatch Orphan Resolver with vault-wide scope across all 01_Domains/ folders
2. Agent identifies all concept notes with zero inbound links (orphans)
3. Agent proposes related_to links to resolve each orphan (semantic justification required)
4. ESC approves link mapping
5. Apply links to orphan notes
6. Verify relationship density: every concept has ≥1 related_to
7. Write batch-10-validation.md
**QA Gate:** Zero orphans vault-wide, density targets met
**Exit criteria:** GREEN gate, all orphans resolved, validation report written

### Phase 9: Session Closeout (ESC, ~25 min)
**Owner:** ESC
**Steps:** Per CLAUDE.md §Session Protocol — Phases 1-5 (accounting, retro, handoff, operational close, integrity verification)
**Exit criteria:** PR created, handoff written, OIR complete, pass-forward presented in-thread

---

## 5. Batch Definitions

### batch-09-existing-dr
**Input files (5):**
| # | File | Words | Filter Intent |
|---|------|-------|--------------|
| 1 | DR-AI-Change-Management-Transformation.md | 6,639 | Extract AI/change mgmt frameworks, transformation patterns |
| 2 | DR-B2B-Podcast-Behavior-Venue-Mgmt.md | 5,224 | Extract venue mgmt content consumption patterns (for data-and-analytics) |
| 3 | DR-B2B-Podcast-Launch-Strategy.md | 6,672 | Extract minimal venue ops (mostly podcast content — expect low yield) |
| 4 | DR-OpEx-CI-Major-Venues.md | 7,662 | Extract CI methodology, quality frameworks, operational transformation |
| 5 | DR-Competitive-Positioning-GTM.md | 5,214 | Extract booking/sales patterns, tenant relations (mostly GTM — expect low yield) |
| **Total** | — | **31,411** | — |

**Primary domains (targets):**
- quality-and-continuous-improvement (expand from 7 → 9-10)
- technology-and-digital (expand from 4 → 6-8)
- data-and-analytics (0 → 3-5) — CRITICAL: first concepts in this domain
- strategy-and-governance (expand from 3 → 5-6)
- people-and-culture (expand from 5 → 7-8)

**Secondary domains (possible):**
- financial-operations (0 → 2-3 if content yields)
- booking-and-sales (0 → 2-3 if content yields)
- tenant-and-partner-relations (0 → 2-3 if content yields)

**Agent assignments:**
- Recon: 1 dispatch, all 5 files, target 15-25 concepts in manifest
- Source Builder: 1 dispatch, Source-0231 through Source-0260 (est. 20-30 sources)
- Concept Builder: 1 dispatch (single agent — batch scope fits), 10-20 concepts target
- QA Auditor: 1 dispatch, 6-dimension scan

**Source range:** Source-0231 through ~Source-0260

**Success targets:**
- 10-20 concept notes created
- 20-30 source notes created
- 4 zero-concept domains brought to scaffolded (1-2 concepts each) OR explicit documentation of content yield constraint
- Zero terminology violations
- Zero schema violations

### batch-10-cross-linking
**Input files:** None (no new research)
**Scope:** Vault-wide quality pass
**Primary actions:**
1. Orphan detection across all 01_Domains/ folders (166+ concept notes post-batch-09)
2. Add missing cross-domain related_to links
3. Validate relationship density (every concept has 1+ related_to)
4. Flag any domain still below minimum viable
5. Write comprehensive batch-10 validation report

**Success targets:**
- Zero orphans vault-wide
- Relationship density: 100% of concepts have ≥1 related_to
- Coverage audit documents domains still below minimum viable

---

## 6. Risk Register

| ID | Risk | Likelihood | Severity | Mitigation |
|----|------|-----------|----------|-----------|
| RISK-S15-001 | DR files 2,3,5 are podcast-heavy, may yield <5 total concepts | High | Medium | Extract aggressively from DR 1 and 4 (AI + OpEx/CI). Accept low yield from podcast files as expected. |
| RISK-S15-002 | data-and-analytics has zero content; batch-09 must establish domain | Medium | High | Recon agent explicitly tasked with data/analytics extraction from all 5 files. Accept even 2-3 concepts as success. |
| RISK-S15-003 | Forward-reference violation: Concept Builder links to notes created in same batch | Medium | Medium | Route in order — sources fully written before concepts begin. Concept agent constrained to existing-only references. |
| RISK-S15-004 | Terminology scan misses source note violations (S14 retro finding) | Low | Medium | Explicitly scope QA Auditor terminology scan to include source notes. |
| RISK-S15-005 | Token budget exhaustion before closeout | Low | High | Monitor at each phase gate. If <20% budget at Phase 8 end, defer batch-10 to S16. |
| RISK-S15-006 | Batch-09 yields duplicates of existing concepts | Medium | Low | Concept Builder checks existing notes; enriches rather than duplicates. Log enrichments. |

---

## 7. Token Budget & Acceptance Criteria

### Token budget estimate
| Phase | Est. Tokens |
|-------|-------------|
| Phase 0-1 (Delta + Plan) | ~40K (consumed) |
| Phase 2-3 (Register + Recon) | ~30K |
| Phase 4-6 (Ready + Route) | ~80K |
| Phase 7 (QA gate) | ~25K |
| Phase 8 (Cross-linking) | ~40K |
| Phase 9 (Closeout) | ~30K |
| **Total estimate** | **~245K / 1M budget** |

Current consumption at plan completion: ~60K. Comfortable through Phase 9 at full quality.

### Session acceptance criteria
- [x] Delta audit complete with machine-readable table
- [x] All S14 warnings remediated
- [x] 9/9 validation reports present
- [x] D#45 fully propagated
- [ ] Operational plan aligned with Alex
- [ ] batch-09 complete: 10-20 concepts, 20-30 sources, zero violations
- [ ] batch-10 complete: zero orphans, density targets met
- [ ] Both batches have validation reports in _Pipeline/Validation/
- [ ] Full GLRC closeout sequence (Phases 1-5) executed
- [ ] PR created with meaningful commit messages
- [ ] Pass-forward prompt presented in-thread

---

## 8. Kanban State

```
BACKLOG          | IN PROGRESS     | REVIEW          | DONE
─────────────────┼─────────────────┼─────────────────┼────────────────────
#4 batch-09      | #3 Operational  |                 | #1 Delta analysis
#5 batch-10      |    plan         |                 | #2 Remediation
#6 Closeout      |                 |                 |    (6/6 resolved)
```

**Next card to move:** #3 → DONE when Alex GL received
**Then:** #4 → IN PROGRESS (batch-09 Phase 2 begins)

---

*Experience Innovation Inc. | VEP KB Session 15 Operational Plan | 2026-04-05*
