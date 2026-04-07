---
title: "CI Improvement Register — Phase D Prioritized Backlog"
lifecycle: active
created: 2026-04-06
source_session: D1
purpose: "Prioritized CI improvements with effort estimates and target sessions for Phase D execution"
---

# CI Improvement Register — Phase D

**Source:** CI Audit D1 (2026-04-06)
**Gap Register:** `_Pipeline/ci-gap-register.yaml` (23 entries)
**Target:** D2 (template architecture), D3 (process standardization), D4 (conditional implementation sweep)

---

## §1. D1 Deliverables (This Session)

Items resolved inline during the D1 audit session.

| # | Improvement | Gap IDs | Effort | Status |
|---|------------|---------|:------:|:------:|
| IMP-D1-01 | Codify wikilink-filename validation in ingestion-rules.md Stage 5 | CI-GAP-006 | S | DONE |
| IMP-D1-02 | Codify validation report pattern policy (per-batch vs consolidated) | CI-GAP-009, CI-GAP-011 | S | DONE |
| IMP-D1-03 | Bump ingestion-rules.md to v2.1 | CI-GAP-008 | S | DONE |

---

## §2. D2 Deliverables — Template Architecture + Schema Update

D2 is the heaviest session: schema alignment, template overhaul, governance artifact schema creation.

| # | Improvement | Gap IDs | Effort | Dependencies | Priority | Status |
|---|------------|---------|:------:|:------------|:--------:|:------:|
| IMP-D2-01 | Resolve `children:` vs `parent_of:` field name — update SCHEMA.yaml | CI-GAP-001, CI-GAP-020 | S | Alex decision (D1) | HIGH | DONE |
| IMP-D2-02 | Fix `related: []` → `related_to: []` in 5 templates | CI-GAP-002 | S | None | HIGH | DONE |
| IMP-D2-03 | Expand Template-Map.md to 7-section MOC structure | CI-GAP-003 | M | None | MEDIUM | DONE |
| IMP-D2-04 | Simplify Template-Source.md body structure | CI-GAP-004 | S | None | MEDIUM | DONE |
| IMP-D2-05 | Align ai_disclosure defaults across all 8 templates | CI-GAP-005 | S | None | LOW | DONE |
| IMP-D2-06 | Create audit report template in .claude/rules/ | CI-GAP-017 | M | IMP-D2-08 | HIGH | DONE |
| IMP-D2-07 | Add `governance_type:` controlled vocabulary to VOCABULARY.yaml | CI-GAP-015 | S | None | MEDIUM | DONE |
| IMP-D2-08 | Add governance artifact schema to SCHEMA.yaml | CI-GAP-014 | M | IMP-D2-01, IMP-D2-07 | HIGH | DONE |
| IMP-D2-09 | Comprehensive SCHEMA.yaml v3.0 update | CI-GAP-018 | L | All D2 items | HIGH | DONE |
| IMP-D2-10 | Assess governance template location (Templates/ vs _sessions/ vs .claude/rules/) | CI-GAP-019 | S | IMP-D2-08 | LOW | DONE |
| IMP-D2-11 | Codify `session:` vs `source_session:` convention | CI-GAP-021 | S | IMP-D2-08 | HIGH | DONE |

**D2 actual effort:** ~520K tokens. All 11 items DONE.

---

## §3. D3 Deliverables — Process Standardization + Governance Consolidation

D3 is backfill, consolidation, and documentation.

