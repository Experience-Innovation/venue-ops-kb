---
title: "Guest Personalization and Customer Data Platforms"
note_type: concept
status: draft
created: 2026-04-06
updated: 2026-04-06
domain: data-and-analytics
tags:
  - concept
  - data-and-analytics
  - personalization
  - cdp
  - loyalty
description: "Customer data platforms for venue operations, guest personalization at scale through mobile apps, in-venue digital signage, and post-event marketing, plus loyalty and rewards program management and ROI measurement."
venue_types:
  - arena
  - stadium
  - convention-centre
  - performing-arts-centre
  - integrated-resort
  - theme-park
vef_alignment:
  - data-management-and-architecture
  - guest-experience
  - ai-and-digital-transformation
sources:
  - "[[Source-0346-Salesforce-Fan-Engagement-CDP]]"
  - "[[Source-0334-Amperity-Seahawks-Fan-Identity-Resolution]]"
  - "[[Source-0336-Seahawks-Amperity-BusinessWire-2025]]"
  - "[[Source-0333-TicketFairy-Connected-Event-Tech-Ecosystem-2026]]"
research_batch: dr-s20-r07-data-analytics
confidence: high
extraction_model: claude-opus-4-6
child_of: "[[Domain-Data-And-Analytics]]"
related_to:
  - "[[Data-And-Analytics-Guest-Identity-Resolution]]"
  - "[[Data-And-Analytics-Predictive-Analytics-Venue-AI]]"
  - "[[Data-And-Analytics-Data-Privacy-Governance]]"
  - "[[Data-And-Analytics-BI-Dashboards-KPI-Frameworks]]"
  - "[[Guest-Experience-Wayfinding-Signage]]"
venue_scale:
  - large
  - mega
delivery_model:
  - in-house
  - hybrid
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---
# Guest Personalization and Customer Data Platforms

## Overview

A Customer Data Platform (CDP) differs from a CRM in that it ingests raw behavioral data from all touchpoints and applies identity resolution to construct a unified profile, rather than relying on manually entered or imported structured records. CDPs enable venue operators to activate personalization at scale by combining data from ticketing, POS, Wi-Fi, loyalty, and app systems into a single actionable view of each guest ([[Source-0346-Salesforce-Fan-Engagement-CDP]]).

## Guest Data Collection Touchpoints

The guest data collection funnel at a modern venue spans multiple interactions across pre-event, in-event, and post-event stages ([[Source-0333-TicketFairy-Connected-Event-Tech-Ecosystem-2026]]):

1. **Ticket purchase:** Name, email, payment method, seat selection, ticket type, promotional code used
2. **Mobile app download / account creation:** Device type, notification preferences, linked payment methods
3. **Wi-Fi authentication:** Email or social login, device fingerprint, dwell time and location within venue
4. **Loyalty / rewards enrollment:** Full profile data, program tier, points balance, linked ticketing account
5. **POS transaction:** Item, quantity, price, location, tender type, timestamp, linked to loyalty card
6. **Beacon / sensor proximity:** Dwell time near specific retail or F&B locations, wayfinding query patterns
7. **Access control scan:** Gate entry timestamp, section accessed, re-entry count
8. **Post-event survey:** Structured ratings, open-text feedback
9. **Social media interaction:** Organic mentions, contest participation, hashtag engagement

The integrated picture of a single attendee's journey from ticket purchase through post-event email open is the input to personalization engines and the foundation for lifetime value modeling ([[Source-0333-TicketFairy-Connected-Event-Tech-Ecosystem-2026]]).

## CDP Platforms for Venue Operations

**Salesforce Data Cloud (formerly Genie CDP).** Calculates composite insights including customer lifetime value scores and fan engagement scores combining media consumption, ticket purchases, and merchandise purchases. Powers predictive models for upgrade receptiveness, churn risk, and satisfaction forecasts. Integrates natively with Marketing Cloud for triggered communications and Commerce Cloud for digital merchandise ([[Source-0346-Salesforce-Fan-Engagement-CDP]]).

**Amperity Customer Data Cloud.** Purpose-built identity resolution for consumer brands, with documented deployments in professional sports including the Seattle Seahawks, Sounders, Mariners, and Trail Blazers. The multi-patented AI/ML identity resolution distinguishes it from deterministic tools. Integrates with Snowflake for data warehouse sharing and supports near-real-time profile updates for in-event activation ([[Source-0336-Seahawks-Amperity-BusinessWire-2025]], [[Source-0334-Amperity-Seahawks-Fan-Identity-Resolution]]).

**Microsoft Dynamics 365 with Azure.** For venues in the Microsoft ecosystem, Dynamics 365 Customer Insights provides CDP-equivalent identity resolution and segmentation capabilities, leveraging Azure Machine Learning for predictive scoring and Power BI for dashboard visualization.

## Personalization Activation Channels

With a unified fan profile established, venues activate personalization through three primary channels:

**Mobile app push notifications.** Event-day notifications personalized by seat location, loyalty status, and purchase history. YinzCam supports content-feed customization, notification preference control, and fan profile hubs for season-ticket members at venues including SoFi Stadium (LA Chargers) and UBS Arena (NY Islanders).

**In-venue digital signage.** Dynamic content delivery at concession menus, wayfinding displays, and concourse screens personalized by audience segment, event type, and real-time inventory levels.

**Post-event marketing.** Triggered email and SMS sequences based on in-venue behavior, attendance patterns, and propensity models. Salesforce Marketing Cloud supports journeys that adapt messaging based on whether a fan attended, what they purchased, and how they rated the experience ([[Source-0346-Salesforce-Fan-Engagement-CDP]]).

## Loyalty and Rewards Programs

Venue loyalty programs structure engagement into tiered models (silver / gold / platinum) with point accrual for ticket purchases, in-venue spend, app engagement, and community activities. ROI measurement typically tracks incremental per-cap spending by members vs. non-members, tier-upgrade rates, renewal rate differentials for loyalty vs. non-loyalty season ticket holders, and program-attributed conversion from single-game to multi-game or season tickets ([[Source-0333-TicketFairy-Connected-Event-Tech-Ecosystem-2026]]).

## Venue-Operator vs. Tenant Data Distinction

Venue-operator analytics cover building performance, total attendance, aggregate per-capita revenue, changeover efficiency, and overall NPS. Tenant/promoter analytics cover team-specific CRM, show-specific demographics, and team-branded app engagement. Shared/negotiated data includes attendee ticketing data (ownership varies by contract), post-event survey data, and per-event F&B performance for promoter settlement. Convention centres have simpler structures where the booking organization typically owns attendee CRM data while the venue owns facility operations data.

## Related Concepts

- [[Data-And-Analytics-Guest-Identity-Resolution]] — the identity layer that CDPs depend on
- [[Data-And-Analytics-Predictive-Analytics-Venue-AI]] — predictive models activated through personalization
- [[Data-And-Analytics-Data-Privacy-Governance]] — consent requirements governing personalization
- [[Data-And-Analytics-BI-Dashboards-KPI-Frameworks]] — metrics measuring personalization effectiveness
- [[Guest-Experience-Wayfinding-Signage]] — physical signage channel for personalized content delivery
