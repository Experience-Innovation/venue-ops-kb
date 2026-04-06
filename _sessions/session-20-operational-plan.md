---
type: operational-plan
session: S20
lifecycle: active
created: 2026-04-06
branch: session-20/b1-a06
machine: MacBook Air (bubblegumpshrimpco)
---

# Session 20 Operational Plan — B.1 DR Ingestion + A-06 Confidence Audit + Delta Remediation

**Session:** S20 (Phase B.5, Session 5 of 6)
**Date:** 2026-04-06
**Branch:** `session-20/b1-a06` (worktree)
**Predecessor:** S19 (A-04 P2 + A-05 + DELTA-012 resolution + DR prompt suite) — PR #9 merged

---

## §1. Context & Scope

**Inherited state:**
- 169 concepts, 290 sources, 27 MOCs, 26/26 domain overviews
- Delta register: 17 entries (12 resolved, 5 deferred)
- 3 zero-concept domains blocking v1.0 (data-and-analytics, booking-and-sales, tenant-and-partner-relations)
- A-04 complete: 60% PASS, zero fabrication, 40% gap rate
- A-05 complete: vault avg 85/100, safety-and-risk 72/100

**New inputs (this session):**
- 5 DR output files from R-06 through R-10 (Perplexity Pro Enterprise Max)
- ~41K words, 732 cited URLs, 69+ extractable concepts
- R-10 covers all 8 DELTA-014 HIGH-severity targets

**Scope decisions:**
1. DR ingestion runs FIRST — fills 3 empty domains (B1 gate), deepens thin domains, provides sources for DELTA-014 resolution
2. A-06 confidence audit runs SECOND — audits enriched corpus, not pre-enrichment corpus
3. A-06 uses hybrid approach: automated scan + manual review of flagged concepts (not full 238-concept manual audit)
4. DELTA-017 consistency remediation integrated with DR processing (safety concepts enriched during extraction)
5. DELTA-015 MED-severity sweep is opportunistic (budget-dependent)

**Scope exclusions:** A-07 (S21), new DR prompt creation, MOC updates (S21 scope)

---

## §2. Brigade Roster

| Role | Owner | Responsibility | Batch Size |
|------|-------|---------------|------------|
| **ESC** | Claude (primary) | Orchestration, extraction manifests, QA gates, governance, A-06 audit methodology, plan accountability | All phases |
| **Recon Agent 1** | Subagent | Read R-06 + R-07, extract entities, produce extraction manifest | 2 DR files |
| **Recon Agent 2** | Subagent | Read R-08 + R-09, extract entities, produce extraction manifest (R-09 CS/BMO filter) | 2 DR files |
| **Recon Agent 3** | Subagent | Read R-10, extract entities, map to DELTA-014 concepts | 1 DR file |
| **Source Writer Agents** (parallel) | Subagents | Create source notes (Source-0291+) from extracted URLs | Batches of 15 |
| **Concept Writer Agents** (parallel) | Subagents | Create concept notes per extraction manifest | Batches of 8-10 |
| **Enrichment Agent** | Subagent | Enrich existing concepts (DELTA-014 resolution, DELTA-017 items) | 8 concepts |
| **A-06 Scanner** | Subagent | Automated confidence-tier-vs-sources scan across all concepts | Full vault |

**Agent dispatch standards:** All prompts include 7 required fields per D-13. Pre-extract binary content before dispatch. Cap batch sizes at 10-15 content-heavy, 8-10 dense. No Bash-heavy agent work.

---

## §3. GLRC Framework

| Dimension | Checkpoint | When | Evidence |
|-----------|-----------|------|----------|
| **Governance** | Operational plan aligned with Alex | Pre-execution | This document |
| **Governance** | Extraction manifest reviewed before note creation | Phase 1 (per DR file) | Manifest in-thread |
| **Lineage** | research_batch assigned to every new note | Phase 1 (every note) | Frontmatter field |
| **Lineage** | sources[] populated with wikilinks to Source notes | Phase 1 (every note) | Frontmatter field |
| **Reconciliation** | Delta register updated with resolution evidence | Phase 3 + Phase 5 | delta-register.yaml |
| **Reconciliation** | Validation report filed | Phase 5 | _Pipeline/Validation/ |
| **Compliance** | Schema validation on all new/modified notes | Phase 1 + Phase 2 | Validation report |
| **Compliance** | Terminology scan before commit | Phase 5 | Clean scan |
| **Compliance** | Single-source flag enforced at Stage 4 Ready gate | Phase 1 | Manifest flags |

