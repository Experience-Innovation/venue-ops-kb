#!/usr/bin/env python3
"""Generate batch-04-event-ops-av source and concept notes."""

import os

BASE = "/Users/bubblegumpshrimpco/Library/CloudStorage/GoogleDrive-alex@experienceinnovation.consulting/Shared drives/Venue Excellence Podcast/Venue Excellence Podcast/venue-ops-kb/.claude/worktrees/session-13-batch-processing"
SOURCES_DIR = os.path.join(BASE, "06_Sources")
DOMAINS_DIR = os.path.join(BASE, "01_Domains")

created_count = 0

# =============================================================
# STEP 1: SOURCE NOTES (Source-0091 through Source-0120)
# =============================================================

sources = [
    # Event Ops sources (0091-0105) — v2-prompt-01-event-ops
    {
        "num": "0091",
        "slug": "IAVM-Blueprint-Event-Management",
        "title": "IAVM Blueprint for Event Management",
        "source_type": "trade-association",
        "url": "https://www.iavm.org/",
        "description": "International Association of Venue Managers (IAVM) provides the Blueprint for Event Management framework, covering scheduling, event coordination, and operational standards for public assembly venues.",
        "domains": ["event-operations", "strategy-and-governance"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0092",
        "slug": "IAVM-Arenas-Performance-Reporting",
        "title": "IAVM Arenas Performance Reporting Handbook",
        "source_type": "trade-association",
        "url": "https://iavm.org/wp-content/uploads/2023/10/IAVMArenasPerformanceReportingHandbook_07302023.pdf",
        "description": "IAVM handbook establishing standardized performance metrics for arena operations including GBOR/NBOR calculations, event settlement methodologies, and financial benchmarking across the arena industry.",
        "domains": ["event-operations", "financial-operations"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0093",
        "slug": "Momentus-Technologies-Venue-Management",
        "title": "Momentus Technologies Venue Management Software",
        "source_type": "vendor-documentation",
        "url": "https://gomomentus.com/venue-management-software",
        "description": "Momentus Technologies (formerly Ungerboeck) provides integrated venue management software covering event booking, scheduling, BEO generation, CRM, and resource management for convention centres and arenas.",
        "domains": ["event-operations", "technology-and-digital"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0094",
        "slug": "ESCA-Exhibition-Services",
        "title": "Exhibition Services and Contractors Association (ESCA)",
        "source_type": "trade-association",
        "url": "https://www.esca.org/",
        "description": "ESCA represents exhibition service contractors providing drayage, material handling, and booth installation services. Publishes guidelines for exhibitor services manuals and general service contractor operations.",
        "domains": ["event-operations", "logistics-and-warehouse"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0095",
        "slug": "IATSE-International",
        "title": "International Alliance of Theatrical Stage Employees (IATSE)",
        "source_type": "trade-association",
        "url": "https://iatse.net/",
        "description": "IATSE represents over 170,000 technicians, artisans, and craftspersons in the entertainment industry. Governs stagehand labor agreements, crew call structures, and work rules for live event production in venues.",
        "domains": ["event-operations", "av-and-production", "people-and-culture"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0096",
        "slug": "Events-Industry-Council",
        "title": "Events Industry Council (EIC)",
        "source_type": "trade-association",
        "url": "https://www.eventscouncil.org/",
        "description": "Events Industry Council represents 30+ member organizations across the events sector. Manages the CMP (Certified Meeting Professional) certification and publishes the APEX (Accepted Practices Exchange) industry standards for event management.",
        "domains": ["event-operations", "booking-and-sales"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0097",
        "slug": "Freeman-GSC",
        "title": "Freeman General Service Contractor",
        "source_type": "vendor-documentation",
        "url": "https://www.freeman.com/",
        "description": "Freeman is a leading general service contractor (GSC) for conventions, exhibitions, and corporate events. Provides drayage, material handling, booth installation, audio-visual, and event technology services across North American convention centres.",
        "domains": ["event-operations", "logistics-and-warehouse", "av-and-production"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0098",
        "slug": "GES-Global-Experience-Specialists",
        "title": "GES Global Experience Specialists",
        "source_type": "vendor-documentation",
        "url": "https://ges.com/",
        "description": "GES (now Viad Corp's Global Experience Specialists) provides exhibition services, event logistics, and experiential marketing for trade shows and conventions. Operates as a general service contractor with material handling and exhibitor services.",
        "domains": ["event-operations", "logistics-and-warehouse"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0099",
        "slug": "Prism-FM-Settlement",
        "title": "Prism.fm Event Settlement Platform",
        "source_type": "vendor-documentation",
        "url": "https://www.prism.fm/",
        "description": "Prism.fm provides event settlement and deal management software for live entertainment venues. Handles financial reconciliation, GBOR/NBOR calculations, promoter profit splits, and ancillary revenue settlement.",
        "domains": ["event-operations", "financial-operations"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0100",
        "slug": "247-Software-Operations",
        "title": "24/7 Software Venue Operations Platform",
        "source_type": "vendor-documentation",
        "url": "https://www.247software.com/",
        "description": "24/7 Software provides real-time venue operations management covering incident tracking, dispatch, inspections, and event-day command center operations for arenas, stadiums, and convention centres.",
        "domains": ["event-operations", "safety-and-risk"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0101",
        "slug": "WeTrack-Event-Management",
        "title": "WeTrack Event Project Management Platform",
        "source_type": "vendor-documentation",
        "url": "https://wetrack.com/",
        "description": "WeTrack provides event project management and planning software used for complex multi-stakeholder event operations, task tracking, and cross-departmental coordination in major venue environments.",
        "domains": ["event-operations", "technology-and-digital"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0102",
        "slug": "Voyage-Control-Dock-Management",
        "title": "Voyage Control Dock and Delivery Management",
        "source_type": "vendor-documentation",
        "url": "https://www.voyagecontrol.com/",
        "description": "Voyage Control provides dock scheduling and delivery management software for venues and facilities. Coordinates loading dock appointments, vehicle tracking, and material flow for event load-in/load-out operations.",
        "domains": ["event-operations", "logistics-and-warehouse"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0103",
        "slug": "USITT-Stage-Management",
        "title": "United States Institute for Theatre Technology (USITT)",
        "source_type": "trade-association",
        "url": "https://www.usitt.org/",
        "description": "USITT advances the knowledge and skills of the entertainment technology industry. Publishes stage management guidelines, technical production standards, and professional development resources for theatrical and live event production.",
        "domains": ["event-operations", "av-and-production"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0104",
        "slug": "FirstNet-Public-Safety-Broadband",
        "title": "FirstNet Public Safety Broadband Network",
        "source_type": "regulatory-document",
        "url": "https://www.firstnet.com/",
        "description": "FirstNet is the nationwide public safety broadband network (Band 14) built with AT&T. Provides dedicated LTE connectivity for first responders at venues and mass gatherings, with priority and preemption capabilities during events.",
        "domains": ["technology-and-digital", "safety-and-risk", "security"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    {
        "num": "0105",
        "slug": "NFPA-1225-Emergency-Communications",
        "title": "NFPA 1225 Standard for Emergency Communications Systems",
        "source_type": "regulatory-document",
        "url": "https://www.nfpa.org/codes-and-standards/nfpa-1225-standard-development/1225",
        "description": "NFPA 1225 provides requirements for Emergency Responder Communication Enhancement Systems (ERCES), including in-building signal boosters and DAS installations required to maintain radio coverage for first responders in large venue structures.",
        "domains": ["safety-and-risk", "technology-and-digital", "facilities-and-building-systems"],
        "research_batch": "v2-prompt-01-event-ops",
    },
    # AV/Production sources (0106-0120) — v2-prompt-06-av-production
    {
        "num": "0106",
        "slug": "AVIXA-Standards",
        "title": "AVIXA Audiovisual Standards",
        "source_type": "trade-association",
        "url": "https://www.avixa.org/standards/current-standards",
        "description": "AVIXA (Audiovisual and Integrated Experience Association) publishes standards governing AV system design, including DISCAS (Digital Signage Display Image Comparison and Assessment), ACU (Audio Coverage Uniformity), and RP-C303.01 (AV cybersecurity). These standards define performance targets for venue AV installations.",
        "domains": ["av-and-production", "technology-and-digital"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0107",
        "slug": "AVIXA-CTS-Certification",
        "title": "AVIXA Certified Technology Specialist (CTS) Program",
        "source_type": "trade-association",
        "url": "https://www.avixa.org/certification-section/about-the-certified-technology-specialist-(cts)-credential",
        "description": "AVIXA CTS certification program validates AV professional competency across design, installation, and integration. CTS-D (Design) and CTS-I (Installation) specializations apply directly to venue AV system specification and deployment.",
        "domains": ["av-and-production", "people-and-culture"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0108",
        "slug": "ESTA-Technical-Standards",
        "title": "ESTA Technical Standards Program",
        "source_type": "trade-association",
        "url": "https://tsp.esta.org/",
        "description": "Entertainment Services and Technology Association (ESTA) Technical Standards Program develops ANSI-accredited standards for entertainment technology including DMX512-A (lighting control), ANSI E1.6 (powered hoists), and rigging safety standards used across venue production.",
        "domains": ["av-and-production", "safety-and-risk"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0109",
        "slug": "ETCP-Certification",
        "title": "Entertainment Technician Certification Program (ETCP)",
        "source_type": "trade-association",
        "url": "https://etcp.esta.org/",
        "description": "ETCP provides portable certification for entertainment riggers (Arena and Theatre tracks) and electricians. ANSI-accredited under ISO 17024, ETCP certification is the recognized competency standard for rigging personnel in arenas, convention centres, and theatres.",
        "domains": ["av-and-production", "safety-and-risk", "people-and-culture"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0110",
        "slug": "NFPA-70-NEC",
        "title": "NFPA 70 National Electrical Code (NEC)",
        "source_type": "regulatory-document",
        "url": "https://www.nfpa.org/codes-and-standards/nfpa-70-standard-development/70",
        "description": "NFPA 70 (National Electrical Code) governs electrical installation requirements including temporary event power distribution, Cam-Lok and Powerlock connector standards, and 400A 3-phase service provisions used in venue production environments.",
        "domains": ["av-and-production", "facilities-and-building-systems", "safety-and-risk"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0111",
        "slug": "NFPA-70E-Electrical-Safety",
        "title": "NFPA 70E Standard for Electrical Safety in the Workplace",
        "source_type": "regulatory-document",
        "url": "https://www.nfpa.org/codes-and-standards/nfpa-70e-standard-development/70e",
        "description": "NFPA 70E establishes electrical safety practices for workers including arc flash risk assessment, PPE requirements, and lockout/tagout procedures applicable to venue production power distribution and temporary electrical installations.",
        "domains": ["av-and-production", "safety-and-risk"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0112",
        "slug": "ANSI-E1-6-Powered-Hoists",
        "title": "ANSI E1.6 Powered Hoist Standard for Entertainment",
        "source_type": "regulatory-document",
        "url": "https://tsp.esta.org/tsp/documents/published_docs.php",
        "description": "ANSI E1.6-1 establishes design, manufacture, and use requirements for powered chain hoists used in entertainment rigging. Covers load rating, braking systems, safety factors, and inspection protocols for overhead rigging in arenas and theatres.",
        "domains": ["av-and-production", "safety-and-risk"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0113",
        "slug": "EVS-Broadcast-Equipment",
        "title": "EVS Broadcast Equipment",
        "source_type": "vendor-documentation",
        "url": "https://evs.com/",
        "description": "EVS provides live production and replay systems used in broadcast compounds at arenas and stadiums. EVS XT-VIA and LSM-VIA servers are the industry standard for instant replay, super slow-motion, and VAR (Video Assistant Referee) operations in live sports broadcasting.",
        "domains": ["av-and-production", "technology-and-digital"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0114",
        "slug": "Evertz-DreamCatcher",
        "title": "Evertz DreamCatcher Replay System",
        "source_type": "vendor-documentation",
        "url": "https://evertz.com/products/DreamCatcher",
        "description": "Evertz DreamCatcher is a software-defined replay and highlight production system used in arena and stadium broadcast operations. Provides multi-channel ingest, clip playout, and real-time highlight packaging for in-venue displays and broadcast feeds.",
        "domains": ["av-and-production", "technology-and-digital"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0115",
        "slug": "Audinate-Dante-Audio-Networking",
        "title": "Audinate Dante Audio Networking Protocol",
        "source_type": "vendor-documentation",
        "url": "https://www.audinate.com/",
        "description": "Dante (Digital Audio Network Through Ethernet) is the dominant networked audio protocol in professional AV, routing hundreds of bidirectional audio channels over standard Ethernet with sub-millisecond latency. Widely deployed in venue PA systems, broadcast infrastructure, and production environments.",
        "domains": ["av-and-production", "technology-and-digital"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0116",
        "slug": "Listen-Technologies-ALS",
        "title": "Listen Technologies Assistive Listening Systems",
        "source_type": "vendor-documentation",
        "url": "https://www.listentech.com/",
        "description": "Listen Technologies provides assistive listening systems (ALS) including RF, infrared, hearing loop, and Wi-Fi-based solutions for venues. Products address ADA Section 219 compliance requirements for assembly areas with audio amplification.",
        "domains": ["av-and-production", "inclusivity-and-accessibility"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0117",
        "slug": "PCI-DSS-v4",
        "title": "PCI DSS v4.0.1 Payment Card Industry Data Security Standard",
        "source_type": "regulatory-document",
        "url": "https://www.pcisecuritystandards.org/",
        "description": "PCI DSS v4.0.1 establishes security requirements for organizations handling payment card data. Applicable to venue point-of-sale systems, ticketing platforms, network segmentation requirements, and any system processing cardholder data in venue environments.",
        "domains": ["technology-and-digital", "security", "financial-operations"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0118",
        "slug": "NIST-CSF-2-0",
        "title": "NIST Cybersecurity Framework 2.0",
        "source_type": "regulatory-document",
        "url": "https://www.nist.gov/cyberframework",
        "description": "NIST Cybersecurity Framework 2.0 provides a comprehensive risk-based approach to managing cybersecurity risk across six functions: Govern, Identify, Protect, Detect, Respond, and Recover. Applicable to venue IT/OT networks, AV systems, and building automation cybersecurity.",
        "domains": ["technology-and-digital", "security"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0119",
        "slug": "Sports-Video-Group",
        "title": "Sports Video Group (SVG)",
        "source_type": "industry-publication",
        "url": "https://www.sportsvideo.org/",
        "description": "Sports Video Group is the industry association for sports production and technology professionals. Publishes technical guidance on broadcast compound design, camera position standards, SMPTE fiber infrastructure, and emerging production technologies for arenas and stadiums.",
        "domains": ["av-and-production"],
        "research_batch": "v2-prompt-06-av-production",
    },
    {
        "num": "0120",
        "slug": "SDVoE-Alliance-AV-over-IP",
        "title": "SDVoE Alliance AV-over-IP Standard",
        "source_type": "trade-association",
        "url": "https://sdvoe.org/",
        "description": "Software Defined Video over Ethernet (SDVoE) Alliance promotes a standards-based platform for AV signal distribution over 10GbE networks. Provides zero-latency, uncompressed 4K video transport used in venue display systems, digital signage networks, and control room applications.",
        "domains": ["av-and-production", "technology-and-digital"],
        "research_batch": "v2-prompt-06-av-production",
    },
]

def write_source(s):
    domains_yaml = "\n".join(f"  - {d}" for d in s["domains"])
    content = f'''---
title: "{s['title']}"
note_type: source
status: draft
created: 2026-04-04
updated: 2026-04-04
source_type: {s['source_type']}
url: "{s['url']}"
accessed: 2026-04-04
description: "{s['description']}"
domains:
{domains_yaml}
research_batch: {s['research_batch']}
tags:
  - source
  - venue-ops
  - batch-04
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
extraction_model: claude-opus-4-6
---

# {s['title']}

{s['description']}

## Source Details

- **Type:** {s['source_type'].replace('-', ' ').title()}
- **URL:** {s['url']}
- **Accessed:** 2026-04-04
- **Research Batch:** {s['research_batch']}
'''
    filename = f"Source-{s['num']}-{s['slug']}.md"
    filepath = os.path.join(SOURCES_DIR, filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return filename

for s in sources:
    fn = write_source(s)
    created_count += 1
    print(f"  Created: {fn}")

print(f"\nSource notes created: {created_count}")

# =============================================================
# STEP 2: CONCEPT NOTES (20 notes)
# =============================================================

concepts = [
    # ── EVENT OPERATIONS (8) ──────────────────────────────────
    {
        "filename": "Event-Operations-Scheduling-Calendar-Management.md",
        "title": "Venue Scheduling and Calendar Management",
        "domain": "event-operations",
        "description": "Multi-use venue calendar management encompassing tiered hold/confirm workflows, event mix optimization, anchor tenant scheduling, and resource allocation across overlapping events in convention centres, arenas, and stadiums.",
        "venue_types": ["convention-centre", "arena", "stadium", "performing-arts-centre", "fairground-exhibition"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "high",
        "sources": [
            "[[Source-0091-IAVM-Blueprint-Event-Management]]",
            "[[Source-0093-Momentus-Technologies-Venue-Management]]",
            "[[Source-0096-Events-Industry-Council]]",
        ],
        "research_batch": "v2-prompt-01-event-ops",
        "child_of": "[[Domain-Event-Operations]]",
        "related_to": [
            "[[Event-Operations-BEO-Client-Services]]",
            "[[Event-Operations-Show-Management]]",
            "[[Booking-And-Sales-Venue-Booking-Lifecycle]]",
        ],
        "supported_by": [
            "[[Source-0093-Momentus-Technologies-Venue-Management]]",
        ],
        "body": """## Overview

Venue scheduling in multi-use facilities requires balancing competing demands from anchor tenants (sports teams, resident companies), touring productions, conventions, and community events. The scheduling function typically operates 12-24 months ahead for major events and manages a pipeline of tentative holds that convert to confirmed bookings.

## Hold/Confirm Workflows

Industry practice uses a tiered hold system where first-option holds give priority to the first party requesting a date. Second and third holds create a queue. When a lower-priority hold receives a firm offer, the venue issues a challenge to higher-priority hold-holders who must confirm or release within a defined window (typically 48-72 hours). Venue management software platforms such as Momentus Technologies automate these workflows.

## Event Mix Optimization

Successful multi-use venues actively manage their event mix to balance revenue, community impact, and facility wear. Arenas typically target 150-200+ event days annually across sports, concerts, family shows, and corporate events. Convention centres optimize for occupancy rate, delegate spending, and room-night generation. The IAVM Framework addresses event mix strategy as a core operational planning function.

## Resource Coordination

Calendar management extends beyond date booking to coordinate shared resources including loading docks, rigging points, catering kitchens, parking, and technical infrastructure. Overlapping events in large convention centres may require simultaneous management of resources across multiple halls and meeting rooms.

## Sources

- [[Source-0091-IAVM-Blueprint-Event-Management]]
- [[Source-0093-Momentus-Technologies-Venue-Management]]
- [[Source-0096-Events-Industry-Council]]""",
    },
    {
        "filename": "Event-Operations-Changeover-Operations.md",
        "title": "Changeover Operations",
        "domain": "event-operations",
        "description": "Physical venue conversion between event configurations including ice-to-court, concert builds, and convention setups. Encompasses crew structures, compressed timelines, union labor coordination, and equipment staging logistics.",
        "venue_types": ["arena", "stadium", "convention-centre", "fairground-exhibition"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles", "employee-experience"],
        "confidence": "high",
        "sources": [
            "[[Source-0091-IAVM-Blueprint-Event-Management]]",
            "[[Source-0095-IATSE-International]]",
            "[[Source-0102-Voyage-Control-Dock-Management]]",
        ],
        "research_batch": "v2-prompt-01-event-ops",
        "child_of": "[[Domain-Event-Operations]]",
        "related_to": [
            "[[Event-Operations-Show-Management]]",
            "[[Event-Operations-Stage-Management]]",
            "[[Logistics-And-Warehouse-Loading-Dock-Operations]]",
        ],
        "body": """## Overview

Changeover operations represent one of the most labor-intensive and time-critical functions in multi-use venue management. A full arena changeover from ice hockey to a concert configuration can require 80-150+ crew members working 12-16 hours to install staging, rigging, floor covering, seating configurations, and production infrastructure.

## Common Changeover Types

Arena changeovers include ice-to-flat floor (concerts, basketball), ice-to-dirt (rodeo, monster trucks), and between sporting configurations (hockey to basketball). Convention centres manage changeovers between exhibit hall configurations, banquet setups, and theater-style arrangements. Stadiums convert between sporting configurations and concert end-stage or center-stage layouts.

## Crew Structures

Changeover crews typically include IATSE stagehands for rigging and production elements, in-house conversion crews for floor systems and seating, and specialized contractors for ice making/removal or turf installation. Union labor agreements govern call times, crew minimums, overtime rates, and meal penalties. Compressed changeover schedules (same-day turnarounds) command premium labor rates.

## Scheduling and Logistics

Changeover scheduling coordinates with loading dock operations for equipment delivery, rigging schedules for overhead work, and building systems teams for HVAC, lighting, and power reconfiguration. Dock management platforms such as Voyage Control help sequence vehicle arrivals during load-in/load-out operations.

## Sources

- [[Source-0091-IAVM-Blueprint-Event-Management]]
- [[Source-0095-IATSE-International]]
- [[Source-0102-Voyage-Control-Dock-Management]]""",
    },
    {
        "filename": "Event-Operations-Show-Management.md",
        "title": "Show Management and Event Day Operations",
        "domain": "event-operations",
        "description": "End-to-end event day supervision encompassing command center operations, run-of-show execution, pre-show briefings, ingress/egress management, and real-time incident coordination across all venue departments.",
        "venue_types": ["all"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles", "guest-experience"],
        "confidence": "high",
        "sources": [
            "[[Source-0091-IAVM-Blueprint-Event-Management]]",
            "[[Source-0100-247-Software-Operations]]",
            "[[Source-0101-WeTrack-Event-Management]]",
        ],
        "research_batch": "v2-prompt-01-event-ops",
        "child_of": "[[Domain-Event-Operations]]",
        "related_to": [
            "[[Event-Operations-Changeover-Operations]]",
            "[[Event-Operations-Radio-Communication-Protocols]]",
            "[[Safety-And-Risk-Emergency-Action-Plans]]",
            "[[Crowd-Management-Ingress-Egress-Modeling]]",
        ],
        "body": """## Overview

Show management is the coordination function that brings all venue departments together for event execution. The show manager or event manager serves as the single point of operational authority on event day, ensuring the run-of-show is executed on schedule while managing real-time adjustments for weather, crowd conditions, artist requirements, and emergencies.

## Command Center Operations

Modern venues operate dedicated event operations centers (EOCs) or command centers staffed by representatives from operations, security, medical, fire safety, guest services, and facility maintenance. Real-time operations platforms such as 24/7 Software provide incident tracking, dispatch, and inspection management. The command center serves as the communication hub linking front-of-house, back-of-house, and external emergency services.

## Run-of-Show

The run-of-show document is the master timeline for event execution, typically organized in 15-minute or 30-minute increments. It sequences door times, pre-show activities, performance segments, intermissions, post-show procedures, and venue clearing. Each line item identifies the responsible department and any dependencies on other departments or external parties.

## Pre-Show Briefings

Industry standard practice calls for a pre-event briefing 60-90 minutes before doors open, attended by all department leads. The briefing covers event-specific details, expected attendance, weather conditions, VIP requirements, known security concerns, and any deviations from standard operating procedures. Larger venues may conduct tiered briefings (senior staff, then departmental briefings).

## Sources

- [[Source-0091-IAVM-Blueprint-Event-Management]]
- [[Source-0100-247-Software-Operations]]
- [[Source-0101-WeTrack-Event-Management]]""",
    },
    {
        "filename": "Event-Operations-BEO-Client-Services.md",
        "title": "Banquet Event Orders and Client Services",
        "domain": "event-operations",
        "description": "Banquet event order (BEO) workflows, pre-event planning cycles, event coordinator roles, exhibitor services guide standards, and post-event survey processes for convention centres and banquet operations.",
        "venue_types": ["convention-centre", "integrated-resort", "arena", "performing-arts-centre"],
        "vef_alignment": ["guest-experience", "operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "high",
        "sources": [
            "[[Source-0093-Momentus-Technologies-Venue-Management]]",
            "[[Source-0096-Events-Industry-Council]]",
            "[[Source-0091-IAVM-Blueprint-Event-Management]]",
        ],
        "research_batch": "v2-prompt-01-event-ops",
        "child_of": "[[Domain-Event-Operations]]",
        "related_to": [
            "[[Event-Operations-Scheduling-Calendar-Management]]",
            "[[Event-Operations-Exhibitor-Services-GSC]]",
            "[[Food-And-Beverage-Banquet-Operations]]",
        ],
        "body": """## Overview

The Banquet Event Order (BEO) is the operational document that translates a client's event requirements into actionable instructions for all venue departments. BEOs detail room setup, audio-visual requirements, food and beverage selections, timing, staffing levels, and special requests. In convention centres, the BEO process typically begins 6-12 months before the event and goes through multiple revision cycles.

## Pre-Event Planning Cycle

The planning cycle follows a structured timeline: initial site visit and requirements gathering, space allocation and floor plan approval, BEO drafting, departmental review, client sign-off, and final distribution. Industry best practice per the Events Industry Council calls for BEO finalization 10-14 business days before the event, though changes within the final week are common and require change order processes.

## Event Coordinator Role

Event coordinators serve as the primary client liaison from booking through post-event follow-up. They translate client requirements into operational specifications, manage the BEO revision process, conduct pre-event walkthroughs, and serve as the client's on-site point of contact during the event. Venue management platforms such as Momentus Technologies support this workflow with integrated CRM and BEO generation.

## Post-Event Processes

Post-event processes include client satisfaction surveys, internal debrief meetings, final billing reconciliation, and lessons-learned documentation. Convention centres typically track Net Promoter Score (NPS) and rebooking rates as key performance indicators for their event services function.

## Sources

- [[Source-0093-Momentus-Technologies-Venue-Management]]
- [[Source-0096-Events-Industry-Council]]
- [[Source-0091-IAVM-Blueprint-Event-Management]]""",
    },
    {
        "filename": "Event-Operations-Exhibitor-Services-GSC.md",
        "title": "Exhibitor Services and General Service Contractors",
        "domain": "event-operations",
        "description": "General service contractor (GSC) operations including Freeman, GES, and Shepard. Covers drayage, material handling, exhibitor services manuals, booth installation, and the contractual relationship between venues, show organizers, and GSCs.",
        "venue_types": ["convention-centre", "fairground-exhibition"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "guest-experience", "systems-processes-clarity-of-roles"],
        "confidence": "high",
        "sources": [
            "[[Source-0094-ESCA-Exhibition-Services]]",
            "[[Source-0097-Freeman-GSC]]",
            "[[Source-0098-GES-Global-Experience-Specialists]]",
        ],
        "research_batch": "v2-prompt-01-event-ops",
        "child_of": "[[Domain-Event-Operations]]",
        "related_to": [
            "[[Event-Operations-BEO-Client-Services]]",
            "[[Logistics-And-Warehouse-Loading-Dock-Operations]]",
            "[[Event-Operations-Changeover-Operations]]",
        ],
        "body": """## Overview

General service contractors (GSCs) are the operational backbone of the trade show and convention industry, providing the labor, equipment, and logistics required to transform empty exhibit halls into functioning exhibitions. The three largest GSCs in North America are Freeman, GES (Global Experience Specialists), and Shepard Exposition Services, collectively handling the majority of major trade shows.

## Drayage and Material Handling

Drayage is the service of receiving, warehousing, and delivering exhibit materials from the loading dock to the booth location. It represents one of the largest single costs for exhibitors and is typically priced per hundredweight (CWT). The Exhibition Services and Contractors Association (ESCA) publishes guidelines for material handling practices and pricing transparency.

## Exhibitor Services Manual

The exhibitor services manual (ESM) is the comprehensive guide distributed to exhibitors detailing all available services, order forms, deadlines, rules, and regulations for a specific show. It covers booth construction guidelines, electrical service ordering, rigging requests, internet connectivity, and material handling schedules. The ESM typically opens for orders 90-120 days before the show.

## Venue-GSC Relationship

The contractual relationship between venues and GSCs varies. Some venues maintain exclusive GSC partnerships while others allow show organizers to select their preferred contractor. The venue provides the facility infrastructure (power, rigging points, loading docks, internet backbone) while the GSC provides the show-specific services layered on top.

## Sources

- [[Source-0094-ESCA-Exhibition-Services]]
- [[Source-0097-Freeman-GSC]]
- [[Source-0098-GES-Global-Experience-Specialists]]""",
    },
    {
        "filename": "Event-Operations-Event-Settlement.md",
        "title": "Event Settlement and Financial Reconciliation",
        "domain": "event-operations",
        "description": "Post-event financial reconciliation processes including GBOR/NBOR calculations, deal structures (flat guarantee, versus deals, co-promotion, promoter profit splits), F&B settlement, ancillary revenue accounting, and settlement timelines.",
        "venue_types": ["arena", "stadium", "performing-arts-centre", "amphitheatre"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "high",
        "sources": [
            "[[Source-0092-IAVM-Arenas-Performance-Reporting]]",
            "[[Source-0099-Prism-FM-Settlement]]",
            "[[Source-0091-IAVM-Blueprint-Event-Management]]",
        ],
        "research_batch": "v2-prompt-01-event-ops",
        "child_of": "[[Domain-Event-Operations]]",
        "related_to": [
            "[[Event-Operations-Show-Management]]",
            "[[Financial-Operations-Revenue-Recognition]]",
        ],
        "body": """## Overview

Event settlement is the post-event financial reconciliation process that determines the final revenue distribution between the venue, promoter, and artist. The settlement process follows standardized methodologies documented in the IAVM Arenas Performance Reporting Handbook, which defines how Gross Box Office Revenue (GBOR) and Net Box Office Revenue (NBOR) are calculated.

## Deal Structures

Live entertainment deal structures include flat guarantee (fixed rental fee regardless of ticket sales), versus deals (the greater of a guarantee or a percentage of NBOR), co-promotion (venue shares in promotion risk and reward), and promoter profit deals (venue receives a percentage of promoter profit after expenses). Each structure carries different risk profiles and requires different settlement calculations.

## GBOR/NBOR Calculations

GBOR represents total ticket revenue at face value. NBOR is calculated by deducting facility fees, ticket rebates, taxes, and other agreed-upon deductions from GBOR. The IAVM handbook standardizes these calculations to enable benchmarking across the arena industry. Settlement platforms such as Prism.fm automate these calculations and manage the documentation workflow.

## Settlement Timeline and Components

Industry standard calls for preliminary settlement within 5-7 business days of the event, with final settlement within 30 days. Settlement accounts for ticket revenue, facility fees, food and beverage splits, merchandise commissions, parking revenue, sponsorship activations, and production cost reimbursements. Each revenue stream has its own split formula defined in the event contract.

## Sources

- [[Source-0092-IAVM-Arenas-Performance-Reporting]]
- [[Source-0099-Prism-FM-Settlement]]
- [[Source-0091-IAVM-Blueprint-Event-Management]]""",
    },
    {
        "filename": "Event-Operations-Stage-Management.md",
        "title": "Stage Management",
        "domain": "event-operations",
        "description": "Stage manager responsibilities including prompt book maintenance, cue calling, rehearsal management, show calling, and coordination with IATSE crews. Covers both theatrical and corporate/convention stage management practices.",
        "venue_types": ["performing-arts-centre", "convention-centre", "arena", "amphitheatre"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles", "employee-experience"],
        "confidence": "high",
        "sources": [
            "[[Source-0103-USITT-Stage-Management]]",
            "[[Source-0095-IATSE-International]]",
            "[[Source-0091-IAVM-Blueprint-Event-Management]]",
        ],
        "research_batch": "v2-prompt-01-event-ops",
        "child_of": "[[Domain-Event-Operations]]",
        "related_to": [
            "[[Event-Operations-Show-Management]]",
            "[[Event-Operations-Changeover-Operations]]",
            "[[Av-And-Production-Entertainment-Lighting-Control]]",
        ],
        "body": """## Overview

The stage manager is the central coordination point for all technical and performance elements during rehearsals and live performances. In professional theatre and touring productions, the stage manager calls all lighting, sound, and scenic cues from the prompt book, coordinates with the IATSE crew, and serves as the communication hub between performers, directors, and technical departments.

## Prompt Book and Cue Calling

The prompt book (also called the calling script) is the master document containing all cue placements, blocking notations, and technical notes. Cues are called using a standardized verbal protocol: warning, standby, and go. USITT publishes guidelines for stage management documentation and cue calling conventions that serve as the industry reference.

## Rehearsal Management

Stage managers manage the rehearsal process including scheduling, maintaining rehearsal reports, tracking blocking changes, and communicating production notes to all departments. In convention and corporate environments, stage managers coordinate presenter rehearsals, manage teleprompter operations, and ensure technical run-throughs are completed before doors open.

## IATSE Crew Coordination

In union venues, the stage manager works within IATSE labor agreements that define crew call procedures, overtime rules, meal breaks, and departmental jurisdiction. The stage manager coordinates with the head carpenter, head electrician, head of props, and head of sound to ensure all technical elements are prepared and executed according to the production schedule.

## Sources

- [[Source-0103-USITT-Stage-Management]]
- [[Source-0095-IATSE-International]]
- [[Source-0091-IAVM-Blueprint-Event-Management]]""",
    },
    {
        "filename": "Event-Operations-Radio-Communication-Protocols.md",
        "title": "Radio Communication Protocols",
        "domain": "event-operations",
        "description": "Two-way radio communication systems for venue operations including DMR, P25, and TETRA digital standards, channel allocation strategies, radio discipline protocols, and command center communication integration.",
        "venue_types": ["all"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "medium",
        "sources": [
            "[[Source-0091-IAVM-Blueprint-Event-Management]]",
            "[[Source-0104-FirstNet-Public-Safety-Broadband]]",
            "[[Source-0100-247-Software-Operations]]",
        ],
        "research_batch": "v2-prompt-01-event-ops",
        "child_of": "[[Domain-Event-Operations]]",
        "related_to": [
            "[[Event-Operations-Show-Management]]",
            "[[Safety-And-Risk-Emergency-Action-Plans]]",
            "[[Technology-And-Digital-DAS-In-Building-Wireless]]",
        ],
        "body": """## Overview

Two-way radio systems are the primary real-time communication backbone for venue operations during events. Effective radio communication enables coordinated response across security, operations, medical, fire safety, guest services, and management teams. Venues typically deploy digital radio systems using DMR (Digital Mobile Radio), P25 (Project 25), or TETRA (Terrestrial Trunked Radio) protocols.

## Channel Allocation

Venue radio channel plans allocate dedicated frequencies to each operational department with a common command channel monitored by all department supervisors. A typical large venue radio plan includes channels for operations, security, medical, fire/life safety, parking, guest services, F&B, maintenance, and an emergency-only command channel. Channel discipline requires users to identify themselves and keep transmissions brief.

## Digital Radio Standards

DMR (ETSI TS 102 361) is the most common digital standard in commercial venue operations, offering encryption, text messaging, and GPS tracking. P25 (TIA-102) is used primarily by public safety agencies and some venues that need interoperability with police and fire departments. TETRA is more common in European and international venue deployments.

## Integration with Command Centers

Modern command center operations integrate radio communications with incident management software platforms such as 24/7 Software, enabling radio traffic to be logged, incidents to be dispatched, and response times to be tracked. FirstNet provides dedicated public safety broadband connectivity that supplements radio systems during major events.

## Sources

- [[Source-0091-IAVM-Blueprint-Event-Management]]
- [[Source-0104-FirstNet-Public-Safety-Broadband]]
- [[Source-0100-247-Software-Operations]]""",
    },
    # ── AV AND PRODUCTION (9) ─────────────────────────────────
    {
        "filename": "Av-And-Production-Line-Array-Sound-Systems.md",
        "title": "Line Array Sound Systems",
        "domain": "av-and-production",
        "description": "Line array PA system design for arenas and stadiums, covering Speech Transmission Index (STI) targets, AVIXA Audio Coverage Uniformity (ACU) standards, distributed audio architectures, and permanent vs. touring sound system considerations.",
        "venue_types": ["arena", "stadium", "convention-centre", "performing-arts-centre", "amphitheatre"],
        "vef_alignment": ["guest-experience", "operational-efficiency-productivity-creativity", "innovation-and-continuous-improvement"],
        "confidence": "high",
        "sources": [
            "[[Source-0106-AVIXA-Standards]]",
            "[[Source-0115-Audinate-Dante-Audio-Networking]]",
            "[[Source-0108-ESTA-Technical-Standards]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Av-And-Production]]",
        "related_to": [
            "[[Av-And-Production-Networked-Audio-Infrastructure]]",
            "[[Av-And-Production-Acoustic-Treatment]]",
            "[[Inclusivity-And-Accessibility-Assistive-Listening-Systems]]",
        ],
        "body": """## Overview

Line array loudspeaker systems are the standard PA configuration for large venues, using multiple transducer elements arrayed vertically to create a controlled, even coverage pattern across the audience area. Permanent installations in arenas and stadiums use distributed line arrays to achieve consistent sound pressure levels from front rows to upper decks, while touring productions bring additional systems optimized for music reproduction.

## Performance Standards

AVIXA's Audio Coverage Uniformity (ACU) standard provides measurable criteria for evaluating sound system performance. Speech Transmission Index (STI) targets for venue PA systems typically require a minimum of 0.50 (fair) for general announcements and 0.60+ (good) for life safety communications. These measurements account for reverberation, background noise, and system equalization.

## Permanent vs. Touring Systems

Most major venues maintain a permanent distributed sound system for announcements, background music, and sports presentation while accommodating touring concert systems that fly from the rigging grid. The permanent system typically covers concourses, concession areas, and provides the base layer for sports and corporate events. Touring line arrays are optimized for full-range music reproduction at concert sound pressure levels.

## Distributed Audio Architecture

Modern venue audio distribution uses networked protocols such as Dante (Digital Audio Network Through Ethernet) to route hundreds of audio channels across the facility over standard Ethernet infrastructure. This replaces legacy analog snake runs with a flexible, scalable digital backbone that serves the permanent PA, broadcast feeds, hearing assistance systems, and production audio simultaneously.

## Sources

- [[Source-0106-AVIXA-Standards]]
- [[Source-0115-Audinate-Dante-Audio-Networking]]
- [[Source-0108-ESTA-Technical-Standards]]""",
    },
    {
        "filename": "Av-And-Production-Networked-Audio-Infrastructure.md",
        "title": "Networked Audio Infrastructure",
        "domain": "av-and-production",
        "description": "Dante, AVB/TSN, and AES67 networked audio protocols for venue production environments. Covers production VLANs, multicast management, redundancy architectures, and routing hundreds of bidirectional audio channels over Ethernet.",
        "venue_types": ["arena", "stadium", "convention-centre", "performing-arts-centre"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "ai-and-digital-transformation", "innovation-and-continuous-improvement"],
        "confidence": "high",
        "sources": [
            "[[Source-0115-Audinate-Dante-Audio-Networking]]",
            "[[Source-0106-AVIXA-Standards]]",
            "[[Source-0108-ESTA-Technical-Standards]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Av-And-Production]]",
        "related_to": [
            "[[Av-And-Production-Line-Array-Sound-Systems]]",
            "[[Av-And-Production-Broadcast-Infrastructure]]",
            "[[Technology-And-Digital-Venue-Cybersecurity]]",
        ],
        "body": """## Overview

Networked audio has replaced analog point-to-point cabling as the standard infrastructure for professional venue audio distribution. By transporting audio as packetized data over Ethernet, networked audio systems provide flexible routing, scalable channel counts, and simplified cabling while maintaining the low latency required for live production.

## Dominant Protocols

Dante (Audinate) is the most widely deployed networked audio protocol in professional AV, supporting up to 512 bidirectional audio channels per network with latency as low as 150 microseconds. AVB/TSN (Audio Video Bridging / Time-Sensitive Networking) is an IEEE standard (802.1BA) offering guaranteed quality of service at the network switch level. AES67 provides an interoperability standard allowing different networked audio protocols to exchange streams.

## Network Architecture

Venue audio networks require dedicated VLANs separated from corporate IT and building management traffic. Best practice calls for redundant primary and secondary networks with automatic failover. Multicast traffic management through IGMP snooping prevents audio streams from flooding non-participating switch ports. Network switches must support PTPv2 (IEEE 1588) clock synchronization for sample-accurate audio delivery.

## Integration Points

Networked audio infrastructure connects permanent PA systems, mixing consoles, broadcast feeds, recording systems, hearing assistance transmitters, and production intercoms. The convergence of these systems on a single network backbone reduces cable plant costs and enables centralized monitoring and management.

## Sources

- [[Source-0115-Audinate-Dante-Audio-Networking]]
- [[Source-0106-AVIXA-Standards]]
- [[Source-0108-ESTA-Technical-Standards]]""",
    },
    {
        "filename": "Av-And-Production-LED-Display-Systems.md",
        "title": "LED Display Systems",
        "domain": "av-and-production",
        "description": "Venue LED display technology including scoreboards, ribbon boards, center-hung video boards, fascia displays, and exterior marquees. Covers pixel pitch selection, AVIXA DISCAS standard, content management, and display lifecycle planning.",
        "venue_types": ["arena", "stadium", "convention-centre", "amphitheatre"],
        "vef_alignment": ["guest-experience", "innovation-and-continuous-improvement", "operational-efficiency-productivity-creativity"],
        "confidence": "high",
        "sources": [
            "[[Source-0106-AVIXA-Standards]]",
            "[[Source-0120-SDVoE-Alliance-AV-over-IP]]",
            "[[Source-0119-Sports-Video-Group]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Av-And-Production]]",
        "related_to": [
            "[[Av-And-Production-Broadcast-Infrastructure]]",
            "[[Av-And-Production-Entertainment-Lighting-Control]]",
            "[[Commercial-And-Revenue-Naming-Rights-Sponsorship]]",
        ],
        "body": """## Overview

LED display systems are central to the modern venue experience, serving game presentation, sponsor activation, wayfinding, and emergency communication functions. A major arena or stadium LED display package typically includes a center-hung main video board, auxiliary scoreboards, ribbon boards along fascias, concourse displays, and exterior signage.

## Pixel Pitch Selection

Pixel pitch (the distance between LED pixel centers, measured in millimeters) determines viewing resolution at a given distance. AVIXA's DISCAS (Digital Signage Display Image Comparison and Assessment Standard) provides a methodology for specifying display resolution based on viewing distance and content type. Center-hung arena boards typically use 4mm-8mm pixel pitch, while ribbon boards and concourse displays may range from 2mm-6mm depending on viewing distance.

## Display Types by Application

Center-hung video boards are the primary presentation surface for sports scores, replays, and entertainment content. Ribbon boards (continuous LED strips along seating fascias) serve as premium sponsorship inventory and real-time statistics displays. End-zone or outfield boards provide additional video surfaces for replays and sponsor content. Convention centre displays include configurable LED walls for general session stages and digital wayfinding.

## Content Management and Signal Distribution

Modern display systems use networked video distribution (SDVoE or NDI) to route content from production control rooms to multiple display surfaces. Content management systems schedule sponsor rotations, integrate with scoring systems, and switch between live camera feeds, pre-produced content, and data-driven graphics.

## Sources

- [[Source-0106-AVIXA-Standards]]
- [[Source-0120-SDVoE-Alliance-AV-over-IP]]
- [[Source-0119-Sports-Video-Group]]""",
    },
    {
        "filename": "Av-And-Production-Entertainment-Lighting-Control.md",
        "title": "Entertainment Lighting Control",
        "domain": "av-and-production",
        "description": "Lighting control protocols for venue production including DMX512-A, sACN (ANSI E1.31), and Art-Net. Covers LED fixture technology, architectural lighting integration, moving light programming, and the convergence of entertainment and architectural lighting systems.",
        "venue_types": ["arena", "performing-arts-centre", "convention-centre", "stadium", "amphitheatre"],
        "vef_alignment": ["guest-experience", "operational-efficiency-productivity-creativity", "innovation-and-continuous-improvement"],
        "confidence": "high",
        "sources": [
            "[[Source-0108-ESTA-Technical-Standards]]",
            "[[Source-0106-AVIXA-Standards]]",
            "[[Source-0103-USITT-Stage-Management]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Av-And-Production]]",
        "related_to": [
            "[[Av-And-Production-Entertainment-Rigging-Systems]]",
            "[[Event-Operations-Stage-Management]]",
            "[[Facilities-And-Building-Systems-Critical-System-Redundancy]]",
        ],
        "body": """## Overview

Entertainment lighting in venues spans from permanent architectural fixtures through touring concert lighting rigs. The lighting control infrastructure must support both environments through standardized protocols, power distribution systems, and rigging infrastructure designed for rapid changeover between configurations.

## Control Protocols

DMX512-A (ANSI E1.11) is the foundational lighting control protocol, transmitting 512 channels of dimmer/parameter data per universe over 5-pin XLR cables. sACN (Streaming ACN, ANSI E1.31) extends DMX over Ethernet, supporting thousands of universes for large-scale installations. Art-Net is a competing Ethernet-based protocol with similar capabilities. ESTA publishes and maintains these standards through its Technical Standards Program.

## LED Fixture Technology

LED fixtures have largely replaced conventional tungsten and discharge sources in venue installations due to lower power consumption, reduced heat output, extended lamp life, and variable color temperature. Modern LED fixtures incorporate RGBW or RGBAL color mixing, providing a wide gamut while maintaining high CRI (Color Rendering Index) for broadcast-quality lighting.

## Architectural Integration

Multi-use venues increasingly design lighting systems that serve both architectural and entertainment functions. Programmable LED house lights can shift from warm white for corporate events to saturated colors for concerts. This convergence requires control systems that bridge building management protocols (DALI, BACnet) with entertainment protocols (DMX512, sACN).

## Sources

- [[Source-0108-ESTA-Technical-Standards]]
- [[Source-0106-AVIXA-Standards]]
- [[Source-0103-USITT-Stage-Management]]""",
    },
    {
        "filename": "Av-And-Production-Entertainment-Rigging-Systems.md",
        "title": "Entertainment Rigging Systems",
        "domain": "av-and-production",
        "description": "Overhead rigging infrastructure for venues including structural grids, chain hoists, automated rigging systems, ANSI E1.6 compliance, ETCP certification for riggers, and rigging safety inspection protocols.",
        "venue_types": ["arena", "performing-arts-centre", "convention-centre", "stadium", "amphitheatre"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "high",
        "sources": [
            "[[Source-0112-ANSI-E1-6-Powered-Hoists]]",
            "[[Source-0109-ETCP-Certification]]",
            "[[Source-0108-ESTA-Technical-Standards]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Av-And-Production]]",
        "related_to": [
            "[[Av-And-Production-Entertainment-Lighting-Control]]",
            "[[Event-Operations-Changeover-Operations]]",
            "[[Safety-And-Risk-Emergency-Action-Plans]]",
        ],
        "governed_by": [
            "[[Source-0112-ANSI-E1-6-Powered-Hoists]]",
        ],
        "body": """## Overview

Entertainment rigging systems provide the overhead infrastructure for suspending lighting, sound, video, scenic elements, and performer flying effects. In arenas and convention centres, rigging loads are typically supported by a structural steel grid with rated attachment points, while theatres use counterweight fly systems or motorized line sets.

## ANSI E1.6 and Safety Standards

ANSI E1.6-1 (Entertainment Technology -- Powered Hoist Systems) establishes requirements for design, manufacture, installation, and use of powered hoists in entertainment applications. The standard addresses load rating methodology, braking systems, safety factors, limit switches, and control system requirements. Compliance with E1.6 is considered the baseline standard for entertainment rigging safety.

## ETCP Certification

The Entertainment Technician Certification Program (ETCP), administered by ESTA, provides portable certification for entertainment riggers in two tracks: Arena and Theatre. ETCP certification validates competency in load calculations, hardware inspection, rigging geometry, safety procedures, and relevant codes and standards. Many venues require ETCP certification for head rigger positions and for riggers working at height.

## Rigging Inspection Protocols

Venue rigging systems require regular inspection of structural attachment points, chain hoists, wire rope, shackles, and control systems. Pre-event rigging inspections verify that all overhead loads are within rated capacities and properly secured. Annual comprehensive inspections by qualified engineers assess structural integrity of the rigging grid and all permanent rigging hardware.

## Sources

- [[Source-0112-ANSI-E1-6-Powered-Hoists]]
- [[Source-0109-ETCP-Certification]]
- [[Source-0108-ESTA-Technical-Standards]]""",
    },
    {
        "filename": "Av-And-Production-Broadcast-Infrastructure.md",
        "title": "Broadcast Infrastructure",
        "domain": "av-and-production",
        "description": "Venue broadcast infrastructure including broadcast compounds, permanent camera positions, SMPTE fiber connectivity, EVS replay systems, VAR (Video Assistant Referee) installations, and the interface between venue production and external broadcasters.",
        "venue_types": ["arena", "stadium"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "innovation-and-continuous-improvement"],
        "confidence": "high",
        "sources": [
            "[[Source-0119-Sports-Video-Group]]",
            "[[Source-0113-EVS-Broadcast-Equipment]]",
            "[[Source-0114-Evertz-DreamCatcher]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Av-And-Production]]",
        "related_to": [
            "[[Av-And-Production-LED-Display-Systems]]",
            "[[Av-And-Production-Networked-Audio-Infrastructure]]",
            "[[Av-And-Production-Hybrid-Event-Streaming]]",
        ],
        "body": """## Overview

Broadcast infrastructure enables the distribution of live event content to television networks, streaming platforms, and in-venue display systems. Major arenas and stadiums are designed with permanent broadcast infrastructure that reduces setup time and cost for regular television productions while accommodating the varying requirements of different broadcast rights holders.

## Broadcast Compound

The broadcast compound is a dedicated area (typically at loading dock level or exterior to the venue) where mobile production trucks park and connect to the venue's broadcast infrastructure. Permanent provisions include power drops (typically 200A-400A three-phase), SMPTE hybrid fiber connections to camera positions, dedicated internet connectivity, and HVAC for truck cooling.

## Camera Positions and Connectivity

Permanent camera positions are built into the venue structure at key locations including center ice/court, corner positions, overhead (skycam rail or cable systems), and goal/basket positions. SMPTE 311M hybrid fiber-optic cable carries video, audio, data, and power between camera positions and the broadcast compound over a single cable, simplifying setup and reducing changeover time.

## Replay and VAR Systems

EVS XT-VIA and LSM-VIA servers are the industry standard for live sports replay, providing multi-channel ingest from all camera feeds with instant access for replay operators and highlight producers. Video Assistant Referee (VAR) installations require dedicated camera feeds, isolated review positions, and communication systems linking the VAR booth to on-field officials. Evertz DreamCatcher provides a software-defined alternative for replay and highlight production.

## Sources

- [[Source-0119-Sports-Video-Group]]
- [[Source-0113-EVS-Broadcast-Equipment]]
- [[Source-0114-Evertz-DreamCatcher]]""",
    },
    {
        "filename": "Av-And-Production-Hybrid-Event-Streaming.md",
        "title": "Hybrid Event Streaming Infrastructure",
        "domain": "av-and-production",
        "description": "Built-in broadcast studios, redundant streaming connectivity, and hybrid event production infrastructure for convention centres and multi-use venues. Covers encoding, CDN integration, and the convergence of in-person and virtual event delivery.",
        "venue_types": ["convention-centre", "arena", "performing-arts-centre", "university-venue"],
        "vef_alignment": ["guest-experience", "innovation-and-continuous-improvement", "ai-and-digital-transformation"],
        "confidence": "medium",
        "sources": [
            "[[Source-0106-AVIXA-Standards]]",
            "[[Source-0119-Sports-Video-Group]]",
            "[[Source-0120-SDVoE-Alliance-AV-over-IP]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Av-And-Production]]",
        "related_to": [
            "[[Av-And-Production-Broadcast-Infrastructure]]",
            "[[Technology-And-Digital-Venue-Cybersecurity]]",
            "[[Event-Operations-Show-Management]]",
        ],
        "body": """## Overview

Hybrid event infrastructure enables venues to deliver simultaneous in-person and virtual event experiences. Convention centres have invested in permanent streaming capabilities including built-in broadcast studios, production control rooms, and redundant internet connectivity to support the growing demand for hybrid conferences, corporate meetings, and live-streamed performances.

## Built-In Production Facilities

Modern convention centres incorporate dedicated broadcast studios and production control rooms equipped with multi-camera switching, graphics generation, audio mixing, and encoding hardware. These facilities provide a turnkey streaming solution for event organizers without requiring external production trucks. Studio spaces range from simple single-camera setups to full multi-camera environments with virtual set capability.

## Streaming Architecture

Hybrid event streaming requires redundant encoding (primary and backup streams), content delivery network (CDN) integration, and sufficient upstream bandwidth to support multiple simultaneous streams. Venues typically provision dedicated internet circuits separate from general attendee Wi-Fi to ensure streaming quality. Encoding formats include RTMP for platform ingest and SRT for contribution-quality feeds between venues.

## Virtual Audience Integration

Effective hybrid events incorporate virtual audience participation through Q&A platforms, polling, chat moderation, and virtual networking tools. The production workflow must manage presenter confidence monitors showing both in-room and virtual audiences, audio mixing that incorporates remote participants, and graphics that serve both display environments.

## Sources

- [[Source-0106-AVIXA-Standards]]
- [[Source-0119-Sports-Video-Group]]
- [[Source-0120-SDVoE-Alliance-AV-over-IP]]""",
    },
    {
        "filename": "Av-And-Production-Production-Power-Distribution.md",
        "title": "Production Power Distribution",
        "domain": "av-and-production",
        "description": "Temporary and permanent power distribution for venue production including Cam-Lok and Powerlock connectors, 400A 3-phase services, NFPA 70/70E compliance, ANSI E1.17 recognition, and the interface between building electrical systems and production power requirements.",
        "venue_types": ["arena", "convention-centre", "performing-arts-centre", "stadium", "amphitheatre", "fairground-exhibition"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "high",
        "sources": [
            "[[Source-0110-NFPA-70-NEC]]",
            "[[Source-0111-NFPA-70E-Electrical-Safety]]",
            "[[Source-0108-ESTA-Technical-Standards]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Av-And-Production]]",
        "related_to": [
            "[[Av-And-Production-Entertainment-Lighting-Control]]",
            "[[Av-And-Production-Entertainment-Rigging-Systems]]",
            "[[Facilities-And-Building-Systems-Critical-System-Redundancy]]",
        ],
        "governed_by": [
            "[[Source-0110-NFPA-70-NEC]]",
            "[[Source-0111-NFPA-70E-Electrical-Safety]]",
        ],
        "body": """## Overview

Production power distribution provides the electrical infrastructure connecting venue building power to touring and in-house production equipment. Large-scale productions require substantial power capacity, with major concert tours drawing 400A-1200A of three-phase power for lighting, sound, video, and stage machinery. The interface between permanent building electrical and temporary production power is governed by NFPA 70 (National Electrical Code) and NFPA 70E (Electrical Safety).

## Connector Standards

Cam-Lok (single-pole cam-type) connectors are the industry standard for production power distribution in North America, available in ratings from 200A to 400A. Powerlock connectors handle higher current applications up to 660A per phase. Color coding follows NEC convention: black/red/blue for phases A/B/C, white for neutral, and green for ground. ESTA's ANSI E1.17 provides additional recognition of entertainment industry electrical practices.

## Venue Power Infrastructure

Venues designed for production use provide dedicated power drops at stage positions, rigging grid locations, and broadcast compound areas. A well-designed arena or convention centre provides multiple 400A 3-phase disconnect switches at floor level and catwalk level, with clearly labeled panel schedules and overcurrent protection sized for production loads.

## Safety Requirements

NFPA 70E requires arc flash risk assessment for all electrical work, including production power connections. Personnel connecting production power must use appropriate PPE based on the incident energy level at the disconnect. Lockout/tagout procedures apply to all production power disconnects. Ground fault monitoring and proper bonding are required for all temporary electrical installations.

## Sources

- [[Source-0110-NFPA-70-NEC]]
- [[Source-0111-NFPA-70E-Electrical-Safety]]
- [[Source-0108-ESTA-Technical-Standards]]""",
    },
    {
        "filename": "Av-And-Production-Acoustic-Treatment.md",
        "title": "Acoustic Treatment and Venue Acoustics",
        "domain": "av-and-production",
        "description": "Venue acoustic design and treatment covering RT60 reverberation targets, absorptive panel systems, multi-use venue acoustic challenges, esports venue acoustics, and the relationship between architectural acoustics and sound system performance.",
        "venue_types": ["arena", "performing-arts-centre", "convention-centre", "stadium"],
        "vef_alignment": ["guest-experience", "operational-efficiency-productivity-creativity"],
        "confidence": "medium",
        "sources": [
            "[[Source-0106-AVIXA-Standards]]",
            "[[Source-0108-ESTA-Technical-Standards]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Av-And-Production]]",
        "related_to": [
            "[[Av-And-Production-Line-Array-Sound-Systems]]",
            "[[Inclusivity-And-Accessibility-Assistive-Listening-Systems]]",
        ],
        "body": """## Overview

Acoustic treatment addresses the interaction between sound energy and the venue environment. In multi-use venues, acoustic design must balance competing requirements: concerts benefit from some reverberation for musical warmth, while speech intelligibility for corporate events and sports announcements requires controlled reverberation. This tension makes acoustic treatment one of the most challenging aspects of multi-use venue design.

## Reverberation Time (RT60)

RT60 measures the time for sound to decay by 60 decibels after the source stops. Target RT60 values vary by venue function: performing arts halls target 1.5-2.2 seconds for orchestral music, while arenas optimized for speech intelligibility target 1.5-2.5 seconds at mid-frequencies. Convention centre meeting rooms typically target 0.8-1.2 seconds. Multi-use venues often compromise in the 1.8-2.5 second range.

## Treatment Approaches

Absorptive panels reduce reverberation by converting sound energy to heat. Materials include fabric-wrapped fiberglass, perforated metal with acoustic backing, and specialized acoustic ceiling systems. Variable acoustic systems (retractable curtains, rotating panels, inflatable chambers) allow venues to adjust reverberation time for different event types, though these systems add significant cost and maintenance complexity.

## Esports and Emerging Applications

Dedicated esports venues and broadcast studios within larger venues require very low RT60 values (0.4-0.8 seconds) to support clear commentary, minimize acoustic bleed between competitor stations, and provide broadcast-quality audio environments. These spaces often use comprehensive room-within-a-room construction to achieve the required isolation and absorption levels.

## Sources

- [[Source-0106-AVIXA-Standards]]
- [[Source-0108-ESTA-Technical-Standards]]""",
    },
    # ── TECHNOLOGY AND DIGITAL (2) ────────────────────────────
    {
        "filename": "Technology-And-Digital-Venue-Cybersecurity.md",
        "title": "Venue Cybersecurity",
        "domain": "technology-and-digital",
        "description": "Cybersecurity frameworks and practices for venue environments covering NIST CSF 2.0 implementation, PCI DSS v4.0.1 compliance for payment systems, network segmentation between IT/OT/AV systems, and AVIXA RP-C303.01 AV security guidance.",
        "venue_types": ["all"],
        "vef_alignment": ["systems-processes-clarity-of-roles", "ai-and-digital-transformation", "data-management-and-architecture"],
        "confidence": "high",
        "sources": [
            "[[Source-0118-NIST-CSF-2-0]]",
            "[[Source-0117-PCI-DSS-v4]]",
            "[[Source-0106-AVIXA-Standards]]",
        ],
        "research_batch": "v2-prompt-05-tech-digital",
        "child_of": "[[Domain-Technology-And-Digital]]",
        "related_to": [
            "[[Av-And-Production-Networked-Audio-Infrastructure]]",
            "[[Technology-And-Digital-DAS-In-Building-Wireless]]",
            "[[Facilities-And-Building-Systems-Critical-System-Redundancy]]",
        ],
        "governed_by": [
            "[[Source-0118-NIST-CSF-2-0]]",
            "[[Source-0117-PCI-DSS-v4]]",
        ],
        "body": """## Overview

Venue cybersecurity addresses the protection of interconnected technology systems that underpin modern venue operations. Venues operate complex network environments spanning corporate IT, building automation (OT), audio-visual production, point-of-sale, ticketing, access control, and public Wi-Fi. Each network segment carries different risk profiles and compliance requirements.

## NIST Cybersecurity Framework 2.0

NIST CSF 2.0 provides a risk-based approach organized around six functions: Govern, Identify, Protect, Detect, Respond, and Recover. For venues, the Govern function is particularly important as it establishes the organizational context for cybersecurity decisions across departments that may not traditionally view themselves as technology stakeholders (F&B, operations, guest services).

## PCI DSS v4.0.1

PCI DSS v4.0.1 governs all systems that store, process, or transmit payment card data. In venue environments, this encompasses point-of-sale terminals, ticketing systems, premium seating ordering systems, and parking payment kiosks. Key requirements include network segmentation isolating cardholder data environments, encryption of card data in transit and at rest, and regular vulnerability scanning.

## AV System Security

AVIXA RP-C303.01 addresses cybersecurity for networked AV systems, which are frequently overlooked in venue security assessments. AV control systems, networked displays, streaming encoders, and production networks present attack surfaces that can compromise venue operations. Best practice calls for dedicated AV VLANs, access control lists restricting traffic between AV and corporate networks, and regular firmware updates for AV equipment.

## Sources

- [[Source-0118-NIST-CSF-2-0]]
- [[Source-0117-PCI-DSS-v4]]
- [[Source-0106-AVIXA-Standards]]""",
    },
    {
        "filename": "Technology-And-Digital-DAS-In-Building-Wireless.md",
        "title": "Distributed Antenna Systems and In-Building Wireless",
        "domain": "technology-and-digital",
        "description": "DAS (Distributed Antenna Systems), ERCES (Emergency Responder Communication Enhancement Systems), FirstNet Band 14 integration, neutral-host architectures, and NFPA 1225 compliance for in-building wireless coverage in large venue structures.",
        "venue_types": ["arena", "stadium", "convention-centre", "integrated-resort"],
        "vef_alignment": ["guest-experience", "systems-processes-clarity-of-roles", "ai-and-digital-transformation"],
        "confidence": "high",
        "sources": [
            "[[Source-0104-FirstNet-Public-Safety-Broadband]]",
            "[[Source-0105-NFPA-1225-Emergency-Communications]]",
            "[[Source-0118-NIST-CSF-2-0]]",
        ],
        "research_batch": "v2-prompt-05-tech-digital",
        "child_of": "[[Domain-Technology-And-Digital]]",
        "related_to": [
            "[[Event-Operations-Radio-Communication-Protocols]]",
            "[[Technology-And-Digital-Venue-Cybersecurity]]",
            "[[Safety-And-Risk-Emergency-Action-Plans]]",
        ],
        "governed_by": [
            "[[Source-0105-NFPA-1225-Emergency-Communications]]",
        ],
        "body": """## Overview

Distributed Antenna Systems (DAS) provide cellular and public safety radio coverage inside large venue structures where building materials attenuate outdoor signals. Modern venue DAS installations serve three distinct functions: commercial cellular service for attendees, public safety radio enhancement for first responders (ERCES), and increasingly, dedicated FirstNet (Band 14) coverage for public safety broadband.

## ERCES and NFPA 1225

Emergency Responder Communication Enhancement Systems (ERCES) are required by NFPA 1225 and adopted fire codes in most jurisdictions for buildings where in-building radio coverage for fire and police frequencies falls below acceptable thresholds. NFPA 1225 specifies minimum signal strength requirements, battery backup duration (typically 24 hours standby plus 2 hours of full operation), and annual testing protocols.

## Neutral-Host Architecture

Most venue DAS installations use a neutral-host architecture where a single distributed antenna infrastructure serves multiple cellular carriers simultaneously. This approach reduces the number of antennas and cable runs compared to carrier-specific installations. The venue or a third-party DAS operator provides the infrastructure, and carriers connect their base station equipment to feed the shared antenna system.

## FirstNet Integration

FirstNet, the nationwide public safety broadband network operating on Band 14 (758-768 MHz / 788-798 MHz), provides dedicated LTE connectivity with priority and preemption capabilities for first responders. Venue DAS installations increasingly incorporate FirstNet as a dedicated public safety broadband layer alongside commercial cellular and legacy land mobile radio (LMR) enhancement.

## Sources

- [[Source-0104-FirstNet-Public-Safety-Broadband]]
- [[Source-0105-NFPA-1225-Emergency-Communications]]
- [[Source-0118-NIST-CSF-2-0]]""",
    },
    # ── INCLUSIVITY AND ACCESSIBILITY (1) ─────────────────────
    {
        "filename": "Inclusivity-And-Accessibility-Assistive-Listening-Systems.md",
        "title": "Assistive Listening Systems",
        "domain": "inclusivity-and-accessibility",
        "description": "Assistive listening system technologies and compliance requirements covering ADA Section 219, hearing loop systems (IEC 60118-4), RF and infrared systems, Wi-Fi-based ALS, and real-time captioning integration for venue accessibility.",
        "venue_types": ["all"],
        "vef_alignment": ["guest-experience", "systems-processes-clarity-of-roles"],
        "confidence": "high",
        "sources": [
            "[[Source-0116-Listen-Technologies-ALS]]",
            "[[Source-0106-AVIXA-Standards]]",
            "[[Source-0107-AVIXA-CTS-Certification]]",
        ],
        "research_batch": "v2-prompt-06-av-production",
        "child_of": "[[Domain-Inclusivity-And-Accessibility]]",
        "related_to": [
            "[[Av-And-Production-Line-Array-Sound-Systems]]",
            "[[Av-And-Production-Networked-Audio-Infrastructure]]",
            "[[Av-And-Production-Acoustic-Treatment]]",
        ],
        "body": """## Overview

Assistive listening systems (ALS) provide enhanced audio delivery for patrons with hearing loss, enabling equitable access to spoken content and performances. ADA Standards for Accessible Design (Section 219) require assembly areas with audio amplification to provide ALS receivers equal to at least 25% of the total seating count, with a minimum number varying by total capacity.

## Technology Options

Hearing loop systems (induction loop, per IEC 60118-4) transmit audio magnetically to telecoil-equipped hearing aids and cochlear implants, providing the most seamless user experience as no separate receiver is needed. RF (radio frequency) systems transmit on dedicated frequencies and work throughout the venue without line-of-sight requirements. Infrared systems offer secure, room-contained transmission but require line-of-sight. Wi-Fi-based systems deliver audio through smartphone apps, leveraging venue Wi-Fi infrastructure.

## Hearing Loop Standards

IEC 60118-4 specifies performance requirements for hearing loop systems including field strength, frequency response, and signal-to-noise ratio. Proper loop installation requires careful design to achieve uniform field strength across the listening area while minimizing signal spillover to adjacent spaces. Counter loops or phased array configurations address metal loss in venues with steel-reinforced concrete construction.

## Captioning and Emerging Technologies

Real-time captioning (CART -- Communication Access Realtime Translation) provides text display of spoken content for patrons who are deaf or hard of hearing. Open captioning on venue displays and personal captioning devices complement ALS technology. AI-powered automatic speech recognition is emerging as a supplementary captioning tool, though accuracy limitations require human oversight for critical communications.

## Sources

- [[Source-0116-Listen-Technologies-ALS]]
- [[Source-0106-AVIXA-Standards]]
- [[Source-0107-AVIXA-CTS-Certification]]""",
    },
]

concept_count = 0

for c in concepts:
    # Build frontmatter
    venue_types_yaml = "\n".join(f"  - {vt}" for vt in c["venue_types"])
    vef_yaml = "\n".join(f"  - {v}" for v in c["vef_alignment"])
    sources_yaml = "\n".join(f'  - "{s}"' for s in c["sources"])
    related_yaml = "\n".join(f'  - "{r}"' for r in c.get("related_to", []))

    # Optional governed_by
    governed_by_block = ""
    if "governed_by" in c:
        gb_yaml = "\n".join(f'  - "{g}"' for g in c["governed_by"])
        governed_by_block = f"governed_by:\n{gb_yaml}\n"

    # Optional supported_by
    supported_by_block = ""
    if "supported_by" in c:
        sb_yaml = "\n".join(f'  - "{s}"' for s in c["supported_by"])
        supported_by_block = f"supported_by:\n{sb_yaml}\n"

    content = f'''---
title: "{c['title']}"
note_type: concept
domain: "{c['domain']}"
status: draft
created: 2026-04-04
updated: 2026-04-04
description: "{c['description']}"
venue_types:
{venue_types_yaml}
vef_alignment:
{vef_yaml}
confidence: {c['confidence']}
sources:
{sources_yaml}
research_batch: {c['research_batch']}
child_of: "{c['child_of']}"
related_to:
{related_yaml}
{governed_by_block}{supported_by_block}tags:
  - concept
  - venue-ops
  - {c['domain']}
  - batch-04
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# {c['title']}

{c['description']}

{c['body']}
'''
    # Determine folder
    domain_folder = c['domain']
    folder = os.path.join(DOMAINS_DIR, domain_folder)
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, c['filename'])
    with open(filepath, 'w') as f:
        f.write(content)
    concept_count += 1
    print(f"  Created: {c['filename']}")

print(f"\nConcept notes created: {concept_count}")
print(f"Total files created: {created_count + concept_count}")
