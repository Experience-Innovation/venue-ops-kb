# R-18: Venue Technology and Digital Infrastructure Refresh
*Knowledge Base Refresh — Technology & Digital Domain | April 2026*

***

## Executive Summary

The venue technology domain has advanced materially since the original v2-prompt-05 concept notes were drafted in early 2026. Across all eight research areas, the state of deployment has shifted from pilot and proof-of-concept toward production-scale rollout: WiFi 7 is live at MLS stadiums, T-Mobile has private 5G at all 29 US MLB ballparks, Evolv's AI weapon detection has faced FTC enforcement action reshaping vendor claims, the NEVI program underwent a freeze-and-reset cycle under the new administration with an August 2025 Interim Final Guidance now governing all states, and PCI DSS 4.0 became fully mandatory in March 2025. The DELTA-019 flag on NEVI sourcing is resolved below with specific statutory references, funding figures, and technical minimums. This document provides enriched content for all five existing concept notes and sourced material for at minimum three new concepts: AI/ML Venue Applications, Autonomous and Robotics Systems, and Data Privacy Regulatory Compliance.

***

## 1. AI/ML Applications in Venue Operations

### 1.1 Deployment State and Adoption Rates

Artificial intelligence has crossed from novelty to operational baseline in venue management. Industry surveys indicate that approximately **50% of event venues have adopted AI** for operations including logistics and space management as of early 2026. The shift is driven by three properties AI brings to high-density event environments: pattern-recognition across datasets too large for human analysis, real-time adaptation to changing conditions during live events, and the ability to personalize services at scale without proportional staffing increases.[^1]

### 1.2 Crowd Analytics and Computer Vision

Computer vision for crowd management is the most widely deployed AI application category in venues. Production systems use convolutional neural networks (CNNs), LSTMs, and attention-based autoencoders to achieve state-of-the-art accuracy in learning spatiotemporal movement patterns. Modern deployments using YOLOv11 and edge computing can detect crowd density hotspots, monitor flow speed and direction, and identify reverse or stalled movement indicative of congestion or distress — all in real time. At the Paris 2024 Olympics, AI systems alerted authorities to crowd surges near venues within seconds, providing an early major-event validation point.[^2][^3]

A technically distinct approach uses LiDAR-generated 3D spatial data rather than video. LiDAR-based spatial intelligence (offered commercially by Outsight, among others) monitors crowd movement without visual identification of individuals, enabling operators to generate live heatmaps, trigger automated alerts when zone thresholds are exceeded, and build historical trend data for future planning — while avoiding many of the biometric consent issues associated with camera-based systems. This privacy-preserving characteristic is becoming a meaningful procurement differentiator given the regulatory environment described in Section 8.[^4]

### 1.3 AI Weapon Detection — Deployment and Regulatory Context

Two platforms dominate AI-assisted weapon detection in venues:

**ZeroEyes** holds full DHS SAFETY Act Designation — the only AI gun detection platform to do so — for its visual firearm detection system, which overlays onto existing IP security cameras. When AI identifies a visible firearm, images route immediately to ZeroEyes' 24/7 human Operations Center (ZOC), which verifies the threat and dispatches actionable intelligence to law enforcement within 3–5 seconds of detection. As of January 2026, ZeroEyes had surpassed 1,000 confirmed gun detections since 2023, with 98% customer retention in North America.[^5][^6]

**Evolv Technology** reported screening over four billion people worldwide through its Evolv Express touchless screening system, making it among the most widely deployed AI-powered security screening technologies globally. However, the FTC settled with Evolv in November 2024 over allegations of deceptive marketing claims. The FTC found that Evolv's technology fundamentally detects metal, not weapons per se — the AI/weapon-detection framing was a marketing distinction rather than a technical one — and that the system missed two handguns and detected knives only 58% of the time in a 2021 MLS Columbus test. Under the settlement, Evolv is prohibited from making unverified claims about weapon detection accuracy, false alarm rates, or AI-driven performance superiority versus metal detectors. Venue procurement teams should treat independent third-party testing requirements as non-negotiable for any AI security screening system.[^7][^8][^9]

### 1.4 AI Predictive Maintenance

AI-driven predictive maintenance for building systems (HVAC, electrical, mechanical) represents one of the highest-ROI AI deployments in venues. The documented performance benchmark range across commercial deployments is:

- 40–60% reduction in emergency maintenance calls
- 20–30% extension of equipment lifespan
- 8–15% energy cost reduction
- 8–15x ROI within the first year
- Typical payback within 3–6 months for a 500,000 sq ft facility[^10]

Systems monitor vibration, current draw, temperature, pressure, and airflow 24/7 using IoT sensors (detailed in Section 3), with ML algorithms detecting degradation patterns weeks to months before failure. For large multi-use venues where HVAC systems account for 40–60% of building energy consumption, AI-optimized predictive control can reduce HVAC energy consumption by 15–25%.[^11][^12]

### 1.5 Dynamic Pricing Engines

AI-powered dynamic pricing is standard practice in primary ticketing and increasingly applied to concessions. In primary ticketing, algorithms adjust face-value prices continuously based on demand signals, remaining inventory, time-to-event, ticket sales velocity, artist or team performance, and external signals including competing event lineups, hotel booking rates, and local economic indicators. Venues typically apply dynamic pricing to select inventory segments — GA or premium seats — rather than the full bowl, with VIP packages often held at fixed rates. In 2026, automated AI pricing engines in venues represent matured, proven technology rather than emerging capability; the active debate has shifted to regulatory scrutiny of per-customer individualized pricing.[^13][^14][^1]

### 1.6 AI/ML Venue Deployment Catalog

| Application | Platform/Vendor Type | Venue Type | Evidence Level |
|---|---|---|---|
| Crowd density analytics (video CV) | YOLOv11, Avigilon, Genetec | Stadium, arena, convention center | Production — Paris 2024, major leagues |
| LiDAR crowd flow monitoring | Outsight, Quanergy | Stadium, airport, convention center | Production — commercial deployment |
| Concession wait-time AI | WaitTime | Stadium (NFL, NCAA) | Production — Bryant-Denny Stadium[^15] |
| AI weapon detection (visible guns) | ZeroEyes | Venues, schools, public spaces | Production — DHS SAFETY Act, 1,000+ detections[^5] |
| Touchless security screening | Evolv Express | Stadiums, subways | Production — FTC consent decree limits claims[^8] |
| AI predictive maintenance | Cimetrics, OxMaint, others | All venue types | Production — verified 8-15x ROI benchmarks[^10] |
| Dynamic pricing engine | Ticketmaster, AXS, SeatGeek | Arena, stadium | Production — standard industry practice[^13] |
| Attendance/staffing forecasting | ML platforms (venue-embedded) | All venue types | Production — multiple documented deployments[^1] |
| Emergency egress simulation | Simio, STEPS | Stadium, arena | Production — used in FIFA 2026 planning[^16] |

***

## 2. Network Infrastructure Evolution

### 2.1 WiFi 7 Venue Deployments

WiFi 7 (802.11be) represents a step-function improvement in venue wireless capability, not an incremental upgrade. Its three headline technical advances combine to address the specific failure modes of high-density wireless environments:

- **Multi-Link Operation (MLO):** A single device simultaneously sends and receives across the 2.4 GHz, 5 GHz, and 6 GHz bands, eliminating the single-band bottleneck that caused per-device throughput collapse during peak periods in prior generations[^17]
- **320 MHz channels:** Double the 160 MHz maximum in WiFi 6E, delivering higher aggregate throughput and reducing interference sensitivity[^18][^19]
- **4096-QAM modulation:** 46 Gbps theoretical maximum data rate vs. 9.6 Gbps for WiFi 6, with practical sustained multi-gigabit performance in dense deployments[^17]

Even legacy devices (WiFi 4/5) show approximately 30% performance improvement when operating on a WiFi 7 network due to reduced channel congestion and improved traffic management. Quality-of-service (QoS) mechanisms in WiFi 7 allow networks to separate and prioritize traffic for fans, operations, broadcast media, and security systems simultaneously.[^19]

**Deployment milestone:** In March 2026, RUCKUS Networks completed installation of a WiFi 7 network at BMO Stadium (Los Angeles Football Club), establishing the first WiFi 7 deployment in Major League Soccer. The network uses RUCKUS T670 access points for under-seat coverage and T670SN hyper-directional APs for concourses and club spaces, managed by the RUCKUS AI™ platform for real-time analytics and predictive issue resolution. As of April 2025, RUCKUS was the only vendor offering a complete WiFi 7 venue solution covering under-seat, overhead narrow-angle, and overhead wide-angle deployment configurations. IDC projects WLAN revenue growing 12% in 2025 with WiFi 7 accounting for over one-third of indoor AP revenue.[^20][^18][^17]