---

## §4. Phase Definitions

### Phase 1: DR Ingestion — R-06 through R-10 (~350K tokens)

**Owner:** ESC + Recon + Writer agents
**Objective:** Process 5 DR files through 5-stage intake pipeline. Create source notes, then concept notes. Fill 3 empty domains to minimum viable (3+). Deepen commercial-and-revenue, financial-operations, ticketing-and-box-office.

**Processing sequence:** R-10 (safety — DELTA-014) → R-06 (booking/sales/ticketing) → R-07 (data/analytics) → R-08 (tenant/partner) → R-09 (commercial/financial, CS filter)

**Rationale for sequence:** R-10 first because it resolves HIGH-severity DELTA-014 (highest-risk items in the register). R-06/R-07/R-08 next because they fill the 3 zero-concept domains (B1 gate). R-09 last because it requires CS/BMO content filtering and overlaps concepts already partially covered.

**Per-file workflow:**
1. Recon agent reads file, produces extraction manifest (concepts, sources, domain mapping, confidence tiers)
2. ESC reviews manifest — validates against VOCABULARY.yaml, checks deduplication, flags single-source concepts
3. Source Writer agents create source notes (Source-0291+)
4. Concept Writer agents create concept notes in target domains
5. ESC runs schema + vocabulary + terminology validation on batch
6. Progress logged

**VOCABULARY.yaml update required:** New `research_batch` entry for R-06 through R-10 output. Propose: `dr-s20-r06-booking-ticketing`, `dr-s20-r07-data-analytics`, `dr-s20-r08-tenant-partner`, `dr-s20-r09-commercial-financial`, `dr-s20-r10-safety-supplementary`.

**Estimated output:**
- ~60-80 new source notes (Source-0291 through ~Source-0370)
- ~40-55 new concept notes across 10+ domains
- ~8 existing concept notes enriched (DELTA-014 targets)

**Exit criteria:**
- All 5 DR files processed through Stage 5
- 3 zero-concept domains at minimum viable (3+ concepts each)
- DELTA-014: 8 concepts enriched with supplementary sources and body text citations
- All new notes pass 34 pre-write validation checks
- Single-source concepts flagged per ingestion-rules.md Stage 4

### Phase 2: A-06 Confidence Tier Audit (~80K tokens)

**Owner:** ESC + A-06 Scanner agent
**Objective:** Verify every confidence tier assignment (high/medium/low) is defensible against the rubric in VOCABULARY.yaml.

**Methodology (hybrid — automated scan + manual review):**

**Step 1 — Automated scan (all ~220+ concepts):**
- Extract `confidence` and `sources[]` count from every concept note frontmatter
- Flag misalignments:
  - `confidence: high` with <2 sources → FLAG (should have direct source with verifiable citation)
  - `confidence: medium` with <2 sources → FLAG (should have multi-source corroboration)
  - `confidence: low` with 3+ sources → FLAG (may warrant upgrade)
  - `confidence:` missing → FLAG
- Produce scan report with per-domain summary

**Step 2 — Manual review (flagged concepts only):**
- For each flagged concept: read body text + sources, determine correct tier
- Apply adjustments: UPGRADE / DOWNGRADE / CONFIRM
- Document rationale per adjustment

**Step 3 — Audit report:**
- File to `_Pipeline/Validation/audit-A06-confidence-tier.md`
- Per-domain confidence distribution (before/after adjustments)
- Flagged concept detail with resolution

**Exit criteria:**
- Scan report produced covering all concepts (existing + new)
- All flagged concepts reviewed and resolved
- Audit report filed with per-domain findings
- Any new delta entries created for systemic issues

