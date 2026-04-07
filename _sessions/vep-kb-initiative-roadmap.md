---
type: initiative-roadmap
domain: [venue-ops-kb, kb-v1.0, ci, post-v1.0-planning, academic-rigor]
version: "1.5"
trust_tier: internal
lifecycle: active
created: 2026-04-05
updated: 2026-04-06
source_session: "S128 init; S16 v1.1; S16 v1.2; S20 v1.3; S21 v1.4; D1 v1.5"
target_repo: venue-ops-kb
target_location: _sessions/vep-kb-initiative-roadmap.md
change_summary: "v1.5 — D1 CI Audit complete. 23 findings across 6 categories (0 CRITICAL, 8 HIGH, 9 MEDIUM, 6 LOW). Gap register + improvement register populated. D-gate exit criteria refined with must-have/should-have/nice-to-have tiers. 4 D1 items resolved inline (wikilink validation, report pattern policy, version bump). D budget revised to 1.3-1.6M (down from 2M). D4 conditional."
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

### B1: Fill 3 empty domains — **COMPLETE (S20)**

**Domains filled in S20 via DR R-06/R-07/R-08:**
- data-and-analytics: 0 → 7 concepts (minimum viable exceeded)
- booking-and-sales: 0 → 5 concepts (minimum viable exceeded)
- tenant-and-partner-relations: 0 → 13 concepts (working depth achieved)

**B1 GATE CLEARED:** All 26 domains at ≥3 concepts. Zero domains at zero.

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
| **S16 (DONE)** | Consolidation Pass: MOC generation (batch-11) + Audit A-01/02/03 (provenance, vocabulary, citation) + METHODOLOGY.md + README + Obsidian mountability + persona expansion (CLAUDE.md v2.1) + delta register init + 4/5 delta entries resolved inline | ~680K actual | 27 MOCs, 3 audit reports, METHODOLOGY.md, updated README, mounted vault, CLAUDE.md v2.1, delta-register.yaml (5 entries, 4 resolved-inline, 1 deferred DELTA-004) |
| **S17 (DONE)** | A-04 Part 1 claim-to-source traceability (82 concepts, domains A-L). 53 PASS (65%), 0 CRITICAL, 5 HIGH. Delta entries DELTA-006 through DELTA-013. | ~600K | Audit report, 8 delta entries, 5 HIGH gaps identified for DR remediation |
| **S18 (DONE)** | CI / Enrichment Cycle — DR remediation (DELTA-007–011) + DELTA-004 bibliographic enrichment (290 source notes × author/publication/publish_date). | ~650K | 30 source notes, 5 concepts enriched, 290/290 author populated, DELTA-004/007–011 resolved |
| **S19 (DONE)** | A-04 Part 2 (87 concepts, domains M-T) + DELTA-012 resolution + A-05 structural consistency. Combined A-04: 169 concepts, 60% PASS, zero fabrication. | ~650K | A-04 P2 audit report, A-05 audit report, DELTA-012 resolved (7/11), DR prompt template v1.0, 5 DR prompts (R-06–R-10) |
| **S20 (DONE)** | B.1 DR ingestion (R-06–R-10) + A-06 confidence tier audit + DELTA-014/015/017 remediation. B1 GATE CLEARED — all 26 domains at 3+. | ~550K | 100 source notes, 38 new concepts, 7 enrichments, A-06 audit report, 10 confidence adjustments, DELTA-014/015/017 resolved |
| **S21 (DONE)** | A-07 final validation + DELTA-018/019/013/016 acceptance + v1.0 tag. ZERO-OPEN GATE CLEARED. | ~450K | A-07 audit report (PASS), 4 delta entries accepted, RELEASE-v1.0.0.md, README v1.0 update, session-operational-plan-template, v1.0.0 tag |

**Note:** Session count increased from 5 to 6 (S16-S21) to accommodate dedicated S18 CI / Enrichment Cycle per Alex directive 2026-04-05. DELTA-004 (260 source notes × 3 fields = ~780 field additions) warrants session-scale focus rather than bundling into A-04 traceability work.

### B.5 Audit Thread Catalogue

