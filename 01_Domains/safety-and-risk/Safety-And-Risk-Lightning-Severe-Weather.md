---
title: "Lightning Detection and Severe Weather Policies"
note_type: concept
domain: "safety-and-risk"
status: draft
created: 2026-04-04
updated: 2026-04-06
description: "Venue weather safety protocols covering lightning detection systems, severe weather decision trees, and weather-specific evacuation and shelter-in-place procedures."
venue_types:
  - stadium
  - amphitheatre
  - fairground-exhibition
  - all
vef_alignment:
  - operational-efficiency-productivity-creativity
confidence: high
sources:
  - "[[Source-0012-NWS-Lightning-Safety-Toolkit]]"
  - "[[Source-0305-NWS-Lightning-Safety-Toolkit-Outdoor-Venues]]"
  - "[[Source-0306-FEMA-P-361-Safe-Rooms-Tornadoes-Hurricanes]]"
  - "[[Source-0307-ICC-500-2020-Storm-Shelter-Standard]]"
  - "[[Source-0308-NFPA-780-2023-Lightning-Protection-Systems]]"
  - "[[Source-0309-Environment-Canada-Lightning-Safety-Venues]]"
research_batch: v2-prompt-03-safety-crowd
child_of: "[[Domain-Safety-And-Risk]]"
related_to:
  - "[[Safety-And-Risk-Emergency-Action-Plans]]"
  - "[[Safety-And-Risk-Heat-Illness-Protocols]]"
tags:
  - concept
  - venue-ops
  - safety-and-risk
  - batch-01
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# Lightning Detection and Severe Weather Policies

Venue weather safety protocols covering lightning detection systems, severe weather decision trees, and weather-specific evacuation and shelter-in-place procedures.

## Overview

Severe weather — particularly lightning — poses significant risk to outdoor venues and events. The National Weather Service (NWS) provides the foundational framework for lightning safety at outdoor venues.

## Lightning Detection

### NWS Resumption Criteria (Corrected)

The NWS Lightning Safety Toolkit for Outdoor Venues establishes two operationally distinct resumption criteria — **not** a "15/12/8-mile" three-phase system ([[Source-0305-NWS-Lightning-Safety-Toolkit-Outdoor-Venues]]):

| Scenario | Resumption Criterion |
|---|---|
| Venue with professional meteorologist + real-time lightning data | Lightning has moved beyond **8 miles** from venue; storm motion taking lightning away; threat of new lightning within 8 miles has ended |
| Venue without professional meteorologist / real-time data | Wait **30 minutes** after last observed thunder or lightning before resuming |

**Correction note:** The "15/12/8-mile" three-radius system (15 miles monitoring, 12 miles preparation, 8 miles mandatory evacuation) used in some commercial and sports safety protocols does not appear verbatim in official NWS publications. This framework likely derives from commercial provider documentation (Perry Weather, Earth Networks) or sports governing body protocols layered on NWS base guidance ([[Source-0305-NWS-Lightning-Safety-Toolkit-Outdoor-Venues]]).

The "30-30 Rule" is widely cited in safety guidance: seek shelter when the lightning flash-to-thunder count is 30 seconds or less (lightning within approximately 6 miles); wait 30 minutes after the last sound of thunder before returning to outdoor activities ([[Source-0305-NWS-Lightning-Safety-Toolkit-Outdoor-Venues]]).

NWS notes that "a significant lightning threat extends outward from the base of a thunderstorm cloud about 6 to 10 miles," and that organized events should account for the time required to evacuate all patrons to safe shelter before beginning evacuation procedures ([[Source-0305-NWS-Lightning-Safety-Toolkit-Outdoor-Venues]]).

Canada's guidance (Environment and Climate Change Canada) is consistent: "Activities do not resume until at least 30 minutes after the last rumble of thunder" ([[Source-0309-Environment-Canada-Lightning-Safety-Venues]]).

### NWS StormReady Recognition Program

