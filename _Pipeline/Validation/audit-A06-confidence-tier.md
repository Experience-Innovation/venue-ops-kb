---
title: "Audit A-06: Confidence Tier Defensibility"
audit_outcome: CONDITIONAL
lifecycle: active
created: 2026-04-06
scope: "207 concepts across 26 domains"
methodology: "Hybrid — automated frontmatter scan + manual review of flagged concepts"
---

# Audit A-06: Confidence Tier Defensibility

## 1. Executive Summary

Automated scan of 207 concept notes across 26 domains, followed by manual review of 18 flagged concepts.

**Vault-wide confidence distribution (pre-audit):**

| Tier | Count | % |
|------|-------|---|
| high | 191 | 92.3% |
| medium | 16 | 7.7% |
| low | 0 | 0.0% |
| MISSING | 0 | 0.0% |

**Vault-wide confidence distribution (post-audit):**

| Tier | Count | % |
|------|-------|---|
| high | 183 | 88.4% |
| medium | 22 | 10.6% |
| low | 2 | 1.0% |
| MISSING | 0 | 0.0% |

**Findings:**
- 18 concept notes flagged by automated scan (16 single-source-high, 2 single-source-medium)
- 26 MOC/domain files with missing `confidence:` field (structurally appropriate per SCHEMA.yaml -- no action required)
- 0 concepts with zero sources
- 0 concepts with missing confidence field
- 0 low-confidence concepts with 3+ sources

**Adjustments made:** 10 total
- 8 downgrades from high to medium
- 2 downgrades from medium to low
- 8 concepts confirmed at current tier despite single-source flag

**Audit outcome: CONDITIONAL** -- adjustments applied; the vault's 92.3% high-confidence concentration is reduced to 88.4% but remains elevated. The absence of any low-confidence concepts prior to this audit indicates a systemic bias toward high-confidence assignment during extraction. Future extraction sessions should apply stricter adherence to the tier definitions.

---

## 2. Per-Domain Confidence Distribution (Post-Audit)

| Domain | High | Medium | Low | Total |
|--------|------|--------|-----|-------|
| av-and-production | 11 | 2 | 0 | 13 |
| booking-and-sales | 5 | 0 | 0 | 5 |
| commercial-and-revenue | 6 | 0 | 0 | 6 |
| crowd-management | 4 | 0 | 0 | 4 |
| data-and-analytics | 6 | 1 | 0 | 7 |
| event-operations | 11 | 1 | 0 | 12 |
| facilities-and-building-systems | 15 | 0 | 0 | 15 |
| financial-operations | 4 | 0 | 0 | 4 |
| food-and-beverage | 10 | 3 | 0 | 13 |
| guest-experience | 5 | 0 | 0 | 5 |
| inclusivity-and-accessibility | 6 | 1 | 0 | 7 |
| legal-compliance-and-licensing | 7 | 0 | 0 | 7 |
| logistics-and-warehouse | 1 | 2 | 0 | 3 |
| marketing-and-communications | 5 | 0 | 0 | 5 |
| parking-and-transportation | 6 | 4 | 0 | 10 |
| people-and-culture | 5 | 2 | 0 | 7 |
| premium-and-vip | 5 | 1 | 0 | 6 |
| quality-and-continuous-improvement | 10 | 0 | 0 | 10 |
| safety-and-risk | 14 | 0 | 0 | 14 |
| security | 5 | 1 | 0 | 6 |
| strategy-and-governance | 8 | 0 | 0 | 8 |
| supply-chain-and-procurement | 3 | 1 | 0 | 4 |
| sustainability-and-environmental | 11 | 0 | 0 | 11 |
| technology-and-digital | 4 | 1 | 0 | 5 |
| tenant-and-partner-relations | 10 | 1 | 2 | 13 |
| ticketing-and-box-office | 6 | 1 | 0 | 7 |

---

## 3. Flagged Concept Detail

### 3.1 Single-Source HIGH Flags (16 concepts)

#### DOWNGRADE: high to medium (8 concepts)

**1. Food-And-Beverage-FOOD-TRAK-Inventory-System.md**
- Source: `Source-0254-Zebra-McCormick-FOOD-TRAK` (vendor documentation)
- Rationale: Single vendor case study. While metrics are directly stated (80% to 98% accuracy, 30+ to 16 hours), the sole source is vendor marketing material with no independent verification. Per tier definitions, high requires "directly stated in DR source with verifiable citation" -- but the verifiability of a vendor's own case study is inherently limited.
- Resolution: **DOWNGRADE to medium**. Flag for supplementary source enrichment.

