---
type: operational-plan
session: S21
lifecycle: active
created: 2026-04-06
branch: session-21/a07-v1
machine: MacBook Air (bubblegumpshrimpco)
---

# Session 21 Operational Plan — A-07 Final Validation + Delta Resolution + v1.0 Tag

**Session:** S21 (Phase B.5, Session 6 of 6 — FINAL)
**Date:** 2026-04-06
**Branch:** `session-21/a07-v1` (worktree)
**Predecessor:** S20 (B.1 DR ingestion + A-06 confidence audit + delta remediation) — PR #10 merged

---

## §1. Context & Scope

**Inherited state:**
- 207 concepts, 390 sources, 27 MOCs, 26/26 domain overviews, 653 total vault notes
- Delta register: 20 entries (16 resolved, 4 deferred: DELTA-013, DELTA-016, DELTA-018, DELTA-019)
- B1 gate: CLEARED (all 26 domains at 3+ concepts)
- 6/7 audit threads complete (A-01 through A-06)
- B.5 gate exit criteria: 7/10 checked
- Confidence distribution: 88.4% high, 10.6% medium, 1.0% low
- Zero fabrication across 20 sessions

**This session's scope:**
1. **Track A — A-07 Final Validation:** Full vault sweep (650+ notes) against validation-rules.md: schema compliance (34 checks), vocabulary enforcement, terminology scan, orphan detection, wikilink integrity, confidence distribution, domain coverage, GLRC provenance chain verification.
2. **Track B — Delta Resolution:** All 4 deferred entries accepted with documented rationale per Alex sign-off (2026-04-06). Zero-open gate cleared.
3. **Track C — v1.0 Publishing:** README update with final statistics, session-operational-plan-template creation (S20 retro improvement), release notes, roadmap v1.4, v1.0.0 tag (post-PR-merge).

**Scope exclusions:** No new DR prompts. No new domain creation. No MOC updates. No enrichment layer work. No Phase D CI work. This is validation, acceptance, and tag — not extraction.

**Delta triage decision (Alex aligned 2026-04-06):**
- DELTA-018 (2 HIGH): **Accept** — educational KB, not legal reference. Primary sources adequate. A-06 already adjusted confidence.
- DELTA-019 (6 MED): **Accept** — niche topics adequately covered for v1.0. Enrichment deferred to Phase E.
- DELTA-013 (13 LOW) + DELTA-016 (10 LOW): **Accept at v1.0** — polish items per severity definition.
- Depth-of-coverage improvements documented as living backlog for post-v1.0 enrichment (Phase E).

---

## §2. Brigade Roster

| Role | Owner | Responsibility |
|------|-------|---------------|
| **ESC** | Claude (primary) | Orchestration, validation execution, delta acceptance, report authoring, governance, plan accountability |
| **Schema Scanner** | Subagent (parallel) | Automated frontmatter scan across 650+ notes: required fields, vocabulary values, format checks |
| **Terminology Scanner** | Subagent (parallel) | Forbidden term scan + old domain slug detection across all .md files |
| **Link Integrity Scanner** | Subagent (parallel) | Wikilink resolution check, orphan detection, bidirectional relationship verification |
| **Coverage Reporter** | Subagent | Per-domain concept counts, confidence distribution, source diversity, GLRC provenance chain completeness |

**Agent dispatch standards:** Per D-13. No Bash-heavy agent work. Scanners receive explicit file lists and output schemas. Cap parallel dispatch at 3-4 agents.

---

## §3. GLRC Framework

| Dimension | Checkpoint | When | Evidence |
|-----------|-----------|------|----------|
| **Governance** | Operational plan aligned with Alex | Pre-execution | This document |
| **Governance** | Delta acceptance rationale documented | Phase 1 | delta-register.yaml entries |
| **Lineage** | A-07 validates 100% provenance chain (ai_disclosure, extraction_model, research_batch, sources) | Phase 2 | A-07 audit report |
| **Reconciliation** | Delta register zero-open confirmed | Phase 1 | delta-register.yaml metrics |
| **Reconciliation** | PM/GLRC delta analysis at session close (new S20 standard) | Phase 5 | Variance table in handoff |
| **Compliance** | Full vault schema validation (34 checks × 650+ notes) | Phase 2 | A-07 audit report |
| **Compliance** | Terminology scan clean | Phase 2 | A-07 audit report |
| **Compliance** | All B.5 gate exit criteria met | Phase 3 | Roadmap v1.4 |

---

## §4. Phase Definitions

### Phase 1: Delta Register Close-Out (~20K tokens)

**Owner:** ESC
**Objective:** Move all 4 deferred delta entries to `accepted` status with documented rationale. Achieve zero-open gate.

