---
title: "Event-Driven HVAC and Ventilation Control"
note_type: concept
domain: "facilities-and-building-systems"
status: draft
created: 2026-04-04
updated: 2026-04-04
description: "BMS platforms schedule HVAC operations based on event timetables and real-time occupancy, using pre-cooling/pre-heating, demand-controlled ventilation (DCV), event-based setpoints, and post-event setback to minimize energy while maintaining comfort and indoor air quality."
venue_types:
  - convention-centre
  - arena
  - stadium
  - performing-arts-centre
vef_alignment:
  - operational-efficiency-productivity-creativity
  - systems-processes-clarity-of-roles
confidence: high
sources:
  - "[[Source-0032-ASHRAE-62-1-Ventilation-Standard]]"
  - "[[Source-0033-ASHRAE-90-1-Energy-Standard]]"
  - "[[Source-0052-Events2HVAC-Integration]]"
research_batch: v2-prompt-02-facilities
child_of: "[[Domain-Facilities-And-Building-Systems]]"
related_to:
  - "[[Facilities-And-Building-Systems-BMS-Platform-Architecture]]"
  - "[[Facilities-And-Building-Systems-Indoor-Air-Quality-Filtration]]"
  - "[[Facilities-And-Building-Systems-Space-Management-Scheduling]]"
governed_by:
  - "[[Source-0032-ASHRAE-62-1-Ventilation-Standard]]"
  - "[[Source-0033-ASHRAE-90-1-Energy-Standard]]"
supported_by:
  - "[[Source-0052-Events2HVAC-Integration]]"
key_metrics:
  - "Energy savings from DCV (10-30%)"
  - "CO2 levels during events"
  - "Pre-cool/pre-heat lead times"
  - "Comfort compliance rates"
best_practices:
  - "Pre-cooling calculated from thermal load and outdoor conditions"
  - "CO2-sensor-driven DCV per ASHRAE 62.1"
  - "Automated post-event setback via calendar integration"
  - "Events2HVAC middleware for scheduling-to-BMS bridge"
common_challenges:
  - "Balancing energy savings against comfort at partial loads"
  - "Variable schedules in convention centres with simultaneous events"
  - "Acoustic constraints in performing arts centres"
tags:
  - concept
  - venue-ops
  - facilities-and-building-systems
  - batch-02
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# Event-Driven HVAC and Ventilation Control

BMS platforms schedule HVAC operations based on event timetables and real-time occupancy, using pre-cooling/pre-heating, demand-controlled ventilation (DCV), event-based setpoints, and post-event setback to minimize energy while maintaining comfort and indoor air quality.

## Core Strategies

- **Pre-cooling/pre-heating:** Calculate lead times based on thermal mass, outdoor conditions, and expected occupancy
- **Demand-controlled ventilation:** CO2 sensors adjust fresh air intake in real time — ASHRAE 62.1-2022 mandates DCV for spaces >500 sq ft with design occupancy of 25+ people per 1,000 sq ft
- **Event-based setpoints:** Different temperature/humidity targets for trade shows, concerts, ice events, and banquets
- **Post-event setback:** Automated reduction to minimum levels after event clearance

## Integration Architecture

Middleware platforms like Events2HVAC bridge venue EMS (Momentus, Ungerboeck) to BMS (Metasys, Desigo CC), automating HVAC staging based on event type, expected attendance, and room configuration.

## Energy Impact

DCV alone achieves 10-30% energy reduction over constant-air-volume baselines. Combined with event scheduling integration, venues report 20-40% HVAC energy savings.

## Sources

- [[Source-0032-ASHRAE-62-1-Ventilation-Standard]]
- [[Source-0033-ASHRAE-90-1-Energy-Standard]]
- [[Source-0052-Events2HVAC-Integration]]
