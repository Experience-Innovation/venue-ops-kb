---
type: operational-plan
session: D2
lifecycle: active
created: 2026-04-06
branch: session-d2/remediation
machine: MacBook Air (bubblegumpshrimpco)
---

# Session D2 Operational Plan — Technical Remediation + Publication Infrastructure

**Session:** D2 (Phase D, Session 2)
**Date:** 2026-04-06
**Predecessor:** D1 (PR #12 merged)
**Branch:** session-d2/remediation
**Worktree:** .claude/worktrees/session-d2-remediation

---

## §1. Context & Scope

**Inherited state:**
- Vault: v1.0.0 — 207 concepts, 390 sources, 26/26 domains at 3+, 27 MOCs, 650 total notes
- Delta register: 20/20 resolved or accepted (zero-open)
- CI gap register: 34 entries (4 resolved D1, 30 open). D2 targets 15 items.
- D1 PR #12 merged — CI audit report, gap register, improvement register, wikilink validation codified
- Gate: GREEN — all D1 deliverables on main

**Key D1 decisions carried forward:**
1. `children:` accepted as canonical field name for domain type (align schema to practice, not migrate 53 notes)
2. CC BY-SA 4.0 confirmed for LICENSE (Alex approved this session)
3. Governance templates: audit report template → `.claude/rules/`; operational plan template stays in `_sessions/` (Alex approved this session)
4. Batch validation reports exempt from audit_outcome frontmatter (codified D1)

**Scope — D2 delivers 6 workstreams:**

1. **Schema + vocabulary foundation** — SCHEMA.yaml v3.0 + VOCABULARY.yaml governance_type
2. **Template alignment** — all 8 content templates schema-compliant + audit report template
3. **Publication infrastructure** — LICENSE, folders 02-05, rule updates (validation v2.1, ingestion v3.0)
4. **METHODOLOGY.md v2.0** — S17-S21 findings, confidence distribution, coverage depth, all-draft transparency
5. **Session artifact + audit report frontmatter backfill** — S12-S19 governance files + A-01–A-05 standardization
6. **Gap register resolution** — all 15 D2-targeted items resolved + pull forward CI-GAP-007 (field-name validation rule, originally D3) and CI-GAP-010/013 (backfill, originally D3)

**Scope exclusions:**
- No content note modifications (CI-GAP-001 resolved by schema update, not note migration)
- No DR prompt design (D3)
- No ingestion or extraction work
- No README.md rewrite (current README references METHODOLOGY.md for details — METHODOLOGY update handles disclosure)

---

## §2. Brigade Roster

| Role | Owner | Responsibility | Scope |
|------|-------|---------------|-------|
| **ESC** | Claude (primary) | All phases — schema design, template edits, rule updates, backfill, QA, governance | All 7 phases |

**No agent dispatches planned.** D2 is schema/template/governance work — sequential, interdependent edits across a small number of files. Agent overhead would exceed benefit.

---

## §3. GLRC Framework

| Dimension | Checkpoint | When | Evidence |
|-----------|-----------|------|----------|
| **Governance** | Operational plan aligned with Alex | Pre-execution | This document |
| **Governance** | SCHEMA.yaml v3.0 self-consistent | Phase 1 exit | Schema validates against itself — all field names in vocabulary, all types have required/optional |
| **Lineage** | Every change traces to a CI-GAP-NNN entry | All phases | Gap register updated with resolution evidence per item |
| **Reconciliation** | Template fields match SCHEMA.yaml exactly | Phase 2 exit | Field-by-field comparison, each template vs schema |
| **Reconciliation** | Backfilled frontmatter consistent with governance schema | Phase 5 exit | Spot-check 3 files per era (S12-S15, S16-S19) |
| **Compliance** | Zero HIGH-severity CI gaps remaining | Phase 6 exit | Gap register status sweep |
| **Compliance** | All rule files at current versions | Phase 3 exit | Version headers verified |

---

## §4. Phase Definitions

### Phase 1: Schema + Vocabulary Foundation (~80K tokens)

**Owner:** ESC
**Objective:** SCHEMA.yaml v3.0 and VOCABULARY.yaml governance_type — the gating deliverable everything else depends on.

**Workflow:**

1. **SCHEMA.yaml v3.0** — comprehensive update:
   - Accept `children:` for domain type (replace `parent_of:` in domain.optional) — CI-GAP-001, CI-GAP-020
   - Add governance artifact schema section with types: handoff, retrospective, operational-plan, pass-forward, delta-analysis, qa-qc-analysis, audit-report, initiative-roadmap, backlog, template — CI-GAP-014
   - Define required/optional fields per governance type, using A-06/A-07 pattern as canonical (title, type, lifecycle, created + type-specific fields)
   - Codify `session:` for single-session artifacts, `source_session:` for multi-session artifacts — CI-GAP-021
   - Add `lifecycle` and `audit_outcome` field definitions to universal governance section (per CLAUDE.md v2.1 frontmatter conventions)
   - Bump version header to 3.0 with changelog — CI-GAP-018
   
2. **VOCABULARY.yaml** — add governance_type:
   - Add `governance_type:` controlled vocabulary list — CI-GAP-015
   - Values: handoff, retrospective, operational-plan, pass-forward, delta-analysis, qa-qc-analysis, audit-report, initiative-roadmap, backlog, template

**Exit criteria:**
- SCHEMA.yaml at v3.0 with governance artifact schema section
- Domain type uses `children:` (not `parent_of:`)
- VOCABULARY.yaml has governance_type list with 10 values
- `session:` vs `source_session:` convention documented in schema

---

### Phase 2: Template Alignment (~60K tokens)

**Owner:** ESC
**Objective:** All 8 content templates schema-compliant + audit report template created.

**Workflow:**

1. **Fix `related:` → `related_to:`** in 5 templates — CI-GAP-002:
   - Template-Organization.md
   - Template-Person.md
   - Template-Map.md
   - Template-Standard.md
   - Template-Technology.md

2. **Expand Template-Map.md** to 7-section MOC structure — CI-GAP-003:
   - Purpose, Domain Overview, Concept Index, Cross-Domain Connections, Reading Paths, Coverage Status, Related MOCs
   - Modeled on actual Map-Guest-Experience.md structure

3. **Simplify Template-Source.md** — CI-GAP-004:
   - Remove 3 body sections (Key Information Extracted, Cited In, Sources)
   - Replace with optional single description section (matching actual source note practice)

4. **Align ai_disclosure defaults** across all 8 templates — CI-GAP-005:
   - Change from "Generated through Human/AI collaboration using Claude..."
   - To CLAUDE.md §10 canonical: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"

5. **Create audit report template** at `.claude/rules/audit-report-template.md` — CI-GAP-017:
   - Canonical frontmatter: title, audit_outcome, lifecycle, created, scope, methodology (A-06/A-07 pattern)
   - Body structure: Summary table, findings by category, gate assessment, AI disclosure
   - CI-GAP-019 resolved: governance templates live in `.claude/rules/` (Alex approved)

**Exit criteria:**
- Zero `related:` fields in any template (all `related_to:`)
- Template-Map.md has 7 body sections
- Template-Source.md has ≤1 body section
- All 8 templates use CLAUDE.md §10 ai_disclosure text
- audit-report-template.md exists in .claude/rules/

---

### Phase 3: Publication Infrastructure + Rule Updates (~50K tokens)

**Owner:** ESC
**Objective:** LICENSE, folder structure, validation rule + ingestion rule updates.

**Workflow:**

1. **Create LICENSE** at vault root — CI-GAP-024:
   - CC BY-SA 4.0 International (full legal text)

2. **Create folders 02-05** with .gitkeep — CI-GAP-025:
   - 02_Standards/.gitkeep
   - 03_Technology/.gitkeep
   - 04_Organizations/.gitkeep
   - 05_People/.gitkeep
   - CI-GAP-034 resolves automatically (dashboard queries now have target folders)

3. **Add field-name validation rule** to validation-rules.md — CI-GAP-007:
   - New rule: "All frontmatter field keys must exist in SCHEMA.yaml universal.required, universal.optional, or {note_type}.required, {note_type}.optional for the note's declared note_type"
   - Bump validation-rules.md to v2.1

4. **Add optional field annotation guidance** to ingestion-rules.md — CI-GAP-029:
   - venue_scale: required when concept behavior varies by venue size
   - delivery_model: required when staffing model differs by delivery approach
   - jurisdiction: required when regulatory requirements vary by geography
   - Empty = "not applicable" is an acceptable state
   - Bump ingestion-rules.md to v3.0

**Exit criteria:**
- LICENSE file exists at vault root with CC BY-SA 4.0 text
- 02_Standards/, 03_Technology/, 04_Organizations/, 05_People/ exist with .gitkeep
- validation-rules.md at v2.1 with field-name validation rule
- ingestion-rules.md at v3.0 with optional field guidance

---

### Phase 4: METHODOLOGY.md v2.0 (~60K tokens)

**Owner:** ESC
**Objective:** Update METHODOLOGY.md to reflect v1.0.0 state — S17-S21 work, current statistics, coverage depth disclosure, all-draft transparency.

**Workflow:**

1. **§5 Vault Statistics** — update from S16 to v1.0.0:
   - 650 total notes, 207 concepts, 390 sources, 27 MOCs
   - 26/26 domains at minimum viable, 10 at working depth, 1 authoritative
   - Confidence: 88.4% high, 10.6% medium, 1.0% low
   - 21 sessions (S4-S21), 40+ DR files processed

2. **§6 GLRC Compliance** — update audit results:
   - A-01 through A-07 all complete with outcomes
   - Bibliographic metadata: 100% author (post-S18 DELTA-004), 24% publication, 2% publish_date
   - Claim-to-source: 60% PASS, zero fabrication (A-04)

3. **§7 Known Limitations** — refresh:
   - Remove "3 empty domains" (all filled S20)
   - Remove "bibliographic metadata gaps" (resolved S18)
   - Remove "claim-to-source not yet audited" (completed S17-S19)
   - Add: all-draft status transparency (CI-GAP-026) — all 207 concepts at status: draft pending human review
   - Add: coverage depth per domain with progressive deepening roadmap (CI-GAP-027)
   - Add: 5 lowest domains single-batch dependent (CI-GAP-028 context)
   - Add: confidence concentration in logistics-and-warehouse (66% medium+low)

4. **§10 Governance & Audit Trail** — update audit history table with A-01 through A-07 outcomes

5. **Version bump** to 2.0, changelog entry

**Exit criteria:**
- METHODOLOGY.md statistics match v1.0.0 vault state
- All-draft status explicitly disclosed
- Per-domain coverage depth table included
- Audit history reflects all 7 audit threads with outcomes
- Known limitations current (stale items removed, new items added)

---

### Phase 5: Session Artifact + Audit Report Frontmatter Backfill (~70K tokens)

**Owner:** ESC
**Objective:** Minimal frontmatter on all pre-S20 session files + standardize audit report frontmatter.

**Workflow:**

**5a. Session artifact backfill** — CI-GAP-013:

Files needing frontmatter added (12 files with no frontmatter):
- session-12-handoff.md
- session-13-handoff.md
- session-14-delta-analysis.md
- session-14-handoff.md
- session-15-delta-analysis.md
- session-15-handoff.md
- session-15-operational-plan.md
- session-15-retro.md
- discovery-manifest.md
- progress.md
- session-d1-operational-plan.md
- session-d1-retro.md

Frontmatter pattern (minimal, per D1 decision #5):
```yaml
---
type: {handoff|retrospective|operational-plan|delta-analysis|discovery-manifest|progress-log}
lifecycle: superseded  # (active for D1 files, progress.md, discovery-manifest)
created: {date from file content or git log}
session: {session number}
---
```

Files with partial frontmatter needing `type:` field added (S16-S18 era, 7 files):
- session-16-handoff.md (has lifecycle but no type)
- session-16-operational-plan.md (has lifecycle but no type)
- session-16-qa-qc-analysis.md (has title but no type/lifecycle)
- session-16-retro.md (has lifecycle but no type)
- session-17-handoff.md (has lifecycle but no type)
- session-17-retro.md (has lifecycle but no type)
- session-18-operational-plan.md (has lifecycle but no type)

**5b. Audit report frontmatter standardization** — CI-GAP-010:

Migrate A-01 through A-05 + Phase8 to canonical A-06/A-07 pattern:
```yaml
---
title: "{report title}"
audit_outcome: {PASS|CONDITIONAL|FAIL}
lifecycle: active  # or superseded if superseded by later audit
created: {original date}
scope: "{audit scope}"
methodology: "{brief methodology}"
---
```

Remove legacy fields: audit_id, audit_name, session, date, phase, category, initiative.

Also update session-18-ci-enrichment-validation.md to match if feasible.

**Exit criteria:**
- All 30 _sessions/ files have YAML frontmatter with at least type + lifecycle + created
- All audit reports in _Pipeline/Validation/ use canonical A-06/A-07 frontmatter pattern
- No `type:` field gaps in governance artifacts

---

### Phase 6: Gap Register Update + QA/QC (~40K tokens)

**Owner:** ESC
**Objective:** Update gap register, self-audit all changes, verify zero HIGH gaps remaining.

**Workflow:**

1. Update ci-gap-register.yaml — mark all D2 items resolved with:
   - resolved_session: D2
   - resolved_date: 2026-04-06
   - resolution_evidence: specific file + change description

2. Self-audit checklist:
   - [ ] SCHEMA.yaml v3.0 internally consistent (all field names exist, all types complete)
   - [ ] All 8 templates pass schema validation against SCHEMA.yaml v3.0
   - [ ] VOCABULARY.yaml governance_type values match SCHEMA.yaml governance types
   - [ ] validation-rules.md field-name rule references SCHEMA.yaml correctly
   - [ ] ingestion-rules.md optional field guidance is complete
   - [ ] LICENSE is valid CC BY-SA 4.0 text
   - [ ] Folders 02-05 exist with .gitkeep
   - [ ] METHODOLOGY.md statistics match README.md v1.0.0 figures
   - [ ] All backfilled frontmatter uses governance_type values from VOCABULARY.yaml
   - [ ] Zero HIGH-severity CI gaps remaining in gap register

3. Remediate any issues found

**Exit criteria:**
- Gap register: zero HIGH, zero unresolved D2 items
- All self-audit checks pass
- ci-improvement-register.md D2 items marked DONE

---

### Phase 7: PM/GLRC Delta Analysis + Session Close-Out (~50K tokens)

**Owner:** ESC + Alex (retro conversation)

**Sub-phase 7a — PM/GLRC Delta Analysis:**

| Artifact | Check |
|----------|-------|
| Initiative roadmap | D2 gate criteria checked, session entry added |
| CI gap register | All D2 items resolved, metrics updated |
| CI improvement register | D2 items marked DONE |
| Progress.md | D2 session entry |
| Pipeline-state.json | Phase updated |

**Sub-phase 7b — Standard Close-Out:**
1. Session accounting (work product inventory + OIR)
2. Retro conversation with Alex
3. Handoff + pass-forward (in-thread)
4. Git commit + push + PR

**Exit criteria:**
- All governance artifacts current
- PR opened
- Pass-forward delivered in-thread

---

## §5. Batch Definitions

No extraction batches. All work is schema/template/governance editing.

| Work Unit | Files Affected | Est. Edits |
|-----------|---------------|-----------|
| SCHEMA.yaml v3.0 | 1 file | 1 major rewrite |
| VOCABULARY.yaml update | 1 file | 1 section addition |
| Template alignment | 8 files in Templates/ + 1 new in .claude/rules/ | 9 file edits |
| Rule updates | 2 files (.claude/rules/) | 2 edits |
| LICENSE + folders | 1 new file + 4 .gitkeep files | 5 new files |
| METHODOLOGY.md v2.0 | 1 file | 1 major edit |
| Session artifact backfill | ~19 files in _sessions/ | 19 frontmatter edits |
| Audit report backfill | ~7 files in _Pipeline/Validation/ | 7 frontmatter edits |
| Gap register update | 1 file | 15+ entry updates |
| Improvement register | 1 file | 11 status updates |

**Total: ~45 file modifications, ~6 new files**

---

## §6. Binary Success Criteria

| # | Criterion | How Measured |
|---|-----------|-------------|
| 1 | SCHEMA.yaml at v3.0 with governance artifact schema | Version header + governance section exists |
| 2 | All 8 content templates schema-compliant | Zero `related:` fields, correct ai_disclosure, Map has 7 sections, Source simplified |
| 3 | Zero HIGH-severity CI gaps remaining | Gap register severity scan |
| 4 | LICENSE file exists (CC BY-SA 4.0) | File present at vault root |
| 5 | Folders 02-05 exist | Directory listing |
| 6 | METHODOLOGY.md updated to v2.0 | Version header + statistics match v1.0.0 |
| 7 | All rule files at current versions | ingestion v3.0, validation v2.1 |
| 8 | All governance artifacts have frontmatter | Frontmatter scan of _sessions/ and _Pipeline/Validation/ |
| 9 | PR opened | gh pr URL |

---

## §7. Risk Register

| Risk | Severity | Mitigation |
|------|----------|------------|
| SCHEMA.yaml governance schema design takes multiple iterations | MEDIUM | Use A-06/A-07 pattern as proven baseline; don't over-engineer |
| Template edits introduce broken fields | LOW | Validate each template against SCHEMA v3.0 post-edit |
| Backfill edits accidentally modify body content | LOW | Frontmatter-only edits; verify H1 heading preserved |
| Token budget exceeded by backfill volume | LOW | Backfill is mechanical (19 files × small frontmatter); batch efficiently |

---

## §8. Token Budget

| Phase | Estimated Tokens | Cumulative |
|-------|:----------------:|:----------:|
| Session start + reads | ~80K | 80K |
| Operational plan | ~30K | 110K |
| Phase 1: Schema + Vocabulary | ~80K | 190K |
| Phase 2: Template alignment | ~60K | 250K |
| Phase 3: Publication infrastructure | ~50K | 300K |
| Phase 4: METHODOLOGY.md | ~60K | 360K |
| Phase 5: Frontmatter backfill | ~70K | 430K |
| Phase 6: Gap register + QA/QC | ~40K | 470K |
| Phase 7: Close-out + PR | ~50K | 520K |
| **Total estimated** | **~520K** | |
| **Budget ceiling** | **600K** | |

**Buffer:** ~80K for remediation, Alex questions, and retro conversation.

---

*AI Disclosure: Operational plan co-produced by Claude (Anthropic) and Alex Jackson, 2026-04-06.*
