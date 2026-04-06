---
title: "Multi-Use Venue Scheduling"
note_type: concept
status: draft
created: 2026-04-06
updated: 2026-04-06
domain: booking-and-sales
tags:
  - concept
  - booking-and-sales
description: "Calendar management for shared and multi-use venues, including priority hierarchies, hold management, changeover windows between configurations, and scheduling software for conflict prevention and real-time availability."
venue_types:
  - arena
  - stadium
  - convention-centre
  - performing-arts-centre
  - fairground-exhibition
vef_alignment:
  - operational-efficiency-productivity-creativity
  - systems-processes-clarity-of-roles
sources:
  - "[[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]]"
  - "[[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]]"
  - "[[Source-0315-Momentus-Technologies-Venue-Management]]"
research_batch: dr-s20-r06-booking-ticketing
confidence: high
extraction_model: claude-opus-4-6
child_of: "[[Domain-Booking-And-Sales]]"
related_to:
  - "[[Booking-And-Sales-Event-Booking-Lifecycle]]"
  - "[[Booking-And-Sales-Venue-Booking-KPIs]]"
venue_scale:
  - medium
  - large
  - mega
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---
# Multi-Use Venue Scheduling

Multi-use venues — arenas hosting hockey, basketball, concerts, family shows, graduation ceremonies, trade shows, and corporate events in a single facility — face inherent scheduling complexity arising from competing user demands, changeover windows, maintenance requirements, and contractual obligations.

## Building States for Scheduling

The IAVM defines standard building states for scheduling purposes [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]] [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]]:

**Event Day** is a revenue-generating day with public-facing activity. This is the primary utilization KPI for arenas, expressed as a percentage of 365 [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

**Non-Event Day** covers internal activities (maintenance, team practice, meetings) with no external guests [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

**Dark Day** means no functions in the venue. Within an event's contracted period, a Dark Day counts as a Use Day (the space is contractually occupied) but not an Event Day (no functions occurred). This distinction is critical for accurate reporting: it prevents occupancy measures from being artificially inflated by load-in/load-out days and contractual dark days, while ensuring the venue accurately reflects that the space is unavailable for secondary booking [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

**Use Day** is the broadest measure, covering Event Days plus move-in/move-out days plus Dark Days within a contracted period [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

## Priority Hierarchies

Public assembly venues operate scheduling with an implicit or explicit priority hierarchy [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]]:

1. **Anchor Tenant Events**: NHL/NBA/NFL/MLS games occupy the highest priority tier, with dates set by league schedules 6-12 months in advance that cannot be displaced
2. **Venue-Owned Programming**: Events the venue is producing directly (in-house/self-promote)
3. **Long-standing Annual Events**: Events with multi-year booking history and contractual right of first refusal
4. **Contracted Future Events**: Third-party bookings with executed agreements
5. **Tentative Holds**: Uncontracted holds pending promoter confirmation, assigned as first or second holds by date
6. **Maintenance Windows**: Planned capital maintenance, ice resurfacing, turf replacement, system upgrades
7. **Community/Non-revenue Events**: Civic uses, charity events, venue-supported programming

The management of multiple holds on the same date requires clear hold-priority policies. Industry practice assigns holds in chronological order: a promoter's "first hold" gives right of first refusal before the "second hold" holder. The second hold holder is notified when the first hold confirms or releases [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

## Changeover Windows and Configuration Management

Major venues operating multiple event types require changeover windows — defined periods between events for physical reconfiguration. Changeover complexity and cost vary by transition type [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]]:

- **Ice to Concert**: Arena ice removal, floor covering, floor-level stage build — typically 24-72 hours depending on stage complexity
- **Concert to Ice**: Stage strike, floor uncovering, ice flooding — typically 48-96 hours
- **Trade Show to Banquet**: Exhibit hall strip-down to flat floor, table/chair set — typically 4-8 hours
- **Arena to Graduation**: Scale-dependent floor seating configuration changes — 4-12 hours

The IAVM arena handbook identifies conversion costs as a distinct seasonal expense line in the sports team P&L template, separate from event-specific expenses [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

## Scheduling Software

Venue scheduling tools must solve for real-time space availability visibility, conflict prevention (no double-booking), hold management, and integration with financial and event management systems [[Source-0315-Momentus-Technologies-Venue-Management]].

Momentus Technologies provides enterprise-grade multi-venue scheduling with CRM integration, where real-time availability reduces double bookings and enables faster inquiry response [[Source-0315-Momentus-Technologies-Venue-Management]]. VenueOps offers a booking calendar with role-based access, financial tracking per booking, and event detail management. Planning Pod provides color-coded drag-and-drop calendars with conflict detection and integration with Google, Outlook, and Apple Calendar [[Source-0315-Momentus-Technologies-Venue-Management]].

## Event Yield vs. Raw Utilization

For arena operators, Event Yield — the average net profit/loss per event across a full season — is a more meaningful performance measure than raw utilization count. A venue packing 200 event days with low-margin community events may generate less net income than one running 150 event days with strong per-cap performance [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

## Sources

- [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]]
- [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]]
- [[Source-0315-Momentus-Technologies-Venue-Management]]
