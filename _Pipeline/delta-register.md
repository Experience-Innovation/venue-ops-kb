---
title: "Delta Register (derived view)"
lifecycle: active
created: 2026-04-05
updated: 2026-04-05
authority: "_Pipeline/delta-register.yaml"
tags:
  - delta-register
  - academic-rigor
  - phase-b5
  - index
---

# Delta Register — Human-Scannable Index

> **Authority:** `_Pipeline/delta-register.yaml` is the authoritative source. This `.md` file is a derived view for human scanning and Obsidian navigation. Keep YAML authoritative; regenerate this view on each register update.

## Purpose

Machine-readable backlog for the **Academic Rigor Initiative** (Phase B.5, S16-S20). Every audit finding, action taken, and deferred item is captured with structured metadata. Zero-open gate at v1.0 release.

## Status Summary

| Metric | Count |
|---|:-:|
| Total entries | 13 |
| Open | 0 |
| In progress | 0 |
| Resolved (inline) | 5 |
| Resolved (batch) | 0 |
| Deferred | 8 |
| Accepted | 0 |

## By Severity

| Severity | Count |
|---|:-:|
| Critical | 0 |
| High | 5 |
| Medium | 3 |
| Low | 5 |

## By Category

| Category | Count | Definition |
|---|:-:|---|
| Provenance | 0 | GLRC chain completeness (ai_disclosure, extraction_model, research_batch, sources) |
| Vocabulary | 3 | Controlled vocabulary drift vs VOCABULARY.yaml |
| Citation | 2 | Source note bibliographic metadata gaps |
| Consistency | 0 | Editorial/structural consistency within domains |
| Obsidian | 1 | Vault mountability, broken links, graph integrity |
| Traceability | 7 | Claim-to-source traceability in concept bodies |
| Confidence | 0 | Confidence tier defensibility |
| Other | 0 | Uncategorized |

## Session Log

| Session | Date | Scope | Opened | Resolved | Deferred |
|---|---|---|:-:|:-:|:-:|
| S16 | 2026-04-05 | Consolidation Pass (B.5 Phase 1) | 5 | 4 (resolved-inline) | 1 → S18 CI cycle (DELTA-004) |
| S17 | 2026-04-05 | A-04 Part 1 traceability audit (82 concepts, A-L) | 8 | 1 (obsidian resolved-inline) | 7 → S18 (6) / S18-S20 (1) |

## Entries

| ID | Category | Severity | Status | Finding | Resolved / Target |
|---|---|:-:|:-:|---|:-:|
| DELTA-001 | vocabulary | low | resolved-inline | `status: active` in roadmap → renamed `lifecycle: active` | ✅ S16 |
| DELTA-002 | vocabulary | low | resolved-inline | `status: active` in operational plan → renamed `lifecycle: active` | ✅ S16 |
| DELTA-003 | vocabulary | low | resolved-inline | `status: PASS` in audit-A01 → renamed `audit_outcome: PASS` | ✅ S16 |
| DELTA-004 | citation | medium | deferred | 260 source notes missing author/publication/publish_date | **S18 CI cycle** |
| DELTA-005 | citation | low | resolved-inline | 26 domain overviews → added 5 framework anchor sources each | ✅ S16 |
| DELTA-006 | obsidian | medium | resolved-inline | 3 broken wikilinks in legal-compliance concepts → renamed/removed | ✅ S17 |
| DELTA-007 | traceability | high | deferred | Gender-Inclusive-Facilities: IPC/UPC + Canadian HR + BMO Field unsourced | S18 |
| DELTA-008 | traceability | high | deferred | Indigenous-Cultural-Programming: TRC + 94 Calls to Action unsourced | S18 |
| DELTA-009 | traceability | high | deferred | Liquor-Licensing: sources are food/labor, not liquor-specific | S18 |
| DELTA-010 | traceability | high | deferred | Responsible-Beverage-Service: covers 1 of 6 named programs | S18 |
| DELTA-011 | traceability | high | deferred | Naming-Rights: Copyright source (17 USC) but Trademark topic (15 USC) | S18 |
| DELTA-012 | traceability | medium | deferred | 11 MED-severity A-04 Part 1 traceability gaps (aggregate) | S18 |
| DELTA-013 | traceability | low | deferred | 13 LOW-severity citation-strengthening opportunities (aggregate) | S18-S20 |

*S16 entries: governance-artifact field conventions + domain overview citations (4 resolved inline + 1 deferred). S17 entries (006-013): from A-04 Part 1 traceability audit of 82 concepts. DELTA-006 obsidian fixes resolved inline. DELTA-007 through DELTA-011 are structural HIGH-severity gaps in single-source or misaligned-source concepts. DELTA-012 + DELTA-013 are aggregate entries for the 24 MED/LOW gaps — see `_Pipeline/Validation/audit-A04-claim-traceability-p1.md` for per-concept breakdown.*

## How to Add an Entry

1. Edit `_Pipeline/delta-register.yaml`
2. Append new entry under `entries:` with sequential `id: DELTA-NNN`
3. Populate all schema fields (see `schema:` block in YAML)
4. Increment `next_id`
5. Update `metrics:` block counts
6. Regenerate this `.md` derived view

## Severity Definitions

- **Critical** — Blocks Obsidian mountability OR publishes false/fabricated information. Must fix same session.
- **High** — Violates a CLAUDE.md Hard Rule OR breaks provenance chain OR breaks claim-to-source traceability.
- **Medium** — Editorial/consistency issue affecting academic rigor.
- **Low** — Polish item. May defer to Phase E.

## Resolution Paths

- **inline-fix** — Fixed in-session during the audit phase that discovered it
- **batch-fix** — Fixed in a dedicated remediation phase later in the same session
- **scheduled-fix** — Deferred to a specific future session
- **escalated** — Surfaced to Alex for scope/policy decision
- **accepted** — Alex accepted as out-of-scope or wont-fix with documented rationale

---

*Authority: `_Pipeline/delta-register.yaml` | Initialized: S16, 2026-04-05*