### Phase 3: Delta Register Sweep (~60K tokens)

**Owner:** ESC
**Objective:** Resolve or advance all 5 deferred delta entries.

| Delta | Severity | S20 Action |
|-------|----------|------------|
| DELTA-014 | HIGH (8 concepts) | Resolved via Phase 1 R-10 processing |
| DELTA-017 | MED (8 items) | Resolve: expand AED Programs body, add relationships to orphaned concepts, normalize body length |
| DELTA-015 | MED (20 concepts) | Opportunistic: enrich from existing corpus + new S20 sources where match exists |
| DELTA-013 | LOW (13 concepts) | Scan for overlaps with new S20 sources; resolve where trivial, defer remainder to S21 |
| DELTA-016 | LOW (10 concepts) | Defer to S21 (per original target_session) |

**DELTA-017 detail (A-05 consistency items):**
- A-05-001: Expand AED Programs body from ~20 lines to domain average (~60 lines) using R-10 content
- A-05-002/003/004: Add `related_to` wikilinks to 3 orphaned safety concepts (Emergency-Action-Plans, Fire-Watch-Protocols, Heat-Illness-Protocols → link to existing safety concepts)
- A-05-005: Add relationships to Security-Access-Control orphan
- A-05-006: Add relationships to Sustainability-Carbon-Tracking orphan
- A-05-007/008: Description length normalization (address 5.4x ratio)

**Exit criteria:**
- DELTA-014 marked resolved-batch with resolution evidence
- DELTA-017 items resolved where source material supports it
- DELTA-015 partially resolved from expanded corpus
- Delta register updated with session-level log entry

### Phase 4: Governance Close (~30K tokens)

**Owner:** ESC

**Deliverables:**
1. Validation report for DR ingestion batches
2. Delta register updated (entries + metrics + session log)
3. progress.md updated (S20 entry + domain processing status table + vault statistics)
4. pipeline-state.json updated
5. VOCABULARY.yaml updated (new research_batch entries)
6. Terminology scan on all modified files
7. Git commit (meaningful message per feedback standard)
8. PR opened via `gh pr create`

**Close-out sequence per global CLAUDE.md:** Phase 1 (session accounting) → Phase 2 (retro conversation) → Phase 3 (handoff + pass-forward) → Phase 4 (operational close) → Phase 5 (verification)

---

## §5. Batch Definitions

### DR Ingestion Batches

| Batch | DR File | Target Domains | Est. Concepts | Est. Sources | Agent Assignment |
|-------|---------|---------------|--------------|-------------|-----------------|
| batch-14-safety-supp | R-10 | safety-and-risk, people-and-culture | 8-12 (mostly enrichment) | 15-20 | Recon 3 + Enrichment |
| batch-15-booking-ticketing | R-06 | booking-and-sales, ticketing-and-box-office, commercial-and-revenue | 12-15 | 15-20 | Recon 1 + Writer |
| batch-16-data-analytics | R-07 | data-and-analytics, technology-and-digital, guest-experience | 12-15 | 15-20 | Recon 1 + Writer |
| batch-17-tenant-partner | R-08 | tenant-and-partner-relations, booking-and-sales, commercial-and-revenue | 8-12 | 10-15 | Recon 2 + Writer |
| batch-18-commercial-financial | R-09 | commercial-and-revenue, financial-operations, ticketing-and-box-office | 8-10 | 10-15 | Recon 2 + Writer (CS filter) |

### A-06 Audit Batch

| Batch | Scope | Method | Agent Assignment |
|-------|-------|--------|-----------------|
| A-06-scan | All ~220+ concepts | Automated frontmatter scan | Scanner agent |
| A-06-review | Flagged concepts only | Manual ESC review | ESC direct |

### Delta Remediation Batch

| Batch | Delta | Concepts | Method |
|-------|-------|----------|--------|
| delta-014-resolve | DELTA-014 | 8 | Integrated with batch-14 |
| delta-017-resolve | DELTA-017 | 8 items | ESC direct post-ingestion |
| delta-015-sweep | DELTA-015 | 20 (opportunistic) | ESC direct |