### 2.2 5G Private Networks in Venues

The private 5G market in venues has reached scale deployment with two major league-wide rollouts announced as of March–April 2026:

**T-Mobile / MLB (all 29 US ballparks):** T-Mobile has deployed fully private 5G networks at all 29 US MLB ballparks using Ericsson EP5G and DOT radios on n41 mid-band spectrum (2469–2690 MHz). Each installation is a dedicated, all-edge affair — no public cores, no public slices — with a unique PLMN ID preventing unauthorized device access. The primary operational use case is MLB's Automated Ball Strike (ABS) system, which went league-wide for the 2026 season and requires low-latency pitch tracking with real-time analysis tablets for umpire challenge decisions. T-Mobile's public 5G SA network provides separately sliced capacity for ticketing, concession payments, and photojournalism.[^21]

**Verizon / NHL (all 25 US arenas):** Verizon has deployed its Private 5G Wireless Network (PWN) across all 25 NHL arenas in the United States as the league's Official 5G Partner. Confirmed use cases include live coach-to-player video access on iPads from the bench, real-time alerts in the NHL Watch Comms app on Apple Watch worn by officials, and scalable capacity for future goalie/net multi-view camera innovations. The NHL Innovation Lab established in spring 2026 uses the Verizon PWN as its dedicated wireless infrastructure.[^22][^23]

**Spectrum approaches:** US carriers diverge on spectrum strategy. Verizon is the primary user of CBRS (Citizens Broadband Radio Service) 3.5 GHz spectrum for 4G LTE and operates the most extensive mmWave networks at venues. T-Mobile uses its licensed n41 spectrum at 2.5 GHz for private networks. At the 2025 PGA Championship, T-Mobile executed the first live NR-DC (New Radio Dual Connectivity) deployment in a private event context, blending 5G SA mid-band with mmWave hotspots at tee boxes for ultra-high throughput uplink.[^24][^25]

The 5G-powered smart stadium market is valued at $7.92 billion in 2025, projected to reach $10.32 billion by 2027.[^26]

### 2.3 DAS Architecture

Distributed Antenna Systems (DAS) remain the foundational cellular coverage layer for enclosed venues. For major stadiums in 2025, Active DAS is the gold standard, particularly for supporting multi-carrier 5G. Active DAS distributes carrier signals via optical fiber from a headend to remote antenna units throughout the venue, with each unit amplifying and re-broadcasting signals — enabling high-capacity coverage in locations where direct cellular propagation fails (under-seat areas, concourses, tunnels, club levels).[^27][^28]

The emerging development is DAS compatibility with 5G millimeter-wave. Sumitomo Electric demonstrated compact 5G mmWave DAS remote units approximately one-tenth the size of standard mmWave base stations at exhibition in February 2025, enabling dense deployment economics that were previously impractical. For large convention centers, DAS typically serves as the carrier-integrated cellular layer while WiFi handles the high-density data load; the optimal venue architecture combines Active DAS for cellular coverage with WiFi 7 for data throughput.[^29]

### 2.4 Network Infrastructure by Venue Type

| Technology | Stadium (70K+ seats) | Arena (20K seats) | Convention Center | Key Standard/Vendor |
|---|---|---|---|---|
| WiFi standard | WiFi 7 (leading edge), WiFi 6E (current base) | WiFi 6E / WiFi 7 deploying | WiFi 6 / WiFi 6E | RUCKUS, Cisco, Aruba |
| 5G private | League-wide (MLB, NHL) | Piloting (NHL Verizon PWN) | Select deployments | Ericsson, Nokia, Verizon |
| DAS | Active DAS, multi-carrier | Active DAS standard | Active DAS required | CommScope, Boingo, ExteNet |
| CBRS small cells | Supplemental capacity | Supplemental capacity | Office/floor coverage | Verizon CBRS |
| Bandwidth target | 1–2 Mbps/attendee sustained | 1–2 Mbps/attendee | 5–10 Mbps/booth | Wi-Fi Alliance guidance |

***

## 3. IoT Sensor Deployments

### 3.1 Occupancy Counting Technologies

Three dominant sensor modalities are in production deployment for venue occupancy intelligence, each with distinct trade-offs:

**LiDAR / 3D Spatial AI:** Generates real-time three-dimensional point clouds of spaces. Not affected by lighting conditions or visual obstructions. Inherently privacy-preserving (no photographic capture of individuals). Enables centimeter-accurate movement tracking and persistent zone monitoring. Used in airport terminals, exhibition centers, and large venues. Higher infrastructure cost per sensor than camera-based systems.[^4]

**Thermal / Infrared cameras:** Count occupants by heat signature. Not affected by low-light conditions. No facial capture. Accuracy degrades when individuals are in close proximity (bodies merge in thermal view). Lower cost per unit than LiDAR. Widely deployed for entry counting and HVAC demand-control.[^30]

**Vision-based / Computer Vision cameras:** Highest contextual intelligence (can distinguish behavior, direction, distress indicators). Subject to lighting variability, occlusion, and privacy regulation when capable of identification. Can be configured for anonymized analytics using body-only tracking without facial capture. Used in concession queue monitoring (WaitTime platform at Bryant-Denny Stadium).[^15]

### 3.2 Environmental and Air Quality Monitoring

IoT environmental monitoring for HVAC optimization has reached operational standard in well-resourced venues. A full IoT environmental sensor suite covers:

| Sensor Type | Protocol | Battery Life | Primary Application |
|---|---|---|---|
| Temperature/Humidity | LoRaWAN, WiFi, BLE | 5–10 years | HVAC optimization, storage monitoring |
| CO₂ / IAQ | LoRaWAN, WiFi | 2–4 years | Ventilation demand control, health compliance |
| Occupancy | WiFi, LoRaWAN, Zigbee | 3–5 years | Space utilization, lighting, cleaning schedules |
| Water Leak | LoRaWAN, WiFi | 5–8 years | Mechanical rooms, bathrooms |
| Vibration | WiFi, Cellular, LoRaWAN | 2–5 years | HVAC, pumps, motors |
| Energy Monitor | WiFi, Ethernet | Powered | Circuit-level tracking, demand response[^31] |

IoT-enabled HVAC systems demonstrate up to 20% energy consumption reduction through real-time occupancy-based adjustment. Predictive maintenance enabled by vibration and temperature IoT sensors can reduce HVAC downtime and unscheduled maintenance costs by up to 40%. Buildings with IoT-managed systems report energy savings of up to 30% annually.[^32][^33]

### 3.3 Asset Tracking (RTLS/UWB)

Real-Time Location Systems (RTLS) for venue asset tracking span a technology spectrum based on required accuracy and budget:

**Ultra-Wideband (UWB):** The high-accuracy gold standard for venues, achieving centimeter-level positioning with latency under 1 ms. UWB anchors are typically PoE-powered with strategic placement; tags are battery-operated with 3–5 year life. Best suited for tracking high-value movable assets (AV equipment, medical devices, powered carts) and applications requiring sub-meter precision. Higher total cost of ownership limits application to high-value use cases.[^34][^35]

**Bluetooth Low Energy (BLE):** Zone-based positioning (3–10m accuracy), low power, integrates with existing mobile ecosystems. Preferred for large-inventory tracking and staff location awareness where zone-level rather than centimeter accuracy is sufficient.[^36][^34]

**RFID / Passive:** Industry standard for high-volume inventory management and automated check-in/check-out of equipment. No real-time location; proximity-based detection. Very low per-tag cost.[^36]

Multi-technology approaches are increasingly common: RFID for item identification + UWB for real-time location on high-value subsets. TB International's integration of Inpixon/INTRANAV's UWB+RFID system achieved a nearly 40% increase in operational efficiency in a warehouse context.[^35]

### 3.4 Standards Governing IoT Security

NIST released an update to its foundational IoT cybersecurity guidance in 2025 — NIST IR 8259r1 (initial public draft, July 2025 comment deadline) — introducing a seventh foundational activity and expanding scope to include industrial IoT, privacy integration, and end-of-life security. The update emphasizes lifecycle-centric security from design through decommissioning, improved transparency and traceability, and preparation for unexpected deployment environments. For venue operators deploying IoT sensor networks, NIST IR 8259r1 provides the applicable cybersecurity baseline for device selection and procurement requirements.[^37][^38]

***

## 4. Cybersecurity for Venue Operations

### 4.1 IT/OT Convergence Threat Landscape

The IT/OT convergence risk for venues has materially worsened in the 2025–2026 period. Dragos' 2026 OT Cybersecurity Report documented that ransomware groups targeting industrial organizations surged **49% year-over-year in 2025**, collectively impacting 3,300 organizations globally with multi-day operational outages. A critical insight for venue operators: the majority of OT-affecting ransomware incidents are misclassified as IT-only events because engineering workstations and HMI (Human-Machine Interface) systems run Windows operating systems and are inventoried as IT assets.[^39]