**2. Parking-And-Transportation-Pre-Paid-Reserved.md**
- Source: `Source-0133-ParkMobile-Case-Studies` (vendor documentation)
- Rationale: ParkMobile case study citing Mercedes-Benz Stadium 70%+ pre-paid adoption. Vendor case study as sole source; metrics are vendor-reported without independent corroboration.
- Resolution: **DOWNGRADE to medium**. Flag for supplementary source enrichment.

**3. Parking-And-Transportation-Self-Operated-Vs-Contracted.md**
- Source: `Source-0131-NPA-Parking-Rate-Study` (trade association)
- Rationale: NPA rate study is an industry body publication, but the body text covers operational models, hybrid approaches, and staffing patterns that extend well beyond what a rate study would contain. Claims in the body are not adequately supported by the single cited source.
- Resolution: **DOWNGRADE to medium**. Body text makes general industry claims not directly traceable to the NPA rate study.

**4. Parking-And-Transportation-Technology-Systems.md**
- Source: `Source-0134-HUB-Parking-Technology` (vendor documentation)
- Rationale: Single vendor source. Body text covers broad parking technology landscape (LPR, PARCS, IoT sensors, cloud dashboards) far exceeding what a single vendor document would cover. Claims about industry convergence and integration trends are unsupported.
- Resolution: **DOWNGRADE to medium**. Broad claims from single vendor source.

**5. Parking-And-Transportation-Transit-Multimodal.md**
- Source: `Source-0132-FHWA-Special-Events` (government document)
- Rationale: FHWA guide is authoritative for traffic management, but body text includes claims about MLB Green club bicycle valet, transit incentive programs, bike-share station placement, and signal timing adjustments -- none attributed to the FHWA source. Significant content extends beyond the single cited source.
- Resolution: **DOWNGRADE to medium**. Body claims exceed source coverage.

**6. People-And-Culture-Prevailing-Wage.md**
- Source: `Source-0159-Davis-Bacon-Act-Overview` (regulatory document)
- Rationale: Body text references multiple specific statutes and programs (CWHSSA, EO 14063, 28 state prevailing wage laws, PLAs) that go well beyond a single Davis-Bacon overview source. While the core regulatory claims are verifiable, the breadth of claims exceeds what one source supports.
- Resolution: **DOWNGRADE to medium**. Multi-statute claims from single regulatory overview source.

**7. Premium-And-Vip-Food-Service-Compliance.md**
- Source: `Source-0140-AGLC-Special-Event-Licence` (regulatory document)
- Rationale: The cited source is about Alberta liquor licensing (AGLC), but the concept is about food service compliance (HACCP, temperature control, allergen management). The source does not directly support the primary claims. This is a source-content mismatch.
- Resolution: **DOWNGRADE to medium**. Source does not directly address the concept's primary subject matter.

**8. Security-Access-Control-Credential-Management.md**
- Source: `Source-0001-CISA-Venue-Security-Guide-2025` (government document)
- Rationale: CISA guide is authoritative, but body text covers general security concepts (RFID types, biometric access, mobile credentials, concentric zone model) that represent broad industry knowledge beyond what a single CISA guide would specify. Many body claims are general practice statements not traceable to the cited source.
- Resolution: **DOWNGRADE to medium**. General practice claims extend beyond single government source.

#### CONFIRM at high (8 concepts)

**9. Facilities-And-Building-Systems-Live-Nation-Blueprint-Studio.md**
- Source: `Source-0260-Pollstar-Live-Nation-1B-Investment` (industry publication)
- Rationale: Pollstar is an authoritative industry publication. The claims ($1B, 18 venues, 10%+ F&B lift) are directly stated in the source and are verifiable against public Live Nation announcements. Single-source is appropriate here -- this is a single-company program reported by a credible industry publication.
- Resolution: **CONFIRM as high**. Source directly states all key claims; Pollstar is a credible industry publication.

**10. Marketing-And-Communications-FTC-Endorsement.md**
- Source: `Source-0145-FTC-Endorsement-Guides` (regulatory document)
- Rationale: The source IS the regulation itself (16 CFR Part 255). Regulatory and legal documents are primary sources by definition. The claims in the body directly describe the regulatory requirements of this specific law.
- Resolution: **CONFIRM as high**. Primary regulatory source directly supports all claims.

**11. Premium-And-Vip-Liquor-Licensing.md**
- Source: `Source-0140-AGLC-Special-Event-Licence` (regulatory document)
- Rationale: The AGLC source is the regulatory authority's own documentation of its licensing framework. The body text directly describes AGLC licence types and requirements. This is a primary regulatory source for the exact topic.
- Resolution: **CONFIRM as high**. Source is the regulatory authority's own documentation on this exact topic.