---

## §6. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| R-09 CS/BMO content not fully filtered | Medium | Exemplar policy violation | CS content scan on all R-09 extracted notes; `cs_exemplar: true` tagging |
| Concept deduplication across R-06/R-08/R-09 (overlapping commercial/booking topics) | High | Duplicate notes created | Cross-file dedup check in extraction manifest; enrich existing notes |
| Token budget exceeded before A-06 complete | Medium | A-06 deferred to S21 | Hybrid approach caps A-06 at ~80K; Phase 3 delta sweep is flexible |
| URL fabrication by extraction agents | Low (mitigated S15) | Fabricated sources | Verbatim-quote requirement in all agent prompts; grep verification |
| Single-source concepts created from thin DR coverage | Medium | Future traceability gaps | Stage 4 Ready gate flag enforced; logged in validation report |
| R-10 doesn't cover Prevailing Wage or Frontline Engagement adequately | Medium | 2/8 DELTA-014 items partially resolved | R-10 assessment shows MEDIUM confidence on these 2; existing corpus search as fallback |

---

## §7. Token Budget

| Phase | Estimate | Cumulative |
|-------|---------|------------|
| Phase 1: DR Ingestion (5 files, ~55 concepts, ~70 sources) | ~350K | 350K |
| Phase 2: A-06 Confidence Audit (hybrid) | ~80K | 430K |
| Phase 3: Delta Sweep (DELTA-014/015/017) | ~60K | 490K |
| Phase 4: Governance Close | ~30K | 520K |
| **Buffer** | ~80K | **600K** |

**Budget ceiling:** 600K tokens (within comfortable operating range per reference_token-budget.md)
**Flex items:** Phase 3 DELTA-015 sweep (can reduce from 20 to top-10 if budget pressure). Phase 2 manual review scope (can reduce to safety-domain-only if needed).

---

## §8. Binary Success Criteria

- [ ] R-10 processed: DELTA-014 concepts enriched with supplementary sources
- [ ] R-06 processed: booking-and-sales at minimum viable (3+ concepts)
- [ ] R-07 processed: data-and-analytics at minimum viable (3+ concepts)
- [ ] R-08 processed: tenant-and-partner-relations at minimum viable (3+ concepts)
- [ ] R-09 processed: commercial-and-revenue and financial-operations deepened (CS content filtered)
- [ ] All 26 domains at minimum viable (3+ concepts) — B1 GATE CLEARED
- [ ] A-06 confidence tier audit complete with per-domain findings report
- [ ] DELTA-014 marked resolved in delta register
- [ ] DELTA-017 consistency items resolved (safety orphans linked, AED expanded)
- [ ] DELTA-015 partially resolved (opportunistic sweep)
- [ ] All new notes pass 34 pre-write validation checks
- [ ] Delta register updated with S20 session log
- [ ] Validation report filed
- [ ] VOCABULARY.yaml updated with new research_batch entries
- [ ] progress.md updated with S20 entry
- [ ] PR opened

**What worked documentation (per S19 Alex directive):**
- Document DR prompt template v1.0 yield across R-06 through R-10
- Document hybrid A-06 methodology if it proves efficient
- Document deduplication patterns across overlapping DR files

---

## Alignment Request

Alex — two items requiring your input before execution:

1. **Research batch naming:** Propose 5 new entries for VOCABULARY.yaml (listed in §4 Phase 1). Alternatively, a single `dr-s20-r06-r10` batch ID covering all 5 files. Recommendation: per-file IDs for traceability.

2. **Processing sequence confirmation:** R-10 first (safety/DELTA-014) → R-06 → R-07 → R-08 → R-09. This prioritizes the highest-risk delta items. Alternative: R-06/R-07/R-08 first (B1 gate) → R-10 → R-09. Recommendation: R-10 first.

---

*AI Disclosure: Operational plan co-produced by Claude (Anthropic) and Alex Jackson, 2026-04-06.*