The attack pathway most relevant to venues is VPN/vendor tunnel exploitation. Affiliates increasingly use compromised credentials sourced from infostealers, password reuse across IT and OT systems, and cloud-synchronized identities to authenticate into VPN portals or firewall interfaces, then pivot to OT-adjacent boundary networks. For venues, "OT" encompasses building management systems (BMS/BAS), HVAC controllers, access control infrastructure, fire suppression, and display/audio systems. An ESXi hypervisor supporting virtualized SCADA can be encrypted by ransomware without any direct interaction with industrial protocols, removing operator visibility and control. Organizations with strong OT detection capabilities contained ransomware incidents in an average of **5 days** versus the industry-wide average of **42 days**.[^39]

GuidePoint Security's GRIT 2026 report found December 2025 was the most active ransomware month ever recorded, with 814 successful attacks — a 42% year-over-year increase — and expects 2026 to continue the trend toward directly targeting OT networks rather than merely disrupting IT.[^40]

### 4.2 PCI DSS 4.0 Compliance for Venue POS

PCI DSS v4.0 became fully mandatory on **March 31, 2025**, when all 51 future-dated requirements converted from best-practice to enforceable. The 2025 transition represents the most significant compliance shift in the PCI landscape in over a decade, adding 64 new requirements (51 previously deferred) addressing phishing, web-skimming, and supply-chain risks.[^41][^42]

For venues, the critical PCI 4.0.1 clarification is expanded merchant accountability for outsourced POS and ticketing systems. If vendor-managed terminals (concession POS, ticketing kiosks) route through the venue's internal WiFi or LAN, those network segments may be deemed in-scope for PCI compliance regardless of outsourced management. Venue operators must:[^43]

- Identify and label all network segments carrying cardholder data, including vendor-managed segments
- Apply strict firewall isolation between POS/ticketing segments and other venue systems
- Collect formal Attestations of Compliance (AOCs) from all third-party payment providers annually
- Ensure staff training encompasses physical terminal security across all concourse and box office locations[^43]

The payment script integrity requirements (Requirement 6.4) are particularly relevant to mobile-enabled ticketing and concession apps, targeting web-skimming attacks against JavaScript payment forms.[^41]

### 4.3 Applicable Cybersecurity Frameworks

| Framework | Current Version | Venue Applicability | Key Addition |
|---|---|---|---|
| NIST CSF | 2.0 (Feb 2024) | Foundational — all venue types | New GOVERN function (6th pillar); supply chain risk management[^44][^45] |
| NIST Cyber AI Profile | Draft Dec 2025 | AI-enabled venue systems | CSF 2.0 applied specifically to AI technology deployments[^46] |
| NIST IR 8259r1 | Initial draft 2025 | IoT device procurement and deployment | 7th foundational activity, industrial IoT, lifecycle security[^37] |
| PCI DSS | 4.0.1 (mandatory Mar 2025) | Ticketing, concessions, parking POS | Expanded merchant accountability for third-party systems[^43][^42] |
| CISA Cross-Sector CPGs | 2.0 (Dec 2025) | Critical infrastructure venues | Updated to NIST CSF 2.0, reflects 2025 adversary tactics[^47] |
| CIS Controls | v8 | Operational baseline | Maps to NIST CSF 2.0 subcategories |

NIST CSF 2.0's GOVERN function establishes the organizational context, risk management strategy, roles, and supply chain risk management oversight that umbrella the other five functions (Identify, Protect, Detect, Respond, Recover). For venues, GOVERN is particularly important for managing the ecosystem of third-party technology vendors — AV integrators, ticketing platforms, concession POS providers, security systems — each of which represents a supply chain risk.[^45]

### 4.4 Cybersecurity Framework Applicability Matrix

| Venue Function | NIST CSF 2.0 | PCI DSS 4.0 | CISA CPGs 2.0 | NIST IR 8259r1 |
|---|---|---|---|---|
| Ticketing / Box Office | All 6 functions | Full scope | Network segmentation | Payment terminal IoT devices |
| Concessions POS | Protect, Detect | Full scope if network-connected | Third-party risk | POS IoT devices |
| BMS / HVAC Controls | IT-OT convergence (all) | Out of scope | OT network visibility | BMS IoT sensors |
| Security / Camera Systems | Protect, Detect | Out of scope | Physical-cyber integration | Camera/sensor IoT |
| WiFi / Guest Network | All 6 functions | Segmentation required | Network monitoring | AP / IoT network devices |
| Vendor Access / Remote Mgmt | GOVERN supply chain | Third-party AOC required | Zero-trust remote access | Vendor-device security |

### 4.5 SOC Models for Large Venues

Large venues increasingly operate under a hybrid or fully managed SOC model rather than building in-house 24/7 security operations capability. CISA's 2025 Year in Review expanded the CyberSentry Program to 42 voluntary critical infrastructure partners, providing advanced threat detection and monitoring for networks supporting National Critical Functions. Venue operators qualifying as critical infrastructure (stadiums and arenas hosting events with federal designation) can access CyberSentry at no cost. For others, managed SOC providers offer venue-tailored services covering both the IT layer (guest WiFi, ticketing, POS) and OT layer (BMS, HVAC, access control) with OT-specific detection signatures.[^47]

***

## 5. Digital Twin Technology Maturity

### 5.1 Platform Maturity and Leading Deployments

Digital twin technology for venues has progressed from singular showcase installations to multi-venue operational programs between 2020 and 2026. SoFi Stadium in Inglewood, California, established the benchmark when it became the **first major US venue to deploy a fully operational digital twin**, announced in late 2020 and built by Willow on a foundation of approximately 1,700 BIM sub-models covering the 70,000-seat stadium and the 300-acre Hollywood Park development. The SoFi implementation integrates real-time data from building systems to optimize HVAC, lighting, and operations, with the digital twin enabling facility managers to analyze occupancy patterns, identify maintenance needs proactively, and model event-day scenarios before implementation.[^48][^49][^50]

Other notable production deployments:
- **Tottenham Hotspur Stadium (London):** Operational digital infrastructure including 3D spatial data as the foundation layer for event management and facility operations[^51]
- **Commonwealth Stadium (Edmonton, Canada):** VenueTwin centimeter-accurate interactive 3D model used for event planning visualization and stakeholder communication[^52]
- **NFL stadiums broadly:** Digital twin-based security checkpoint modeling has reduced entry wait times by over 30% while reducing the physical footprint required for screening[^53]
- **FIFA 2026 host stadiums:** Real-time operational monitoring during matches using digital twin infrastructure, with laser-scanning providing measurement-grade 3D models[^51]

### 5.2 BIM-CMMS Integration

The maturation pathway for venue digital twins follows a predictable sequence: (1) architectural BIM model captures spatial and asset data during construction; (2) BIM is linked to CMMS for maintenance work order management; (3) real-time sensor data elevates the static BIM model to a live digital twin. Research published in 2025 confirms that BIM and CMMS can be directly linked without compromising information synchronization, with the 3D spatial environment enabling faster identification of potential issues and more efficient maintenance operations. The BIM Summit 2025 in Toronto highlighted asset information models (AIMs) as the critical connector between BIM outputs and CMMS/CAFM systems for facility management post-construction.[^54][^55]

A foundational principle: a BIM model becomes a digital twin when continuously updated by live sensor data. BIM alone provides spatial and asset intelligence; digital twins add real-time operational state, predictive simulation, and what-if analysis capability.[^56]

### 5.3 Simulation Capabilities

The operationally mature use cases for venue simulation via digital twin platforms include:

- **Emergency evacuation modeling:** Crowd flow simulation under various exit configuration scenarios, tested virtually before event-day implementation[^16][^57]
- **HVAC load prediction:** Simulation of occupancy-driven cooling/heating demand to pre-configure systems before crowd arrival[^49]
- **Security checkpoint optimization:** Testing staffing and lane configurations against projected arrival waves to eliminate bottleneck zones[^16][^53]
- **Concession placement analysis:** Modeling foot traffic patterns to identify optimal locations for new food/beverage service points[^16]

Simulation platforms like Simio offer discrete-event simulation embedded with operational data, enabling "what-if" stress tests of entry procedures, security configurations, and staff deployment before live implementation.[^16]

### 5.4 Digital Twin Maturity Assessment