| # | Improvement | Gap IDs | Effort | Dependencies | Priority |
|---|------------|---------|:------:|:------------|:--------:|
| IMP-D3-01 | Add field-name validation rule to validation-rules.md | CI-GAP-007 | S | IMP-D2-01 (field name resolution) | HIGH | DONE (pulled to D2) |
| IMP-D3-02 | Backfill A-01–A-05 audit report frontmatter to canonical pattern | CI-GAP-010 | M | IMP-D2-06 (audit template) | MEDIUM | DONE (pulled to D2) |
| IMP-D3-03 | Document S18 validation report variance as acceptable | CI-GAP-012 | S | None | LOW |
| IMP-D3-04 | Backfill S12-S19 session artifact frontmatter | CI-GAP-013 | L | IMP-D2-08 (governance schema) | HIGH | DONE (pulled to D2) |
| IMP-D3-05 | Add minimal frontmatter to progress.md | CI-GAP-016 | S | None | LOW | DONE (pulled to D2, included in IMP-D3-04) |
| IMP-D3-06 | Document batch numbering convention | CI-GAP-022 | S | None | MEDIUM |
| IMP-D3-07 | Document DR input file naming convention | CI-GAP-023 | S | None | LOW |
| IMP-D3-08 | Bump validation-rules.md to v2.1 | CI-GAP-007 | S | IMP-D3-01 | MEDIUM | DONE (pulled to D2) |
| IMP-D3-09 | Bump ingestion-rules.md to v3.0 (final D-phase version) | CI-GAP-008 | S | All D3 rule updates | LOW | DONE (pulled to D2) |

**D3 estimated effort:** ~350K tokens (backfill + documentation + rule updates)

**D3 critical path:** IMP-D3-04 (session backfill, largest effort) + IMP-D3-01 (field-name validation)

---

## §4. D4 Deliverables (Conditional) — Implementation Sweep

D4 only required if D2-D3 produce template/schema changes that need vault-wide application.

| # | Improvement | Gap IDs | Effort | Dependencies | Priority |
|---|------------|---------|:------:|:------------|:--------:|
| IMP-D4-01 | If `children:` → `parent_of:` migration: update 26 domain notes | CI-GAP-001 | M | IMP-D2-01 decision | CONDITIONAL |
| IMP-D4-02 | Vault-wide field-name validation sweep | CI-GAP-007 | M | IMP-D3-01 (rule codified) | MEDIUM |
| IMP-D4-03 | Final validation pass post-migration | N/A | M | All D4 items | HIGH |

**D4 estimated effort:** ~300K tokens if migration needed; ~100K if not

**D4 trigger:** D4 is only needed if D2 decisions require vault-wide note modifications. If D2 resolves field-name issues by updating SCHEMA.yaml to match practice (no note changes), D4 reduces to a validation sweep only.

---

## §4b. Content / Data Science Improvements (D1 Comprehensive Sweep)

Items identified from knowledge engineer + data science perspective during the comprehensive vault sweep.

### D2 — Publication Infrastructure

| # | Improvement | Gap IDs | Effort | Priority | Status |
|---|------------|---------|:------:|:--------:|:------:|
| IMP-D2-12 | Create LICENSE file (CC BY-SA 4.0) | CI-GAP-024 | S | HIGH | DONE |
| IMP-D2-13 | Create empty 02_Standards/, 03_Technology/, 04_Organizations/, 05_People/ folders with .gitkeep | CI-GAP-025 | S | HIGH | DONE |
| IMP-D2-14 | Update METHODOLOGY.md with S17-S21 findings, confidence distribution, coverage depth, single-source methodology | CI-GAP-033 | M | MEDIUM | DONE |
| IMP-D2-15 | Update METHODOLOGY.md to disclose all-draft status and progressive deepening model | CI-GAP-026 | S | MEDIUM | DONE |
| IMP-D2-16 | Update METHODOLOGY.md to disclose per-domain coverage depth | CI-GAP-027 | S | MEDIUM | DONE |
| IMP-D2-17 | Add optional field annotation guidance to ingestion-rules.md (venue_scale, delivery_model, jurisdiction) | CI-GAP-029 | S | MEDIUM | DONE |

### D3 — DR Prompt Design (Content Enrichment Targets)

| # | Improvement | Gap IDs | Effort | Priority |
|---|------------|---------|:------:|:--------:|
| IMP-D3-10 | Design DR prompts targeting 6 highest-priority domains for working-depth enrichment | CI-GAP-027, CI-GAP-028 | L | HIGH |
| IMP-D3-11 | Design DR prompt for logistics-and-warehouse domain (66% medium+low confidence) | CI-GAP-030 | M | HIGH |
| IMP-D3-12 | Design DR prompt for crowd-management + supply-chain cross-batch enrichment | CI-GAP-028 | M | MEDIUM |
| IMP-D3-13 | Design DR prompt for parking-and-transportation independent source enrichment | CI-GAP-031 | M | LOW |

