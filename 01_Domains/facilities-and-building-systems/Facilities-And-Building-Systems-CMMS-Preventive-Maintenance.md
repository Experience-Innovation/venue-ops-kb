---
title: "CMMS and Preventive Maintenance Programs"
note_type: concept
domain: "facilities-and-building-systems"
status: draft
created: 2026-04-04
updated: 2026-04-04
description: "Computerized Maintenance Management Systems (CMMS) provide structured work order management, PM scheduling, asset tracking, and compliance documentation for large venue facilities, with platforms ranging from enterprise (IBM Maximo) to mid-market (Limble, UpKeep, Fiix)."
venue_types:
  - all
vef_alignment:
  - operational-efficiency-productivity-creativity
  - systems-processes-clarity-of-roles
confidence: high
sources:
  - "[[Source-0037-IBM-Maximo-Asset-Management]]"
  - "[[Source-0046-ASHRAE-180-Inspection-Maintenance]]"
  - "[[Source-0045-IFMA-Facility-Management-Resources]]"
research_batch: v2-prompt-02-facilities
child_of: "[[Domain-Facilities-And-Building-Systems]]"
related_to:
  - "[[Facilities-And-Building-Systems-Predictive-Condition-Based-Maintenance]]"
  - "[[Facilities-And-Building-Systems-Capital-Planning-Lifecycle-Funding]]"
governed_by:
  - "[[Source-0046-ASHRAE-180-Inspection-Maintenance]]"
supported_by:
  - "[[Source-0037-IBM-Maximo-Asset-Management]]"
key_metrics:
  - "PM completion rate"
  - "Work order backlog"
  - "Mean time to repair"
  - "Maintenance cost per sq ft per year"
best_practices:
  - "ASHRAE 180 as baseline PM cadence"
  - "Mobile-first CMMS for field technicians"
  - "Integration with BMS alarm feeds for auto-generated work orders"
  - "Asset criticality ranking for scheduling"
common_challenges:
  - "Data entry discipline across large maintenance teams"
  - "Integration between CMMS and legacy BMS"
  - "Scheduling PM during limited venue dark periods"
tags:
  - concept
  - venue-ops
  - facilities-and-building-systems
  - batch-02
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# CMMS and Preventive Maintenance Programs

Computerized Maintenance Management Systems (CMMS) provide structured work order management, PM scheduling, asset tracking, and compliance documentation for large venue facilities, with platforms ranging from enterprise (IBM Maximo) to mid-market (Limble, UpKeep, Fiix).

## Platform Tiers

- **Enterprise:** IBM Maximo, IBM TRIRIGA — 10,000+ assets, predictive analytics, EAM integration
- **Mid-market:** Fiix, Limble, UpKeep — cloud-native, mobile-first, rapid deployment
- **Venue-specific:** Momentus facilities module — integrated with event scheduling
- **Light-duty:** Snapfix, ClickMaint — photo-based work orders, low training overhead

## PM Program Structure

ASHRAE 180 establishes the baseline inspection and maintenance cadence for HVAC systems. Large venues extend this to electrical distribution, plumbing, fire suppression, building envelope, and grounds.

## Venue-Specific Challenges

The primary constraint is access — venues operate on tight event schedules with limited dark periods for maintenance. Asset criticality ranking ensures life-safety systems get priority scheduling.

## Sources

- [[Source-0037-IBM-Maximo-Asset-Management]]
- [[Source-0046-ASHRAE-180-Inspection-Maintenance]]
- [[Source-0045-IFMA-Facility-Management-Resources]]
