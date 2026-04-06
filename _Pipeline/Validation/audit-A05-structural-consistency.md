---
audit_id: A-05
audit_name: Peer-Review-Style Structural Consistency (domains M-T)
session: S19
date: 2026-04-06
phase: Audit execution + report
category: consistency
audit_outcome: CONDITIONAL PASS (vault average 85/100 editorial consistency; safety-and-risk at 72/100 requires remediation)
initiative: "Academic Rigor Initiative Phase B.5"
---

# Audit A-05: Peer-Review-Style Structural Consistency

## Audit Scope

**Goal:** Evaluate structural consistency of concept notes within each domain — description length, section headings, relationship density, source count distribution, and body length — to assess whether a reader experiences a coherent voice across the corpus.

**Scope:** 87 concept notes across 12 active domains (M-T). Tenant-and-partner-relations skipped (0 concepts).

**Methodology:** Per-domain metrics collection with cross-domain comparison. Flagging thresholds: description max >3x min, body length >5x variance, relationship density 0 where peers have 3+, description outliers (<15 or >80 words).

## Cross-Domain Consistency Metrics

| Domain | Concepts | Desc Words (min-max) | Body Lines (min-max) | Rel Density (avg) | Sources (avg) | Single-Src | Heading Uniformity | Score |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| marketing-and-comms | 5 | 34-78 | 40-50 | 1.8 | 2.0 | 0 | 100% | 95 |
| premium-and-vip | 6 | 48-72 | 40-70 | 2.5 | 2.5 | 0 | 90% | 92 |
| supply-chain-procurement | 4 | 52-75 | 35-50 | 1.5 | 2.5 | 0 | 90% | 90 |
| people-and-culture | 7 | 25-95 | 40-85 | 2.4 | 2.0 | 0 | 85% | 88 |
| sustainability-environ | 11 | 38-68 | 40-60 | 2.1 | 2.3 | 1 | 80% | 87 |
| technology-and-digital | 5 | 42-88 | 35-70 | 1.8 | 2.4 | 0 | 75% | 86 |
| parking-transportation | 10 | 38-65 | 45-60 | 1.4 | 2.0 | 4 | 100% | 85 |
| strategy-governance | 8 | 45-98 | 40-80 | 2.6 | 2.4 | 2 | 60% | 85 |
| quality-and-CI | 10 | 31-82 | 40-80 | 2.8 | 2.5 | 2 | 70% | 82 |
| security | 6 | 32-85 | 25-50 | 1.5 | 1.5 | 2 | 80% | 80 |
| safety-and-risk | 14 | 18-85 | 20-70 | 2.1 | 1.6 | 7 | 75% | 72 |
| ticketing-box-office | 1 | 58 | 45 | 1.0 | 2.0 | 0 | N/A | N/A |
| **VAULT AVG** | **87** | **18-98** | **20-85** | **2.0** | **2.1** | **18** | **81%** | **85** |

## Key Findings

### Finding 1: Safety-and-Risk Structural Inconsistency (72/100)

Safety-and-risk is the weakest domain structurally:
- **Body length 3.5x variance** (20-70 lines) — AED Programs is ~20 lines vs Mass Casualty ~70 lines
- **50% single-source** (7/14 concepts) — highest single-source rate of any domain
- **3 orphaned concepts** (AED, Fire Watch, Incident Command) — 0 relationship wikilinks while peers have 2-4
- **Description range 18-85 words** (4.7x ratio)

**Root cause:** Extraction imbalance. Simpler operational concepts (AED, Fire Watch) were extracted with less depth than complex frameworks (Tabletop Exercises, Mass Casualty). Not methodology drift — content-complexity variance that wasn't normalized during extraction.

### Finding 2: Heading Pattern Variation Is Appropriate

Concepts organized around regulatory frameworks (Baldrige, EFQM, LEED) naturally produce framework-specific heading hierarchies (e.g., "Seven Categories", "RADAR Scoring", "Certification Tiers"). Concepts organized around operational functions use generic structures ("Overview", "Key Components", "Best Practices").