**12. Quality-And-Continuous-Improvement-IAVM-Venue-Excellence.md**
- Source: `Source-0188-IAVM-Venue-Excellence-Award` (trade association)
- Rationale: IAVM is the organization that administers the award. The source is their own documentation of the program's criteria, weighting, and process. A primary source from the issuing body.
- Resolution: **CONFIRM as high**. Primary source from the program's administering organization.

**13. Quality-And-Continuous-Improvement-Shingo-Prize.md**
- Source: `Source-0187-Shingo-Institute` (trade association / academic institution)
- Rationale: The Shingo Institute at Utah State University is the entity that administers the Shingo Prize. Their documentation is the primary source for the framework's dimensions, principles, and scoring.
- Resolution: **CONFIRM as high**. Primary source from the framework's administering institution.

**14. Safety-And-Risk-Business-Continuity-Planning.md**
- Source: `Source-0002-CISA-Dependency-Disruptions-Guide-2026` (government document)
- Rationale: CISA is an authoritative federal government source. The January 2026 guide specifically addresses dependency disruptions for stadiums and arenas. While body text includes general BCP concepts (BIA, RTO, 3-2-1 backup), these are well-established practices that the CISA guide references within its framework.
- Resolution: **CONFIRM as high**. Authoritative government source specifically addressing venue BCP.

**15. Strategy-And-Governance-MTCC-Beyond-Convention.md**
- Source: `Source-0242-MTCC-Business-Strategic-Plan-2025-2028` (primary document)
- Rationale: The source is the MTCC's own publicly disclosed business plan. This is a primary document describing the organization's own strategic framework. All claims (three pillars, performance targets, governance structure) are directly from the plan.
- Resolution: **CONFIRM as high**. Primary document from the organization describing its own program.

**16. Strategy-And-Governance-Organizational-Readiness-AI.md**
- Source: `Source-0255-Unleash-Organizational-Readiness-AI` (industry publication)
- Rationale: The claims are specific and quantitative (52% of employees, 34,000 workers, 24 countries) and directly stated in the cited source covering the Qualtrics research. The research methodology is described with enough specificity for verification.
- Resolution: **CONFIRM as high**. Specific quantitative claims directly from cited source.

### 3.2 Single-Source MEDIUM Flags (2 concepts)

**17. Tenant-And-Partner-Relations-Multi-Tenant-Scheduling-Governance.md**
- Source: `Source-0351-IAVM-Venue-Executive-Competency-Standards` (1 source)
- Current: medium | Sources: 1
- Analysis: Per VOCABULARY.yaml, medium requires "inferred from multiple sources or corroborated across batches." This concept has only 1 source and already self-flags with a Limitations section acknowledging single-source status. The body makes specific claims about NBA scheduling priority, convertible seating (Utah Delta Center), and Capital One Arena locker room facilities that extend beyond the IAVM source into general knowledge territory.
- Resolution: **DOWNGRADE to low**. Single-source concept with body claims extending beyond the cited source. Correctly self-identified as needing supplementary enrichment.

**18. Tenant-And-Partner-Relations-Performing-Arts-Resident-Companies.md**
- Source: `Source-0368-IAVM-PAC-Standard-Performance-Reporting` (1 source)
- Current: medium | Sources: 1
- Analysis: Same structural issue. Single IAVM PAC handbook source. The concept self-flags single-source status. Per tier definitions, single-source concepts belong in the low tier. The body includes specific pricing models ("11% of gross ticket sales") and cross-subsidy economics from a single source.
- Resolution: **DOWNGRADE to low**. Single-source concept per tier definition.

### 3.3 Missing Confidence -- Domain/MOC Files (26 files)

All 26 domain overview files (`Domain-*.md`, `note_type: domain`) lack a `confidence:` field. Per SCHEMA.yaml, `confidence` is optional for domain-type notes -- it appears under `universal.optional`, not `domain.required`. Domain overviews are structural aggregation notes (MOCs) that summarize child concepts rather than making independent claims. The absence of a confidence field is **structurally appropriate**.

- Resolution: **NO ACTION**. Missing confidence on domain notes is by design per schema.

---

## 4. Adjustments Made

| # | File | Change | Updated Date |
|---|------|--------|-------------|
| 1 | `Food-And-Beverage-FOOD-TRAK-Inventory-System.md` | high to medium | 2026-04-06 |
| 2 | `Parking-And-Transportation-Pre-Paid-Reserved.md` | high to medium | 2026-04-06 |
| 3 | `Parking-And-Transportation-Self-Operated-Vs-Contracted.md` | high to medium | 2026-04-06 |
| 4 | `Parking-And-Transportation-Technology-Systems.md` | high to medium | 2026-04-06 |
| 5 | `Parking-And-Transportation-Transit-Multimodal.md` | high to medium | 2026-04-06 |
| 6 | `People-And-Culture-Prevailing-Wage.md` | high to medium | 2026-04-06 |
| 7 | `Premium-And-Vip-Food-Service-Compliance.md` | high to medium | 2026-04-06 |
| 8 | `Security-Access-Control-Credential-Management.md` | high to medium | 2026-04-06 |
| 9 | `Tenant-And-Partner-Relations-Multi-Tenant-Scheduling-Governance.md` | medium to low | (already 2026-04-06) |
| 10 | `Tenant-And-Partner-Relations-Performing-Arts-Resident-Companies.md` | medium to low | (already 2026-04-06) |

