---
type: template
lifecycle: active
created: 2026-04-06
source_session: S21
purpose: "Gold-standard operational plan template for VEP KB processing sessions"
---

# Session Operational Plan Template

**Usage:** Copy this template at session start. Fill all 8 sections before execution begins. Present to Alex for alignment.

**Authority:** Global CLAUDE.md §Operational Planning, feedback_gold-standard-operational-plan.md, feedback_operational-plan-to-standard.md

---

## {{section_1}} Context & Scope

**Inherited state:**
- Concept count, source count, MOC count, domain coverage status
- Delta register status (entries open/resolved/deferred)
- Gate status from prior session
- Key decisions or constraints carried forward

**New inputs (this session):**
- DR files, research materials, or other inputs available
- Estimated extractable entities

**Scope decisions:**
1. [Numbered list of what's in scope and sequencing rationale]

**Scope exclusions:**
- [What is explicitly NOT in scope]

---

## {{section_2}} Brigade Roster

| Role | Owner | Responsibility | Batch Size |
|------|-------|---------------|------------|
| **ESC** | Claude (primary) | Orchestration, QA gates, governance, plan accountability | All phases |
| [Agent role] | Subagent | [Specific task] | [Size] |

**Agent dispatch standards:** Per D-13 (7 required fields). Pre-extract binary content before dispatch. Cap batch sizes (10-15 content-heavy, 8-10 dense). No Bash-heavy agent work. No bypassPermissions for Agent SDK agents.

---

## {{section_3}} GLRC Framework

| Dimension | Checkpoint | When | Evidence |
|-----------|-----------|------|----------|
| **Governance** | Operational plan aligned with Alex | Pre-execution | This document |
| **Lineage** | [Provenance checks] | [Phase] | [Evidence] |
| **Reconciliation** | [Delta/validation checks] | [Phase] | [Evidence] |
| **Compliance** | [Schema/vocabulary/terminology checks] | [Phase] | [Evidence] |

---

## {{section_4}} Phase Definitions

### Phase 1: [Name] (~XK tokens)

**Owner:** [Role]
**Objective:** [Clear statement]

**Workflow:**
1. [Step-by-step]

**Exit criteria:**
- [Binary pass/fail conditions]

### Phase N-1: QA/QC + Remediation (~XK tokens)

**Owner:** ESC
**Objective:** Self-audit all prior phase outputs. Fix any issues found.

### Phase N: PM/GLRC Delta Analysis + Session Close-Out (~XK tokens)

**Owner:** ESC + Alex (retro conversation)
**Objective:** Mandatory close-out per protocol + PM/GLRC delta analysis.

**Sub-phase Na — PM/GLRC Delta Analysis (MANDATORY per S20 codification):**

Systematic comparison of session work against all governance artifacts:

| Artifact | Check |
|----------|-------|
| Initiative roadmap | Session items marked complete, gate criteria updated |
| Delta register | Status accurate, metrics match entries |
| Progress.md | Session entry complete, domain table updated |
| Pipeline-state.json | Status current |
| Domain overviews | node_count fields accurate (if concepts created) |
| VOCABULARY.yaml | New entries added (if new research batches processed) |

Output: variance table with fixes applied in-session. Any unfixable variance documented in OIR.

**Sub-phase Nb — Standard Close-Out:**
1. Session accounting (work product inventory + OIR with 8 required fields per item)
2. Retro conversation with Alex (Claude presents assessment, Alex responds, feedback processed, THEN document written)
3. Handoff + pass-forward (in-thread for copy)
4. Progress.md + pipeline-state.json update
5. Git commit + push + PR via `gh pr create`

---

## {{section_5}} Batch Definitions

| Batch | Agent | Scope | Size |
|-------|-------|-------|------|
| [batch-id] | [Agent role] | [What's processed] | [File/note count] |

---

## {{section_6}} Binary Success Criteria

| # | Criterion | How Measured |
|---|-----------|-------------|
| 1 | [Outcome] | [Evidence] |

---

## {{section_7}} Risk Register

| Risk | Severity | Mitigation |
|------|----------|------------|
| [Risk] | [LOW/MEDIUM/HIGH] | [Mitigation] |

---

## {{section_8}} Token Budget

| Phase | Estimated Tokens | Cumulative |
|-------|:----------------:|:----------:|
| Session start | XK | XK |
| Phase 1 | XK | XK |
| ... | ... | ... |
| **Total estimated** | **XK** | |
| **Budget ceiling** | **XK** | |

---

*Template created S21 (2026-04-06) per S20 retro improvement: PM/GLRC Delta Analysis codified as mandatory close-out phase.*
*AI Disclosure: Template co-produced by Claude (Anthropic) and Alex Jackson.*