**Workflow:**
1. Update DELTA-013 → accepted (13 LOW citation-strengthening items — cosmetic, non-structural)
2. Update DELTA-016 → accepted (10 LOW citation-strengthening items — cosmetic, non-structural)
3. Update DELTA-018 → accepted (2 HIGH people-culture gaps — primary sources adequate for educational KB; confidence already adjusted by A-06)
4. Update DELTA-019 → accepted (6 MED no-corpus-match — niche topics for Phase E enrichment)
5. Update metrics section: 0 deferred, 4 new accepted
6. Document depth-of-coverage improvement areas in delta register notes for Phase E backlog continuity

**Exit criteria:**
- Delta register: 0 open, 0 in-progress, 0 deferred
- All accepted entries have `resolution_path`, `resolved_session: S21`, `resolved_date`, and `resolution_evidence`
- Rationale references Alex sign-off date (2026-04-06)

### Phase 2: A-07 Final Validation (~200K tokens)

**Owner:** ESC + Scanner agents (parallel dispatch)
**Objective:** Full vault sweep per validation-rules.md. This is the final quality gate before v1.0.

**Sub-phase 2a — Automated Scans (parallel agents):**

| Scan | Scope | Tool |
|------|-------|------|
| Schema compliance | 650+ notes × 34 checks | Frontmatter parser agent |
| Vocabulary enforcement | All controlled fields vs VOCABULARY.yaml | Grep-based agent |
| Terminology scan | All .md files for forbidden terms + old slugs | Grep-based agent |
| Orphan detection | 01-07 folders: notes with 0 inlinks | Link scan agent |
| Wikilink integrity | All frontmatter wikilinks resolve to existing files | Link scan agent |
| GLRC provenance | 100% ai_disclosure, extraction_model, research_batch on concept/source notes | Frontmatter parser agent |

**Sub-phase 2b — Coverage & Distribution Reports:**

| Report | Scope |
|--------|-------|
| Domain coverage | Per-domain concept count, threshold status (minimum viable/working/authoritative) |
| Confidence distribution | Vault-wide + per-domain high/medium/low counts |
| Source diversity | Per-domain unique source count |
| Relationship density | Per-domain relationship link count |

**Sub-phase 2c — Manual Review of Flagged Items:**
- Any schema/vocabulary violations fixed inline
- Any orphans linked or documented
- Any broken wikilinks repaired

**Sub-phase 2d — A-07 Audit Report:**
- File to `_Pipeline/Validation/audit-A07-final-validation.md`
- Structured per validation-rules.md report format
- Overall outcome: PASS / CONDITIONAL PASS / FAIL
- Per-check results with evidence

**Exit criteria:**
- A-07 report filed with PASS or CONDITIONAL PASS (with accepted items only)
- Zero CRITICAL or HIGH findings unresolved
- Any new findings below HIGH either fixed inline or documented as accepted

### Phase 3: v1.0 Publishing (~50K tokens)

**Owner:** ESC
**Objective:** README update, release notes, roadmap v1.4, session-operational-plan-template creation.

**Workflow:**
1. **README.md update:**
   - Replace S16 statistics with v1.0 final numbers (207 concepts, 390 sources, 26/26 domains, 27 MOCs)
   - Update "Known gaps" section: remove stale "3 domains at 0" reference; document actual v1.0 limitations (non-concept note types at 0, all notes at draft status, depth-of-coverage improvement areas)
   - Add v1.0 release date
   - Update Academic Rigor Initiative status to complete

2. **Session-operational-plan-template.md** (new file):
   - 8-section template codifying the gold-standard operational plan format
   - Includes new PM/GLRC Delta Analysis as mandatory close-out phase (S20 retro improvement)
   - Filed in `_sessions/` or `Templates/`

3. **Release notes** (RELEASE-v1.0.0.md at vault root):
   - Initiative summary (20 sessions, S4–S21)
   - Vault statistics
   - Academic rigor initiative summary (7 audit threads, 20 delta entries)
   - Depth-of-coverage assessment with improvement roadmap
   - Methodology reference
   - Known limitations
   - What's next (Phase D CI, Phase E enrichment)
   - AI disclosure

4. **Roadmap v1.4:**
   - Mark S21 complete
   - Mark Phase B.5 complete (all gate exit criteria met)
   - Mark Phase C gates checked
   - Update risk register

**Exit criteria:**
- README reflects v1.0 state
- Release notes filed
- Roadmap v1.4 committed
- Session-operational-plan-template created with PM/GLRC Delta Analysis phase

### Phase 4: QA/QC + Remediation (~30K tokens)

