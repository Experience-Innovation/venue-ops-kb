---
title: "Anti-Scalping and Ticketing Regulations"
note_type: concept
status: draft
created: 2026-04-06
updated: 2026-04-06
domain: ticketing-and-box-office
tags:
  - concept
  - ticketing-and-box-office
description: "Jurisdictional analysis of anti-scalping and ticketing regulations across North America, including the US federal BOTS Act of 2016, Alberta's Consumer Protection Act bot prohibition, Ontario's evolving resale price cap legislation, and the 2026 Live Nation/DOJ settlement fee cap provisions."
venue_types:
  - arena
  - stadium
  - performing-arts-centre
  - amphitheatre
  - fairground-exhibition
vef_alignment:
  - systems-processes-clarity-of-roles
  - guest-experience
sources:
  - "[[Source-0330-Alberta-Ticket-Sales-Regulations]]"
  - "[[Source-0324-Globe-Mail-Live-Nation-DOJ-Settlement]]"
  - "[[Source-0323-NYT-Live-Nation-Antitrust-Settlement]]"
  - "[[Source-0322-IDDataWeb-Verified-Fan-Scalping]]"
research_batch: dr-s20-r06-booking-ticketing
confidence: medium
extraction_model: claude-opus-4-6
child_of: "[[Domain-Ticketing-And-Box-Office]]"
related_to:
  - "[[Ticketing-And-Box-Office-Ticketing-Platform-Architecture]]"
  - "[[Ticketing-And-Box-Office-Mobile-Digital-Ticketing]]"
jurisdiction:
  - us-federal
  - us-state
  - canada-provincial
varies_by:
  - "[[Domain-Legal-Compliance-And-Licensing]]"
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---
# Anti-Scalping and Ticketing Regulations

Anti-scalping and ticketing regulations vary significantly across North American jurisdictions, creating a complex compliance landscape for venue operators. The regulatory environment is actively evolving, with major developments in both federal antitrust enforcement and provincial/state consumer protection legislation.

## United States Federal

No comprehensive federal anti-scalping law exists in the United States. The primary federal instrument is the **BOTS Act of 2016** (Better Online Tickets Sales Act), which prohibits the use of automated software to circumvent ticket purchase limits established by ticket sellers [[Source-0322-IDDataWeb-Verified-Fan-Scalping]].

At the state level, laws vary significantly. Some states (such as New York) have required fee transparency and implemented additional enforcement against bot use. The March 2026 Live Nation/DOJ antitrust settlement introduced a **service fee cap of 15%** of ticket face value at Live Nation-operated amphitheaters, establishing a new regulatory baseline for ticketing fees at those venues [[Source-0324-Globe-Mail-Live-Nation-DOJ-Settlement]].

## Alberta (Canada)

Alberta's Consumer Protection Act regulations (effective August 1, 2018) established one of North America's more comprehensive ticket sales regulatory frameworks [[Source-0330-Alberta-Ticket-Sales-Regulations]]:

The regulations ban the use of bot software for purchasing event tickets. Primary sellers must perform due diligence to detect and prevent bot purchases and cancel bot-purchased tickets. Secondary sellers face refund obligations: full refunds are required if the event is cancelled before ticket use, if the ticket was purchased by bot and cancelled by the primary seller, if the ticket fails to grant entry as promised, if the ticket does not match its description, or if the ticket is counterfeit [[Source-0330-Alberta-Ticket-Sales-Regulations]].

Businesses and consumers harmed by bot use may pursue civil action. No general cap on resale prices exists as of early 2026. Exemptions apply to non-profit organizations reselling donated tickets for fundraising and platforms that only advertise (not facilitate) sales [[Source-0330-Alberta-Ticket-Sales-Regulations]].

## Ontario (Canada)

Ontario's Ticket Sales Act 2017 is being actively amended as of March 2026. The Ontario government introduced legislation to ban the resale of tickets above face value (proposed as zero premium). This reverses the government's 2019 repeal of anti-scalping provisions. Enforcement mechanisms and penalties were still under development as of March 2026. If enacted, the legislation would apply to all resales going forward and to platforms facilitating resales [[Source-0323-NYT-Live-Nation-Antitrust-Settlement]].

## Antitrust Enforcement as Regulation

The March 2026 Live Nation/DOJ settlement functions as a form of de facto regulation for the ticketing industry [[Source-0324-Globe-Mail-Live-Nation-DOJ-Settlement]] [[Source-0323-NYT-Live-Nation-Antitrust-Settlement]]:

Ticketmaster's exclusive venue contracts are capped at 4-year maximum duration. Venues may allocate ticket inventory to competing platforms. Ticketmaster must make portions of its technology platform accessible to rival ticketing firms. Live Nation must divest 13+ amphitheaters and end exclusive booking arrangements. Some state attorneys general were continuing independent litigation as of the settlement date [[Source-0324-Globe-Mail-Live-Nation-DOJ-Settlement]].

## Operational Implications for Venues

Venue operators must navigate this jurisdictional complexity by understanding which regulations apply in their jurisdiction, implementing compliant ticketing policies, training staff on applicable consumer protection requirements, and working with ticketing platform partners to ensure platform-level compliance with bot prohibition and fee transparency requirements [[Source-0330-Alberta-Ticket-Sales-Regulations]].

**Confidence note**: This concept is rated medium confidence because the regulatory landscape is actively evolving. Ontario legislation was still in development at the time of research, and the full implications of the 2026 DOJ settlement are not yet settled, with some states pursuing independent litigation.

## Sources

- [[Source-0330-Alberta-Ticket-Sales-Regulations]]
- [[Source-0324-Globe-Mail-Live-Nation-DOJ-Settlement]]
- [[Source-0323-NYT-Live-Nation-Antitrust-Settlement]]
- [[Source-0322-IDDataWeb-Verified-Fan-Scalping]]
