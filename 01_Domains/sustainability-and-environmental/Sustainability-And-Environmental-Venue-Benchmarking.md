---
title: "Venue Sustainability Benchmarking"
note_type: concept
domain: "sustainability-and-environmental"
status: draft
created: 2026-04-04
updated: 2026-04-04
description: "Sustainability benchmarking programs (ENERGY STAR Portfolio Manager, BOMA 360, Green Sports Alliance Play to Zero) enable venues to compare performance against peers on energy, water, waste, and carbon metrics, driving accountability and identifying improvement opportunities."
venue_types:
  - convention-centre
  - arena
  - stadium
  - performing-arts-centre
vef_alignment:
  - data-management-and-architecture
  - innovation-and-continuous-improvement
confidence: high
sources:
  - "[[Source-0048-ENERGY-STAR-Commercial-Buildings]]"
  - "[[Source-0053-BOMA-International-Resources]]"
  - "[[Source-0036-Green-Sports-Alliance]]"
research_batch: v2-prompt-02-facilities
child_of: "[[Domain-Sustainability-And-Environmental]]"
related_to:
  - "[[Sustainability-And-Environmental-LEED-Green-Building]]"
  - "[[Sustainability-And-Environmental-Carbon-Tracking-ESG]]"
key_metrics:
  - "ENERGY STAR score (1-100)"
  - "Energy use intensity (kBtu/sq ft)"
  - "Water use intensity (gal/sq ft)"
  - "Waste diversion rate (%)"
best_practices:
  - "Monthly utility data entry in ENERGY STAR Portfolio Manager"
  - "Peer group comparison within venue type"
  - "Normalize for event count and occupancy"
  - "Trend analysis over 3-5 year periods"
common_challenges:
  - "Normalization across venue types and sizes"
  - "Inconsistent utility metering infrastructure"
  - "Sub-metering for multi-tenant venues"
  - "Data availability for water and waste"
tags:
  - concept
  - venue-ops
  - sustainability-and-environmental
  - batch-02
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# Venue Sustainability Benchmarking

Sustainability benchmarking programs (ENERGY STAR Portfolio Manager, BOMA 360, Green Sports Alliance Play to Zero) enable venues to compare performance against peers on energy, water, waste, and carbon metrics, driving accountability and identifying improvement opportunities.

## Benchmarking Platforms

- **ENERGY STAR Portfolio Manager:** EPA's free tool — benchmarks energy and water for commercial buildings, including arenas and convention centres. Scores 1-100 against national peer group.
- **BOMA 360:** Performance-based designation covering operations, energy, environment, tenant relations
- **Play to Zero (Green Sports Alliance):** Sports-specific sustainability dashboard tracking energy, waste, water, and transport

## Key Metrics Tracked

- Energy use intensity (kBtu/sq ft/year or kBtu/event)
- Water use intensity (gallons/sq ft/year)
- Waste diversion rate (%)
- GHG emissions intensity (kgCO2e/sq ft or per event)

## Normalization Challenges

Venue benchmarking requires normalization for: climate zone, event frequency, event type mix, occupancy levels, and operating hours. A convention centre hosting 300 events/year cannot be directly compared to one hosting 100 without adjustment.

## Sources

- [[Source-0048-ENERGY-STAR-Commercial-Buildings]]
- [[Source-0053-BOMA-International-Resources]]
- [[Source-0036-Green-Sports-Alliance]]
