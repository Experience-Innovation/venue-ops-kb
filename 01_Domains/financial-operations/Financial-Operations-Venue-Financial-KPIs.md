---
title: "Venue Financial KPIs"
note_type: concept
domain: financial-operations
status: draft
created: 2026-04-06
updated: 2026-04-06
description: "Financial performance metrics and benchmarks used by venue operators across venue types, covering occupancy and utilization, per-capita spending, operating margin, booking pace, and revenue yield metrics, with source-backed benchmark values for convention centres, stadiums, and performing arts centres."
venue_types:
  - convention-centre
  - arena
  - stadium
  - performing-arts-centre
  - fairground-exhibition
vef_alignment:
  - operational-efficiency-productivity-creativity
  - data-management-and-architecture
confidence: high
sources:
  - "[[Source-0371-Ottawa-Convention-Centre-Business-Plan-2024-25]]"
  - "[[Source-0382-Oracle-Stadium-of-the-Future-Report]]"
  - "[[Source-0375-StatsCan-Performing-Arts-Industry-2024]]"
  - "[[Source-0372-Tampa-Sports-Authority-FY2024-Audit]]"
  - "[[Source-0376-ABA-Managing-Performance-Venue-Rentals-2024]]"
research_batch: dr-s20-r09-commercial-financial
child_of: "[[Domain-Financial-Operations]]"
related_to:
  - "[[Financial-Operations-Venue-Budgeting-Forecasting]]"
  - "[[Commercial-And-Revenue-Venue-Revenue-Taxonomy]]"
  - "[[Commercial-And-Revenue-Sponsorship-Naming-Rights]]"
  - "[[Domain-Data-And-Analytics]]"
key_metrics:
  - "Occupancy / utilization rate (%)"
  - "Booking pace ($)"
  - "Per-capita F&B spend ($)"
  - "Operating margin (%)"
  - "Revenue per available sq ft"
  - "Cost per attendee ($)"
  - "Labor cost as % of revenue"
  - "Utility cost per sq ft ($)"
tags:
  - concept
  - venue-ops
  - financial-operations
  - financial-kpis
  - benchmarking
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# Venue Financial KPIs

A practical financial KPI dashboard for venue operators must include both commercial performance metrics and operational cost-control indicators. The specific metrics that matter most vary by venue type, but the underlying measurement disciplines are consistent: track utilization, revenue yield, per-capita economics, and cost ratios against both internal budget targets and external benchmarks ([[Source-0371-Ottawa-Convention-Centre-Business-Plan-2024-25|Ottawa Convention Centre Business Plan]]; [[Source-0376-ABA-Managing-Performance-Venue-Rentals-2024|ABA Rental Study 2024]]).

## Core Metrics

### Occupancy and Utilization

For convention centres, occupancy is measured as square feet sold against available square feet. Full occupancy under ordinary operating conditions is approximately 70%, reflecting the reality that setup, teardown, and seasonal demand patterns prevent 100% utilization. The Ottawa Convention Centre's 2024-25 target was 43%, indicating a facility in an early growth or repositioning phase ([[Source-0371-Ottawa-Convention-Centre-Business-Plan-2024-25|Ottawa Convention Centre Business Plan]]).

### Booking Pace

Booking pace measures forward-sold revenue over a defined period. It is a leading indicator that is often more actionable than trailing realized revenue because it reveals demand trajectory. The Ottawa Convention Centre targeted $21 million in booking pace for 2024-25 ([[Source-0371-Ottawa-Convention-Centre-Business-Plan-2024-25|Ottawa Convention Centre Business Plan]]).

### Per-Capita Spending

Per-capita F&B spending is an increasingly important metric, particularly for event-driven venues. Oracle data reports average U.S. stadium fan spend of approximately $42 per game on food and beverage ([[Source-0382-Oracle-Stadium-of-the-Future-Report|Oracle Stadium of the Future]]). Per-cap metrics are useful because they normalize revenue performance against attendance, enabling comparison across events of different sizes.

### Operating Margin

Operating margin varies significantly by venue type and ownership model. Statistics Canada data for the Canadian performing arts industry in 2024 shows an overall sector operating margin of 12.6%, but not-for-profit organizations operated at -2.4% ([[Source-0375-StatsCan-Performing-Arts-Industry-2024|Statistics Canada Performing Arts 2024]]). Convention centres typically operate at thin margins (the Ottawa Convention Centre projected approximately 3.85% net operating surplus against gross revenue). Stadium and arena operating margins are shaped substantially by tenant revenue-sharing structures ([[Source-0372-Tampa-Sports-Authority-FY2024-Audit|Tampa Sports Authority FY2024 Audit]]).

### Revenue per Available Space

Revenue per available square foot (RevPAS) or revenue per available seat adapts hospitality industry yield metrics to the venue context. This metric is useful for convention centres and performing arts venues that need to optimize revenue from a fixed spatial asset across multiple event types and calendar periods.

## Cost-Control Metrics

### Expense Ratios

The Ottawa Convention Centre's 2024-25 budget documents expense composition relative to gross revenue: facilities at approximately 26.6%, utilities at 6.3%, sales and marketing at 10.9%, and general and administration at 10.4% ([[Source-0371-Ottawa-Convention-Centre-Business-Plan-2024-25|Ottawa Convention Centre Business Plan]]). These ratios provide a useful convention-centre benchmark, though absolute values vary by market, facility age, and labor environment.

### Cost per Attendee

Cost per attendee normalizes operating expenditure against throughput, enabling cross-event and cross-venue comparison. This metric is particularly useful in arenas and stadiums where the number of events and attendees varies significantly year over year.

### Labor and Utility Costs

Labor cost as a percentage of revenue and utility cost per square foot are foundational control metrics. Both are sensitive to venue scale, climate, facility age, and delivery model (in-house vs. outsourced staffing).

## Benchmarking Programs

IAVM financial benchmarking programs collect data across member venues to establish comparative performance metrics. Publicly owned venues are also subject to governmental financial reporting requirements that produce benchmark-ready data, though the reporting format and level of operational detail vary by jurisdiction ([[Source-0372-Tampa-Sports-Authority-FY2024-Audit|Tampa Sports Authority FY2024 Audit]]).

## Sources

- [[Source-0371-Ottawa-Convention-Centre-Business-Plan-2024-25]]
- [[Source-0382-Oracle-Stadium-of-the-Future-Report]]
- [[Source-0375-StatsCan-Performing-Arts-Industry-2024]]
- [[Source-0372-Tampa-Sports-Authority-FY2024-Audit]]
- [[Source-0376-ABA-Managing-Performance-Venue-Rentals-2024]]