| Thread | Audit Type | Session | Status | Key Finding |
|---|---|:-:|---|---|
| A-01 | Provenance chain completeness | S16 | **PASS** | 100% ai_disclosure, extraction_model, research_batch |
| A-02 | Controlled vocabulary enforcement | S16 | **PASS** | Zero drift from VOCABULARY.yaml |
| A-03 | Citation format standardization | S16 | **PASS** (required) | 100% required fields; bibliographic enrichment resolved S18 |
| A-04 | Claim-to-source traceability | S17+S19 | **CONDITIONAL PASS** | 169 concepts: 60% PASS, zero fabrication, 40% gap rate |
| A-05 | Structural consistency | S19 | **CONDITIONAL** | Vault avg 85/100; safety-and-risk 72/100 (remediated S20) |
| A-06 | Confidence tier defensibility | S20 | **CONDITIONAL** | 88.4% high, 10.6% medium, 1.0% low (10 adjustments) |
| A-07 | Final validation + v1.0 tag | S21 | **PASS** | 650 files validated, 31 wikilinks remediated, zero violations post-fix |

### B.5 Principles

1. **Delta register is the authoritative backlog.** All findings logged, all actions traced, all deferrals time-boxed to a target session.
2. **Obsidian mountability as publishing gate.** Every session closes with a mountable vault.
3. **Academic-publishing bar.** Editorial consistency, terminological precision, citation integrity, methodological transparency.
4. **Machine-readable persistence.** Delta register = YAML authority + .md derived. Audit reports = structured markdown with Dataview-queryable frontmatter.

### B.5 Gate Exit Criteria

- [x] All 7 audit threads (A-01 through A-07) complete with reports filed — A-07 PASS (S21)
- [x] Delta register zero-open (all findings resolved or explicitly accepted) — 20/20: 16 resolved, 4 accepted (Alex sign-off 2026-04-06)
- [x] 100% provenance chain completeness — A-01 PASS (S16), A-07 confirmed (S21)
- [x] Zero vocabulary drift — A-02 PASS (S16), A-07 confirmed (S21)
- [x] All source notes carry full bibliographic metadata — DELTA-004 resolved (S18): 100% author, 24% publication, 2% publish_date
- [x] 100% claim-to-source traceability on concept body text — A-04 CONDITIONAL PASS: 60% full PASS, zero fabrication, 40% enriched via DR
- [x] METHODOLOGY.md published and aligned — completed S16
- [x] README reflects v1.0 state — updated S21 with final statistics (207 concepts, 390 sources, 26/26 domains)
- [x] Obsidian mountability verified at each session close — verified S16–S21 (31 broken wikilinks remediated in A-07)
- [ ] Alex sign-off: "Academic rigor initiative complete, v1.0 can release"

---

## §4. Phase C: v1.0 Release

**Gates for v1.0:**
- [x] All 26 domains ≥3 concepts (B1 complete S20)
- [x] MOCs generated (B2 complete S16)
- [x] Phase B.5 Academic Rigor initiative complete (9/10 gate exit criteria met, Alex sign-off pending)
- [x] Final validation passed (A-07 PASS, S21)
- [x] Terminology scan clean (A-07 confirmed, S21)
- [x] All provenance chains complete (A-07 confirmed, S21)
- [x] Git history clean with meaningful commit messages
- [x] README updated with v1.0 release notes (S21)
- [x] METHODOLOGY.md published (S16)
- [x] Vault mounts cleanly in Obsidian (S21 — 31 broken wikilinks remediated)

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

### D-Session Sequencing (Revised D1 — Streamlined to Publication)

| Session | Focus | Budget | Deliverables | Status |
|---|---|:-:|---|:-:|
| **D1: Comprehensive Audit** | Technical CI audit (templates, pipeline, validation, session artifacts, governance, conventions) + content/data science audit (domain coverage, confidence, source diversity, publication readiness). | ~500K | CI audit report (34 findings), gap register (34 entries), improvement register, wikilink validation codified, validation report policy codified | ✅ COMPLETE 2026-04-06 |
| **D2: Technical Remediation + Publication Infrastructure** | SCHEMA.yaml v3.0, all templates aligned, governance artifact schema, audit report template, LICENSE file, folder structure (02-05), METHODOLOGY.md update, rule updates, session artifact backfill. All HIGH/MEDIUM CI gaps resolved. | ~520K actual | SCHEMA v3.0, 8 updated templates, governance schema, LICENSE, 4 empty folders, METHODOLOGY v2.0, validation-rules v2.1, ingestion-rules v3.0, backfilled session artifacts, 22 CI gaps resolved | COMPLETE 2026-04-06 |
| **D3: DR Prompt Design + Specification** | Design structured prompts for Perplexity Pro targeting: 6 priority domains to working depth, logistics confidence enrichment, cross-batch corroboration, non-concept entity extraction guidance. Alex runs prompts externally. | ~300K | Structured DR prompt specifications (R-20 through R-2X), domain-specific extraction targets, expected yield estimates | Scheduled |
| **D4: Final Ingestion + Publication-Ready Release** | Ingest DR output from D3, domain deepening, non-concept note extraction (standards, technology, organization, person), final validation, METHODOLOGY final update, publication gate. | ~600K | Enriched KB, non-concept notes populated, final validation report, publication-ready vault | Gated on D3 DR output |

