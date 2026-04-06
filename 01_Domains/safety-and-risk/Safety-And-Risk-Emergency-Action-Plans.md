---
title: "Emergency Action Plans (EAPs)"
note_type: concept
domain: "safety-and-risk"
status: draft
created: 2026-04-04
updated: 2026-04-06
description: "Written, event-specific documents governing venue response to unplanned events, covering hazard protocols, ICS integration, evacuation maps, shelter-in-place procedures, communication hierarchies, and designated roles."
venue_types:
  - all
vef_alignment:
  - operational-efficiency-productivity-creativity
  - systems-processes-clarity-of-roles
confidence: high
sources:
  - "[[Source-0007-IAVM-Venue-Safety-Security-Committee]]"
  - "[[Source-0003-NFPA-101-Life-Safety-Code-2024]]"
  - "[[Source-0028-Calgary-Indoor-Fire-Requirements]]"
  - "[[Source-0299-Alberta-OHS-Code-Part-7-Emergency-Preparedness]]"
  - "[[Source-0306-FEMA-P-361-Safe-Rooms-Tornadoes-Hurricanes]]"
  - "[[Source-0307-ICC-500-2020-Storm-Shelter-Standard]]"
research_batch: v2-prompt-03-safety-crowd
child_of: "[[Domain-Safety-And-Risk]]"
related_to:
  - "[[Safety-And-Risk-Incident-Command-System]]"
  - "[[Safety-And-Risk-Tabletop-Exercises]]"
  - "[[Safety-And-Risk-Crisis-Communication-Protocols]]"
  - "[[Safety-And-Risk-Business-Continuity-Planning]]"
  - "[[Safety-And-Risk-GBAC-STAR-Accreditation]]"
  - "[[Safety-And-Risk-Fire-Watch-Protocols]]"
  - "[[Safety-And-Risk-Life-Safety-Evaluation]]"
  - "[[Safety-And-Risk-AED-Programs]]"
  - "[[Crowd-Management-Crowd-Manager-Staffing]]"
governed_by:
  - "[[Source-0003-NFPA-101-Life-Safety-Code-2024]]"
tags:
  - concept
  - venue-ops
  - safety-and-risk
  - batch-01
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# Emergency Action Plans (EAPs)

Written, event-specific documents governing venue response to unplanned events, covering hazard protocols, ICS integration, evacuation maps, shelter-in-place procedures, communication hierarchies, and designated roles.

## Overview

Emergency Action Plans (EAPs) are foundational safety documents required for all assembly occupancies. The 2024 edition of NFPA 101 expanded EAP requirements to explicitly address security features alongside traditional fire-safety procedures.

## Key Components

- Purpose statement and scope of the plan
- Business Continuity and Recovery (BCR) team identification
- Procedures organized by emergency type (fire, severe weather, active threat, medical, utility failure)
- Evacuation routes with maps for each venue zone
- Communication trees with designated spokespersons
- Drill cadence and exercise schedule
- Post-incident review process

## Regulatory Requirements

- NFPA 101 requires EAPs for assembly occupancies
- OSHA General Duty Clause (Section 5(a)(1)) mandates employers provide safe workplaces
- Calgary Fire Department requires 30-day advance permit packages including EAPs for indoor special events
- Alberta OHS Code Part 7 requires emergency response plans

## Alberta OHS Code Part 7 — Detailed Requirements

Alberta's Occupational Health and Safety Code, Part 7 (ss. 115-118), provides the most prescriptive provincial emergency response planning framework in Canada ([[Source-0299-Alberta-OHS-Code-Part-7-Emergency-Preparedness]]).

**Section 115** requires employers to establish an ERP for any emergency requiring rescue or evacuation, with mandatory worker involvement in the planning process and a requirement to keep the plan current ([[Source-0299-Alberta-OHS-Code-Part-7-Emergency-Preparedness]]).

**Section 116** specifies a 10-element mandatory ERP content list ([[Source-0299-Alberta-OHS-Code-Part-7-Emergency-Preparedness]]):
1. Identification of potential emergencies
2. Procedures for identified emergencies
3. Location and operation of emergency equipment and PPE
4. Training requirements
5. Location and use of emergency facilities
6. Fire protection requirements
7. Alarm and emergency communication requirements
8. First aid services required
9. Procedures for rescue and evacuation
10. Designated rescue and evacuation workers

