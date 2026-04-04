---
title: "Predictive and Condition-Based Maintenance"
note_type: concept
domain: "facilities-and-building-systems"
status: draft
created: 2026-04-04
updated: 2026-04-04
description: "Predictive maintenance uses IoT sensors, vibration analysis, thermal imaging, and AI/ML algorithms to forecast equipment failures before they occur, shifting venues from reactive or time-based maintenance to condition-based strategies that reduce downtime and extend asset life."
venue_types:
  - convention-centre
  - arena
  - stadium
  - performing-arts-centre
  - integrated-resort
vef_alignment:
  - operational-efficiency-productivity-creativity
  - ai-and-digital-transformation
  - data-management-and-architecture
confidence: high
sources:
  - "[[Source-0037-IBM-Maximo-Asset-Management]]"
  - "[[Source-0046-ASHRAE-180-Inspection-Maintenance]]"
research_batch: v2-prompt-02-facilities
child_of: "[[Domain-Facilities-And-Building-Systems]]"
related_to:
  - "[[Facilities-And-Building-Systems-CMMS-Preventive-Maintenance]]"
  - "[[Facilities-And-Building-Systems-BMS-Platform-Architecture]]"
  - "[[Facilities-And-Building-Systems-BIM-Digital-Twin]]"
governed_by:
  - "[[Source-0046-ASHRAE-180-Inspection-Maintenance]]"
supported_by:
  - "[[Source-0037-IBM-Maximo-Asset-Management]]"
key_metrics:
  - "Mean time between failures (MTBF)"
  - "Unplanned downtime hours"
  - "Maintenance cost per sq ft"
  - "Predicted vs actual failure rate"
best_practices:
  - "Vibration sensors on rotating equipment"
  - "Thermal imaging for electrical distribution panels"
  - "AI-driven anomaly detection integrated with CMMS"
  - "Condition-based oil analysis for refrigeration compressors"
common_challenges:
  - "Sensor deployment cost for existing facilities"
  - "Data quality and false positive management"
  - "Staff training on condition monitoring interpretation"
tags:
  - concept
  - venue-ops
  - facilities-and-building-systems
  - batch-02
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# Predictive and Condition-Based Maintenance

Predictive maintenance uses IoT sensors, vibration analysis, thermal imaging, and AI/ML algorithms to forecast equipment failures before they occur, shifting venues from reactive or time-based maintenance to condition-based strategies that reduce downtime and extend asset life.

## Maturity Levels

1. **Reactive:** Fix when broken (highest cost, maximum downtime)
2. **Preventive:** Time-based schedules per ASHRAE 180 (baseline standard)
3. **Condition-based:** Intervene when sensor data indicates degradation
4. **Predictive:** AI/ML forecasts failure windows from historical and real-time data

## Technology Stack

- **Vibration analysis:** Accelerometers on AHUs, pumps, chillers — detects bearing wear, imbalance, misalignment
- **Thermal imaging:** Identifies hot spots in electrical panels, overloaded circuits
- **IoT sensors:** Temperature, humidity, pressure, flow rate on critical systems
- **CMMS integration:** IBM Maximo, Fiix, Limble — AI-generated work orders from sensor alerts

## Venue-Specific Applications

Arena ice plants, convention centre AHU arrays, stadium electrical distribution — all benefit from continuous monitoring given the catastrophic cost of mid-event failures.

## Sources

- [[Source-0037-IBM-Maximo-Asset-Management]]
- [[Source-0046-ASHRAE-180-Inspection-Maintenance]]