**Total D-initiative budget:** ~1.9M tokens across 4 sessions (streamlined from original D+E arc of ~4M+ across 7-14 sessions)

**Key architectural change (D1 alignment):** Original Phase D (4 sessions, CI-only) + Phase E (6-10 sessions, enrichment) collapsed into a focused 4-session sequence ending at publication-ready. D3 produces prompts for Alex → Perplexity Pro; D4 ingests the output. No separate Phase E.

### D-Gate Exit Criteria (Refined from D1 audit)

**D2 Gate — Technical Compliance (Blocking D3 Prompt Design):** ALL CLEARED 2026-04-06
- [x] D1 audit complete: CI gap register populated (34 entries), improvements prioritized
- [x] SCHEMA.yaml v3.0 published — governance artifact schema, field name resolution, S16-S21 refinements (D2)
- [x] All 8 content templates schema-aligned — no undefined fields, correct field names (D2)
- [x] Audit report template published in .claude/rules/ (D2)
- [x] Wikilink-filename validation codified in pipeline (ingestion-rules.md v2.1 Step 5b)
- [x] Field-name validation rule added to validation-rules.md v2.1 Rule #35 (D2, pulled from D3)
- [x] Validation report pattern documented (batch vs audit vs consolidated)
- [x] governance_type vocabulary published in VOCABULARY.yaml v3.0 (D2)
- [x] LICENSE file created — CC BY-SA 4.0 International (D2)
- [x] Folders 02-05 created (empty with .gitkeep) (D2)
- [x] METHODOLOGY.md v2.0 updated with S17-S21 findings + coverage disclosure (D2)
- [x] Zero unresolved HIGH-severity CI gaps — 10/10 HIGH resolved (D2)
- [x] All rule files at current versions — ingestion v3.0, validation v2.1 (D2)
- [x] S12-S19 session artifacts backfilled with frontmatter (D2, pulled from D3)

**D3 Gate — Prompt Design (Blocking D4 Ingestion):**
- [ ] DR prompts designed for 6 priority domains
- [ ] Logistics-and-warehouse confidence enrichment prompt specified
- [ ] Cross-batch corroboration prompts for single-batch domains
- [ ] Non-concept entity extraction guidance documented
- [ ] Alex completes Perplexity Pro DR execution

**D4 Gate — Publication-Ready:**
- [ ] DR output ingested — domains enriched toward working depth
- [ ] Non-concept notes extracted (standards, technology, organization, person)
- [ ] Final validation pass — zero schema violations, zero broken wikilinks
- [ ] METHODOLOGY.md final update with post-enrichment statistics
- [ ] README.md updated with final counts and publication metadata
- [ ] Alex sign-off: "Knowledge base complete and ready for publication"

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
| 3 domains at zero (B1 target) | MEDIUM | 🟢 **Resolved S20** | DR R-06/R-07/R-08 filled all 3 domains. B1 gate cleared. |
| URL fabrication capability (Recon agents, S15) | MEDIUM | 🟢 Mitigated | Verbatim-quote + grep warning standard active. Enforced again in S20 (5 parallel agents, zero fabrication). |
| Non-concept note types at 0 | LOW | 🟡 Deferred by design | Phase E |
| CS/BMO exemplar content leakage | LOW | 🟢 Walled | CLAUDE.md Hard Rule #4 active. R-09 CS content filtered in S20 (6 body refs + 4 URLs excluded). |
| Vivid Array content leakage | LOW | 🟢 Walled | CLAUDE.md Hard Rule #3 + terminology scan |
| Academic rigor bar enforcement | MEDIUM | 🟢 **Substantially addressed** | 6/7 audit threads complete. Delta register at 17/20 resolved. A-07 final validation in S21. |
| Obsidian mountability drift | LOW | 🟢 Addressed | Every session closes with mountability verification. Phase B.5 publishing gate active. |
| **Confidence inflation from single-source extraction** | **MEDIUM** | 🟡 **New S20** | **A-06 identified pattern: S14-S15 over-assigned high confidence. 10 concepts adjusted. Single-source flag at Stage 4 now enforced.** |