This is **appropriate content-driven variation**, not editorial drift. A reader would expect framework-specific structure when reading about a named framework.

### Finding 3: Description Length Outliers

| Concept | Domain | Words | Issue |
|---|---|:-:|---|
| AED Programs | safety-and-risk | 18 | Under minimum viable (suggests truncated extraction) |
| DEI Training | people-and-culture | 95 | Over target (includes certification names in description) |
| Disney Chain of Excellence | strategy-governance | 98 | Over target (longest description in vault) |
| Access Control | security | 85 | Over target |
| Baldrige Framework | quality-CI | 82 | Over target |

**Recommendation:** Establish description length target of 30-70 words (median ~40). Descriptions >80 words should move detail to body text. Descriptions <25 words may indicate underextraction.

### Finding 4: Relationship Density Variance

Domains with richly linked concepts (quality-CI avg 2.8, strategy avg 2.6) coexist with sparsely linked domains (parking avg 1.4, security avg 1.5). Within safety-and-risk, 3 concepts have 0 relationships while others have 4.

**Specific orphaned concepts requiring relationship enrichment:**
- Safety-And-Risk-AED-Programs → related_to: Medical Staffing, Emergency Action Plans
- Safety-And-Risk-Fire-Watch-Protocols → related_to: Life Safety Evaluation, Emergency Action Plans
- Safety-And-Risk-Incident-Command-System → related_to: Emergency Action Plans, Tabletop Exercises, Crisis Communication
- Security-Access-Control → related_to: Patron Screening, AI Video Surveillance, Layered Security
- Sustainability-Carbon-Tracking → related_to: Renewable Energy, Net Zero Carbon Events

### Finding 5: Source Count Distribution

Average source count is 2.1 per concept. Domains above 2.5 (quality-CI, premium-VIP, supply-chain) demonstrate stronger traceability. Safety-and-risk at 1.6 average is the weakest — consistent with A-04 Part 2 findings.

## Remediation Items

| ID | Finding | Domain | Action | Priority |
|:-:|---|---|---|:-:|
| A-05-001 | AED Programs underextracted (18-word desc, ~20-line body) | safety-and-risk | Expand body text to 40-50 lines | HIGH |
| A-05-002 | 7/14 safety concepts single-source | safety-and-risk | Supplementary source enrichment (overlaps DELTA-014) | HIGH |
| A-05-003 | 3 orphaned safety concepts (0 relationships) | safety-and-risk | Add related_to wikilinks | HIGH |
| A-05-004 | Body length variance 3.5x in safety domain | safety-and-risk | Normalize shorter concepts to 40-50 lines | MED |
| A-05-005 | Security Access Control orphaned | security | Add related_to links to domain peers | MED |
| A-05-006 | Sustainability Carbon Tracking orphaned | sustainability | Add related_to links to domain peers | MED |
| A-05-007 | 2 single-source parking concepts | parking | Secondary source enrichment | LOW |
| A-05-008 | Description length range 18-98 words (5.4x) | vault-wide | Establish 30-70 word target; review outliers | MED |

## Delta Register Entry

DELTA-017 captures all A-05 consistency findings as a single aggregate entry.

## Summary

**Status: CONDITIONAL PASS** (vault average 85/100; safety-and-risk at 72/100 requires remediation)

The M-T corpus demonstrates strong editorial consistency for an academic-publishing standard. 10 of 12 active domains score 80+ on structural consistency. The primary variance driver is **content-complexity-driven extraction imbalance** in the safety-and-risk domain, where simpler operational concepts were extracted with less depth than complex regulatory frameworks.

**Cross-domain heading variation is appropriate** — framework-specific concepts warrant framework-specific structure. Source count distribution and relationship density are generally healthy, with safety-and-risk as the consistent outlier needing enrichment.

**Combined with A-04 Part 2:** Safety-and-risk is the highest-risk domain across both traceability (93% gap rate) and consistency (72/100 score). This domain should be prioritized for S20 remediation.

---

*Session 19 · Audit A-05 · Academic Rigor Initiative Phase B.5 Session 4*
