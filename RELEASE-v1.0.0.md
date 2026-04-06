# Release Notes — v1.0.0

**Release date:** 2026-04-06
**Tag:** `v1.0.0`
**Repository:** [Experience-Innovation/venue-ops-kb](https://github.com/Experience-Innovation/venue-ops-kb)

---

## Overview

v1.0.0 is the initial release of the Venue Operations Knowledge Base — an open-source, educational Obsidian vault mapping 26 operational domains of large-scale venue management. Built to academic-publishing standards through Human/AI collaboration across 21 processing sessions.

This knowledge base serves 35,000-50,000 mid-to-senior venue operations professionals across North America. It is designed as a peer-reviewable scholarly reference that the venue operations industry can cite and build upon.

---

## What's Included

### Vault Contents

| Note Type | Count | Description |
|-----------|:-----:|-------------|
| Concept notes | 207 | Operational concepts across 26 domains |
| Source notes | 390 | Citation notes with URLs, bibliographic metadata, and provenance |
| Domain overviews | 26 | Scope definitions and key functions per domain |
| Maps of Content | 27 | Navigational overviews (26 domain MOCs + 1 master ecosystem map) |
| **Total** | **650** | |

### Domain Coverage

All 26 domains reach minimum viable depth (3+ concepts):

| Depth Tier | Domains | Count |
|------------|---------|:-----:|
| Authoritative (15+) | facilities-and-building-systems | 1 |
| Working depth (8-14) | safety-and-risk, av-and-production, food-and-beverage, tenant-and-partner-relations, event-operations, sustainability-and-environmental, parking-and-transportation, quality-and-continuous-improvement, strategy-and-governance | 9 |
| Minimum viable (3-7) | All remaining domains | 16 |

### 26-Domain Taxonomy

Locked in Session 9 via middle-out method against five industry frameworks (Baldrige, EFQM, AIPC, IAVM, Excellence Canada):

Guest Experience, People & Culture, Food & Beverage, Event Operations, Facilities & Building Systems, Safety & Risk, Security, Crowd Management, Sustainability & Environmental, Technology & Digital, AV & Production, Data & Analytics, Financial Operations, Commercial & Revenue, Ticketing & Box Office, Booking & Sales, Supply Chain & Procurement, Logistics & Warehouse, Parking & Transportation, Marketing & Communications, Premium & VIP, Legal/Compliance/Licensing, Inclusivity & Accessibility, Strategy & Governance, Quality & Continuous Improvement, Tenant & Partner Relations.

### Confidence Distribution

| Tier | Count | Percentage | Definition |
|------|:-----:|:----------:|------------|
| High | 183 | 88.4% | Directly stated in source with verifiable citation |
| Medium | 22 | 10.6% | Inferred or single non-authoritative source |
| Low | 2 | 1.0% | Single source with limited evidence |

### Quality Metrics

- **Zero fabrication** across 21 sessions and 207 concept notes
- **100% GLRC provenance chain** — ai_disclosure, extraction_model, research_batch on every concept
- **100% schema compliance** — 650 notes validated against 34 pre-write checks
- **Zero vocabulary drift** — all controlled fields match VOCABULARY.yaml
- **Zero forbidden terminology** — no Vivid Array, no old domain slugs
- **Zero broken wikilinks** — 606 related_to links, 207 child_of links, 676 source links all verified
- **26/26 domain node_count accuracy** — frontmatter matches actual file counts

---

## Academic Rigor Initiative (Phase B.5)

Seven audit threads completed across Sessions 16-21:

| Thread | Focus | Outcome |
|--------|-------|---------|
| A-01 | Provenance chain completeness | PASS |
| A-02 | Controlled vocabulary enforcement | PASS |
| A-03 | Citation format standardization | PASS |
| A-04 | Claim-to-source traceability | CONDITIONAL PASS (60% full pass, zero fabrication) |
| A-05 | Structural consistency | CONDITIONAL (vault avg 85/100) |
| A-06 | Confidence tier defensibility | CONDITIONAL (10 adjustments applied) |
| A-07 | Final validation (v1.0 gate) | PASS |

**Delta register:** 20 entries catalogued across 6 sessions. 16 resolved through remediation, 4 accepted at v1.0 with documented rationale and Alex sign-off.

---

## Depth-of-Coverage Improvement Roadmap

v1.0 establishes minimum viable coverage across all 26 domains. The following areas are documented for post-v1.0 enrichment:

### Priority Enrichment Targets

| Priority | Area | Current State | Target |
|----------|------|---------------|--------|
| HIGH | logistics-and-warehouse depth | 3 concepts (floor), 67% medium confidence | 8+ concepts, improved source diversity |
| HIGH | financial-operations depth | 4 concepts | 8+ concepts |
| HIGH | crowd-management depth | 4 concepts | 8+ concepts |
| HIGH | DELTA-018 remediation | 2 accepted HIGH items (Prevailing Wage, Frontline Engagement) | Supplementary labor law sources |
| MEDIUM | 6 DELTA-019 concepts | Niche regulatory topics accepted at v1.0 | 1-2 targeted source notes each |
| MEDIUM | 15 minimum-viable domains | 3-7 concepts each | Working depth (8+) per strategic priority |
| LOW | 23 DELTA-013/016 concepts | Citation-strengthening polish items | 1 supplementary source each |

### Non-Concept Note Types

Standards, Technology, Organization, and Person note types are at 0 count — deferred by design since Session 11. Extraction from existing source corpus is the planned approach for post-v1.0 enrichment.

### Review Status

All 650 notes at `status: draft`. Human review passes (draft to reviewed to canonical) are scheduled as post-v1.0 work. AI-extracted content requires human validation before promotion.

---

## Methodology

Full methodology published in `METHODOLOGY.md` at vault root. Key points:

- **Research source:** Perplexity Pro deep research (13 primary prompts + 6 supplementary/remediation batches)
- **Processing model:** Claude Opus 4.6 (Anthropic) via Claude Code
- **Pipeline:** Five-stage intake (Receive, Register, Rinse, Ready, Route)
- **Validation:** 34 pre-write checks per note, 7 audit threads, delta register discipline
- **Taxonomy:** 26 domains via middle-out method (Baldrige/EFQM/AIPC/IAVM/Excellence Canada)
- **Relationships:** 7-type taxonomy (parent_of, child_of, implements, governed_by, supported_by, related_to, varies_by, scales_with)
- **Transparency:** EU AI Act aligned provenance chain, published limitations, reproducible from DR prompt to claim

---

## Known Limitations

1. All content at `status: draft` — requires human review for promotion
2. 88.4% high confidence concentration may reflect extraction-phase optimism despite A-06 corrections
3. Non-concept note types (Standards, Technology, Organizations, People) not yet extracted
4. 15 of 26 domains at minimum viable depth only
5. North American venue operations focus — international coverage limited to referenced frameworks
6. Source URLs verified at access date — link rot expected over time
7. Vendor documentation used as sources carries inherent bias (flagged in A-06 patterns)

---

## What's Next

### Phase D: Continuous Improvement Initiative (3-4 sessions)
CI audit, template architecture, visual indicator system, process standardization. Must complete before public release.

### Phase E: Post-v1.0 Enhancements
- Domain deepening per priority targets above
- Non-concept note type extraction
- Human review passes (draft to reviewed to canonical)
- Fresh DR for fast-evolving domains (technology-and-digital, data-and-analytics)
- Community feedback integration

---

## Session History

21 sessions from Session 4 (early March 2026) through Session 21 (April 6, 2026):

| Phase | Sessions | Focus |
|-------|----------|-------|
| A: Foundation | S4-S15 | Taxonomy, methodology, schema, extraction pipeline, initial 169 concepts |
| B.5: Academic Rigor | S16-S21 | 7 audit threads, delta register, MOC generation, bibliographic enrichment, DR remediation, confidence audit, final validation |

---

## AI Disclosure

This knowledge base was developed through Human/AI collaboration using Claude (Anthropic, Opus 4.6). Alex Jackson (Principal, Experience Innovation Inc.) holds human accountability for all content, methodology decisions, and strategic direction. Full methodology, confidence distributions, limitations, and reproducibility guidance are published in `METHODOLOGY.md`.

---

*Experience Innovation Inc. | Venue Operations Knowledge Base v1.0.0 | April 6, 2026*