### D4 — Final Ingestion + Publication-Ready

| # | Improvement | Gap IDs | Effort | Priority |
|---|------------|---------|:------:|:--------:|
| IMP-D4-04 | Extract non-concept note types (standard, technology, organization, person) from existing 390-source corpus | CI-GAP-032 | XL | MEDIUM |
| IMP-D4-05 | Ingest DR output from D3 prompts — domain deepening + enrichment | CI-GAP-027, 028, 030, 031 | XL | HIGH |
| IMP-D4-06 | Final validation pass + METHODOLOGY.md final update + publication gate check | N/A | L | HIGH |

---

## §5. D-Gate Exit Criteria (Draft)

For Phase D to exit and Phase E enrichment to begin, all of the following must be true:

### Must-Have (Blocking Phase E)

1. [ ] **SCHEMA.yaml v3.0 published** — incorporates governance artifact schema, field name resolution, S16-S21 refinements (IMP-D2-09)
2. [ ] **All 8 content templates schema-aligned** — no undefined fields, correct field names, body scaffolding matches actual usage (IMP-D2-02 through IMP-D2-05)
3. [ ] **Audit report template published** — canonical frontmatter + body structure for all future audits (IMP-D2-06)
4. [ ] **Wikilink-filename validation in pipeline** — prevents recurrence of S14-S15 truncation pattern (IMP-D1-01)
5. [ ] **Field-name validation rule added** — prevents schema-practice divergence (IMP-D3-01)
6. [ ] **Validation report pattern documented** — per-batch vs consolidated policy clear (IMP-D1-02)
7. [ ] **governance_type vocabulary published** — controlled vocabulary for session artifact type fields (IMP-D2-07)
8. [ ] **Zero unresolved HIGH-severity CI gaps** — all 8 HIGH items in gap register resolved

### Should-Have (Strengthen Quality but Don't Block)

9. [ ] S12-S19 session artifacts backfilled with frontmatter (IMP-D3-04)
10. [ ] A-01–A-05 audit report frontmatter backfilled to canonical pattern (IMP-D3-02)
11. [ ] Batch numbering convention documented (IMP-D3-06)
12. [ ] All rule files at current versions (ingestion v3.0, validation v2.1)

### Nice-to-Have (Phase E or Later)

13. [ ] Governance templates in Templates/ directory (IMP-D2-10)
14. [ ] progress.md frontmatter added (IMP-D3-05)
15. [ ] DR input file naming standardized for Phase E (IMP-D3-07)

### Sign-Off

16. [ ] Alex sign-off: "CI initiative complete, Phase E can begin"

---

## §6. Revised Session Arc (D1 Alignment with Alex)

The original Phase D (4 sessions) + Phase E (6-10 sessions) collapses into a streamlined 4-session sequence:

| Session | Scope | Estimated Tokens | Deliverables |
|---------|-------|:----------------:|-------------|
| **D1** (this session) | Comprehensive audit — technical + content/data science | ~500K | CI audit report (34 findings), gap register, improvement register, 4 inline fixes, D-gate criteria |
| **D2** | Technical remediation + publication infrastructure | ~500K | SCHEMA v3.0, all templates aligned, governance schema, LICENSE, folder structure, METHODOLOGY update, rule updates, session artifact backfill, all HIGH/MEDIUM CI gaps resolved |
| **D3** | DR prompt design + specification | ~300K | Structured prompts for Alex → Perplexity Pro. Targeting: 6 priority domains, logistics confidence, cross-batch enrichment, non-concept entity extraction guidance |
| **D4** | Final ingestion + publication-ready release | ~600K | DR output ingestion, domain deepening, non-concept note extraction, final validation, METHODOLOGY final update, publication gate |
| **Total** | | **~1.9M** | Publication-ready KB |

**Key change:** D3 is no longer "process standardization" — it's DR prompt engineering. Alex takes D3 output to Perplexity Pro. D4 is the final ingestion + publication session.

---

---

*AI Disclosure: Improvement register co-produced by Claude (Anthropic) and Alex Jackson, 2026-04-06.*