**Owner:** ESC
**Objective:** Self-audit all Phase 1-3 outputs. Fix any issues found.

**Checks:**
- Delta register internally consistent (metrics match entries, all fields populated)
- A-07 report internally consistent (findings match scan data)
- README statistics match actual vault counts
- Release notes accurate against session history
- All new files pass schema/vocabulary/terminology checks
- No forbidden terms in any new content

### Phase 5: PM/GLRC Delta Analysis + Session Close-Out (~100K tokens)

**Owner:** ESC + Alex (retro conversation)
**Objective:** Mandatory close-out per protocol + new PM/GLRC delta analysis standard.

**Sub-phase 5a — PM/GLRC Delta Analysis (new S20 standard):**
Systematic comparison of S21 work against all governance artifacts:

| Artifact | Check |
|----------|-------|
| Roadmap v1.4 | All S21 items marked complete, Phase B.5 gate criteria checked |
| Delta register | Zero-open confirmed, metrics accurate |
| Progress.md | S21 entry complete, domain table updated |
| Pipeline-state.json | Status current |
| Domain overviews | node_count fields accurate |
| VOCABULARY.yaml | No new entries needed |
| README | Statistics match vault counts |
| Release notes | Accurate against session history |

Output: variance table with fixes applied in-session.

**Sub-phase 5b — Standard Close-Out:**
1. Session accounting (work product inventory + OIR)
2. Retro conversation with Alex
3. Handoff + pass-forward (for Phase D)
4. Progress.md + pipeline-state.json update
5. Git commit + push + PR via `gh pr create`

---

## §5. Batch Definitions

No extraction batches in S21. All work is validation, acceptance, and publishing.

Validation scan batches (parallel agent dispatch):

| Batch | Agent | Scope | Size |
|-------|-------|-------|------|
| scan-schema | Schema Scanner | 01_Domains/ (233 files) + 06_Sources/ (390 files) + 07_MOCs/ (27 files) | ~650 files |
| scan-terminology | Terminology Scanner | All .md files in vault | ~700 files |
| scan-links | Link Integrity Scanner | All frontmatter wikilinks | ~2000+ links |

---

## §6. Binary Success Criteria

| # | Criterion | How Measured |
|---|-----------|-------------|
| 1 | A-07 validation report filed (PASS or CONDITIONAL PASS with accepted items only) | `_Pipeline/Validation/audit-A07-final-validation.md` exists with outcome |
| 2 | Delta register zero-open (all entries resolved or accepted with Alex sign-off) | `delta-register.yaml` metrics show 0 open + 0 deferred |
| 3 | README reflects v1.0 state | Statistics match actual vault counts |
| 4 | v1.0.0 tag applied (post-PR-merge, Alex decision) | `git tag -l v1.0.0` returns result |
| 5 | PM/GLRC delta analysis executed at session close | Variance table in handoff document |
| 6 | PR opened | `gh pr list` shows S21 PR |
| 7 | Release notes filed | `RELEASE-v1.0.0.md` exists at vault root |
| 8 | Session-operational-plan-template created with PM/GLRC Delta Analysis phase | Template file exists |

---

## §7. Risk Register

| Risk | Severity | Mitigation |
|------|----------|------------|
| A-07 surfaces CRITICAL/HIGH findings requiring resolution | MEDIUM | Budget reserves 30K tokens for Phase 4 remediation. Any schema violation is deterministic and fixable inline. |
| Wikilink integrity scan reveals widespread broken links | LOW | S17 DELTA-006 fixed 3; no further reports. If found, batch-fix with grep/sed. |
| Token budget insufficient for full close-out | LOW | 1M context window, ~400K estimated consumption. Comfortable margin per reference_token-budget.md. |
| v1.0.0 tag timing depends on PR merge (Alex decision) | LOW | Tag command documented in plan. Can be applied in-session if Alex merges synchronously, or documented as first action for post-merge. |

---

## §8. Token Budget

| Phase | Estimated Tokens | Cumulative |
|-------|:----------------:|:----------:|
| Session start (scan, reads, plan) | 50K | 50K |
| Phase 1: Delta register close-out | 20K | 70K |
| Phase 2: A-07 final validation | 200K | 270K |
| Phase 3: v1.0 publishing | 50K | 320K |
| Phase 4: QA/QC + remediation | 30K | 350K |
| Phase 5: PM/GLRC delta analysis + close-out | 100K | 450K |
| **Total estimated** | **450K** | |
| **Budget ceiling** | **500K** | (comfortable within 1M window) |

---

*AI Disclosure: Operational plan co-produced by Claude (Anthropic) and Alex Jackson, 2026-04-06.*