---

## §8. Sequencing — Recommended Next Sessions

| Session | Focus | Est. Budget | Prereq | Status |
|---|---|:-:|---|:-:|
| **S16** | Consolidation Pass (batch-11 MOCs + A-01/02/03 + METHODOLOGY + README + Obsidian mount + CLAUDE.md v2.1 + 4/5 delta entries resolved inline) | ~680K actual | None | ✅ COMPLETE 2026-04-05 |
| **S17** | Academic Rigor A-04 (traceability, domains 1-13) | ~600K | S16 close | Scheduled |
| **S18** | **CI / Enrichment Cycle** — DELTA-004 bibliographic enrichment (260 source notes × author/publication/publish_date) + optional FI-01 wikilink scanner tooling | ~650K | S17 close | Scheduled |
| **S19** | Academic Rigor A-04 Part 2 (domains 14-26) + A-05 peer-review consistency | ~650K | S18 close | Planned |
| **S20** | Academic Rigor A-06 (confidence) + delta register zero-open sweep | ~600K | S19 close | Planned |
| **S21** | A-07 batch-12 final validation + v1.0 tag | ~400K | All B.5 items complete | Planned |
| **S22+** | Fresh DR research prompts for 3 empty domains (Alex-led) | — | — | Awaiting DR availability |
| **S23+** | B1 extraction session | ~650K | S22 DR output | Awaiting DR availability |
| **S24+** | Phase D CI-dedicated sessions (D1-D4) | ~2M total | v1.0 released | Gated |

**Note:** B1 (filling 3 empty domains) can be interleaved anywhere in the B.5 sequence once fresh DR is available. B.5 audit work does NOT block on B1. S18 CI / Enrichment Cycle was inserted per Alex directive 2026-04-05.

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
| 1.2 | 2026-04-05 | S16 (close-out update) | Marked S16 complete with actual scope (4/5 delta entries resolved inline). Inserted dedicated S18 CI / Enrichment Cycle session (DELTA-004 centerpiece: 260 source notes × bibliographic metadata enrichment) per Alex directive. Shifted A-04 Part 2 to S19, extending Phase B.5 from 5 sessions to 6 (S16-S21). Updated §3b B.5 sequencing and §8 recommended next sessions. |
| 1.3 | 2026-04-06 | S20 (close-out update) | Marked S17-S20 complete in §3b session table. B1 gate cleared — all 26 domains at 3+. 6/7 audit threads complete with status/findings. Risk register: 3 risks resolved (B1 domains, academic rigor, mountability), 1 new (confidence inflation). B.5 gate exit criteria: 7/10 checked. §8 sequencing updated. Vault at 207 concepts, 390 sources. |
| 1.4 | 2026-04-06 | S21 (close-out update) | Phase B.5 COMPLETE. S21 marked done: A-07 PASS (650 files, 31 wikilinks remediated), DELTA-013/016/018/019 accepted (zero-open gate cleared). B.5 gate exit criteria: 10/10 (pending Alex sign-off). Phase C gates: all checked. README updated to v1.0 state. RELEASE-v1.0.0.md filed. Session-operational-plan-template created (S20 retro improvement). Risk register: confidence inflation mitigated (A-06 applied). v1.0.0 tag pending PR merge. |
| 1.5 | 2026-04-06 | D1 (CI Audit) | Phase D begun. D1 CI audit complete: 23 findings across 6 categories (template, pipeline, validation, session, governance, convention). Gap register (YAML) + improvement register (MD) populated. D-gate exit criteria refined (8 must-have, 3 should-have, 3 nice-to-have). 4 D1 items resolved inline: wikilink-filename validation (ingestion-rules v2.1 Step 5b), validation report pattern policy (batch vs audit vs consolidated), version bump. D budget revised 1.3-1.6M (down from 2M). D4 conditional on D2 decisions. |

---

*AI Disclosure: Co-produced by Claude (Anthropic) and Alex Jackson, 2026-04-05.*
*v1.0-DRAFT drafted in kitchen-sync session S128 worktree; v1.1 persisted and extended in venue-ops-kb S16.*
