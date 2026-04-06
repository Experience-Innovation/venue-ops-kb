---
title: "DR Prompt R-06 — Venue Booking, Sales, and Ticketing Operations"
prompt_id: R-06
session: S19
created: 2026-04-06
target_domains:
  - booking-and-sales
  - ticketing-and-box-office
gap_reference: "booking-and-sales: 0 concepts (empty, blocks v1.0). ticketing-and-box-office: 1 concept (scaffolded). Both are customer-facing transaction domains critical to venue revenue operations."
lifecycle: active
---

DR PROMPT R-06 — Venue Booking, Sales, and Ticketing Operations

CONTEXT: The KB has zero concept notes in booking-and-sales and only 1 concept note in ticketing-and-box-office (Subscription-Season-Management). These are two of three empty domains that block v1.0 release. Every venue type — convention centres, arenas, stadiums, performing arts centres, fairgrounds — operates a booking or ticketing function, making this a foundational gap. The existing source corpus (290 notes) has minimal coverage of booking workflows, event contracting, ticketing platform architecture, or box office operations.

RESEARCH OBJECTIVE: Produce comprehensive operational reference on venue booking lifecycle, event sales processes, ticketing platform operations, and box office management across public assembly venue types (convention centres, arenas, stadiums, performing arts centres, fairgrounds, amphitheatres) as of April 2026.

PRIMARY RESEARCH QUESTIONS:

1. EVENT BOOKING LIFECYCLE AND SALES PROCESS: What is the standard booking pipeline for public assembly venues from initial inquiry through contract execution? Stages of the booking funnel (inquiry, qualification, site visit, proposal, negotiation, contract, advance planning, event execution, settlement). How do booking processes differ by venue type — convention centre (multi-day, multi-space) vs. arena (single-event, promoter-driven) vs. performing arts centre (season programming vs. rental)? What CRM and venue management platforms support the booking pipeline (Momentus/Ungerboeck, VenueOps, Tripleseat, iVvy)? What KPIs measure booking performance (conversion rate, lead time, utilization rate, revenue per available room/seat)?

2. EVENT CONTRACTING AND LICENSE AGREEMENTS: What are the standard contract structures for venue rentals vs. co-promotion vs. license agreements? Key contract terms: rental fees, percentage deals, flat fee + overage, co-promotion splits. Rider requirements for touring productions and concerts. Insurance and indemnification requirements in event contracts. Force majeure and cancellation provisions — how did post-COVID contract language evolve? IAVM and industry standard contract templates or frameworks.

3. TICKETING PLATFORM ARCHITECTURE AND OPERATIONS: What is the current ticketing technology landscape for public assembly venues? Primary ticketing platforms (Ticketmaster/Live Nation, AXS/AEG, SeatGeek, Eventbrite, Paciolan, Tickets.com). Exclusive ticketing agreements — terms, duration, revenue splits. Primary vs. secondary market integration. Mobile ticketing, digital wallet integration, NFC/RFID credential systems. Anti-fraud and anti-scalping technology (Verified Fan, blockchain ticketing, dynamic QR). PCI DSS compliance requirements for ticketing operations.

4. BOX OFFICE OPERATIONS AND STAFFING: What does a modern box office operation look like? Staffing models (in-house vs. outsourced to ticketing partner). Will-call and day-of-show operations. Accessible ticketing compliance (ADA/AODA requirements for ticket purchasing). Refund and exchange policies and their operational impact. Group sales and subscription management workflows. Revenue recognition and settlement timing.

5. DYNAMIC PRICING AND YIELD MANAGEMENT: How are venues and promoters implementing dynamic pricing for tickets? Revenue management systems adapted from hospitality/airline industries. Variable pricing by section, event, demand, and time-to-event. Platinum/premium/VIP pricing tiers. Fan perception and transparency considerations. Case studies: which venues or promoters have published results from dynamic pricing implementation?

6. CONVENTION CENTRE BOOKING SPECIFICITY: How does convention centre booking differ from entertainment venue ticketing? Space allocation and room block management. Catering minimums and F&B revenue guarantees. Exhibitor services and decorator coordination. Citywide convention booking — relationship with CVB/destination marketing organizations. Lead time cycles (convention bookings 2-5 years ahead vs. concert bookings 3-12 months). Lost business reporting and competitive analysis.

7. VENUE UTILIZATION AND SCHEDULING: How do multi-use venues manage scheduling across competing demands? Dark days, changeover windows, maintenance holds. Priority hierarchies (anchor tenant, season ticket events, third-party rentals). Scheduling software and calendar management tools. Utilization metrics — how do venues benchmark occupancy and revenue per available date?

SOURCE QUALITY:
- PRIORITY 1: IAVM (International Association of Venue Managers) publications — venue management textbook, professional development materials, industry benchmarks
- PRIORITY 2: Ticketing industry reports — Ticketmaster/Live Nation investor disclosures, AXS/AEG operational documentation, INTIX (International Ticketing Association) resources
- PRIORITY 3: Convention industry — PCMA (Professional Convention Management Association), ASAE, CEIR (Center for Exhibition Industry Research), destination marketing organization reports
- PRIORITY 4: Trade press — Pollstar, VenuesNow, Facilities & Event Management magazine, Sports Business Journal
- AVOID: Ticketing platform marketing materials without operational specifics. Social media commentary on ticket pricing. Fan advocacy pieces without operational data.

OUTPUT STRUCTURE:
- Event booking lifecycle framework (stages, decision points, contract types by venue type)
- Ticketing platform comparison matrix (features, market position, venue type alignment)
- Dynamic pricing implementation guide (models, case studies, fan perception management)
- Convention centre booking process guide (space management, lead times, CVB relationships)
- Box office operations reference (staffing, compliance, settlement, technology)
- Venue utilization and scheduling framework (metrics, tools, priority management)
- Contract terms reference (standard clauses, post-COVID evolution, rider frameworks)

KNOWN CONTEXT: The KB already covers: subscription-season-management (1 concept in ticketing), premium-and-vip revenue models and pricing (6 concepts), commercial-and-revenue community funding (2 concepts), event-operations (12 concepts covering event-day execution, not booking). Momentus Technologies appears as a source (Source-0093) but only for venue management software broadly. This prompt targets ONLY the booking/sales pipeline, ticketing operations, and box office management — not event-day execution, not premium hospitality delivery, not F&B service.

CONSTRAINTS: North American focus (US + Canada) with international examples where relevant. Include both entertainment venues (arenas, stadiums, PACs) and business event venues (convention centres). Note jurisdictional differences in ticketing regulation (e.g., anti-scalping laws vary by state/province). Any Calgary Stampede content tagged as exemplar only per KB policy. Distinguish between venue-operated ticketing and promoter-controlled ticketing — different operational models with different KB implications.
