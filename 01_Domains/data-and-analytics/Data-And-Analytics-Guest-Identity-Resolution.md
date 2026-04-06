---
title: "Guest Identity Resolution"
note_type: concept
status: draft
created: 2026-04-06
updated: 2026-04-06
domain: data-and-analytics
tags:
  - concept
  - data-and-analytics
  - identity-resolution
  - master-data-management
description: "The process of determining that fragmented guest records across ticketing, POS, Wi-Fi, loyalty, and app systems belong to the same physical person, using deterministic and probabilistic matching approaches."
venue_types:
  - arena
  - stadium
  - convention-centre
  - performing-arts-centre
  - integrated-resort
  - fairground-exhibition
vef_alignment:
  - data-management-and-architecture
  - guest-experience
sources:
  - "[[Source-0334-Amperity-Seahawks-Fan-Identity-Resolution]]"
  - "[[Source-0335-Amperity-Identity-Resolution-Platform]]"
  - "[[Source-0336-Seahawks-Amperity-BusinessWire-2025]]"
  - "[[Source-0333-TicketFairy-Connected-Event-Tech-Ecosystem-2026]]"
  - "[[Source-0346-Salesforce-Fan-Engagement-CDP]]"
research_batch: dr-s20-r07-data-analytics
confidence: high
extraction_model: claude-opus-4-6
child_of: "[[Domain-Data-And-Analytics]]"
related_to:
  - "[[Data-And-Analytics-Venue-Data-Architecture]]"
  - "[[Data-And-Analytics-Guest-Personalization-CDP]]"
  - "[[Data-And-Analytics-Predictive-Analytics-Venue-AI]]"
  - "[[Data-And-Analytics-Data-Privacy-Governance]]"
venue_scale:
  - large
  - mega
delivery_model:
  - in-house
  - hybrid
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---
# Guest Identity Resolution

## Overview

Guest identity resolution is the process of determining that fragmented records across ticketing, POS, Wi-Fi, loyalty, and app systems belong to the same physical person. Without it, per-capita analytics are inaccurate, personalization is impossible, and churn models train on corrupted data ([[Source-0334-Amperity-Seahawks-Fan-Identity-Resolution]]). The problem is structural: a fan who buys a ticket through one platform, connects to Wi-Fi under an email alias, and makes a concession purchase with a card registered to a different name appears as three unrelated individuals unless an identity-resolution layer bridges the gap ([[Source-0333-TicketFairy-Connected-Event-Tech-Ecosystem-2026]]).

## Matching Methodologies

Two primary methodological approaches exist for resolving guest identities across venue systems ([[Source-0335-Amperity-Identity-Resolution-Platform]]):

**Deterministic matching** uses exact matches on email address, phone number, or unique identifier. This approach delivers high precision but misses more than 40% of cross-system associations when fans use different contact details across platforms ([[Source-0335-Amperity-Identity-Resolution-Platform]]).

**Probabilistic / AI-assisted matching** uses ML models combining deterministic signals with behavioral and contextual similarity — purchase timing, geographic proximity, name variants. Amperity's multi-patented identity resolution platform, deployed by the Seattle Seahawks, achieved a 61.5% deduplication rate across all fan records and uncovered 5,000 previously unidentified fans, reducing audience segmentation time from days to minutes ([[Source-0336-Seahawks-Amperity-BusinessWire-2025]], [[Source-0334-Amperity-Seahawks-Fan-Identity-Resolution]]).

## Documented Deployments

**Seattle Seahawks / Amperity (2025).** Unified fan data across ticketing, retail, digital, and engagement systems into a single identity graph. Key results: 61.5% deduplication rate; 5,000 previously unidentified fans discovered; segmentation time reduced from days to minutes; seamless integration with Snowflake for data warehouse sharing and near-real-time profile updates ([[Source-0336-Seahawks-Amperity-BusinessWire-2025]]).

**Salesforce Data Cloud.** Calculates composite insights including customer lifetime value scores and fan engagement scores by combining media consumption, ticket purchases, and merchandise purchases. The identity resolution function within Salesforce Data Cloud constructs unified profiles from raw behavioral data ingested across all touchpoints ([[Source-0346-Salesforce-Fan-Engagement-CDP]]).

## Convention Centre vs. Team-Operated Venue Considerations

For venues as distinct from team-operated venues, the identity resolution challenge is amplified because the operator holds different data relationships than the tenants. A convention centre knows which companies booked meeting rooms and what catering was ordered, but the exhibitor companies hold the attendee-level CRM data. Venue master data management must account for these split custody arrangements, and data-sharing agreements should be specified in booking contracts ([[Source-0333-TicketFairy-Connected-Event-Tech-Ecosystem-2026]]).

## Data Quality Dependencies

Effective identity resolution depends on upstream data quality across all contributing systems. Inconsistent data entry practices at individual touchpoints — misspelled names, formatting variations in phone numbers, use of personal versus work email — compound the matching challenge. The transition from deterministic to probabilistic matching is driven by recognition that real-world data is inherently messy; rule-based exact matching reaches a ceiling of accuracy that only ML-based approaches can overcome ([[Source-0335-Amperity-Identity-Resolution-Platform]]).

## Privacy and Consent Implications

Identity resolution inherently involves combining personal information from multiple sources, which raises data privacy obligations under GDPR, PIPEDA, and CCPA. Venues deploying identity resolution must ensure that consent collected at each individual touchpoint covers the downstream unification and use of the resulting unified profile. The line between "improving service" and "building surveillance profiles" is drawn by the specificity of consent obtained at the point of collection.

## Related Concepts

- [[Data-And-Analytics-Venue-Data-Architecture]] — upstream integration architecture that feeds identity resolution
- [[Data-And-Analytics-Guest-Personalization-CDP]] — downstream personalization that depends on resolved identities
- [[Data-And-Analytics-Predictive-Analytics-Venue-AI]] — churn and propensity models that require clean identity data
- [[Data-And-Analytics-Data-Privacy-Governance]] — consent and compliance frameworks governing identity data
