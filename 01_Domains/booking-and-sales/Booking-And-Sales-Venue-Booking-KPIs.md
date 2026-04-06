---
title: "Venue Booking KPIs"
note_type: concept
status: draft
created: 2026-04-06
updated: 2026-04-06
domain: booking-and-sales
tags:
  - concept
  - booking-and-sales
description: "Key performance indicators for venue booking operations including utilization rate, Revenue Per Occupied Square Foot (RevPOS), opportunity conversion ratio, per-cap revenue, and event yield metrics across venue types."
venue_types:
  - all
vef_alignment:
  - operational-efficiency-productivity-creativity
  - data-management-and-architecture
sources:
  - "[[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]]"
  - "[[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]]"
  - "[[Source-0316-KPI-Depot-Event-Venue-Utilization]]"
research_batch: dr-s20-r06-booking-ticketing
confidence: high
extraction_model: claude-opus-4-6
child_of: "[[Domain-Booking-And-Sales]]"
related_to:
  - "[[Booking-And-Sales-Event-Booking-Lifecycle]]"
  - "[[Booking-And-Sales-Convention-Centre-Booking-Operations]]"
  - "[[Booking-And-Sales-Multi-Use-Venue-Scheduling]]"
key_metrics:
  - "Venue Utilization Rate"
  - "Revenue Per Occupied Square Foot (RevPOS)"
  - "Opportunity Conversion Ratio"
  - "Per Cap"
  - "Event Yield"
  - "Average Revenue Per Event (ARPE)"
  - "Cost per Dark Day"
venue_scale:
  - small
  - medium
  - large
  - mega
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---
# Venue Booking KPIs

Key performance indicators for venue booking operations measure the financial productivity and operational efficiency of the venue's booking function. KPIs vary significantly by venue type, with convention centres, arenas, and stadiums each tracking distinct primary metrics suited to their operating models.

## Utilization KPIs

**Venue Utilization Rate** is calculated as Total Booked Days/Hours divided by Total Available Days/Hours. A rate of 60% represents the baseline for healthy event space operations; 70% or above is considered good, and 80% or above is excellent. Top-performing convention centres and arenas strive to exceed 80% [[Source-0316-KPI-Depot-Event-Venue-Utilization]].

**Capacity Utilization (Ticket Sell-Through Rate)** measures actual tickets sold as a percentage of available inventory. An average of 70-80% is considered decent, while 90% or above is excellent [[Source-0316-KPI-Depot-Event-Venue-Utilization]].

**Event Days** for arenas represents total days with revenue-generating activity, expressed as a percentage of 365 [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

**Occupancy Percentage** for convention centres is calculated as Gross Occupied Square Feet divided by Gross Available Square Feet, calculated for the full period being measured [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

## Revenue Productivity KPIs

**Revenue Per Occupied Square Foot (RevPOS)** divides Total Revenue by Gross Occupied Square Feet and serves as the primary productivity ratio for convention centres [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

**Average Revenue Per Event (ARPE)** divides Total Revenue by Total Events, providing a per-event productivity measure applicable across venue types [[Source-0316-KPI-Depot-Event-Venue-Utilization]].

**Revenue Per Available Date (RevPAD)** is an emerging metric analogous to hotel RevPAR. It divides total revenue generated in a period by the total available event-date units (each bookable space multiplied by total available dates), providing a yield management framing that accounts for both price and volume [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

## Sales Pipeline KPIs

**Opportunity Conversion Ratio** is the percentage of tracked opportunities that result in contracted events, calculated as Contracted Events divided by the sum of Contracted and Lost Opportunities. The IAVM recommends tracking this ratio consistently over time and breaking it down by lead source, event type, and market segment [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

**Booking Conversion Rate** measures site tours resulting in signed contracts, a key indicator for the private/wedding and corporate venue segments [[Source-0316-KPI-Depot-Event-Venue-Utilization]].

**Lead Time to Booking** tracks average days from first inquiry to contract execution, providing insight into sales cycle efficiency.

## Arena-Specific KPIs

The IAVM Arenas Handbook defines several arena-specific metrics [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]]:

**Per Cap** measures net ancillary revenue (F&B, merchandise, parking) per turnstile count, capturing the venue's ability to monetize each attendee beyond ticket revenue [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

**Event Yield** calculates the sum of net profit/loss from all events divided by total events in a season. This is a more meaningful performance measure than raw utilization count because it reveals whether increased activity actually contributes to the bottom line [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

**Event ROI** divides Net Event Income by Cost of Investment, multiplied by 100 [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

**Cost per Dark Day** calculates the full overhead cost of each non-revenue day, quantifying the financial impact of unbooked dates [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]].

## Convention Centre Pace Reporting

The IAVM framework tracks **Pace Reporting** as a forward-looking early warning system. By tracking year-over-year booking accumulation for future years (1, 2, and 3+ years forward), convention centres can assess whether their pipeline is ahead of or behind historical benchmarks, enabling proactive sales investment decisions [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]].

## Sources

- [[Source-0311-IAVM-Convention-Center-Performance-Reporting-Framework]]
- [[Source-0313-IAVM-Arenas-Performance-Reporting-Handbook]]
- [[Source-0316-KPI-Depot-Event-Venue-Utilization]]
