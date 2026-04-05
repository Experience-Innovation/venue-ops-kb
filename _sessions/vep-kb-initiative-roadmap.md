---
type: initiative-roadmap
domain: [venue-ops-kb, kb-v1.0, ci, post-v1.0-planning, academic-rigor]
version: "1.1"
trust_tier: internal
status: active
created: 2026-04-05
updated: 2026-04-05
source_session: S128 (KitchenSync harness — v1.0-DRAFT); S16 persistence + Phase B.5 insert (v1.1)
target_repo: venue-ops-kb
target_location: _sessions/vep-kb-initiative-roadmap.md
change_summary: "v1.1 — persisted from S128, corrected S16 scope (no new DR available → Consolidation Pass), inserted Phase B.5 Academic Rigor initiative (S17-S20) per Alex 2026-04-05 directive"
---

# VEP KB Initiative Roadmap

**Initiative:** Venue Operations Knowledge Base v1.0 — open-source educational Obsidian KB mapping 26 operational domains
**Authority:** `venue-ops-kb/CLAUDE.md v2.1` (processing assignment prompt), `VEP-KB-Data-Science-Methodology_v1.0.md`, `VEP-Source-of-Truth_v1.0.md` (Decisions #26-42 + D#45)
**Audience:** 35-50K mid-to-senior venue operations professionals, North America
**Status as of 2026-04-05:** Phase B in progress — S16 Consolidation Pass underway

---

## §1. Initiative Purpose

Build a structured, validated, fully-sourced Obsidian knowledge base mapping the venue operations ecosystem across 26 operational domains. Every claim sourced and cited. Full transparency on AI tools, methodology, and process (GLRC-grade, EU AI Act aligned). **Academic-publishing bar** — the deliverable is a scholarly open-source reference an entire industry may cite.

**Strategic roles:**
1. Podcast credibility backbone (Venue Excellence Podcast)
2. EXi proof case (enterprise-grade AI-processed knowledge meeting GLRC standards)
3. Community value (educational resource for venue professionals)
4. Trust building (AI contribution visible, auditable, accountable)
5. **Academic-grade industry reference** — peer-reviewable scholarly open-source resource

**Scope discipline:** open-source educational KB. NOT podcast content, NOT internal EXi tools, NOT client engagement material, NOT a sales asset.

---

## §2. Phase A: Worklog (Complete, S4–S15)

**Summary:** 15 sessions, 2026-03 through 2026-04-05. Built from zero to 169 concepts + 260 sources + 26/26 domain overviews + 23 domains with concepts + 11 validation reports.

| Session | Date | Focus | Key Outcome |
|---|---|---|---|
| S4 | early 2026-03 | Foundation + pre-taxonomy | Methodology anchored; Vivid Array wall established; CS exemplar policy |
| S9 | 2026-03 | 26-domain taxonomy lock | Decision #30: 26 domains (up from 17). Middle-out anchored in Baldrige/EFQM/AIPC/IAVM/Excellence Canada |
| S10 | 2026-03 | Schema + methodology v2.0 | D#31: 7-type relationships; D#35: cross-cutting dimensions; GLRC transparency layer |
| S11 | 2026-04-03 | Persona + vault architecture | CLAUDE.md v2.0 — Knowledge Engineer persona; 5-stage intake pipeline |
| S12 | 2026-04 | Batches 00-01 | 79 notes, 3 domains at minimum viable+ |
| S13-S14 | 2026-04 | Research ingestion batches | Coverage expansion; D#45 Operational Excellence scope clarified |
| S15 | 2026-04-05 | batch-09 + batch-10 | 47 new notes (17 concepts + 30 sources), 52 bidirectional cross-links, financial-operations domain established |

**Vault state at S15 close:**
- 169 concept notes · 260 source notes · 26/26 domain overviews · 1 MOC · 11 validation reports
- 4 domains authoritative (15+) · 6 working depth (8+) · 11 minimum viable (3+) · 2 scaffolded · 3 at zero
- Gate: GREEN at S15 close

**GLRC compliance:** 100% AI disclosure, 100% research_batch tagging, sequential source numbering (Source-0001 → Source-0260), zero terminology violations.

---

## §3. Phase B: Path to v1.0 (In Progress)

**Definition of v1.0:** every domain at minimum viable (3+ concepts), complete cross-linking, batch-11 MOCs generated, Phase B.5 Academic Rigor initiative complete, batch-12 final validation passed.

### B1: Fill 3 empty domains (HIGH priority — blocks v1.0)

**Domains at zero concepts:** data-and-analytics, booking-and-sales, tenant-and-partner-relations

**Blocker:** DR corpus exhausted for these domains (zero yield from all 5 existing DR files).

**POA:**
1. **Fresh DR research session** (Alex) — produce new DR prompts targeting these 3 domains
2. **Extraction session** (Claude) — process new DR output → concept notes to reach 3+ per domain

**Acceptance:** all 26 domains at ≥3 concepts (minimum viable threshold).

### B2: MOC generation (batch-11) — IN PROGRESS (S16)

**Scope:** generate 26 enriched Maps of Content for all domains + update master MOC.

**Status:** Executing in S16 (Consolidation Pass).

**Acceptance:** `07_MOCs/` contains 27 MOC notes (26 domain + 1 master); discovery layer complete; navigable graph.

### B3: Final validation pass (batch-12) — DEFERRED to end of Phase B.5

**Scope:** pre-v1.0 validation sweep.

**Acceptance:** zero schema violations, zero vocabulary violations, zero orphan notes, zero fabrication flags, all cross-refs resolve.

### B4 (optional, post-v1.0): Enrichment layer

Standards, Technology, Organization, Person notes currently at 0 (deferred by design from S11). Not blocking v1.0. Treat as v1.1 candidate or Phase E work.

---

## §3b. Phase B.5: Academic Rigor Initiative (NEW — multi-session, S16-S20)

**Context:** Per Alex's 2026-04-05 directive, the KB is being built to academic-publishing standards — the bar for an open-source educational resource an entire industry may cite in perpetuity. Editorial rigor, terminological precision, citation integrity, methodological transparency, and Obsidian mountability are publishing gates, not aspirations.

**Gate logic:** Phase B.5 must complete before v1.0 release. No shortcut.

```
Phase B (B1+B2) → Phase B.5 (Academic Rigor) → Phase C (v1.0 Release)
                       ↑ GATE
```

### B.5 Session Sequencing

| Session | Focus | Est. Budget | Deliverables |
|---|---|:-:|---|
| **S16 (CURRENT)** | Consolidation Pass: MOC generation (batch-11) + Audit A-01/02/03 (provenance, vocabulary, citation) + METHODOLOGY.md + README + Obsidian mountability + persona expansion (CLAUDE.md v2.1) + delta register init | ~545K | 27 MOCs, 3 audit reports, METHODOLOGY.md, updated README, mounted vault, CLAUDE.md v2.1, delta-register.yaml |
| **S17** | Audit A-04 Claim-to-source traceability (concept notes, domains 1-13) + delta register continuation | ~600K | 13 domain audit reports + delta register updates |
| **S18** | Audit A-04 continued (domains 14-26) + A-05 peer-review-style consistency pass | ~600K | 13 domain audit reports + consistency audit + delta register updates |
| **S19** | Audit A-06 confidence tier audit + delta register sweep (resolve all deferred items) | ~600K | Confidence audit + delta register zero-open |
| **S20** | A-07 batch-12 final validation + v1.0 tag | ~400K | Final validation report + v1.0.0 tag + release notes |

### B.5 Audit Thread Catalogue

| Thread | Audit Type | Target Session | Status |
|---|---|:-:|---|
| A-01 | Provenance chain completeness (ai_disclosure, extraction_model, research_batch, sources on 100% of notes) | S16 | Scheduled |
| A-02 | Controlled vocabulary strict enforcement (zero drift vs VOCABULARY.yaml) | S16 | Scheduled |
| A-03 | Citation format standardization (source note bibliographic metadata) | S16 | Scheduled |
| A-04 | Claim-to-source traceability (every factual body claim cites source) | S17-S18 | Planned |
| A-05 | Peer-review-style structural consistency (depth/structure uniformity per domain) | S18 | Planned |
| A-06 | Confidence tier audit (high/medium/low defensibility) | S19 | Planned |
| A-07 | batch-12 final validation | S20 | Planned |

### B.5 Principles

1. **Delta register is the authoritative backlog.** All findings logged, all actions traced, all deferrals time-boxed to a target session.
2. **Obsidian mountability as publishing gate.** Every session closes with a mountable vault.
3. **Academic-publishing bar.** Editorial consistency, terminological precision, citation integrity, methodological transparency.
4. **Machine-readable persistence.** Delta register = YAML authority + .md derived. Audit reports = structured markdown with Dataview-queryable frontmatter.

### B.5 Gate Exit Criteria

- [ ] All 7 audit threads (A-01 through A-07) complete with reports filed
- [ ] Delta register zero-open (all findings resolved or explicitly accepted)
- [ ] 100% provenance chain completeness
- [ ] Zero vocabulary drift
- [ ] All source notes carry full bibliographic metadata
- [ ] 100% claim-to-source traceability on concept body text
- [ ] METHODOLOGY.md published and aligned
- [ ] README reflects v1.0 state
- [ ] Obsidian mountability verified at each session close
- [ ] Alex sign-off: "Academic rigor initiative complete, v1.0 can release"

---

## §4. Phase C: v1.0 Release

**Gates for v1.0:**
- [ ] All 26 domains ≥3 concepts (B1 complete)
- [ ] MOCs generated (B2 complete)
- [ ] Phase B.5 Academic Rigor initiative complete (all gate exit criteria met)
- [ ] Final validation passed (B3 / S20 complete)
- [ ] Terminology scan clean
- [ ] All provenance chains complete
- [ ] Git history clean with meaningful commit messages
- [ ] README updated with v1.0 release notes
- [ ] METHODOLOGY.md published
- [ ] Vault mounts cleanly in Obsidian

**Output:** `venue-ops-kb` at tag `v1.0.0`, published/announced per Alex's release plan.

---

## §5. Phase D: Post-v1.0 CI Initiative (Multi-Session, GATED)

**Context:** Per Alex's 2026-04-05 directive, CI session deferred until post-v1.0 ("CI session needs to be completed once v1.0 of the KB is complete, before we start going through enrichment passes and then eventually putting this out to the public").

### Gate Logic (MANDATORY)

```
Phase C (v1.0 Release) → Phase D (CI Initiative COMPLETE) → Phase E (Enrichment + Public Release)
                            ↑ GATE — cannot skip or defer further
```

**Rationale:** Enrichment and public release compound any template/indicator/process drift that exists. CI BEFORE those phases means the public-facing KB ships with standardized templates, clean visual language, and documented CI improvements.

### D-Scope (multi-session)

**Revised estimate:** 3-4 sessions (multi-session initiative).

### D-Session Sequencing

| Session | Focus | Budget | Deliverables |
|---|---|:-:|---|
| **D1: CI Audit + Gap Analysis** | Sweep existing templates, workflows, validation formats, CI registers from S4–S20. Catalog what exists, what's missing, what's inconsistent. | ~500K | CI audit report + gap register + improvement register |
| **D2: Template Architecture + Visual Indicator System** | Design unified template architecture. Visual-indicator system (iconography, severity markers, status glyphs). | ~500K | Template catalogue (versioned) + visual-indicator design spec + migration plan |
| **D3: Process Standardization + Governance Consolidation** | Standardize processing workflow, pipeline state tracking, progress.md format, validation report template. | ~500K | Standardized workflow docs + consolidated CI register format + process compliance checks |
| **D4 (conditional): CI Implementation Sweep** | Apply new templates + indicators + standardized workflow across v1.0 artifacts. | ~500K | Migrated v1.0 corpus + migration validation report |

**Total D-initiative budget:** ~2M tokens across 3-4 sessions

### D-Gate Exit Criteria

- [ ] D1 audit complete: CI gap register populated, improvements prioritized
- [ ] D2 template architecture + visual-indicator system ratified by Alex
- [ ] D3 standardized workflows published
- [ ] Migration plan produced
- [ ] Zero unresolved CRITICAL or HIGH severity CI findings
- [ ] Alex sign-off: "CI initiative complete, Phase E can begin"

---

## §6. Phase E: Post-v1.0 Enhancements (future backlog)

**Content depth:**
- E1: Enrichment layer — Standards, Technology, Organization, Person notes
- E2: Domain deepening — progress domains from minimum viable → working depth → authoritative per strategic priority
- E3: Additional domains if post-v1.0 research surfaces domains not in the 26 (unlikely, taxonomy locked)

**Infrastructure:**
- E4: Dataview dashboards — real-time coverage, relationship density, confidence distribution
- E5: Public publishing pipeline — export Obsidian vault → static site for public access
- E6: Feedback intake — community question routing → KB updates

**Quality:**
- E7: Fresh DR for high-change domains (tech-and-digital, data-and-analytics likely to drift fastest)
- E8: Human review passes — promote notes from `draft` → `reviewed` → `canonical`

---

## §7. Risk Register (updated 2026-04-05)

| Risk | Severity | Status | Mitigation |
|---|:-:|---|---|
| 3 domains at zero (B1 target) | MEDIUM | 🟡 Open | Fresh DR research required (Alex action) |
| URL fabrication capability (Recon agents, S15) | MEDIUM | 🟢 Mitigated | Verbatim-quote + grep warning standard active |
| Non-concept note types at 0 | LOW | 🟡 Deferred by design | Phase E |
| CS/BMO exemplar content leakage | LOW | 🟢 Walled | CLAUDE.md Hard Rule #4 active |
| Vivid Array content leakage | LOW | 🟢 Walled | CLAUDE.md Hard Rule #3 + terminology scan |
| **Academic rigor bar not enforced consistently** | **MEDIUM** | 🟡 **New — being addressed via Phase B.5** | **Delta register + per-session audit discipline** |
| **Obsidian mountability drift** | **LOW** | 🟡 **New — addressed via Phase B.5 publishing gate** | **Every session closes with mountability verification** |

---

## §8. Sequencing — Recommended Next Sessions

| Session | Focus | Est. Budget | Prereq | Status |
|---|---|:-:|---|:-:|
| **S16** (current) | Consolidation Pass (B2 MOCs + A-01/02/03 + METHODOLOGY + README + Obsidian mount + CLAUDE.md v2.1) | ~545K | None | IN PROGRESS |
| **S17** | Academic Rigor A-04 (traceability, domains 1-13) | ~600K | S16 close | Scheduled |
| **S18** | Academic Rigor A-04 (domains 14-26) + A-05 consistency | ~600K | S17 close | Planned |
| **S19** | Academic Rigor A-06 (confidence) + delta register sweep | ~600K | S18 close | Planned |
| **S20** | A-07 batch-12 final validation + v1.0 tag | ~400K | All B.5 items complete | Planned |
| **S21** | Fresh DR research prompts for 3 empty domains (Alex-led) | — | — | Awaiting DR availability |
| **S22** | B1 extraction session | ~650K | S21 DR output | Awaiting DR availability |
| **S23+** | Phase D CI-dedicated sessions (D1-D4) | 2M total | v1.0 released | Gated |

**Note:** B1 (filling 3 empty domains) can be interleaved anywhere in the B.5 sequence once fresh DR is available. B.5 audit work does NOT block on B1.

---

## §9. References

**Authority documents:**
- `venue-ops-kb/CLAUDE.md v2.1` — processing assignment prompt (expanded persona, academic rigor vision)
- `VEP-KB-Data-Science-Methodology_v1.0.md` — Q1-Q5 methodology
- `VEP-Source-of-Truth_v1.0.md` — Decisions #26-42 + D#45
- `.claude/rules/VOCABULARY.yaml` — 26-domain taxonomy, 7-type relationships
- `.claude/rules/SCHEMA.yaml` — frontmatter schema per note type
- `_Pipeline/delta-register.yaml` — Academic Rigor initiative backlog (NEW, S16)

**Session handoffs (worklog):**
- `_sessions/session-12-handoff.md` → `session-15-handoff.md`
- `_sessions/progress.md` — running CI register

**Publishing artifacts (to be created in S16):**
- `METHODOLOGY.md` (vault root) — public-facing methodology statement
- Updated `README.md` — public-facing intro + navigation

**Research plan:**
- `VEP-KB-Research-Plan_v2.0.md` — 13 DR prompts + supplementary batches

---

## §10. Ownership

| Role | Responsibility |
|---|---|
| **Alex Jackson** | Strategic direction, DR research prompts, human review (draft → reviewed → canonical), v1.0 release decision, delta register acceptance decisions |
| **Claude (ESC)** | Processing pipeline, extraction, validation, cross-linking, governance maintenance, audit execution, delta register discipline |
| **Greg Newton** | CS exemplar review (when flagged) |

---

## Change Log

| Version | Date | Session | Summary |
|---|---|---|---|
| 1.0-DRAFT | 2026-04-05 | S128 (KitchenSync, drafted for S16 persistence) | Initial roadmap — worklog + Phase B path to v1.0 + Phase D post-v1.0 CI + Phase E backlog |
| 1.1 | 2026-04-05 | S16 (persistence + scope correction) | Persisted to venue-ops-kb. Corrected S16 scope (no new DR → Consolidation Pass, not B1 extraction). Inserted Phase B.5 Academic Rigor initiative (S17-S20). Updated risk register. Updated sequencing. Added delta register as authoritative backlog mechanism. |

---

*AI Disclosure: Co-produced by Claude (Anthropic) and Alex Jackson, 2026-04-05.*
*v1.0-DRAFT drafted in kitchen-sync session S128 worktree; v1.1 persisted and extended in venue-ops-kb S16.*