The NWS StormReady Recognition Program is a voluntary certification for outdoor venues including sporting arenas, concert venues, water parks, raceways, and amusement parks. Requirements span four categories ([[Source-0305-NWS-Lightning-Safety-Toolkit-Outdoor-Venues]]):

| Category | Requirement |
|---|---|
| **Information Reception** | Locally-run lightning detection system OR commercial notification subscription; NOAA Weather Radio on location |
| **Decision Support** | Written lightning safety plan; contact information for emergency management and weather service provider |
| **Public Notification** | Multiple patron notification methods: outdoor warning sirens, PA system, TV/radio, text/email alerts, social media, staff announcements |
| **Protection Program** | Means to shelter patrons; written emergency operations safety plan; shelter location signage |

Certification requires a site visit by the local StormReady Advisory Board, with recertification every 3 years ([[Source-0305-NWS-Lightning-Safety-Toolkit-Outdoor-Venues]]).

### Technology
Commercial lightning detection providers include ([[Source-0305-NWS-Lightning-Safety-Toolkit-Outdoor-Venues]]):

| Provider | Network | Key Specifications |
|---|---|---|
| **Vaisala / NLDN** | National Lightning Detection Network | 100+ ground-based sensors; cloud-to-ground detection; ~84m accuracy; 40+ years continuous operation |
| **Perry Weather** | Uses NLDN data | Real-time alerts in <20 seconds; customizable distance alerts; on-site WBGT monitoring |
| **Earth Networks** | Total Lightning Network | ~100m accuracy; detects in-cloud and cloud-to-ground lightning |
| **DTN** | Commercial weather service | Lightning detection within broader meteorological intelligence services |

### NFPA 780 — Lightning Protection Systems

NFPA 780 (2023 Edition) provides requirements for lightning protection system installation for structures including assembly venues (arenas, amphitheatres, grandstands) ([[Source-0308-NFPA-780-2023-Lightning-Protection-Systems]]). The standard uses the Rolling Sphere Method and Protection Angle Method to determine coverage zones and integrates with NFPA 70 (NEC) grounding requirements. NFPA 780 is not mandatory unless adopted by the local AHJ; it governs design and installation where a system is installed but does not require installation ([[Source-0308-NFPA-780-2023-Lightning-Protection-Systems]]).

## Other Severe Weather

- **Tornado:** Watch/Warning/Post-storm phases; shelter-in-place in lowest interior spaces
- **FEMA P-361** (3rd Edition, 2015) provides safe room guidance with 250 mph design wind speed. Guideline document, not enforceable unless FEMA grant funds are used ([[Source-0306-FEMA-P-361-Safe-Rooms-Tornadoes-Hurricanes]])
- **ICC 500-2020** is the enforceable ANSI-approved standard for storm shelters, referenced in IBC 2021. IBC Section 423 does **not** mandate storm shelters for Group A assembly occupancies (arenas, stadiums, concert venues) ([[Source-0307-ICC-500-2020-Storm-Shelter-Standard]])
- **High winds:** Threshold-based protocols for temporary structures, rigging, and signage
- **Earthquake:** Drop/Cover/Hold On; 60-second debris settling count before evacuation; post-earthquake structural assessment

## Venue Type Differentiation

Protocols differ significantly between outdoor stadiums (full weather exposure), indoor arenas (structural integrity focus), and convention centres (limited weather exposure, focus on roof loading and power systems).

## Sources

- [[Source-0012-NWS-Lightning-Safety-Toolkit]]
- [[Source-0305-NWS-Lightning-Safety-Toolkit-Outdoor-Venues]]
- [[Source-0306-FEMA-P-361-Safe-Rooms-Tornadoes-Hurricanes]]
- [[Source-0307-ICC-500-2020-Storm-Shelter-Standard]]
- [[Source-0308-NFPA-780-2023-Lightning-Protection-Systems]]
- [[Source-0309-Environment-Canada-Lightning-Safety-Venues]]
