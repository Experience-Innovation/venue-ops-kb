---
title: "Networked Audio Infrastructure"
note_type: concept
domain: "av-and-production"
status: draft
created: 2026-04-04
updated: 2026-04-04
description: "Dante, AVB/TSN, and AES67 networked audio protocols for venue production environments. Covers production VLANs, multicast management, redundancy architectures, and routing hundreds of bidirectional audio channels over Ethernet."
venue_types:
  - arena
  - stadium
  - convention-centre
  - performing-arts-centre
vef_alignment:
  - operational-efficiency-productivity-creativity
  - ai-and-digital-transformation
  - innovation-and-continuous-improvement
confidence: high
sources:
  - "[[Source-0115-Audinate-Dante-Audio-Networking]]"
  - "[[Source-0106-AVIXA-Standards]]"
  - "[[Source-0108-ESTA-Technical-Standards]]"
research_batch: v2-prompt-06-av-production
child_of: "[[Domain-Av-And-Production]]"
related_to:
  - "[[Av-And-Production-Line-Array-Sound-Systems]]"
  - "[[Av-And-Production-Broadcast-Infrastructure]]"
  - "[[Technology-And-Digital-Venue-Cybersecurity]]"
tags:
  - concept
  - venue-ops
  - av-and-production
  - batch-04
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# Networked Audio Infrastructure

Dante, AVB/TSN, and AES67 networked audio protocols for venue production environments. Covers production VLANs, multicast management, redundancy architectures, and routing hundreds of bidirectional audio channels over Ethernet.

## Overview

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
- [[Source-0108-ESTA-Technical-Standards]]