| Capability | Platform | Venue Type | Maturity | ROI Evidence |
|---|---|---|---|---|
| 3D spatial modeling (static) | Willow, VenueTwin, OnePlan | All venue types | High — broad commercial deployment | Reduced site visits, remote planning[^57] |
| BIM-CMMS integration | Multiple (IBM Maximo, Archibus) | Arena, stadium, convention center | Medium — growing adoption | Faster maintenance identification[^54] |
| Real-time operational twin | Willow (SoFi Stadium) | NFL/NBA/NHL stadiums | Medium — leader-follower gap | HVAC optimization, proactive maintenance[^50] |
| Crowd flow simulation | Simio, Legion, MassMotion | Stadium, arena, airport | Medium-High — FIFA 2026 use | 30%+ entry wait time reduction (NFL)[^53] |
| Evacuation simulation | Legion, MassMotion | Stadium, arena | Medium — regulatory acceptance growing | Pre-event planning validation |
| Predictive HVAC twin | Cimetrics, Siemens | Large venues, convention centers | High — building sector leading | 15–25% energy reduction[^12] |

The digital stadium sector is projected to expand at 20.6% annually between 2025 and 2037, reaching US$191.7 billion.[^58]

***

## 6. EV Charging Infrastructure and the NEVI Program

### 6.1 NEVI Program Overview and Legal Authority

The National Electric Vehicle Infrastructure (NEVI) Formula Program was established under the Infrastructure Investment and Jobs Act (IIJA), Public Law 117-58, signed November 2021. The program allocates **$5 billion over fiscal years 2022–2026** to states for the deployment of EV charging infrastructure, administered by the Federal Highway Administration (FHWA) under the Department of Transportation.[^59][^60]

**Statutory framework:**
- Up to **80% federal cost share** for eligible project costs[^59]
- Eligible costs include: equipment acquisition, installation, network connection, operation and maintenance, and long-term data sharing[^59]
- Chargers must be non-proprietary, allow open-access payment methods, and be publicly accessible or available to authorized commercial motor vehicle operators from more than one company[^59]

### 6.2 2025 Program Freeze and Interim Final Guidance

**Critical chronology for 2025 (DELTA-019 resolution):**

| Date | Event |
|---|---|
| June 11, 2024 | Biden Administration issues Final NEVI Formula Program Guidance |
| February 6, 2025 | FHWA under Trump Administration freezes all NEVI funding obligations nationwide; rescinds all prior guidance |
| Late 2025 | Federal court orders release of allocated funds to states |
| August 11, 2025 | FHWA issues Interim Final Guidance (IFG), restoring program; replaces ALL previous guidance documents[^61][^62][^63] |
| FY2026 | $885 million apportioned; at least 384 EV charging ports built through late 2025[^64] |

The August 2025 IFG, issued by Transportation Secretary Sean P. Duffy, is the controlling governance document for the NEVI program as of April 2026. It streamlines state plan requirements, reduces community engagement to statutory minimums, eliminates labor standards and environmental siting mandates added under the prior administration, and removes mandatory mile-spacing requirements. As of August 2025, 84% of NEVI Formula program funds remained unobligated — a figure cited by the new administration as evidence of the prior guidance's implementation failure.[^65]

### 6.3 Technical Standards (As of August 2025 IFG)

The following technical minimum standards remain in effect under the IFG:

| Requirement | Standard |
|---|---|
| DCFC minimum output | 150 kW per port simultaneously[^66][^67] |
| Minimum ports per site | 4 DCFC ports (total 600 kW site capacity)[^67] |
| Uptime requirement | 97% operational availability[^67] |
| Required connector (DCFC) | CCS Type 1 (SAE J1772 Combo); CHAdeMO only from FY2022 funds[^66] |
| AC Level 2 connector | Permanently attached J1772[^66] |
| DCFC voltage range | 250–920 VDC[^66] |
| Pricing display | Must display $/kWh before transaction initiation[^66] |
| Network interoperability | OCPI 2.2.1 (network-to-network, required by 2025)[^66] |
| Charger-to-network protocol | OCPP 2.0.1 (required by 2025)[^66] |
| Plug and Charge | ISO 15118-2 capable (software compliance by 2025)[^66] |
| Security architecture | Chargers must support switching network providers without hardware changes[^66] |

### 6.4 Venue Parking Eligibility

Under the August 2025 IFG, once FHWA certifies that a state's Alternative Fuel Corridors (AFCs) are fully built out (FBO), NEVI program funds may be used for EV charging infrastructure on any public road or in **other publicly accessible locations**, explicitly including parking facilities at public buildings, public schools, and public parks, as well as publicly accessible parking facilities owned by private entities. This expansion directly enables venue parking applications. States must prioritize AFC buildout first, but the FBO threshold unlocks venue, convention center, and arena parking as eligible NEVI sites.[^64][^62]

### 6.5 Revenue Models and Venue Deployment Considerations

For venues considering EV charging infrastructure, three operating models apply:

| Model | Description | Revenue/Cost Profile |
|---|---|---|
| Free amenity | Venue provides charging as an attendee amenity, absorbs electricity cost | Cost center; differentiator for EV-driving attendees |
| Fee-based (venue-operated) | Venue sets $/kWh rates (required under NEVI), retains revenue minus electricity and maintenance | Revenue potential; requires compliance infrastructure |
| Third-party operator | CPO (ChargePoint, EVgo, Blink) installs and operates; venue receives site host fee or revenue share | Zero capex; limited control over pricing/uptime |

NEVI-funded stations require open-access payment and public pricing transparency regardless of operating model.[^59]

### 6.6 Canadian ZEV Infrastructure Program (ZEVIP)

