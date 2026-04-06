---
title: "Event Booking Lifecycle"
note_type: concept
status: draft
created: 2026-04-06
updated: 2026-04-06
domain: booking-and-sales
tags:
  - concept
  - booking-and-sales
description: "The structured sales pipeline that transforms initial venue inquiries into contracted, revenue-generating events, encompassing stages from opportunity capture through post-event settlement and lost-business tracking."
venue_types:
  - all
vef_alignment:
  - operational-efficiency-productivity-creativity
  - systems-processes-clarity-of-roles
sources:
  - "[[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]]"
  - "[[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]]"
  - "[[Source-0312-Northstar-Planning-Citywide-Convention]]"
  - "[[Source-0314-Cal-Performances-What-Is-Presenting]]"
  - "[[Source-0315-Momentus-Technologies-Venue-Management]]"
research_batch: dr-s20-r06-booking-ticketing
confidence: high
extraction_model: claude-opus-4-6
child_of: "[[Domain-Booking-And-Sales]]"
related_to:
  - "[[Booking-And-Sales-Venue-Booking-KPIs]]"
  - "[[Booking-And-Sales-Event-Contracting-License-Agreements]]"
  - "[[Booking-And-Sales-Convention-Centre-Booking-Operations]]"
  - "[[Booking-And-Sales-Multi-Use-Venue-Scheduling]]"
key_metrics:
  - "Opportunity Conversion Ratio"
  - "Lead Time to Booking"
  - "Booking Conversion Rate"
venue_scale:
  - small
  - medium
  - large
  - mega
delivery_model:
  - in-house
  - hybrid
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---
# Event Booking Lifecycle

The event booking lifecycle is the structured sales pipeline that transforms initial venue inquiries into contracted, revenue-generating events. The pipeline encompasses clearly defined stages from opportunity capture through post-event settlement, with each stage requiring specific operational actions and documentation.

## Pipeline Stages

The IAVM Convention Center Performance Reporting Framework defines the standard booking pipeline stages that apply, with venue-type variations, across all public assembly venues [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]]:

**Opportunity** is the initial stage, triggered when any inquiry for a venue-hosted event type is captured from a call, web form, trade show, or CVB referral. Every tracked opportunity must eventually resolve as either a successful booking or a documented lost event [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

**Proposal (Tentative)** occurs when a written offer detailing dates, spaces, and services is issued to the prospective client. Space is tentatively held during this stage. Multiple revisions of the proposal count as a single proposal for tracking purposes [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

**Definite** status is reached when the booking is confirmed in writing by authorized agents of both parties, typically through a letter of intent or letter of agreement [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

**Contracted (Licensed) Event** requires a fully executed agreement with a binding deposit. This is the stage at which the booking becomes a firm financial commitment [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

**Event Execution** covers the active event period, including move-in and move-out days. Revenue generation and service delivery occur during this stage [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

**Settlement** is the post-event financial reconciliation, where final accounting is performed against the pro forma and revenue is recognized [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

Three non-completion outcomes are tracked: **Lost Events** (no contract at any pre-contract stage), **Cancelled Events** (previously contracted events that did not occur, triggering cancellation clauses), and **Turned Down Events** (venue declined to issue an offer, a sub-category of Lost Events) [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

## Venue Type Variations

The booking pipeline structure is broadly consistent across venue types, but three dimensions diverge significantly: who initiates the booking, lead time, and deal structure.

**Convention centres** operate the most formal multi-stage sales process. Citywide bookings may originate through a CVB/DMO and can be placed 2-10 years in advance [[Source-0312-Northstar-Planning-Citywide-Convention]]. A long-term sales team handles business beyond 18 months while a short-term team focuses on the immediate window [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

**Arenas** operate primarily in a promoter-driven model for entertainment content, where the booking inquiry comes inbound from a touring artist's booking agent through a concert promoter. Booking windows for major touring acts range from approximately 3-12 months, while sports anchor tenant events occupy permanent priority calendar positions [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

**Performing arts centres** operate multiple booking models simultaneously. As presenters, they program their own seasons 1-3 seasons in advance, bearing marketing and financial risk. As rental facilities, they operate a standard inbound inquiry-to-contract pipeline for third-party producers [[Source-0314-Cal-Performances-What-Is-Presenting]].

**Stadiums** blend anchor-tenant scheduling (league season games set 12+ months out) with event-by-event promoter bookings. **Fairgrounds** operate on seasonal and annual cycles, with the anchor fair event occupying peak dates surrounded by year-round rentals [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

## Sales Activity Metrics

Sales activity metrics precede and support the pipeline. The IAVM framework tracks sales calls, number of prospects with activity, site visits (including associated Gross Area Days consumed), and planning/pre-event meetings. These are operational inputs, not performance outputs: they drive conversion but should not inflate occupancy metrics [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

## CRM and Technology Platform Support

Venue management and CRM platforms such as Momentus Technologies (formerly Ungerboeck) provide full lifecycle support from CRM and booking through contracts, operations, finance, and analytics, with features including real-time availability to reduce double bookings and automated contract generation [[Source-0315-Momentus-Technologies-Venue-Management]].

## Sources

- [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]]
- [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]]
- [[Source-0312-Northstar-Planning-Citywide-Convention]]
- [[Source-0314-Cal-Performances-What-Is-Presenting]]
- [[Source-0315-Momentus-Technologies-Venue-Management]]
