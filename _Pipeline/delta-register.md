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
| Total entries | 5 |
| Open | 0 |
| In progress | 0 |
| Resolved (inline) | 4 |
| Resolved (batch) | 0 |
| Deferred | 1 |
| Accepted | 0 |

## By Severity

| Severity | Count |
|---|:-:|
| Critical | 0 |
| High | 0 |
| Medium | 1 |
| Low | 4 |

## By Category

| Category | Count | Definition |
|---|:-:|---|
| Provenance | 0 | GLRC chain completeness (ai_disclosure, extraction_model, research_batch, sources) |
| Vocabulary | 3 | Controlled vocabulary drift vs VOCABULARY.yaml |
| Citation | 2 | Source note bibliographic metadata gaps |
| Consistency | 0 | Editorial/structural consistency within domains |
| Obsidian | 0 | Vault mountability, broken links, graph integrity |
| Traceability | 0 | Claim-to-source traceability in concept bodies |
| Confidence | 0 | Confidence tier defensibility |
| Other | 0 | Uncategorized |

## Session Log

| Session | Date | Scope | Opened | Resolved | Deferred |
|---|---|---|:-:|:-:|:-:|
| S16 | 2026-04-05 | Consolidation Pass (B.5 Phase 1) | 5 | 4 (resolved-inline) | 1 → S18 CI cycle (DELTA-004) |

## Entries

| ID | Category | Severity | Status | Finding | Resolved / Target |
|---|---|:-:|:-:|---|:-:|
| DELTA-001 | vocabulary | low | resolved-inline | `status: active` in roadmap → renamed `lifecycle: active` | ✅ S16 |
| DELTA-002 | vocabulary | low | resolved-inline | `status: active` in operational plan → renamed `lifecycle: active` | ✅ S16 |
| DELTA-003 | vocabulary | low | resolved-inline | `status: PASS` in audit-A01 → renamed `audit_outcome: PASS` (other audit reports already used convention) | ✅ S16 |
| DELTA-004 | citation | medium | deferred | 260 source notes missing author/publication/publish_date | **S18 CI cycle (centerpiece)** |
| DELTA-005 | citation | low | resolved-inline | 26 domain overviews → added 5 framework anchor sources each | ✅ S16 |

*Entries 001-003 + 005 resolved in S16 per Alex directive 2026-04-05 to fix inline where scope permits. Entry 004 deferred to S18 — reframed as the Academic Rigor Initiative's first **Continuous Improvement / Enrichment Cycle** session with 260-source bibliographic enrichment as the centerpiece deliverable.*

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