For Canadian venues (relevant given the KB's Alberta context), Natural Resources Canada administers the **Zero Emission Vehicle Infrastructure Program (ZEVIP)**, a $680 million program running through March 31, 2027. ZEVIP provides up to **50% of total project costs** with a maximum of **$2 million per project** per application (limit of two project proposals per applicant). The program targets EV charger deployment in public places, workplaces, multi-unit residential buildings, on-street, and fleet applications. The government's infrastructure targets are 84,500 chargers and 45 hydrogen stations deployed by 2029. ZEVIP is open to venue owners/operators as eligible site hosts for publicly accessible charging.[^68][^69]

***

## 7. Autonomous and Robotics Applications

### 7.1 Cleaning and Sanitation Robots

Autonomous floor-scrubbing robots are in production deployment in sports facilities. The Cleanfix RA660 Navi provides an illustrative case: operating in a 450 m² sports hall (La Grande Béroche), the robot is programmed to run during off-hours and autonomously maintains floor cleanliness without disrupting daily activities. Vendors active in the venue/facility space include Cleanfix, Tennant (with Autonomo), and Avidbots (Neo platform). The category is commercially mature for large, flat-floor environments (concourses, exhibition halls, playing surfaces during non-event periods). UV disinfection robots saw significant deployment acceleration post-COVID in arenas and convention centers and remain in use at venues with high-frequency events.[^70]

### 7.2 Food Delivery and Concession Robots

In-venue food delivery robotics is bifurcating into two operational models:

**Concourse rover delivery (fan-facing):** Kiwibot operates food delivery robots at 21+ college campuses and is integrating into 45 USL Superleague matches in 2025. Each GPS-enabled robot has a sensor array tracking real-time local data; fans scan a QR code at section entrances to retrieve orders. The Al Lang Stadium (St. Petersburg, FL) pilot announced in April 2025 integrates Kiwibot with GrubHub for concession delivery to accessible areas.[^71]

**Automated concession preparation:** Next Bite Robotics has developed a fully autonomous robotic concession preparation system targeting stadium food service, claiming 30-second order delivery versus 30-minute traditional wait times. The platform addresses the chronic stadium experience pain point of concession queues pulling fans out of their seats during action.[^72]

**AI wait-time systems (human-staffed):** An intermediate category uses computer vision and AI (not physical robots) to monitor queue lengths and display real-time wait times via stadium apps and digital signage. WaitTime deploys ceiling-mounted cameras with anonymized body-tracking CV at venues including Bryant-Denny Stadium (University of Alabama), enabling fans to select less congested stands from their seats.[^15]

### 7.3 Autonomous Shuttles

Autonomous low-speed electric shuttles have reached controlled public deployment for first/last-mile applications. The most directly relevant North American deployment for venue operations is the **Aurrigo Auto-Shuttle Mk2** pilot at Kanata North Business Association (Ottawa), launched October 2025. This marks Canada's first all-season, medium-speed autonomous shuttle operating on public roads. The Level 4 electric, nine-passenger vehicle runs a 4.5 km, eight-stop loop linking businesses and transit connections, with full winter-ready engineering for snow and ice conditions. The pilot was designed to validate autonomous shuttle technology in real Canadian weather conditions before broader transit deployment.[^73][^74][^75]

For venue parking-to-venue circulation, low-speed autonomous shuttles (top speed ~25 mph) represent the appropriate application tier, solving first/last-mile gaps between remote parking areas and venue gates. Benefits include reduced congestion from parking-seekers, fuel savings, and potentially lower per-ride costs versus human-operated shuttles, though per-ride cost advantages have not yet been broadly quantified in public data.[^76]

### 7.4 Drone Applications

Venue drone use divides into three distinct application categories with different regulatory and operational profiles:

**Facility inspection:** Drone-based structural inspection of venue roofs, facades, and large structural elements is commercially mature. Drones achieve DIN-certified accuracy of up to 99.9% with 1–3 cm horizontal tolerances over 40-meter spans, reducing safety risks and costs versus traditional rope-access inspection. AI algorithms automatically detect and classify structural defects including cracks, corrosion, and misalignments.[^77][^78]

**Security surveillance:** Law enforcement agencies (not venue operators) deploy drones for perimeter monitoring at major events. Commercial drones are typically banned within restricted airspace zones around major sporting events, creating a liability and regulatory barrier to private venue-operated drone security programs. Drone security programs are operationally feasible only in partnership with or operated by law enforcement.[^79][^80]

**Broadcast/media coverage:** Stadium drone cinematography is established and governed by FAA waiver/authorization processes in the US.

### 7.5 Liability and Insurance Considerations

Liability frameworks for autonomous systems in public assembly venues remain nascent. Key risk categories include:
- **Physical injury:** Autonomous robots operating in crowds create new product liability exposure; venue operators should require vendor-carried products liability insurance and indemnification clauses
- **System failure at critical moments:** Autonomous concession/delivery failures during peak event periods require fallback staffing protocols
- **Data/sensor privacy:** Robots equipped with cameras or sensors may trigger biometric privacy obligations under BIPA, CCPA, or PIPEDA in certain use configurations
- General commercial liability policies have not standardized autonomous robotics coverage; specialized endorsements are required

***

## 8. Data Privacy Regulations Affecting Venue Technology

### 8.1 United States — California CCPA/CPRA

The California Privacy Protection Agency (CPPA) finalized a major regulations package under CCPA/CPRA, approved by the California Office of Administrative Law on September 22, 2025, effective **January 1, 2026**. The package covers:[^81]

- **Automated Decision-Making Technology (ADMT):** Consumers gain the right to opt out of ADMT used for significant decisions (including facial recognition, identity verification, and profiling based on sensitive location). This directly impacts venues using AI-driven access control, dynamic pricing calibrated to individual profiles, or marketing personalization engines[^82]
- **Cybersecurity audits:** Required for qualifying businesses; certifications must be submitted to CPPA on a deadline-specific schedule[^81]
- **Risk assessments:** Required for processing of sensitive personal information, which includes biometric identifiers, precise geolocation, and inferences drawn from personal data[^82]
- **Compliance timeline:** Risk assessments and cybersecurity audit requirements phase in through 2028[^83]
- **Penalties:** $7,500 per intentional violation per individual; $2,500 per unintentional[^84]

A venue collecting location, behavioral, and payment data through WiFi login, mobile app, and loyalty programs may meet the CCPA threshold (100,000+ California residents annually or 50%+ revenue from data sharing). The 2026 ADMT opt-out rights create a specific compliance obligation for venues deploying AI-driven personalization or facial recognition entry systems.[^84]

### 8.2 Canada — PIPEDA and OPC Biometrics Guidance

The Office of the Privacy Commissioner of Canada (OPC) issued updated biometrics guidance on **August 11, 2025** — the first update since 2011 — covering both federal institutions and private-sector organizations deploying biometric technologies. Key requirements under PIPEDA for venues deploying facial recognition, fingerprint scanning, or similar systems:[^85][^86]

- **Express consent** required before collecting biometric data; brief or transient use is still considered sensitive[^86]
- Biometric information that uniquely identifies an individual is **always sensitive** under PIPEDA[^87]
- Strong physical, organizational, and technical security measures required; cancellable biometrics and encryption recommended[^86]
- Biometric data breaches must be reported to OPC and affected individuals when risk of significant harm exists[^86]
- **Quebec additional requirements:** Organizations must notify Quebec's Commission d'accès à l'information (CAI) at least **60 days** before deploying any biometric system, even without stored data; a Privacy Impact Assessment (PIA) is mandatory before deployment[^87]

Canadian venues (including Alberta) operate under PIPEDA for private-sector activity. Quebec's CAI requirements apply to venues hosting Quebec-based customers or operating in Quebec.

### 8.3 US Biometric Privacy State Laws

As of 2025, more than 20 US states have enacted or proposed biometric privacy laws. The three most consequential for venues:[^88]

| Law | Jurisdiction | Key Requirements | Enforcement Mechanism |
|---|---|---|---|
| BIPA (2008, as amended) | Illinois | Written consent before collection; retention policy; data destruction schedule | Private right of action; $1,000–$5,000/violation; class actions[^89] |
| CUBI | Texas | Notice and consent before collection; reasonable security | AG civil penalties: $25,000/violation[^89] |
| BPPA | Washington | Transparency and consent; data minimization; consumer rights | AG enforcement[^88] |

Illinois BIPA litigation remained active through 2025, with major settlements including a $51.75M facial recognition settlement (65,000–125,000 class members), a $47.5M settlement involving 150,000 facial-recognition subjects, and an $8.75M settlement covering 660,000 students. The litigation risk under BIPA is existential for venues deploying facial recognition in Illinois without rigorous consent architecture.[^89]

For venues using facial recognition for entry (a growing application in league-wide ticketing programs), **opt-in consent architecture** is the compliance standard under BIPA and the OPC guidance — not merely notice. The practical implication is that facial recognition ticketing must be offered as an opt-in alternative to conventional scanning, not as the default method.

### 8.4 GDPR Implications for International Events

GDPR applies to any event — regardless of where the organizer is based — that collects personal data from EU or EEA individuals. For North American venues hosting international competitions (FIFA 2026, Grand Slam tennis, Formula 1 circuits), GDPR governs data collected from EU-resident attendees and ticketholders. Key implications:[^90][^91]

- **Legal basis required** for all personal data processing (consent for marketing, legitimate interest for security/operations)[^91]
- **72-hour breach notification** to EU supervisory authority if a breach involves EU resident data[^91]
- **Data minimization:** Collect only what is necessary for stated purposes; 90 days post-event is a commonly cited retention benchmark[^92]
- **Penalties:** Up to €20 million or 4% of annual global revenue, whichever is greater[^91]

### 8.5 Privacy Regulatory Matrix — Venue Technology Impact

| Regulation | Jurisdiction | Technology Triggering Compliance | Key Venue Obligation |
|---|---|---|---|
| CCPA/CPRA (2026 updates) | California | WiFi login, apps, loyalty, facial recognition, AI personalization | ADMT opt-out; biometric consent; risk assessments[^81][^82] |
| PIPEDA + OPC Biometrics Guidance | Canada (federal) | Facial recognition, fingerprint access, behavioral analytics | Express consent; breach notification; data minimization[^86] |
| CAI + Law 25 | Quebec | Any biometric system | 60-day pre-deployment notice; mandatory PIA[^87] |
| Illinois BIPA | Illinois | Facial recognition, fingerprint, voice biometrics | Written opt-in consent; retention policy; private right of action[^89] |
| Texas CUBI | Texas | Facial recognition, fingerprint | Notice and consent; $25K/violation AG enforcement[^89] |
| Washington BPPA | Washington | Facial recognition, fingerprint | Consent; data minimization; consumer rights[^88] |
| EU GDPR | International events (EU attendees) | All PII collection from EU residents | Legal basis; 72-hr breach notice; €20M max penalty[^91] |
| PCI DSS 4.0 | Universal (payment card acceptance) | Ticketing, concessions, parking POS | Full 64-requirement compliance from March 2025[^41][^43] |

***

## Knowledge Gaps and Research Limitations

Several areas warrant acknowledgment as incomplete or requiring direct primary-source verification:

1. **WiFi 7 bandwidth-per-attendee benchmarks:** Industry guidance from the Wi-Fi Alliance on 2026–2027 recommended bandwidth-per-attendee for different venue types (convention center vs. stadium vs. arena) was not surfaced in independent verified form during this research cycle. The commonly cited 1–2 Mbps/attendee sustained figure for stadia derives from operator experience, not Wi-Fi Alliance formal guidance documentation.

2. **NEVI venue-specific case studies:** No published case studies of venues that have successfully obtained NEVI funding for parking EV charging were identified as of April 2026. The August 2025 IFG that unlocked venue parking eligibility is recent; deployments are likely in early planning stages.

3. **Autonomous robotics liability insurance standards:** No authoritative industry standards body or major insurer has published venue-specific guidelines for autonomous systems liability coverage as of this research date.

4. **CISA public assembly venue guidance:** A specific CISA guidance document targeted at public assembly venues (as distinct from general critical infrastructure) was not identified. Venue operators should apply CISA's sector-agnostic resources and the Commercial Facilities Sector-Specific Plan.

5. **Rogers Canada 5G venue deployments:** Canadian carrier 5G private network venue deployments equivalent to the MLB (T-Mobile) and NHL (Verizon) US programs were not identified in this research cycle. The Canadian wireless venue market may lag US league-driven deployment.

---

## References

1. [AI-Powered Venue Operations in 2026: Automating Management for ...](https://www.ticketfairy.com/blog/ai-powered-venue-operations-in-2026-automating-management-for-efficiency-and-enhanced-experiences) - Machine learning models can forecast attendance and staffing needs by analyzing historical data, tic...

2. [Enhancing crowd management through behaviourally informed ...](https://www.sciencedirect.com/science/article/pii/S2590123025042562) - Deep learning architectures like CNNs, LSTMs, GANs, and attention-based autoencoders achieve state-o...

3. [Smart AI-Powered Crowd and Event Management - KE Leaders](https://keleaders.com/smart-ai-powered-crowd-and-event-management/) - Real-Time Monitoring & Analysis. Using computer vision systems like YOLOv11 and edge computing, AI a...

4. [How Spatial AI Is Transforming Crowd Management in Modern ...](https://insights.outsight.ai/how-spatial-ai-is-transforming-crowd-management-in-modern-venues/) - Spatial AI and LiDAR enable venues to monitor crowds in real time, improving safety, guest experienc...

5. [ZeroEyes Marks Successful 2025 Highlighted by Rapid Growth ...](https://www.zeroeyes.com/blog/zeroeyes-marks-successful-2025-highlighted-by-rapid-growth-expanded-partnerships-1-000-confirmed) - After achieving sustained growth in North America with 98% customer retention, ZeroEyes extended its...

6. [ZeroEyes Marks Successful 2025 Highlighted by Rapid Growth ...](https://www.prnewswire.com/news-releases/zeroeyes-marks-successful-2025-highlighted-by-rapid-growth-expanded-partnerships-1-000-confirmed-real-world-firearm-detections-302659286.html) - ZeroEyes' AI gun detection and intelligent situational awareness software layers onto existing digit...

7. [Evolv Technology Surpasses 4 Billion People Screened Worldwide](https://evolv.com/resources/press-releases/evolv-technology-surpasses-four-billion-people-screened-worldwide-screening-more-people-per-day-than-the-tsa-in-2025/) - Evolv Technology has screened over 4 billion people worldwide, more people per day than the TSA, sin...

8. [FTC Takes Action Against Evolv Technologies for Deceiving Users ...](https://www.ftc.gov/news-events/news/press-releases/2024/11/ftc-takes-action-against-evolv-technologies-deceiving-users-about-its-ai-powered-security-screening) - In the proposed FTC settlement order, Evolv would be banned from making unsupported claims about its...

9. [FTC Settlement with Stadium Security Company Evolv Technologies](https://sportslitigationalert.com/ftc-settlement-with-stadium-security-company-evolv-technologies-allegations-and-implications/) - The FTC claimed Evolv misled customers about how accurately its Evolv Express scanners could detect ...

10. [AI-Powered Predictive Maintenance for HVAC Systems](https://ifactoryapp.com/industries/hvac/ai-predictive-maintenance-hvac-systems-guide) - The results are documented and dramatic: 40–60% reduction in emergency calls, 20–30% extension of eq...

11. [AI-Driven Predictive Maintenance in HVAC Systems - Cimetrics](https://cimetrics.com/ai-driven-predictive-maintenance-in-hvac-systems/) - This article details the major advantages of AI-driven predictive maintenance in HVAC systems, and h...

12. [Predictive Maintenance for Zero-Emission Building Pathways - Oxand](https://oxand.com/en/predictive-maintenance-zero-emission-building-pathways-roi-first/) - IoT and AI-powered predictive maintenance cuts building maintenance costs, trims HVAC energy 15–25%,...

13. [Dynamic Ticket Pricing in 2026: Strategies to Maximize Revenue ...](https://www.ticketfairy.com/blog/dynamic-ticket-pricing-in-2026-strategies-to-maximize-revenue-and-attendance) - Dynamic pricing adjusts ticket costs in real time based on demand, allowing events to capture more r...

14. [AI dynamic pricing could impact what each shopper pays individually](https://www.yahoo.com/news/articles/ai-dynamic-pricing-could-impact-205330701.html) - AI dynamic pricing could impact what each shopper pays individually. Jozef Korzeniewski. Wed, March ...

15. [How AI is Revolutionizing Stadium Concessions with Real-Time ...](https://markets.chroniclejournal.com/chroniclejournal/article/tokenring-2025-10-30-from-seats-to-snacks-how-ai-is-revolutionizing-stadium-concessions-with-real-time-wait-times) - Among the most impactful innovations are new systems that allow attendees to view real-time concessi...

16. [Stadium Digital Twin: Revolutionize Venue Management - Simio](https://www.simio.com/stadium-digital-twin) - Stadium operators implementing digital twin and simulation technologies achieve quantifiable returns...

17. [What Every CIO Can Learn From MLS's First Wi-Fi 7 Stadium - Forbes](https://www.forbes.com/sites/stevemcdowell/2026/03/05/what-every-cio-can-learn-from-mlss-first-wi-fi-7-stadium/) - According to IDC, WLAN revenue is expected to grow by 12% in 2025, with Wi-Fi 7 shipments accounting...

18. [Flawless connectivity for packed stadiums: How Wi-Fi 7 delivers](https://www.ruckusnetworks.com/blog/2025/flawless-connectivity-for-packed-stadiums-how-wi-fi-7-delivers-unrivaled-performance/) - RUCKUS is the first and only vendor as of April 2025 to offer a complete Wi-Fi 7 solution for large ...

19. [Transforming the Stadium Experience with WiFi 7 - The Fast Mode](https://www.thefastmode.com/expert-opinion/47302-transforming-the-stadium-experience-with-wifi-7) - Another benefit is that even older devices can see positive changes from WiFi 7 deployment – data sh...

20. [LAFC and RUCKUS Networks Deploy Next-Generation Wi-Fi 7 ...](https://www.businesswire.com/news/home/20260303722554/en/LAFC-and-RUCKUS-Networks-Deploy-Next-Generation-Wi-Fi-7-Network-at-BMO-Stadium) - Next-generation wireless infrastructure from RUCKUS, optimized by AI, sets new standard for fan expe...

21. [30 stadiums, 30 networks – T-Mobile knocks it out of the park](https://rcrtech.com/rcrwirelessnews/t-mobile-private-5g-stadiums-baseball/) - T-Mobile has deployed fully private 5G networks across all 30 MLB ballparks, using Ericsson hardware...

22. [The Rink Reimagined: How Verizon's Private 5G is ... - NAB Show](https://www.nabshow.com/session/how-to-deliver-the-2026-fifa-world-cup/) - This presentation explores the successful, league-wide deployment of Verizon's Private 5G Wireless N...

23. [NHL Innovation Lab next chapter in League's technology journey](https://www.nhl.com/news/nhl-innovation-lab-next-step-in-technology-journey) - The deployment of Verizon's Private 5G Wireless Network will provide the NHL Innovation Lab with a d...

24. [AT&T, T-Mobile, Verizon diverge on 5G Super Bowl strategies](https://www.lightreading.com/5g/at-t-t-mobile-verizon-diverge-on-5g-super-bowl-strategies) - A new report from Signals Research Group (SRG) helps to highlight the different 5G strategies employ...

25. [Inside T-Mobile's Private 5G Network at the PGA - LinkedIn](https://www.linkedin.com/pulse/inside-t-mobiles-private-5g-network-pga-john-saw-cicgc) - The 2025 PGA Championship at Quail Hollow isn't just another sports event; it's a proving ground for...

26. [Fifth Generation (5G)-Powered Smart Stadiums Market](https://finance.yahoo.com/news/fifth-generation-5g-powered-smart-094400461.html) - The 5G-powered smart stadium market has been experiencing unprecedented growth, expecting to rise fr...

27. [The Future of DAS Communication Systems in 2025: 5G Integration ...](https://dassystems.com/the-future-of-das-communication-systems-in-2025-5g-integration-edge-computing-and-smart-connectivity/) - Distributed Antenna Systems (DAS) will evolve into highly efficient, 5G-powered networks designed to...

28. [DAS for Stadiums in 2025: How to Keep Fans Connected in High ...](https://www.rsrf.com/blog/das-for-stadiums) - Discover how to implement DAS for stadiums to improve connectivity, fan experience, and operational ...

29. [27 February 2025 - Sumitomo Electric](https://sumitomoelectric.com/press/2025/02/prs018) - Our company will be exhibiting our Distributed Antenna System (DAS), which enables high-speed, high-...

30. [Smart Crowd Management in 2026: Tech Solutions to Keep Large ...](https://www.ticketfairy.com/blog/smart-crowd-management-in-2026-tech-solutions-to-keep-large-events-safe-and-efficient) - Computer Vision for Counting and Density Analysis. One of the most transformative tools in crowd man...

31. [Best IoT Sensors for Facility Management 2026 - Oxmaint](https://oxmaint.com/industries/facility-management/best-iot-sensors-for-facility-management-2026) - Best IoT sensors for facility management in 2026, covering smart temperature, humidity, air quality,...

32. [Revolutionize HVAC Efficiency with IoT Sensors in 2025](https://www.marhy.com/revolutionize-hvac-efficiency-with-iot-sensors-in-2025/) - Yes, IoT sensors can improve indoor air quality by automatically adjusting ventilation and filtratio...

33. [HVAC Sensors in the Real World: 5 Uses You'll Actually See (2025)](https://www.linkedin.com/pulse/hvac-sensors-real-world-5-uses-youll-actually-see-2025-tubtf) - HVAC sensors enable dynamic adjustment of heating and cooling based on occupancy and environmental c...

34. [RFID vs. Bluetooth Beacons: 2025 Performance & Price Guide](https://nextwaves.com/blog/rfid-rtls-vs-bluetooth-beacons-choosing-the-right-tracking-technology-for-2025) - Compare RFID RTLS, Bluetooth Beacons, and UWB. Get 2025-2026 price estimates and performance data fo...

35. [Ultra-Wideband Technology: Redefining Precision in Asset Tracking](https://logisticsviewpoints.com/2025/05/27/ultra-wideband-technology-redefining-precision-in-asset-tracking/) - UWB systems provide highly accurate, real-time positioning data, particularly effective in indoor en...

36. [Asset Tracking Technologies Today: RTLS, UWB, RFID & More](https://wisersystems.com/blog/asset-tracking-technologies-comprehensive-guide/) - RTLS combines hardware and software to continuously track the location of assets ... RFID's low-cost...

37. [NIST's 2025 IoT Cybersecurity Update: What You Need to Know](https://cybersecurity.industry411.com/2025/05/21/nists-2025-iot-cybersecurity-update/) - The updated guidance introduces a seventh foundational activity and widens the focus to include indu...

38. [Workshop on Foundational Cybersecurity Activities for IoT Device ...](https://www.nist.gov/news-events/events/2025/03/workshop-foundational-cybersecurity-activities-iot-device-manufacturers) - NIST will host a full-day hybrid workshop at the NCCoE to continue discussions related to a major up...

39. [Ransomware surge in 2025 exposes mounting OT risk as industrial ...](https://industrialcyber.co/ransomware/ransomware-surge-in-2025-exposes-mounting-ot-risk-as-industrial-impacts-outpace-it-narratives/) - Dragos tracked 119 ransomware groups targeting industrial organizations in 2025, collectively impact...

40. [5 Trends Driving OT Security in 2026: From State-Sponsored Attacks ...](https://nexusconnect.io/articles/5-trends-driving-ot-security-in-2026-from-state-sponsored-attacks-to-ai-powered-threats) - GuidePoint expects 2026 to be another big year for ransomware, finding December 2025 to be the most ...

41. [PCI DSS 4.0: Facts and Compliance Insights in 2025](https://www.clearlypayments.com/blog/pci-dss-4-0-facts-and-compliance-insights-in-2025/) - PCI DSS 4.0 changes become mandatory in 2025. Learn what's new: continuous risk analysis, stronger p...

42. [PCI DSS 4.0 Mandatory Requirements: 2025 Compliance Guide](https://linfordco.com/blog/pci-dss-4-0-requirements-guide/) - Learn PCI DSS 4.0's 47 mandatory requirements that are now in effect. Complete guide covering authen...

43. [PCI DSS 4.0.1 for Venues—Why Outsourced POS and Ticketing Are ...](https://docs.bentosecurity.com/en/articles/4790721) - PCI 4.0.1 emphasizes verifying the compliance status of your vendors and having written contracts th...

44. [[PDF] The NIST Cybersecurity Framework (CSF) 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) - The NIST Cybersecurity Framework (CSF) 2.0 provides guidance to industry, government agencies, and o...

45. [What is NIST Cybersecurity Framework (CSF) 2.0? - Safe Security](https://safe.security/resources/insights/nist-cybersecurity-framework/) - NIST CSF 2.0 represents the most significant update to the framework. Released as a public draft in ...

46. [NIST releases draft AI cybersecurity framework profile to guide ...](https://siliconangle.com/2025/12/17/nist-releases-draft-ai-cybersecurity-framework-profile-guide-secure-ai-adoption/) - CSF 2.0 organizes risk management around core functions like Govern, Identify, Protect, Detect, Resp...

47. [CISA 2025 Year in Review focuses on driving security and ...](https://industrialcyber.co/cisa/cisa-2025-year-in-review-focuses-on-driving-security-and-resilience-across-critical-infrastructure/) - CISA 2025 Year in Review focuses on driving security and resilience across critical infrastructure. ...

48. [The Early Rise of Digital Twins in Sport—and How the Olympic ...](https://www.linkedin.com/pulse/early-rise-digital-twins-sportand-how-olympic-became-next-todd-iujec) - Announced in late 2020, SoFi Stadium became the first major U.S. venue to deploy a fully operational...

49. [Digital Twin Technology: Revolutionizing Stadium Management](https://www.simio.com/blog/digital-twin-technology-revolutionizing-stadium-management) - Digital twin tech boosts stadium operations by optimizing security, concessions, and fan engagement ...

50. [SoFi Stadium Builds Out Digital Twin for Operations and Maintenance](https://www.enr.com/articles/50568-sofi-stadium-builds-out-digital-twin-for-operations-and-maintenance) - As home of both the Rams and the Chargers, it's the first NFL stadium that has a digital twin being ...

51. [FIFA 2026: Why Every Host Stadium Needs a Digital Twin](https://www.thefuture3d.com/blog/fifa-2026-stadium-digital-twins/) - A stadium digital twin is a precise, measurement-grade 3D model of the entire facility — interior an...

52. [Commonwealth Stadium digital twin event plans | VenueTwin](https://www.venuetwin.com/case-studies/how-venue-twin-is-a-game-changer-for-commonwealth-stadium/) - Commonwealth Stadium in Edmonon, Canada, uses VenueTwin to visualize its event plans so stakeholders...

53. [Smart Stadiums: AI Trends & Benefits 2026 | Go Wombat](https://gowombat.team/blog/posts/how-smart-stadiums-are-evolving-into-digital-ecosystems) - They rolled out digital twins across entire stadiums to keep crowds moving smoothly, fine-tune the c...

54. [[PDF] Proposed BIM-CMMS Framework for Facility Management in Digital ...](https://www.americaspg.com/article/pdf/3746) - To achieve this, an integrated framework combining Building. Information Modeling (BIM) and Computer...

55. [BIM, AI, and Digital Twins: Key Lessons from Toronto's BIM Summit ...](https://www.linkedin.com/pulse/bim-ai-digital-twins-key-lessons-from-torontos-summit-valeria-cuadra-la01f) - The BIM Summit 2025 in Toronto reinforced the importance of collaboration, innovation, and technolog...

56. [Why a Digital Twin is the Next Big Thing - SWG NA](https://www.swg.com/na/blog/digital-twin-the-next-big-thing/) - A digital twin is the next level of BIM in providing data and enabling improved service. BIM models ...

57. [Digital Twins Revolutionize Stadium Planning and Fan Experience](https://www.linkedin.com/posts/robkinder-sports-tech-law_sportstech-uksportstech-digitaltwins-activity-7426961912778895360-qK7d) - Digital twins are turning stadiums into always-on, virtual versions of themselves. That's changing h...

58. [[PDF] Digital - stadiums - PwC](https://www.pwc.com/m1/en/publications/documents/2024/digital-stadiums-eng.pdf) - The digital stadium sector is projected to witness significant growth, expanding by 20.6% annually b...

59. [National Electric Vehicle Infrastructure (NEVI) Formula Program](https://afdc.energy.gov/laws/12744) - The acquisition, installation, and network connection of EV chargers to facilitate data collection, ...

60. [Understanding the U.S. NEVI Program in 2025 – EVDANCE](https://evdances.com/blogs/blog/understanding-the-current-status-of-the-u-s-national-electric-vehicle-infrastructure-nevi-program) - Explore the current status, progress, and challenges of the U.S. National Electric Vehicle Infrastru...

61. [[PDF] National Electric Vehicle Infrastructure Formula Program Interim ...](https://www.dot.state.wy.us/files/live/sites/wydot/files/shared/Planning/Electric%20Vehicles/NEVI-Interim-Final-Program-Guidance-8-11-2025.pdf) - The Program provides $5 billion of funding to States to deploy electric vehicle (EV) charging infras...

62. [New Federal Highway Administration Guidance on EV Infrastructure](https://www.climatesolutionslaw.com/2025/09/new-federal-highway-administration-guidance-on-ev-infrastructure-what-comes-next/) - Despite the comment period following IFG issuance on August 11, 2025, States still need to submit up...

63. [National Electric Vehicle Infrastructure (NEVI) Program Updated ...](https://electrificationcoalition.org/resource/national-electric-vehicle-infrastructure-nevi-program-updated-guidance/) - On August 11, 2025, the U.S. Department of Transportation (DOT) released updated interim final NEVI ...

64. [The United States of NEVI - ACT News](https://www.act-news.com/news/the-united-states-of-nevi/) - The NEVI program, funded with $5 billion through FY 2026, has resumed momentum after a 2025 funding ...

65. [President Trump's Transportation Secretary Sean P. Duffy Unveils ...](https://www.transportation.gov/briefing-room/president-trumps-transportation-secretary-sean-p-duffy-unveils-revised-nevi-guidance) - President Trump's Transportation Secretary Sean P. Duffy Unveils Revised NEVI Guidance to Allow Stat...

66. [US Minimum Standards for EV Charging Infrastructure - eDRV](https://edrv.io/guide/nevi-minimum-standards-for-ev-charging-infrastructure) - This guide covers the most important requirements on EV Charging Stations and Networks that receive ...

67. [It Just Got Easier To Install NEVI-Funded EV Charging Stations ...](https://qmerit.com/blog/nevi-program-charging-incentive-updates/) - The NEVI Formula Program is a $5 billion initiative distributing formula grants to states from 2022 ...

68. [Zero Emission Vehicle Infrastructure Program](https://natural-resources.canada.ca/energy-efficiency/transportation-energy-efficiency/zero-emission-vehicle-infrastructure-program) - The Government of Canada's ZEV charging and refuelling infrastructure targets are currently 84,500 c...

69. [Zero Emission Vehicle Infrastructure Program](https://natural-resources.canada.ca/energy-efficiency/transportation-energy-efficiency/zero-emission-vehicle-infrastrusture/zero-emission-vehicle-infrastructure-program) - Budget 2022 proposes to invest an additional $1.7 billion to extend the government's purchase incent...

70. [Autonomous Cleaning in a Sports Hall | Case Study - YouTube](https://www.youtube.com/watch?v=IVHLdrbAP3s) - ... Sports Hall Promo 2024 until 31. January 2025! For questions, contact us directly at robotic@cle...

71. [Delivery robots could roll into Al Lang Stadium - St Pete Catalyst](https://stpetecatalyst.com/delivery-robots-could-roll-into-al-lang-stadium/) - Kiwibots are now delivering food on 21 college campuses, and the company hopes to reach 30 by the en...

72. [Next Bite Robotics Revolutionizes Stadium Concessions with Fast ...](https://www.linkedin.com/posts/next-bite-robotics_nextbiterobotics-foodtech-sportstech-activity-7440126640065769472-ju7F) - It showcases the rapid progress in agile control of humanoid robots over the past year, demonstratin...

73. [Launching Canada's First Medium-Speed Autonomous Shuttle](https://www.kanatanorthba.com/knsmartshuttle/) - The shuttle will operate along a 4.5 km route with eight designated stops, linking businesses, resta...

74. [Aurrigo launches Canada's first all-season, medium-speed ...](https://aurrigo.com/aurrigo-launches-canadas-first-all-season-medium-speed-autonomous-shuttle-in-kanata/) - The 4.5 km route has been strategically designed to link businesses, restaurants, community spaces, ...

75. [Aurrigo debuts winter-ready autonomous shuttle in Canada](https://www.autonomousvehicleinternational.com/news/mobility-solutions/aurrigo-debuts-winter-ready-autonomous-shuttle-in-canada.html) - There will be eight designated stops along the route, linking businesses, restaurants, community spa...

76. [Automated Vehicles: Low Speed Shuttles | ITS Deployment Evaluation](https://www.itskrs.its.dot.gov/briefings/executive-briefing/automated-vehicles-low-speed-shuttles) - The two Mcity shuttles are fully-automated, 11-seat, all-electric shuttles manufactured by NAVYA tha...

77. [How Ai is Improving Drone Inspections in 2025 - VSI Aerial](https://www.vsiaerial.com/post/ai-drone-inspections-in-2025) - Advanced AI algorithms automatically detect and classify structural defects - such as cracks, corros...

78. [2025 roof inspection: drone vs. satellite vs. aircraft - Airteam](https://www.airteam.ai/en/blog/drohne-vs-satelliten-flugzeug-dachinspektion-vergleich-2025) - Drones achieve 99.9% DIN accuracy vs. 50cm+ satellite deviation. Ultimate comparison 2025: Costs, pr...

79. [Why not drone surveillance for big events with nearby roofs? - Reddit](https://www.reddit.com/r/NoStupidQuestions/comments/1nkdqaa/why_not_drone_surveillance_for_big_events_with/) - They have been used in the past, but it's a balance typically all drones are completely banned withi...

80. [How drones are changing the security landscape for large sports ...](https://www.asapident.com/how-drones-are-changing-the-security-landscape-for-large-sports-venues/) - This guide explores how drones are becoming instrumental in securing large sports venues, their appl...

81. [California Finalizes Regulations to Strengthen Consumers' Privacy](https://cppa.ca.gov/announcements/2025/20250923.html) - The regulations go into effect January 1, 2026. However, there is additional time for businesses to ...

82. [Privacy update: CCPA/CPRA regulations finalized - Grant Thornton](https://www.grantthornton.com/insights/articles/advisory/2025/privacy-update-ccpa-cpra-regulations-finalized) - California finalizes CCPA/CPRA rules on ADMT, risk assessments, and cybersecurity audits—compliance ...

83. [CCPA 2025 updated regulations: What's new, what's next, and what ...](https://www.dlapiper.com/insights/publications/2025/09/ccpa-2025-updated-regulations) - The updated regulations take effect January 1, 2026, with compliance for certain components spanning...

84. [CCPA Privacy Policy Requirements 2025: Complete Compliance ...](https://secureprivacy.ai/blog/ccpa-privacy-policy-requirements-2025) - This comprehensive guide breaks down exactly what your privacy policy must contain to achieve CCPA c...

85. [Privacy Commissioner of Canada publishes guidance on biometrics](https://www.priv.gc.ca/en/opc-news/news-and-announcements/2025/nr-c_250811/) - Privacy Commissioner of Canada publishes guidance on biometrics. August 11, 2025 – Gatineau, QC. As ...

86. [Canada's Officer of the Privacy Commissioner Issues Guidance on ...](https://www.jdsupra.com/legalnews/canada-s-officer-of-the-privacy-9356957/) - Valid, meaningful, and express consent is required for the collection, use, and disclosure of biomet...

87. [Privacy Commissioner of Canada's new guidance on biometrics - BLG](https://www.blg.com/en/insights/2025/09/privacy-commissioner-of-canadas-new-guidance-on-biometrics-what-does-it-mean-for-your-business) - On Aug. 11, 2025, the Office of the Privacy Commissioner of Canada (OPC) issued its final Guidance f...

88. [Biometric Privacy Laws in 2025: What Security Integrators Need to ...](https://www.parabit.com/post/biometric-privacy-laws-in-2025-what-security-integrators-need-to-know) - In 2025, more than 20 US states have enacted or proposed biometric privacy laws, making legal compli...

89. [2025 Year-In-Review: Biometric Privacy Litigation](https://www.privacyworld.blog/2025/12/2025-year-in-review-biometric-privacy-litigation/) - CUBI allows the Texas Attorney General to seek civil penalties of $25,000 per violation, meaning tha...

90. [GDPR Compliance for Events](https://gdprlocal.com/gdpr-compliance-for-events/) - If you are running events in 2025, GDPR compliance is not a formality; it is necessary for building ...

91. [Navigating Global Data Privacy in Event Tech: GDPR, CCPA ...](https://www.ticketfairy.com/blog/navigating-global-data-privacy-in-event-tech-gdpr-ccpa-compliance-strategies-for-2026) - Master data security regulations for events in 2026. Learn how GDPR, CCPA, and global compliance fra...

92. [Navigating Privacy at Corporate Events: GDPR and U.S. ... - LinkedIn](https://www.linkedin.com/pulse/navigating-privacy-corporate-events-gdpr-us-focus-ilia-dubovtsev-msnge) - The GDPR, enforceable since May 2018, applies to any organisation processing personal data of EU res...