---

## 5. Patterns Observed

### Pattern 1: High-confidence inflation from single-source concepts
The vault entered this audit with 92.3% high-confidence concepts and 0% low-confidence concepts. The VOCABULARY.yaml definitions are clear that high requires "directly stated in DR source with verifiable citation" and low covers "single source, indirect reference, or expert opinion." The complete absence of low-confidence concepts indicates a systemic bias during extraction: concepts were assigned high confidence based on the quality of the source rather than the breadth of corroboration and the traceability of body claims to the cited source.

### Pattern 2: Source-content mismatch
One concept (Premium Food Service Compliance) cited a liquor licensing source (AGLC) for food safety compliance claims. This suggests the source was assigned based on research batch association rather than content alignment. Source-content mismatches are a data quality risk -- they create false provenance chains.

### Pattern 3: Body text scope exceeding source scope
Multiple flagged concepts (Parking Technology, Transit Multimodal, Prevailing Wage, Access Control) contain body text that makes claims well beyond what the single cited source could support. This is a characteristic pattern of extraction sessions where general industry knowledge is written into the body while only the primary source is cited. The body content may be factually correct, but it is not traceable to the cited source -- which is the standard this KB requires.

### Pattern 4: Vendor documentation as sole source
Three concepts cited vendor case studies or vendor documentation as their sole source (FOOD-TRAK/Zebra, ParkMobile, HUB Parking). Vendor documentation carries inherent bias -- metrics reported by vendors about their own products lack independent verification. These concepts are correctly downgraded to medium pending supplementary independent sources.

### Pattern 5: Parking-and-transportation domain concentration
The parking-and-transportation domain accounts for 4 of the 8 high-to-medium downgrades, suggesting this domain was processed with weaker source diversity than other domains. This is consistent with the v2-prompt-11-premium-guest research batch, which covered parking alongside premium/VIP and guest experience -- parking may have received secondary extraction attention.

### Pattern 6: Regulatory/primary sources defensible at high
Concepts citing regulatory documents (FTC, AGLC), issuing body documentation (IAVM, Shingo Institute), or government sources (CISA) as their sole source were confirmed at high when the body claims stayed within the scope of the cited document. Primary sources from authoritative bodies satisfy the "verifiable citation" requirement even at single-source count.

---

## 6. Recommendations for Future Sessions

1. **Apply stricter tier definitions during extraction.** The extraction pipeline should default to medium when only one non-regulatory source is available, and reserve high for concepts with either (a) a primary/regulatory source or (b) 2+ independent corroborating sources.

2. **Flag vendor documentation at extraction time.** Any concept sourced solely from vendor case studies or vendor documentation should be assigned medium at extraction, never high, regardless of the specificity of the claims. Vendor sources have inherent independence limitations.

3. **Validate source-content alignment.** The source cited in frontmatter must directly address the concept's primary subject matter. A liquor licensing source should not be the sole citation for a food safety compliance concept.

4. **Audit body text scope against source scope.** When body text makes claims beyond what the cited source can reasonably support, either (a) add sources that cover the additional claims, or (b) downgrade confidence to reflect the gap.

5. **Prioritize parking-and-transportation for source enrichment.** This domain has the highest concentration of single-source concepts and would benefit from targeted supplementary research.

6. **Target 2-5% low-confidence representation.** The complete absence of low-confidence concepts before this audit was itself a finding. A well-calibrated knowledge base should have some concepts at low confidence -- particularly niche, emerging, or expert-opinion concepts. The current 1.0% (2 concepts) is closer to appropriate but should increase as the vault grows.

7. **Integrate single-source flagging into the ingestion pipeline.** The ingestion-rules.md Stage 4 already flags single-source concepts. This flag should be enforced as a confidence ceiling: single non-regulatory sources cap confidence at medium.

---

*Audit conducted 2026-04-06 by Claude Opus 4.6 as part of Session 20 Phase B.5 academic rigor initiative.*
*AI Disclosure: Audit methodology designed by Alex Jackson, EXi. Automated scan + manual review executed by Claude Opus 4.6. All confidence tier adjustments subject to human review.*