**Section 117(1-3)** requires training that includes exercises simulating potential emergencies identified in the ERP ([[Source-0299-Alberta-OHS-Code-Part-7-Emergency-Preparedness]]).

Critically, Part 7 does not specify a minimum occupant threshold for mandatory ERP development. The trigger is any emergency "requiring rescue or evacuation," which applies to all public assembly occupancies ([[Source-0299-Alberta-OHS-Code-Part-7-Emergency-Preparedness]]).

## Multi-Province ERP Comparison

Canadian provincial and federal OHS requirements for emergency response planning vary significantly ([[Source-0299-Alberta-OHS-Code-Part-7-Emergency-Preparedness]]):

| Jurisdiction | Governing Regulation | Key ERP Requirements | Assembly-Specific Provisions |
|---|---|---|---|
| **Alberta** | OHS Code Part 7, ss. 115-118 | ERP required for any rescue/evacuation risk; worker involvement; 10-element content list | No specific assembly threshold; applies universally |
| **British Columbia** | WorkSafeBC OHS Reg Part 4, ss. 4.13-4.14 | Risk assessment; written rescue/evacuation procedures; annual drills | Written procedures required where persons need physical assistance (s. 4.13(3)(f)) |
| **Federal** | Canada Labour Code SOR/86-304, ss. 17.4-17.10 | Written evacuation plan if >50 employees; annual drills; 24-hr advance notice to fire department | >50-employee threshold for written plan |
| **Ontario** | OHSA; Ontario Reg 851 | General duty under OHSA; no assembly-specific OHS regulation | No codified venue-emergency-planning section comparable to Alberta's Part 7 |

Ontario has the largest regulatory gap among major provinces: no assembly-venue-specific OHS regulation comparable to Alberta's Part 7 exists. Ontario venues rely on the general duty clause of the OHSA, the Fire Protection and Prevention Act, and the Ontario Building Code ([[Source-0299-Alberta-OHS-Code-Part-7-Emergency-Preparedness]]).

## Storm Shelter Standards

**FEMA P-361** (3rd Edition, 2015) provides safe room guidance for tornadoes and hurricanes with a 250 mph design wind speed and 15-lb 2x4 missile impact resistance at 100 mph. FEMA P-361 is a guideline document (not enforceable) unless FEMA grant funds are used for construction ([[Source-0306-FEMA-P-361-Safe-Rooms-Tornadoes-Hurricanes]]).

**ICC 500-2020** is the enforceable ANSI-approved standard for storm shelters, referenced in IBC 2021. IBC Section 423 mandates ICC 500 compliance for Group E occupancies (K-12 schools, occupant load >=50), 911 call stations, emergency operations centers, and fire/rescue/police stations. However, IBC Section 423 does **not** currently mandate storm shelters for Group A assembly occupancies (arenas, stadiums, concert venues) ([[Source-0307-ICC-500-2020-Storm-Shelter-Standard]]). ICC 500 Section 108 requires the owner to submit a written statement of responsibility and emergency preparedness plan to the AHJ during the permit process ([[Source-0307-ICC-500-2020-Storm-Shelter-Standard]]).

## Venue Type Variations

EAP complexity scales with venue size and event type. A convention centre hosting a trade show requires different protocols than a stadium hosting a concert. Multi-day festivals require the most comprehensive plans due to extended exposure periods and camping accommodations.

## Sources

- [[Source-0007-IAVM-Venue-Safety-Security-Committee]]
- [[Source-0003-NFPA-101-Life-Safety-Code-2024]]
- [[Source-0028-Calgary-Indoor-Fire-Requirements]]
- [[Source-0299-Alberta-OHS-Code-Part-7-Emergency-Preparedness]]
- [[Source-0306-FEMA-P-361-Safe-Rooms-Tornadoes-Hurricanes]]
- [[Source-0307-ICC-500-2020-Storm-Shelter-Standard]]
