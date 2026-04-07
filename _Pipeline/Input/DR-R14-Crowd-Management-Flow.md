# R-14: Crowd Management and Flow Engineering for Public Assembly Venues

## Executive Summary

Crowd management and flow engineering sit at the intersection of physics, behavioral science, architecture, and regulatory compliance. This domain carries direct life-safety implications: every major crowd disaster of the past four decades has exposed a preventable failure in one or more of its constituent disciplines — crush prevention science, density monitoring, ingress/egress design, occupancy regulation, simulation modeling, crowd management planning, and professional staffing. This report synthesizes current scientific understanding, technology capabilities, regulatory frameworks, simulation tools, planning methodologies, post-incident regulatory evolution, and professional standards as of April 2026. It provides the depth and sourcing needed for practitioner reference, replacing thin concept-note coverage with authoritative, citeable material.

***

## 1. Crush Prevention Science and Crowd Dynamics

### 1.1 The Physics of Crowd Crush

Crowd crush is not caused by "panic" — the term is largely a media and lay invention. The physical mechanism is **compressive asphyxia** from sustained lateral or anterior–posterior pressure on the thorax. At extreme crowd densities, the combined force of many bodies pressing against one another restricts chest excursion and blocks venous return, producing traumatic asphyxiation while victims remain upright. Victims may expire while still standing, only collapsing when surrounding pressure briefly abates. Research on the Itaewon crush found that individuals of smaller stature and lower body mass faced disproportionate lethality under the same crowd forces, underscoring that force thresholds are population-dependent.[^1]

The decisive triggering mechanism in most disasters is not deliberate stampeding but **crowd turbulence** — a phenomenon characterized by large, random, uncontrollable displacements of individuals in all directions once density crosses critical thresholds. At average densities of approximately **6 persons per square meter**, local density peaks can reach 9 per square meter or higher, because density distribution is never homogeneous. When the maximum local density reaches approximately **7 persons per square meter**, a transition from laminar (smooth, directional) flow to longitudinally unstable flow occurs, characterized by upstream-moving stop-and-go waves of roughly 45-second periodicity. A subsequent transversal instability then generates crowd turbulence with displacement waves up to 12 meters, placing people at serious risk of falling and trampling. Research from Helbing et al. published in the journal Advances in Complex Systems confirms that crowd turbulence, not deliberate pushing, was "a crucial factor" in the Love Parade deaths.[^2][^3]

### 1.2 John Fruin's Level of Service Framework

John J. Fruin of the Port of New York Authority introduced the **Level of Service (LOS)** concept for pedestrian facilities in his 1971 Transportation Research Board paper *Designing for Pedestrians: A Level-of-Service Concept* and his landmark book *Pedestrian Planning and Design*. Fruin more than any other individual defined the density and speed relationship as guidelines for comfort and safety in places of public assembly, and his LOS standards remain a foundational reference in venue design and pedestrian engineering worldwide.[^4][^5]

The framework grades pedestrian facilities from A (free flow) through F (complete breakdown) based on area per person:

| LOS Grade | Area per Person | Flow Characteristics | Design Application |
|-----------|----------------|----------------------|-------------------|
| **A** | ≥35 sq ft (≥3.3 m²) | Free speed selection, easy bypass | Premium design target for terminals |
| **B** | 25–35 sq ft (2.3–3.3 m²) | Normal speed, minor conflicts in bi-directional flow | Acceptable for transportation buildings |
| **C** | 15–25 sq ft (1.4–2.3 m²) | Restricted speed; stride and direction adjustments required | Most crowded public areas — design maximum for recurrent peaks |
| **D** | 10–15 sq ft (0.9–1.4 m²) | Severely restricted speed; multiple conflicts; reverse flow nearly impossible | Only for highest-density public areas |
| **E** | 5–10 sq ft (0.5–0.9 m²) | Shuffling gait; approaches theoretical capacity; frequent stoppages | Only for very short peak durations |
| **F** | <5 sq ft (<0.5 m²) | Complete flow breakdown; loss of individual control | Not recommended; represents loss of control, not flow |

[^6][^4]

Fruin's critical density — the point at which flow volumes decline even as crowding increases — occurs at approximately **2–3 persons per square meter**. Above this threshold, the system is operating in the unstable regime where any perturbation can trigger stop-and-go waves. Practitioners should note that Fruin made his measurements in pedestrian street environments; direct application to standing concert audiences, where behaviors differ markedly from pedestrian flows, requires professional judgment.[^7][^5]

### 1.3 Professor Keith Still's DIM-ICE Framework

Professor Dr. G. Keith Still, Professor of Crowd Science at Buckinghamshire New University (UK), developed the **DIM-ICE risk model** from systematic analysis of crowd accidents and incidents worldwide. The model provides a structured analytical framework for event planners, venue managers, and licensing authorities by decomposing crowd risk into two orthogonal dimensions:[^8][^9]

**Three primary influences on crowd behaviour (DIM):**
- **Design** — physical capacity, throughput, geometry, and layout of the venue or site
- **Information** — social media, signage, PA announcements, news, and communications affecting crowd expectations and decisions
- **Management** — operational processes, procedures, staffing, and real-time interventions

**Three primary phases of crowd behaviour (ICE):**
- **Ingress** — arrival at the venue, queueing, access routes, admission processes
- **Circulation** — movement within the venue, concourse use, amenity access, inter-stage migration
- **Egress** — departure from the venue, post-event dispersal

Both dimensions are assessed for **Normal** and **Emergency** modes, producing a 3×3×2 matrix that surfaces interaction effects invisible to checklist-based planning. The DIM-ICE matrix is applied alongside four core analytical tools described in Still's 2014 CRC Press book *Introduction to Crowd Science*: the DIM-ICE risk model, **RAMP Analysis** (Routes, Areas, Movement, People/profile), **Risk and Congestion Mapping**, and a Decision Support Analysis matrix for strategic and tactical options.[^10][^11][^12][^13][^8]

A later evolution, **DIM-ALICED**, developed by Crowd Safety Training (UK), extends the phases to include Arrival, Last Mile, Ingress, Circulation, Egress, and Dispersal — adding time-related elements that capture risk outside the formal venue boundary. For multi-stage festivals and urban outdoor events, this extended model better reflects the full attendee journey.[^14]

In operational application, the DIM-ICE framework translates directly into crowd management plan elements: venue capacity and throughput calculations (D), communications plans and pre-event information strategy (I), and staffing, steward deployment, and contingency procedures (M) — all mapped across the ingress, circulation, and egress phases at the start of planning.[^15][^10]

### 1.4 Helbing and Johansson: Density-Flow Research and Crowd Turbulence

Dirk Helbing (ETH Zürich) and Anders Johansson produced foundational quantitative research on crowd dynamics at extreme densities through empirical video analysis of the 2006 Mecca Hajj, where crowd densities reached among the highest ever measured in a public gathering. Their paper *From Crowd Dynamics to Crowd Safety: A Video-Based Analysis* (published in *Advances in Complex Systems*) revealed that **local pedestrian densities can exceed 9 persons per square meter even when average densities are 6 persons per square meter**, because density is spatially heterogeneous and concentrates at bottlenecks.[^16][^17]

Key density-flow transitions identified by Helbing et al.:[^18][^2]
1. **Smooth laminar flow** — low density, predictable directional movement
2. **Stop-and-go waves** — onset at 40–65% spatial occupancy; backward-propagating pressure waves at ~0.6 m/s interval
3. **Crowd turbulence** — transversal instability above ~7 persons/m²; uncontrolled multidirectional displacements

The practical implication for venue managers is that density monitoring must be **leading-indicator driven**, not reactive: by the time crowd turbulence is visually evident on CCTV, sufficient pressure has already accumulated for fatalities. Intervention thresholds should be set at 4–5 persons/m² (well before the critical 6 persons/m² average that triggers dangerous local peaks), and all monitoring and staffing plans should be calibrated to that operational threshold.[^17][^2]

***

## 2. Crowd Density Monitoring Technology

### 2.1 CCTV-Based Video Analytics

Camera-based crowd analytics is currently the most widely deployed technology for real-time density monitoring in public assembly venues. Modern systems pair **edge-AI processing directly on camera hardware** with cloud-based pattern analysis, enabling sub-second density estimates without transmitting raw video off-site.[^19][^20]

**Axis Communications** provides computer vision capabilities via its ARTPEC-8 chipset cameras with edge-based deep learning processing units. BriefCam Video Content Analytics — available embedded on Axis deep-learning cameras through the AXIS Camera Application Platform (ACAP) partnership — delivers real-time alerts up to **six times faster** than server-based analytics and achieves a 5–10x reduction in bandwidth usage by processing at the edge. BriefCam analytics include crowd density estimation, heat-map generation, and anomaly detection for abnormal crowd movement patterns.[^21][^20][^22][^19]

Accuracy for well-configured 2D edge-AI camera systems is approximately **95–98%** in controlled conditions. Positioning cameras at overhead angles of 20–35 feet provides optimal coverage for density estimation and movement pattern detection.[^23][^24]

### 2.2 LiDAR-Based Crowd Monitoring

**Light Detection and Ranging (LiDAR)** sensors create 3D point cloud representations of physical space by emitting pulsed laser light and measuring return times. Because LiDAR data consists entirely of geometric coordinates without color, texture, or facial features, the technology provides **inherent privacy preservation at the sensing level** — not merely through post-processing anonymization. A 2026 arxiv preprint specifically examining LiDAR for crowd management confirms that LiDAR achieves cm-level distance accuracy and high people-counting performance even in dense, occluded environments where camera systems degrade.[^25]

LiDAR's primary advantages for venue deployment are: accuracy in poor lighting and outdoor environments where camera performance degrades; inherent GDPR and privacy compliance without additional processing steps; and resistance to occlusion because 3D point clouds can separate overlapping individuals that appear merged in 2D camera images. The global people counting system market is projected to grow from $1.1 billion in 2023 to $2.3 billion by 2028, with LiDAR-based solutions taking an increasing share.[^26][^25]

### 2.3 Thermal Imaging

Thermal infrared cameras detect body heat signatures, generating person counts and density estimates without capturing any visible-spectrum identifying features. Terabee and similar manufacturers achieve **95–98% counting accuracy** using Time-of-Flight technology that records low-resolution depth maps with no personally identifiable information. Thermal imaging maintains accuracy in complete darkness and outdoor environments with variable ambient lighting, making it suitable for night festivals and large outdoor venues where standard cameras lose performance.[^27]

### 2.4 WiFi Probe Counting and Bluetooth Beacons

WiFi probe counting works by detecting management frames broadcast by smartphones searching for known networks. Historically deployed for footfall estimation in retail and outdoor public spaces, this approach has been **severely degraded by MAC address randomization** — a privacy feature implemented across iOS (since 2013) and Android (since 2014) that causes smartphones to broadcast temporary, random MAC addresses rather than the device's permanent identifier. Current accuracy for WiFi probe counting is **below 50%** in most deployments, with no directionality (unable to distinguish entries from exits) and no ability to track unique returning devices. Bluetooth beacons using BLE (Bluetooth Low Energy) face similar limitations.[^23]

For venues requiring meaningful density data, WiFi/Bluetooth counting is not recommended as a primary monitoring technology as of 2026. It retains some value only for very rough outdoor footfall trending where precise counts are not safety-critical.[^23]

### 2.5 Integration Architecture and Command Center Operations

Modern venues integrate multiple sensor feeds into a **Real-Time Command Center (RTCC)** that converts raw density data into actionable situational awareness. Key integration elements include:[^24][^28]

- **Heat-map visualization** overlaying density estimates on venue floor plans, updated in real time, enabling operators to identify developing bottlenecks before they become emergencies[^24]
- **Threshold-based automated alerting** that triggers pre-configured notification chains (radio, intercom, staff deployment) when density exceeds operational thresholds — typically set at 4+ persons/m²[^28]
- **Predictive modeling** that analyzes historical flow patterns and current sensor data to forecast crowd behavior 15–20 minutes ahead, enabling proactive rather than reactive intervention[^29]
- **Integration with access control** — automatic gate-locking, entry-rate throttling, and turnstile management to regulate inflow when density thresholds are approached[^28]
- **Drone and elevated mast cameras** providing aerial perspective to supplement fixed infrastructure, particularly useful for outdoor festival sites where fixed camera coverage is incomplete[^24]

Operational protocols should define clear intervention triggers at three levels: advisory (above 3 persons/m²), operational response (above 4 persons/m²), and emergency (above 5–6 persons/m²), with specific actions prescribed for each level in the event safety plan.[^30][^29]

***

## 3. NFPA Occupancy Requirements for Assembly Venues

### 3.1 NFPA 101 Life Safety Code: Chapters 12 and 13

**NFPA 101** (*Life Safety Code*) governs occupancy and egress requirements for both new assembly occupancies (Chapter 12) and existing assembly occupancies (Chapter 13). An assembly occupancy is defined in Section 3.3.152.2 as any occupancy used for a gathering of 50 or more persons for deliberation, worship, entertainment, eating, drinking, amusement, or awaiting transportation.[^31]

**Occupant Load Factors (Table 7.3.1.2):**

| Use Type | Area per Person | Area Basis |
|----------|----------------|------------|
| Concentrated assembly — chairs only, no tables | 7 sq ft (0.65 m²) | Net |
| Less concentrated assembly — tables and chairs | 15 sq ft (1.4 m²) | Net |
| Fixed seating | Count of seats | N/A |
| Bench-type seating without arms | 18 linear inches | N/A |
| Kitchen | 100 sq ft | Net |

[^32][^33][^34][^35]

The **IBC (International Building Code)** adds a specific **standing space** occupant load factor of **5 sq ft net per person** (Table 1004.5, 2018–2024 editions) that NFPA 101's Table 7.3.1.2 does not explicitly enumerate. Practitioners using NFPA 101 for standing-room concert venues must consult the applicable code edition and the Authority Having Jurisdiction (AHJ) for confirmation of the applicable factor.[^36][^37][^32]

**Means of Egress — Travel Distance Limits (Chapters 12/13):**
- New assembly occupancies (unsprinklered): maximum **200 ft** travel distance to exit[^38]
- New assembly occupancies (sprinklered): maximum **250 ft** travel distance to exit[^38]
- Minimum **two exits** required for occupant loads that trigger Chapter 12/13 thresholds; three exits required for occupant loads of 501–1,000; four or more for loads exceeding 1,000[^39]
- Minimum exit width derived from egress capacity factors: 0.3 in/person (unsprinklered) or 0.2 in/person (sprinklered) per unit width of stair; wider minimums apply to level components[^38]

**Crowd Manager Requirements (Section 12.7.6):**
NFPA 101 Section 12.7.6.1 requires every assembly occupancy to provide a minimum of **one trained crowd manager or crowd manager supervisor**. Where the occupant load exceeds 250, one additional trained crowd manager is required for **every 250 occupants** or portion thereof. Two limited exceptions exist: (1) assembly occupancies used exclusively for religious worship with an occupant load not exceeding 2,000, and (2) where the AHJ permits a reduced ratio based on the presence of an approved automatic sprinkler system and the nature of the event.[^40][^41][^31]

**Drill Requirements (Section 12.7.7):**
Section 12.7.7 requires that assembly occupancy staff be trained and drilled in emergency procedures. These crowd manager and drill requirements are not referenced in the National Building Code of Canada, a gap noted by Canadian fire safety practitioners.[^42]

**Sprinkler Requirements:**
Under the 2024 edition of NFPA 101, assembly occupancies with occupant loads exceeding 100 in existing occupancies require automatic sprinkler protection, and the 2024 edition also requires portable fire extinguishers in both new and existing assembly occupancies.[^43][^44]

### 3.2 NFPA 102 — Grandstands, Folding and Telescopic Seating, Tents, and Membrane Structures

**NFPA 102** extracts and consolidates requirements from NFPA 5000 and NFPA 101 specifically for life safety in temporary and permanent spectator seating, tents, and membrane structures. Key provisions include:[^45][^46]

- **Seating spacing**: Bleachers and grandstands require seat spacing of not less than **22 inches** back-to-back[^47]
- **Footboard depth**: Minimum **9 inches** with secure supports[^47]
- **Maximum seats per aisle**: 11 seats from farthest seat to aisle (outdoor); 6 seats (indoor); for bleachers, 20 (outdoor) and 9 (indoor)[^47]
- **Grouped units**: No more than three grandstand units grouped together before a 2-hour fire-rated firewall, or 50 ft of open space between groupings[^47]
- **Height limits**: Freestanding grandstands no more than 20 ft; portable grandstands within structures no more than 12 ft[^47]
- **Annual inspection**: Owners must arrange annual inspection of all bleachers, folding/telescopic seating, and grandstands by a qualified person — trained by manufacturer, professional engineer, or registered architect[^46]

NFPA 102 is primarily applicable to Type III, IV, and V construction grandstands; Type I and II construction is governed by NFPA 5000.[^47]

### 3.3 IBC Assembly Occupancy Provisions

The **International Building Code** classifies assembly occupancies into five subgroups based on use:[^48][^49]

| IBC Group | NFPA Equivalent | Typical Examples |
|-----------|----------------|-----------------|
| A-1 | Assembly | Fixed seating theaters, concert halls, production venues |
| A-2 | Assembly | Restaurants, banquet halls, nightclubs |
| A-3 | Assembly | Gyms, museums, places of worship, indoor sports |
| A-4 | Assembly | Arenas, indoor pools, tennis facilities |
| A-5 | Assembly | Bleachers, grandstands, outdoor stadiums |

The fundamental distinction between IBC and NFPA 101 is temporal scope: the IBC governs the design and construction of buildings (certificate of occupancy standard), while NFPA 101 governs ongoing life safety compliance including inspection, testing, and maintenance of installed systems. In jurisdictions that have adopted both codes, the IBC applies at the design/construction phase and NFPA 101 governs operational life safety — including crowd manager requirements, drill schedules, and ongoing egress maintenance. A building serving as an assembly occupancy under both codes must satisfy the more restrictive provisions of whichever code applies to the element in question.[^50]

### 3.4 AHJ Enforcement and Fire Marshal Inspection

The **Authority Having Jurisdiction (AHJ)** — typically the local fire marshal or fire department — oversees enforcement of fire and life safety codes for assembly venues. Enforcement variations across jurisdictions are substantial: NFPA standards are model codes with no inherent legal force until adopted by a state or local jurisdiction, and many jurisdictions have adopted amended versions with local modifications. Venue operators must verify which edition of NFPA 101 (currently up to the 2024 edition) and which edition of the IBC their jurisdiction has adopted.[^51]

For special events, fire marshal inspection processes typically include:[^52][^53]
- Pre-event plan review (site layout, egress routes, capacity calculations, crowd management plan)
- Walk-through inspection during setup/move-in
- Occupancy permit confirmation confirming posted maximum occupant load
- Daily visits or spot inspections during multi-day events
- Move-out/breakdown inspection

The AHJ retains authority to reduce permitted occupant loads based on site-specific conditions, egress limitations, or event characteristics, regardless of the calculated theoretical maximum — a critical point for outdoor festival operators where formal load calculations may produce higher numbers than the AHJ is willing to certify.[^51]

***

## 4. Ingress/Egress Modeling and Simulation Tools

### 4.1 Overview of Pedestrian Simulation

Pedestrian simulation tools use **agent-based modeling** to replicate the movement of individual virtual pedestrians through a digital representation of a venue or site. Each agent is assigned characteristics (walking speed, responsiveness, purpose) and makes routing decisions based on local environmental conditions, enabling emergent crowd behavior to develop from the interaction of thousands of individual agents rather than being imposed top-down. Surveys of pedestrian evacuation model users identify Pathfinder, STEPS, MassMotion, Legion, and VISSIM/Viswalk as the most widely known and used tools in the field.[^54][^55][^56]

### 4.2 Legion (Bentley Systems)

**LEGION** is Bentley Systems' pedestrian modeling and simulation solution, employing microscopic learning-adaptive agent modeling to produce realistic crowd behavior that responds to spatial context. Key workflow: import CAD/IFC architectural drawings to define the physical space, specify pedestrian demand (volumes, arrival distributions), designate areas of interim activity (queuing, waiting), and link operational data to produce timed movement simulations. LEGION has been used extensively in the design of transit infrastructure (airports, rail stations), sports stadia, and high-footfall public buildings. Over time, Bentley has been working toward integrating LEGION's pedestrian simulation within its AECOsim BIM environment, allowing pedestrian simulation as part of an integrated BIM workflow.[^57][^54]

### 4.3 Pathfinder (Thunderhead Engineering)

**Pathfinder** offers two simulation modes: a **Steering mode** (default — agents use a steering system to move and avoid each other, no specified flow rates) and an **SFPE mode** (agents follow SFPE Handbook flow-rate equations for doors and stairs). Each agent adapts to changes in door availability, environmental cues, signage, and alerts in real time. Thunderhead publishes a detailed **Verification and Validation (V&V)** document confirming compliance with verification and validation standards for system, software, and hardware. Pathfinder is one of the three most widely recognized pedestrian evacuation models in survey data, used extensively for building and venue egress time analysis, performance-based fire safety engineering, and post-incident analysis.[^58][^59][^60][^56]

### 4.4 Oasys MassMotion

Originally developed by Arup engineers for understanding crowding impacts on major infrastructure projects, **Oasys MassMotion** is now the most flexible commercially available crowd simulation software globally according to its developer. The tool models hundreds of thousands of individual pedestrians with distinct personalities and routes in complex 3D environments including multi-level buildings, curved surfaces, and stairs. Applications span airports, train stations, stadia, office towers, galleries, theme parks, and public events. MassMotion supports fire egress analysis, transport and aviation planning, urban and commercial planning, and architecture. In the post-COVID context, the tool was used to model social distancing scenarios for attractions reopening after lockdown. Arup maintains a dedicated MassMotion practice and uses it as a client deliverable tool for venue and transport infrastructure projects globally.[^55][^61][^62][^63]

### 4.5 STEPS (Mott MacDonald)

**STEPS** — Simulation of Transient Evacuation and Pedestrian Movement Software — is a microsimulation tool for pedestrian movement developed by Mott MacDonald. STEPS Version 5.4 is a grid-based model originally designed for pedestrian flows in transportation systems, subsequently extended to building evacuation. Key features: agent-based modeling of both normal day-to-day flow and emergency evacuation; gradient impact (stairs, ramps) included in simulation; BIM interface for importing building geometry. STEPS is the second most widely recognized pedestrian model (after Pathfinder) in professional survey data.[^64][^65][^66][^56][^67]

### 4.6 Practical Applications and Validation

Simulation tools serve three distinct phases of venue life:[^30][^54][^55]
1. **Design phase**: Testing multiple layout alternatives before construction to optimize egress routes, identify choke points, and validate compliance with travel-distance limits
2. **Operational planning**: Modeling specific event configurations (e.g., GA floor vs. reserved seating, stage orientation) to optimize staffing deployment, gate allocation, and emergency procedures
3. **Post-incident analysis**: Reconstructing crowd dynamics from recorded data to determine what failed and why — used in accident investigation and litigation

No universal international validation standard for pedestrian simulation software currently exists, though most tools are validated against SFPE Handbook equations for egress flows and against empirical data sets from documented crowd movements. For regulatory acceptance, practitioners must typically demonstrate that their chosen tool produces results consistent with the validation cases in its published V&V documentation, and that input assumptions reflect actual conditions. Cost varies significantly: LEGION and MassMotion are enterprise tools requiring training and ongoing license fees suitable for specialist consultancies; Pathfinder offers more accessible pricing and is widely used by fire safety engineers and building designers without a dedicated pedestrian simulation practice.[^59][^60]

***

## 5. Event Crowd Management Plans

### 5.1 Comprehensive Plan Structure

A crowd management plan (CMP) for a public assembly event integrates physical design, operational protocols, staffing, communications, and emergency procedures into a single documented framework. The UK HSE publication *Managing Crowds Safely* and its successor guidance define the management responsibility framework: crowd safety is primarily a management responsibility requiring a health and safety management system that anticipates, monitors, and controls crowding risks — not a police or security responsibility by default.[^68]

Key elements of a CMP aligned with best practice:
- Expected occupant counts and per-zone density limits
- Crowd risk assessment (using DIM-ICE or equivalent framework) across ingress, circulation, and egress phases
- Barrier layout and specifications (see 5.2)
- Staffing plan with roles, ratios, and communication protocols
- Crowd monitoring methodology (technology + human spotters)
- Intervention trigger thresholds and associated response actions
- Show-stop criteria and authority chain (see 5.5)
- Emergency action plan including multi-agency coordination
- Post-event debrief and review process[^69][^68]

### 5.2 Barrier Planning — Rigid vs. Flexible Systems and Front-of-Stage Design

Barriers serve multiple functions in crowd management: directing flow, separating zones, preventing unauthorized access, and — most critically at high-energy events — managing crowd pressure at front-of-stage areas. The science of **front-of-stage (FOS) barrier design** has evolved substantially since the 1974 Rockefeller Plaza incident that catalyzed the first pop concert code in the UK.[^70]

**Pit barrier configurations**:[^71][^72]
- **Standard pit barrier** (Mojo-style): a straight or slightly curved line of reinforced steel/aluminum panels with staff working corridor behind; suitable for moderate-density events
- **Curved/arc barrier**: deflects crowd pressure **laterally** toward stage wings rather than allowing pressure to concentrate at the center; recommended by experts for large-scale rock and pop events[^72][^70]
- **D-barrier**: semi-circular front pen creating a D-shape from above; creates a contained front section with known density and multiple access points
- **T-barrier / center thrust**: a barrier extending into the crowd from the center, breaking crowd into left/right halves and reducing surge depth — used at very large stadium concerts
- **Multi-pen system (Roskilde model)**: after nine fatalities at Roskilde Festival in 2000 during a Pearl Jam performance, Roskilde redesigned its main stage area into a multi-pen system subdividing the front audience into sections of approximately **500 people per pen**, each with its own entry and exit points, and staff passages no more than **4 meters** from any person in the crowd[^73][^74][^75]

Best practice recommendations for FOS barriers:[^76][^70]
- Consult Stage Manager, Head of Security, Crowd Manager, and Medical teams before finalizing barrier layout
- Never place the barrier directly against the stage — maintain operational space for staff and a clear sight line for front-row patrons
- Never stake, strap, or permanently secure barriers that must be movable for emergency extraction
- Include integrated steps on the staff-side of FOS barriers to allow security to reach into the crowd and extract distressed attendees
- Build in mid-crowd aisles and horizontal walkways for large GA fields so no point is more than a few meters from accessible staff

### 5.3 Mosh Pit and Crowd Surfing Management

Mosh pits and circle pits at high-energy music events generate localized high-density zones with complex lateral dynamics distinct from normal crowd flow. Venue operators' **duty of care** extends explicitly to areas of known energetic crowd behavior: organizing and supervising a mosh pit environment without adequate staffing and physical safety measures exposes operators to serious liability.[^77][^78]

Operational protocols for mosh pit management:[^77]
- Pre-show briefing of front-barrier and floor security on anticipated crowd behavior and specific planned activities (e.g., artist-encouraged Wall of Death)
- Medical staff positioned at front barrier and lateral positions before high-energy acts
- Dual-barrier systems (front pit and secondary crowd section) to contain surge within a controlled, staffed zone
- Spotters on raised platforms at front corners of stage for bird's-eye monitoring
- Pre-defined crowd density thresholds at which barrier extraction procedures activate
- Clear cancellation criteria for high-risk activities (e.g., Wall of Death suspended in wet/muddy conditions)

### 5.4 Festival and Multi-Stage Crowd Management

Multi-stage festivals present unique crowd management challenges: **headliner surge migration** — the movement of large audience sections between stages as headliner acts approach — creates transient high-density flows in circulation corridors that may not have been designed for simultaneous peak movement. Key operational measures:[^15][^30]
- Staggered set times to prevent simultaneous migration surge
- Width and capacity calculations for inter-stage pathways under headliner migration scenarios
- Pre-positioned steward deployments on key migration routes
- Distributed amenities (food, water, toilets, merchandise) around the site to prevent gravitational concentration toward a single zone
- Loop pathways eliminating dead-ends that force crowd reversals into oncoming flow

### 5.5 Show-Stop Protocols

A show-stop — the cessation of a performance for safety reasons — must be planned in advance, never improvised. The Astroworld disaster (see Section 6.2) demonstrated the catastrophic consequences of ambiguity about who has authority to stop a show and under what conditions.

A formalized show-stop procedure includes:[^79][^80]
- **Designated authority**: a single named role (Festival Director, Safety Officer, or Event Safety Manager) with unambiguous stop-show authority, and a designated backup if that person is unreachable
- **Pre-defined objective triggers**: density thresholds, weather criteria (e.g., lightning within 6 miles), barrier integrity alerts, medical mass-casualty declaration — written as explicit conditional statements, not judgment calls in the moment
- **Communication chain**: the designated authority issues a stop order via radio to the Stage Manager and Sound Engineer simultaneously; the Sound Engineer mutes audio; the Lighting Engineer brings up house lights
- **Redundant communication**: PA announcements, big-screen messages, SMS push, social media — no reliance on a single channel
- **Artist management integration**: the stop order is communicated to artist's Tour Manager or personal security on stage; artists must be briefed pre-show that a stop order requires immediate compliance
- **Post-stop crowd management**: once music stops, the focus shifts to controlled crowd management — directing dispersal, activating emergency medical response if needed, communicating clear instructions to crowd[^81][^79]

The NFPA 101-compliant crowd management plan and NFPA 12.7.6-required crowd managers must both be involved in show-stop protocol development.[^82][^40]

### 5.6 The UK Purple Guide (The Event Safety Guide)

The **Purple Guide** (officially *The Event Safety Guide to Health, Safety and Welfare at Events*) is the UK's principal reference document for outdoor event safety planning, maintained by the Events Industry Forum. Targeted at all venue owners and event organizers where the Health and Safety at Work Act applies, the Purple Guide provides:[^83][^84][^69]
- Systematic hazard identification methodology including surging, swaying, and overcrowding risks
- Risk assessment framework for crowd safety
- Precautions and control measures
- Staff selection and training guidance
- Emergency planning and evacuation procedures including multi-agency coordination
- Crowd monitoring approaches
- Post-event review requirements

The Purple Guide was last substantively updated in 2014 (web-based edition), with section-level updates maintained through 2024. In the UK regulatory ecosystem, it operates alongside the **Green Guide** (SGSA, sports grounds) and the HSE publication *Managing Crowds Safely*. Compliance with the Purple Guide is typically expected by Safety Advisory Groups (SAGs) — multi-agency groups convened by local authorities for event licensing — as evidence of competent event safety management.[^85][^84][^83]

***

## 6. Post-Incident Regulatory Evolution

### 6.1 Hillsborough Disaster (1989) — The UK's Founding Framework

On 15 April 1989, during an FA Cup semi-final at Hillsborough Stadium, Sheffield, 97 Liverpool FC supporters were killed in a crowd crush in the Leppings Lane end terracing. An estimated 3,000 people were compressed into pens with an official capacity of 2,200 and a Health and Safety Executive-assessed safe capacity of 1,693. The South Yorkshire Police had opened a gate to relieve external congestion without closing the tunnel to the already-full central pens, and no provision existed for monitoring or controlling the internal distribution of spectators.[^86]

**Lord Justice Taylor's Report (1990)** concluded that the primary cause was a failure of crowd control by South Yorkshire Police and condemned the design of standing terraces as inherently hazardous. Key recommendations and outcomes:[^85][^86]

- **All-seater stadia**: Top-tier football grounds in England and Wales converted to all-seater within a defined timescale, eliminating the standing terrace conditions that enabled density-to-crush transitions[^87][^85]
- **Green Guide**: Emerged as the authoritative manual for sports ground safety, covering capacity calculations, emergency egress, and structural safety[^85]
- **Football Spectators Act 1989**: Established the Football Licensing Authority (FLA) to issue licences admitting spectators to designated matches, introducing criminal penalties for breaching licensing requirements[^88][^89]
- **Safety Advisory Groups (SAGs)**: Multi-agency groups bringing together local authorities, emergency services, and event organizers for coordinated risk assessment and safety planning[^85]
- **SGSA (Sports Grounds Safety Authority)**: Created in 2011 under the Sports Grounds Safety Authority Act 2011 to replace the FLA, serving as safety regulator for football grounds in England and Wales and as the UK government's independent advisor on sports ground safety internationally[^90][^88]

The Safety of Sports Grounds Act 1975 — which established the safety certificate system for designated grounds accommodating more than 10,000 spectators — remains the fundamental legislative basis for sports ground safety certification, supplemented by the Fire Safety and Safety of Places of Sport Act 1987 (enacted after the Bradford City fire). The SGSA published the **sixth edition of the Green Guide** in November 2018, updating references to British Standards, Building Regulations, and advisory documents.[^91][^92][^93][^90]

The Hillsborough Independent Panel (2012) confirmed that "crowd safety was compromised at every level" and that up to 41 of the 97 who died might have survived with better emergency response coordination. A second inquest (2016) returned verdicts of unlawful killing. The disaster's legacy extends beyond the UK: the Green Guide is used globally by architects, designers, and regulators as a best-practice reference for stadium development.[^94][^95][^86]

### 6.2 Astroworld Festival (2021, Houston)

On 5 November 2021, 10 people died and hundreds were injured at the Astroworld Festival in Houston, Texas, during Travis Scott's headlining performance at NRG Park. The crowd compressed toward the stage as Scott performed, and event control failed to stop the show despite a mass-casualty event being declared.[^96][^97]

The Houston Police Department released a 1,266-page investigative report in July 2023 — the most detailed public account of the event's decision-making failures. Key findings: internal communications documented concern about crowd conditions hours before the fatalities; authority to halt the performance was ambiguous; and the absence of a clear show-stop chain of command contributed to the continuation of the event past the point at which intervention could have prevented fatalities.[^97][^98]

A Harris County grand jury declined to indict Scott or five other individuals in June 2023, determining that "no crime did occur" and "no single individual was criminally responsible". Hundreds of civil suits against Scott and Live Nation remain active. Notably, as of 2023, neither Houston nor Harris County had adopted any new regulations or standards for concert security, venue safety, or event planning in response to the disaster.[^96][^97]

The post-Astroworld **Texas Governor's Task Force on Concert Safety** has continued to advocate for regulatory reform, finding in 2025 that event promoters routinely falsify permit applications or bypass the approval process entirely. Reform proposals include universal permitting templates creating consistent statewide safety standards, mandatory documentation of crowd management plans and emergency procedures, and significantly higher fines for non-compliance — but no legislative timeline had been established as of mid-2025.[^99]

### 6.3 Seoul Halloween Crowd Crush (2022, Itaewon)

On 29 October 2022, 159 people died and 196 were injured in a crowd surge in the narrow streets of Itaewon, Seoul, during Halloween festivities. The surge occurred in a steep alley approximately 4 meters wide with no formal crowd management plan, no designated event organizer, and no crowd control staffing — despite police having correctly anticipated massive attendance.[^100][^101][^102]

The South Korean National Police Agency special task force concluded in January 2023 that "inadequate preparation by the police and government, despite multiple prior warnings, was the primary cause". Police had dispatched 137 officers to Itaewon that night, but they were assigned to monitor drugs and assault rather than crowd density or flow. The investigation resulted in criminal charges against 23 individuals — primarily law enforcement and local municipal officials — for involuntary manslaughter and negligence.[^101][^102]

The Seoul police chief was acquitted at trial in October 2024, with the court finding the prosecution's evidence insufficient to demonstrate a failure of duty. South Korea's National Assembly approved special legislation in May 2024 mandating a new independent investigation committee, and in July 2025, President Lee Jae Myung ordered a fresh investigative unit involving police and prosecutors. As of April 2026, the independent committee had commenced its investigation.[^103][^104][^105][^100]

The Itaewon disaster prompted South Korean authorities to issue guidance on managing large unstructured public gatherings in urban environments — a previously under-regulated category distinct from licensed ticketed events. The crush highlighted that crowd management frameworks focused on ticketed venues with defined operators leave a significant regulatory gap for spontaneous urban mass gatherings.

### 6.4 Love Parade Disaster (2010, Duisburg)

On 24 July 2010, 21 people died and more than 500 were injured at the Love Parade electronic music festival in Duisburg, Germany, when crowd flow collapsed in a single-entry ramp-and-tunnel connecting the festival area to surrounding streets. The site design routed all 1.4 million attendees — both arriving and departing — through a **single tunnel**, creating a fatal bidirectional flow conflict at a bottleneck that event organizers' own exit analysis had identified as potentially exceeding 2 persons per square meter (the regulatory maximum) but proceeded with anyway.[^106][^107][^108]

Analysis by Helbing et al. identified **crowd quakes** (crowd turbulence events) as a key factor in the deaths, distinguishing the mechanism from deliberate stampeding. A witness statement analysis (published in *Safety Science*, 2023) of 136 police-collected witness accounts confirmed the experience of sudden, uncontrollable forces and near-complete loss of individual mobility before collapses occurred.[^109][^3]

Pre-event design documentation obtained by *Der Spiegel* revealed that authorities had been warned the tunnel was "too narrow, too small" for the anticipated crowd by a senior police union official a year before the event. City officials' planning documents showed that the capacity analysis was aware of densities exceeding regulatory limits but proceeded on an assumption of manageable departure timing.[^110][^106]

No criminal convictions resulted from the disaster; charges against 10 defendants — including city officials and event organizers — were dropped by Duisburg District Court in 2020 after a ten-year legal process, citing insufficient causal evidence against named individuals.[^108]

The Love Parade's primary regulatory legacy is as a case study in simulation failure: the pre-event analysis did not adequately model the bidirectional conflict dynamic of a single shared entry/exit route. Its use in crowd science education has driven adoption of stricter requirements for independent entry and exit paths at mass events and reinforced the absolute requirement that pedestrian simulation tools be used to test single-entry scenarios before approval.[^111]

***

## 7. Crowd Management Staffing and Training Standards

### 7.1 UK Standards — SIA Licensing and NVQ Qualifications

In the United Kingdom, individuals providing security at events are required to hold a licence issued by the **Security Industry Authority (SIA)** under the Private Security Industry Act 2001. The SIA licence requirement applies to roles involving physical presence for security purposes — including crowd management, access control, and door supervision at licensed events.[^112][^113]

The minimum baseline qualification for frontline stewarding roles at sporting events and festivals is the **Level 2 NVQ/RQF Certificate in Spectator Safety**, mapped to Skills Active Spectator Safety National Occupational Standards. This qualification is recommended as the minimum in the SGSA Green Guide and Purple Guide. Units include:[^114][^115]
- Preparing for spectator events
- Assisting with spectator movement and crowd issue management
- Conflict management and resolution
- Dealing with incidents at spectator events
- Team and organizational support[^115]

The qualification framework extends to Level 5 for crowd safety management professionals, with Crowd Safety Training (UK) offering a range of certifications through that progression. Senior stewards and supervisors are governed by separate National Occupational Standards (e.g., SKASS7 — Prepare Stewards and Venues for Spectator Events) covering steward briefing, assignment, and pre-event venue verification.[^116][^117]

British Security Industry Association (BSIA) Crowd Management Section membership requires **ISO 9001 UKAS certification** as a condition of admission, establishing a quality management baseline for commercial crowd management companies operating in the UK.[^118]

### 7.2 US Standards — IAVM Trained Crowd Manager and NFPA Requirements

In the United States, crowd manager training and certification is driven primarily by **NFPA 101 Section 12.7.6** requirements, which mandate trained crowd managers at specified ratios in all assembly occupancies.[^41][^119][^42]

The **International Association of Venue Managers (IAVM)** operates the **Trained Crowd Manager** certification program — explicitly designed to train individuals who will serve as crowd managers within the meaning of NFPA 101. The program covers crowd dynamics, safety and security hazard identification, emergency response planning, and communication strategies for large crowds. IAVM also offers two senior professional credentials: the **Certified Venue Professional (CVP)** (launched 2015, 150-question examination covering venue operations, event planning, safety, and HR) and the **Certified Venue Executive (CVE)** — the industry's senior leadership credential.[^120][^121][^122][^123]

NFPA 101 Section 12.7.6.2 lists ten specific training requirements for crowd managers, including understanding roles and responsibilities, hazard identification, and emergency procedures. The IAVM Trained Crowd Manager program is structured to cover these ten competency areas, enabling venues to demonstrate compliance.[^124][^120][^42]

### 7.3 Comparison of UK and US Frameworks

| Dimension | UK Framework | US Framework |
|-----------|-------------|-------------|
| **Licensing authority** | Security Industry Authority (SIA) — mandatory licence for security roles | No federal licensing; NFPA 101 requires trained crowd managers |
| **Baseline qualification** | Level 2 NVQ Certificate in Spectator Safety | IAVM Trained Crowd Manager certification |
| **Staffing ratios** | Green Guide-based (sports grounds); Purple Guide (events) — AHJ discretion | 1 crowd manager per 250 occupants (NFPA 101 12.7.6.1) |
| **Senior professional** | Level 5 qualification; BSIA membership | CVP / CVE (IAVM) |
| **Legal basis** | Private Security Industry Act 2001; Safety of Sports Grounds Act 1975 | NFPA 101 (model code, jurisdiction-adopted) |
| **Regulatory oversight** | SIA (national); SGSA (sports grounds) | AHJ (local fire marshal / fire department) |

[^121][^118][^114][^112][^115][^90][^120][^40]

The UK system is more prescriptive and nationally consistent due to the SIA's mandatory licensing regime. The US system relies on model code adoption and local AHJ enforcement, creating significant inter-jurisdictional variation in both requirements and enforcement intensity.

***

## 8. Synthesis: Translating Science into Operations

### 8.1 From Density Research to Operational Thresholds

The scientific consensus from Fruin, Still, Helbing, and Johansson converges on a tiered operational density management framework that venue managers can implement directly:

| Density Level | Area per Person | Operational Status | Required Action |
|--------------|----------------|-------------------|----------------|
| <2 persons/m² (>5 sq ft) | Safe/comfortable | LOS B–C; acceptable for circulation areas | Routine monitoring |
| 2–3 persons/m² | LOS D–E; critical density threshold | Advisory level | Increase monitoring frequency; prepare intervention |
| 3–4 persons/m² | Approaching crowd turbulence onset | Operational response | Active crowd management interventions; throttle ingress |
| 4–5 persons/m² | Pre-turbulence | High alert | Emergency protocols activate; stop-show consideration |
| >6 persons/m² | Crowd turbulence risk; local peaks >9 persons/m² | Emergency | Immediate stop-show; emergency services activation |

[^7][^6][^2][^30]

### 8.2 The Regulatory Gap: Urban Mass Gatherings

Hillsborough, Love Parade, and Itaewon each exposed a structural limitation in crowd safety regulation: frameworks built around licensed venues with defined operators do not extend to informal urban mass gatherings, public spaces hosting spontaneous crowds, or festival sites with ambiguous operator responsibility. The Itaewon disaster (no organizer, no safety plan, no crowd management staffing for a gathering of over 100,000 in narrow streets) represents this gap most starkly.[^102][^100]

Emerging regulatory responses in South Korea and the academic literature on crowd safety law advocate for statutory frameworks that trigger crowd safety obligations based on anticipated attendance density regardless of whether an organizer is formally defined — an approach that would require cities to take proactive responsibility for crowd management planning in known high-attendance public spaces.[^125]

### 8.3 Technology Integration: The 2026 State of Practice

As of April 2026, leading venues are deploying **multi-layered monitoring architectures** combining AI-video analytics (95–98% accuracy) for zone-level density mapping, LiDAR for high-accuracy point counting at critical choke points (entry gates, tunnel access), thermal imaging for outdoor environments and low-light conditions, and real-time command center visualization aggregating all feeds into a single operational picture. Pressure-sensing barriers — including the Crowd Cushion™ system piloted at some venues — represent an emerging category of physical infrastructure instrumentation that provides direct crowd force measurement rather than inferred density estimates, triggering alerts when compressive forces approach dangerous thresholds.[^25][^30][^28][^23][^24]

Crowd analytics vendors such as WaitTime, in partnership with Axis Communications, are marketing themselves as converting existing CCTV infrastructure into proactive crowd intelligence platforms without requiring hardware replacement — a significant accessibility improvement for venues with legacy camera infrastructure.[^126]

---

## References

1. [A Crowd Disaster Study: The Itaewon Seoul Crush - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11456318/) - Reports from other crowd disasters suggest that the compressive forces leading to traumatic asphyxia...

2. [[PDF] Crowd turbulence: the physics of crowd disasters - arXiv](https://arxiv.org/pdf/0708.3339.pdf) - For example, at average densities of 6 persons per m2 the local densities can reach values up to 9 p...

3. ['Crowd Quakes' Were A Key Factor In LoveParade Disaster](https://www.technologyreview.com/2012/06/28/85633/crowd-quakes-were-a-key-factor-in-loveparade-disaster/) - A rare form of crowd turbulence, rather than deliberate pushing, stampeding or trampling, was a cruc...

4. [[PDF] DESIGNING FOR PEDESTRIANS: A LEVEL-OF-SERVICE CONCEPT](https://onlinepubs.trb.org/Onlinepubs/hrr/1971/355/355-001.pdf) - When critical density is exceeded, flow volumes fall below the specified design level, and pedestria...

5. [PhD Chapter 3 - Crowd Dynamics | Prof. Dr. G. Keith Still](http://www.gkstill.com/CV/PhD/Chapter3.html) - John Fruin researched crowds in the early 1970's. His book Pedestrian Planning and Design [6] has be...

6. [Pedestrian Level of Service Standards | PDF | Stairs - Scribd](https://www.scribd.com/document/371131651/PedestrianPlanningAndDesign-JJFruin-1971) - Pedestrian Level of Service Standards | PDF | Stairs | Services (Economics)

50%(2)50% found this do...

7. [Crowds - Levels of Service (Fruin) | Prof. Dr. G. Keith Still](http://www.gkstill.com/Support/crowd-flow/fruin/Fruin1.html) - As density increased flow increases, but only until critical density is reached (2-3 people per squa...

8. [DIM-ICE risk analysis - Event Meta-Model - Keith Still](https://www.gkstill.com/Support/WhyModel/dimice.html) - The aim of this work is to draw the users attention to the underlying elements that give rise to cro...

9. [[PDF] DIM - ICE - Keith Still](https://www.gkstill.com/Support/Links/Documents/dim---ice.pdf) - Crowd Dynamics is an established scientific approach to crowd safety and, as a company; we have been...

10. [The Importance of Education & Training in the World of Crowd Safety](https://thegcma.com/articles/the-importance-of-education-amp-training-in-the-world-of-crowd-safety) - The DIM-ICE matrix is a shorthand version of elements of the crowd management plan. 2. Crowd Dynamic...

11. [Introduction to Crowd Science - LinkedIn](https://www.linkedin.com/pulse/introduction-crowd-science-prof-dr-g-keith-still) - In this chapter, we introduce several modelling techniques for crowd and event risk analysis. Specif...

12. [Book - Introduction to Crowd Science | Prof. Dr. G. Keith Still](http://www.gkstill.com/Support/Book.html) - This is a book about how to apply simple, practical techniques to help you understand crowd risks an...

13. [Introduction to Crowd Science - 1st Edition - G Keith Still - Routledge](https://www.routledge.com/Introduction-to-Crowd-Science/Still/p/book/9780367866709) - The book outlines a simple modeling approach to crowd risk analysis and crowds safety in places of p...

14. [Crowd Safety Management and Why You Need to Understand it's ...](https://www.sabre-risk.com/post/crowd-safety-management-and-why-you-need-to-understand-it-s-importance) - DIM-ICE was a model first used by its founder, Professor Dr Keith ... Crowds are dynamic, and the co...

15. [Crowd Management: 2 The need of a systematic approach](https://yourope.org/know-how/crowd-management-2-the-need-of-a-systematic-approach/) - The so-called DIM-ICE Meta Matrix (Source: Prof. Dr. G. Keith Still) offers a simple planning approa...

16. [Crowd turbulence: the physics of crowd disasters - Academia.edu](https://www.academia.edu/483814/Crowd_turbulence_the_physics_of_crowd_disasters) - Local pedestrian densities can exceed 9 persons per m² even at average densities of 6 persons per m²...

17. [FROM CROWD DYNAMICS TO CROWD SAFETY: A VIDEO-BASED ...](https://folia.unifr.ch/global/documents/31426) - When conditions become congested, the flow drops significantly, which can cause stop-and-go waves an...

18. [How simple rules determine pedestrian behavior and crowd disasters](https://pmc.ncbi.nlm.nih.gov/articles/PMC3084058/) - Moreover, the combination of pedestrian heuristics with body collisions generates crowd turbulence a...

19. [Computer vision | Axis Communications](https://www.axis.com/for-developers/computer-vision) - The cameras are equipped with advanced video analytics capabilities, processing and analyzing data d...

20. [BriefCam Partners With Axis Communications for Video Analytics on ...](https://www.sdmmag.com/articles/99959-briefcam-partners-with-axis-communications-for-video-analytics-on-deep-learning-cameras) - By enabling BriefCam analytics on the edge, users receive real-time alerts up to six times faster, a...

21. [Occupancy management and monitoring - Axis Communications](https://www.axis.com/solutions/occupancy-management-and-monitoring) - Gain real-time insights into occupancy and crowd movement in large venues. Optimize entry points, st...

22. [BriefCam Introduces Video Analytics Enabled on Deep Learning ...](https://www.briefcam.com/company/press-releases/briefcam-introduces-video-analytics-enabled-on-deep-learning-cameras-from-axis-communications/) - BriefCam is one of the first to leverage the AXIS Camera Application Platform (ACAP) to enable compr...

23. [The Ultimate Guide to People Counting Technology: 3D, Edge AI ...](https://www.viziosense.com/post/the-ultimate-guide-to-people-counting-technology-3d-edge-ai-cameras-and-wifi-compared) - 2D cameras + Edge AI: best balance of accuracy (95–98%), privacy, scalability, and cost; supports zo...

24. [Crowd Monitoring and Management: Technology & Proven Tactics](https://www.criticalts.com/articles/modern-approaches-for-effective-crowd-monitoring-and-management/) - Positioning cameras at 20–35 feet gives command staff a real-time overhead view of crowd density, mo...

25. [LiDAR for Crowd Management: Applications, Benefits, and Future ...](https://arxiv.org/html/2603.27663v1) - Light detection and ranging (LiDAR) sensors can serve as an alternative and complementary technology...

26. [How LiDAR-Based People Counters Improve Accuracy in High ...](https://www.metrolla.com/blogs/how-lidar-based-people-counters-improve-accuracy-in-high-traffic-areas) - LiDAR (Light Detection and Ranging) technology has emerged as a game-changing solution, offering unp...

27. [Camera based people counting devices: security challenges](https://www.terabee.com/count-with-caution-security-challenges-of-camera-based-people-counting-devices/) - While camera-based people counting devices raise significant privacy concerns, other people counting...

28. [Checklist for Real-Time Crowd Monitoring Systems | ESI Technologies](https://esicorp.com/checklist-for-real-time-crowd-monitoring-systems/) - Hardware: Surveillance cameras (fixed, PTZ, thermal, multi-sensor) and RFID readers ensure accurate ...

29. [7 Essential Crowd Control Strategies for Event Safety](https://newenglandsecurity.com/ensuring-event-safety-top-strategies-with-crowd-control-services/) - Effective crowd management divides large spaces into manageable sections with dedicated pathways bet...

30. [Crush-Proofing Your Venue in 2026: Preventing Crowd Surges and ...](https://www.ticketfairy.com/blog/crush-proofing-your-venue-in-2026-preventing-crowd-surges-and-ensuring-fan-safety) - Establish Clear Emergency Protocols: Define who can stop a show or order an evacuation, and under wh...

31. [[PDF] UTRGV Environmental Health, Safety, and Risk Management](https://www.utrgv.edu/ehsrm/_files/documents/fire-safety/crowd-management-training.pdf) - 12.7.6.1 Assembly occupancies shall be provided with a minimum of one trained crowd manager or crowd...

32. [Decoded: Calculating the Occupant Load - I Dig Hardware](https://idighardware.com/2025/04/decoded-calculating-the-occupant-load-2/) - According to the International Building Code (IBC) standing space is calculated using an occupant lo...

33. [[PDF] CALCULATING OCCUPANT LOAD](https://clarkston-wa.com/wp-content/uploads/2020/10/CalculatingOccupantLoadFactSheet.pdf) - This is typically considered to be a concentrated assembly use and the factor of 7 ft2/person (net) ...

34. [[PDF] Calculating Occupant Loads in Assembly Occupancies](https://sfm.illinois.gov/content/dam/soi/en/web/sfm/sfmdocuments/documents/calculating-occupant-loads-for-assembly-occupancies-march-2022.pdf) - For example, in an assembly occupancy, the two most commonly used occupant load factors are 7 ft2/pe...

35. [Calculating Occupant Load for Life Safety - Markel](https://www.markel.com/insights-and-resources/insights/calculating-occupant-load-for-life-safety) - In areas under 10,000 square feet, the occupant load shall not exceed 1 person per 5 ft²; In areas o...

36. [[PDF] Calculating the Occupant Load - I Dig Hardware](https://idighardware.com/wp-content/uploads/2014/07/Decoded-Sep14-Calculating-Occupant-Load.pdf) - According to the. International. Building Code. (IBC), standing space is calculated using an occupan...

37. [[PDF] HOW TO CALCULATE AN OCCUPANT LOAD? - MeyerFire](https://www.meyerfire.com/uploads/1/6/0/7/16072416/ls182.02_-_summary.pdf) - The lower an occupant load factor (ie: 5 sf/person for standing room concert venues), the more occup...

38. [NFPA 101 Exit Path Design Guidelines | PDF | Safety - Scribd](https://www.scribd.com/document/804943002/Basics-of-Exit-Path-Design-as-per-NFPA-101) - Exit access corridors: Minimum 8 ft wide. • Travel distance: o Sprinklered: Max 200 ft o Unsprinkler...

39. [50.07.060 Means of Egress and Exit Routes](https://law.tmchippewa.com/us/nsn/tmchippewa/council/code/50.07.060) - (A) In existing assembly occupancies, dead-end corridors shall not exceed 240 inches, or 20 feet (NF...

40. [Crowd Control Regulations - GW Safety](https://safety.gwu.edu/crowd-control-regulations) - Assembly Occupancies (indoor events), shall be provided with a minimum of one trained crowd manager ...

41. [[PDF] Crowd Management](https://fire-marshal.ri.gov/sites/g/files/xkgbur726/files/documents/crowdmanagement/CMPresentation.pdf) - NFPA 101 12/13.7.6.1 Assembly occupancies shall be provided with a minimum of one trained crowd mana...

42. [CFSA Blog - Canadian Fire Safety Association](https://canadianfiresafety.com/news/view/crowd-managers-and-drills-are-they-required-in-canada) - I want to shine a light on the additional requirements of NFPA 101 for crowd managers and drills. .....

43. [[PDF] First Revision No. 6590-NFPA 101-2024 [ Section No. 12.1.6 ]](https://docinfofiles.nfpa.org/files/AboutTheCodes/101/101_A2026_SAF_AXM_FD_FRReport.pdf) - Assembly occupancies shall be limited to the building construction types specified in Table. 12.1.6,...

44. [A Guide to Changes in the 2024 Edition of NFPA 101](https://insulation.org/io/articles/a-guide-to-changes-in-the-2024-edition-of-nfpa-101/) - However, in the 2024 edition of NFPA 101, both new and existing assembly occupancies now require por...

45. [Standard for Grandstands, Folding and Telescopic Seating, Te](https://www.firesafetycouncil.com/bookstraining/codes-amp-standards/n-102-21-standard-for-grandstands-folding-and-telescopic-seating-te) - NFPA 102 provides requirements extracted from NFPA 5000 and NFPA 101 for life safety in relation to ...

46. [Grandstand and Bleacher Inspection Requirements - TNRMT](https://www.tnrmt.com/grandstand-and-bleacher-inspection-requirements/) - The owner shall arrange an annual inspection of all bleachers, folding and telescopic seating, and g...

47. [NFPA codes for aluminum bleachers - The Park Catalog](https://www.theparkcatalog.com/blog/nfpa-safety-codes-and-standards-guide-you-to-safe-bleacher-installation/) - Aluminum bleacher seating, guards and railings · For bleachers and grandstands, the seating shall be...

48. [Occupancy Classifications in the International Building Code](https://nfsa.org/2024/01/08/occupancy-classifications-in-the-ibc/) - Assembly occupancies are divided into five subgroups (Groups A-1 through A-5) and are classified by ...

49. [Demystifying the Relationship Between the NFPA and IBC ...](https://blog.koorsen.com/demystifying-the-relationship-between-the-nfpa-and-ibc-requirements-for-sprinklers) - This post will focus specifically on the occupancy classifications in the IBC and the sprinkler syst...

50. [Navigating IBC and NFPA differences - HFM Magazine](https://www.hfmmagazine.com/articles/4500-navigating-ibc-and-nfpa-differences) - The IBC includes an additional occupancy classification: utility and miscellaneous occupancy. There ...

51. [Who is Responsible for Crowd Safety & Crowd Management?](https://firesystems.net/2021/11/16/who-is-responsible-for-crowd-safety-crowd-management/) - The Authority Having Jurisdiction (AHJ) oversees fire code ... Fire marshal inspections are designed...

52. [Outdoor Special Event Fire Code Requirements - The City of Calgary](https://www.calgary.ca/safety/events/outdoor-fire-code-requirements.html) - Inspection of the event · A walk-through with the event coordinator during the move-in or set-up per...

53. [Indoor Special Event Fire Code Requirements - The City of Calgary](https://www.calgary.ca/safety/events/indoor-fire-code-requirements.html) - Create a Request for a Special Event Inspection as below or call 311. · Compile all of the required ...

54. [[PDF] LEGION® Modeling and Simulation | Bentley Systems](https://www.bentley.com/wp-content/uploads/PDS-LEGION-Modeling-Simulation-LTR-EN-LR.pdf) - LEGION is Bentley's pedestrian modeling, simulation, and analysis solution. It enables users to prev...

55. [MassMotion: Pedestrian simulation for the most realistic outcomes ...](https://www.oasys-software.com/news/launch-of-massmotion-multi-language/) - MassMotion is now the most flexible, commercially-available crowd simulation software in the world.

56. [[PDF] An Online Survey of Pedestrian Evacuation Model Usage and Users](https://d-nb.info/1205733922/34) - Abstract. Pedestrian evacuation models are often used to assess life safety in the performance-based...

57. [LEGION and the Technology of Pedestrian Simulation - AECbytes](https://www.aecbytes.com/feature/2018/Legion-PedestrianSimulation.html) - In the same way, simulating pedestrians can help building designers streamline foot traffic, avoid c...

58. [Pathfinder | Crowd Movement Simulation and Egress Software](https://www.thunderheadeng.com/pathfinder/) - Design safer spaces with Pathfinder crowd & egress simulation software. Request a Free Trial and eas...

59. [[PDF] Verification and Validation - Thunderhead Files | Hosted on Fast.io](https://files.thunderheadeng.com/support/files/verification_validation.pdf) - This document presents verification and validation test data for the Pathfinder simulator. The follo...

60. [[PDF] Pathfinder - Verification and Validation - Thunderhead Engineering](https://files.thunderheadeng.com/support/documents/pathfinder-verification-validation-2021-2.pdf) - ... validation test data for the Pathfinder simulator. The ... Standard for System, Software, and Ha...

61. [Pedestrian Simulation - Oasys](https://www.oasys-software.com/solutions/pedestrian-simulation/) - Pedestrian simulation uses real-world data to model and simulate the movement of people-like agents ...

62. [COVID-19 and social distancing: crowd analysis for attractions](https://blooloop.com/theme-park/in-depth/oasys-massmotion-crowd-control-covid-19/) - Software solution Oasys MassMotion is a potential game-changer for attractions working on post-COVID...

63. [MassMotion - Arup](https://www.arup.com/services/digital-solutions/massmotion/) - MassMotion is the world's most flexible pedestrian and crowd simulation software. Based on pioneerin...

64. [STEPS Simulating Pedestrian Dynamics - YouTube](https://www.youtube.com/playlist?list=PLLWWNKTB00_yd_HtX4hmPh_fW9qo_bnNG) - STEPS simulating pedestrian dynamics. Mott MacDonald · 1:37. BIM Interface. Mott MacDonald ... Build...

65. [STEPS - YouTube](https://www.youtube.com/watch?v=lyy2kom2IW8) - STEPS is an acronym for Simulation of Transient Evacuation and Pedestrian Movement Software ... STEP...

66. [[PDF] practicalities-and-limitations-of-coupling-fds-with-evacuation ... - WSP](https://www.wsp.com/-/media/insights/sweden/documents/2018/practicalities-and-limitations-of-coupling-fds-with-evacuation-software.pdf) - STEPS Software. STEPS is an agent-based pedestrian movement tool developed by Mott Macdonald [8]. ST...

67. [[PDF] pedestrian modelling for persons with restricted mobility at transport ...](https://aetransport.org/public/downloads/i3oDc/5043-57e27f3f2d996.pdf) - The Mott MacDonald in-house pedestrian simulation model (STEPS) has included gradient impact within ...

68. [Managing crowds safely - HSE](https://www.hse.gov.uk/pubns/indg142.htm) - A report entitled Managing crowd safety in public venues: a study to generate guidance for venue own...

69. [[PDF] HSE purple guide - Managing crowds safely - Dorset Council](https://www.dorsetcouncil.gov.uk/documents/35024/295806/HSE+purple+guide.pdf/4d4626a7-9062-d246-b901-f7b26a7b2b9e?version=1.0&t=1619382412103) - This booklet aims to provide practical guidelines on managing crowd safety in a systematic way by se...

70. [[PDF] Front of Stage Barrier Systems - Patron Management -](http://patronmanagement.org/wp-content/uploads/2011/02/barrier-research.pdf) - This paper considers the safety of mass crowds in front of a stage at an open-air concert event. Dur...

71. [Pit Barrier: Managing Crowd Pressure at the Front-of-Stage Zone](https://barrierhq.com/blogs/fos-barriers/pit-barrier-managing-crowd-pressure-at-the-front-of-stage-zone) - Reinforced straight FOS panels (steel or aluminum) · Corner units to wrap around the stage · Door mo...

72. [Barricades and Penning: Safer Festival Pits by Design - Ticket Fairy](https://www.ticketfairy.com/blog/barricades-and-penning-safer-festival-pits-by-design) - Effective pit safety starts with barricade layout. The shape and configuration of your front-of-stag...

73. [Roskilde Raises Issues of Crowd Safety - LSi Online](https://www.lsionline.com/news/roskilde-raises-issues-of-crowd-safety-gotkwq/) - An investigation has been launched following the news over the weekend that eight fans had been crus...

74. [Roskilde Festival's Crowd Safety Lessons | PDF - Scribd](https://www.scribd.com/document/420625626/MT-Crowd-Sensegiving) - This document summarizes a study on crowd sensegiving at the Roskilde Festival after the 2000 Pearl ...

75. [Festival Pit Design: Barriers, Pens, and Pressure Releases](https://www.ticketfairy.com/blog/festival-pit-design-barriers-pens-and-pressure-releases) - After a tragic crowd crush in 2000, Roskilde's producers redesigned the main stage pit with an innov...

76. [7 Unwritten Rules of Front of Stage Barrier Safety | Iain Morrison](https://www.linkedin.com/posts/iainmorrison1_7-unwritten-rules-of-front-of-stage-barrier-activity-7314044098003251200-5VDl) - 1. Consult early, consult widely. · 2. Never hug the stage. · 3. Never push it too far back. · 4. Ne...

77. [Wall of Death Ethics: Safely Managing Mosh Pit Mayhem at Rock ...](https://www.ticketfairy.com/blog/wall-of-death-ethics-safely-managing-mosh-pit-mayhem-at-rock-metal-festivals) - Barriers and Space Management: Check your stage barrier setup and overall crowd layout before the fe...

78. [Festival Risk Management and Safety Planning - Ticket Fairy](https://www.ticketfairy.com/blog/festival-risk-management-and-safety-planning-secrets-for-an-incident-free-event) - Duty of Care: The legal and moral obligation of festival organizers to take reasonable measures to p...

79. [Stopping the Show: Empowering Festival Teams to Pause ...](https://www.ticketfairy.com/blog/stopping-the-show-empowering-festival-teams-to-pause-performances-for-safety) - Learn how to implement a safe show stop procedure for festivals. Discover expert crowd management sa...

80. [[DOC] Venue Event Operations Manual - Live Music Office](https://livemusicoffice.com.au/wp-content/uploads/2016/04/9-Venue-Event-Operations-Manual-Template.docx) - At present it is envisaged that a venue event representative from the CRISIS TEAM, Police Commander,...

81. [Festival Incident Reporting and Communication Protocol - Ticket Fairy](https://www.ticketfairy.com/blog/festival-incident-reporting-and-communication-protocol) - They need to be in the loop for any issue that might require a public announcement, an emergency res...

82. [Audience Crowd Management Safety Plan Checklist [FREE PDF]](https://www.popprobe.com/checklist-library/entertainment/audience-safety/b27-ent-crowd-management-safety-checklist) - NFPA 101 Section 12.7. 6.2 requires assembly venues with 250 or more occupants to have trained crowd...

83. [The Purple Guide Light | PDF - Scribd](https://www.scribd.com/document/932418504/The-Purple-Guide-Light) - Crowd Management crowd management Last Updated: 20th April 2024 Even for smaller events, the managem...

84. [[PDF] The Purple guide to health, safety and welfare at events](https://oldbuckpc.co.uk/wp-content/uploads/2025/01/5-The-Purple-Guide-key-points-2024_Optimized.pdf) - Effective planning is central to putting on a safe event. • Prepare an event safety plan. • Have app...

85. [Hillsborough: The catalyst for change - Hendersons Health and Safety](https://www.hendersonsafety.com/hillsborough-the-catalyst-for-change) - The Taylor Report also laid the groundwork for modern event safety practices. The “Green Guide” emer...

86. [Hillsborough disaster - Wikipedia](https://en.wikipedia.org/wiki/Hillsborough_disaster) - Blaming Liverpool fans persisted even after the Taylor Report of 1990, which found that the main cau...

87. [The Taylor report unpicked: Class bias | Daly History Blog](https://dalyhistory.wordpress.com/2010/12/27/the-taylor-report-unpicked-class-bias/) - The Taylor report was the NINTH such report into saftey at football grounds. In 1973 the first Green...

88. [Sports Grounds Safety Authority independent review - GOV.UK](https://www.gov.uk/government/publications/review-of-the-sports-grounds-safety-authority/sports-grounds-safety-authority-independent-review) - The SGSA is the safety regulator for football grounds in England and Wales, and is the UK government...

89. [Standing at Football | Addleshaw Goddard LLP](https://www.addleshawgoddard.com/en/insights/insights-briefings/2020/litigation/standing-at-football/) - The power of the Football Licensing Authority, that body later to be superseded by the Sports Ground...

90. [Legislation - SGSA - Sports Grounds Safety Authority](https://sgsa.org.uk/regulatory-support/legislation/) - Under the 1975 Act, the Secretary of State (for Culture, Media and Sport) may designate any sports g...

91. [Launch of the new (6th edition) SGSA Guide to Safety at Sports ...](https://www.levelplayingfield.org.uk/news-item/launch-of-the-new-6th-edition-sgsa-guide-to-safety-at-sports-grounds/) - The sixth edition ensures all references to British Standards, Building Regulations and other adviso...

92. [PBC TODAY: Safety Design Standards In Sports Stadia: How Green ...](https://legendsglobal.com/safety-design-standards-in-sports-stadia-how-green-guide-6-is-applied/) - The Green Guide was revised in November 2018 to its sixth edition, which came 10 years after the pub...

93. [Stadium safety | Edge Hill University](https://www.edgehill.ac.uk/departments/academic/law/research-and-knowledge-exchange/centre-for-sports-law-research/sports-law-insights-two-faces-sports-law/stadium-safety/) - The Safety of Sports Grounds Act 1975 provides for licensing of sports grounds and, following the Br...

94. [Guide to Safety at Sports Grounds (Green Guide) - SGSA](https://sgsa.org.uk/document/greenguide/) - The Green Guide details the assessment of a ground's safe capacity. It outlines how to calculate the...

95. [Sports ground safety guidance | Journals - MODUS | RICS](https://ww3.rics.org/uk/en/journals/built-environment-journal/sports-ground-safety-guidance.html) - Last year, the SGSA published the sixth edition of the Guide to Safety at Sports Grounds, commonly r...

96. [Houston police release report on Travis Scott's 2021 Astroworld ...](https://www.texastribune.org/2023/07/28/travis-scott-houston-concert-police-report/) - “Someone's going to end up dead”: New evidence emerges in Travis Scott Astroworld tragedy. A new Hou...

97. [Houston PD releases report on Travis Scott Astroworld disaster](https://www.latimes.com/entertainment-arts/music/story/2023-07-28/travis-scott-astroworld-festival-houston-police-report) - The Houston Police Department has released its report into the 2021 Astroworld crowd-crush disaster ...

98. [Why didn't Astroworld police report attempt to pin blame?](https://www.houstonlanding.org/houston-police-astroworld-report-contains-1266-pages-but-no-blame-for-tragedy/) - HOUSTON, TEXAS - NOVEMBER 05: Travis Scott performs during 2021 Astroworld Festival at NRG Park on N...

99. [Texas task force finds widespread event security violations, pushes ...](https://www.c-mw.net/post-astroworld-texas-finds-widespread-security-violations-and-pushes-for-reform/) - Texas officials are pushing for stricter concert safety regulations after discovering event promoter...

100. [South Korea's parliament approves independent investigation of the ...](https://ottawa.citynews.ca/2024/05/02/south-koreas-parliament-approves-independent-investigation-of-the-devastating-2022-halloween-crush/) - In early 2023, a police special investigation concluded that police and municipal officials failed t...

101. [Seoul Halloween crowd crush - Wikipedia](https://en.wikipedia.org/wiki/Seoul_Halloween_crowd_crush) - A special police task force initiated an investigation within days of the event and concluded on 13 ...

102. [Legal Analysis of Itaewon Crowd Crush - Seoul Law Group](https://seoullawgroup.com/itaewon-crowd-crush/) - Witnesses of the Itaewon Crowd Crush have claimed that there were few police officers on the streets...

103. [Special panel begins probe into 2022 Halloween crowd crush](https://www.koreatimes.co.kr/southkorea/society/20250617/special-panel-begins-probe-into-2022-halloween-crowd-crush) - The committee convened the first meeting to approve the launch of the investigation into the victims...

104. [Seoul police chief acquitted over Halloween crush - BBC](https://www.bbc.com/news/articles/c4gql68dwxxo) - Kim Kwang-ho has been found not guilty of negligence that led to the deaths of 159 revellers in the ...

105. [South Korea's Lee orders new investigation team to look into deadly ...](https://www.reuters.com/world/asia-pacific/south-koreas-lee-orders-new-investigation-team-look-into-deadly-2022-crush-2025-07-17/) - South Korean President Lee Jae Myung has ordered the setting up of a new investigation team, involvi...

106. [Disaster Plan: Love Parade Documents Reveal a Series of Errors](https://www.spiegel.de/international/germany/disaster-plan-love-parade-documents-reveal-a-series-of-errors-a-710834.html) - Documents show just how sloppy event planning was -- and reveal the mistakes made by both the city a...

107. [Love Parade disaster - Wikipedia](https://en.wikipedia.org/wiki/Love_Parade_disaster) - A crowd disaster at the 2010 Love Parade electronic dance music festival in Duisburg, North Rhine-We...

108. [Loveparade stampede: Who was responsible? - DW.com](https://www.dw.com/en/loveparade-duisburg-trial/a-54243446) - It shows a ramp at the narrow tunnel entrance — the only entrance and exit point — which became a le...

109. [Inside a life-threatening crowd: Analysis of the Love Parade disaster ...](https://www.sciencedirect.com/science/article/pii/S0925753523001716) - This paper analyzes a random sample of 136 of these witness statements, focusing on how those presen...

110. [Organisers blamed for German Love Parade deaths - BBC News](https://www.bbc.com/news/world-europe-10753448) - Survivors of a stampede at a free dance music festival in Germany in which 19 people were killed hav...

111. [[PDF] Lessons learned and consequences from the Love Parade Disaster ...](https://svpt.uni-wuppertal.de/fileadmin/bauing/svpt/Publikationen/LoPa_EVC_Beitrag_english.pdf) - Abstract. The tragic events at the Love Parade Duisburg 2010 with 21 deaths and over 650 injured was...

112. [[PDF] SIA | Events Guidance - GOV.UK](https://assets.publishing.service.gov.uk/media/627a2055e90e074ee7344bfa/sia-security-at-events.pdf) - The purpose of this guidance is to help you to identify the roles at your event that may require a s...

113. [Stadium/Crowd Management - Star Protection Services](https://www.star-protection.com/copy-of-services-1) - All staff are highly trained for a wide ranging and diverse range of sites and clients and are fully...

114. [[PDF] QNUK Level 2 NVQ Certificate in Spectator Safety (RQF)](https://qualifications-network.co.uk/wp-content/uploads/2020/02/QNUK-Level-2-NVQ-Certificate-in-Specatator-Safety-Qualification-Specification-Final.pdf) - This qualification is designed for people who intend to work as Steward at a public event. The quali...

115. [Level 2 Certificate in Spectator Safety - NGTC Group Training](https://www.ngtc.co.uk/ngtc-course/new-spectator-safety-nvq-level-2/) - This is the standard qualification for accessing frontline employment within events and crowd contro...

116. [Training Courses - Industry Leading Qualifications](https://crowdsafetytraining.com/training-courses/) - We provide a wide-range of innovative, world-leading crowd safety and management courses for people ...

117. [Prepare stewards and venues for spectator events](https://ukstandards.org.uk/en/nos-finder/SKASS7/prepare-stewards-and-venues-for-spectator-events) - "This standard is about allocating responsibilities to stewards, briefing the stewards and checking ...

118. [Crowd management criteria - British Security Industry Association](https://www.bsia.co.uk/crowd-criteria/) - Companies wishing to join the BSIA's Crowd Management Section must meet the following criteria in or...

119. [Crowd Manager Training - for Civilians and Non-Fire Service](https://rickyrescue.com/crowd-manager-training/85-crowd-manager-training-non-fire-service.html) - Under current national fire codes, assembly occupancies of between 50 and 250 people require at leas...

120. [IAVM Trained Crowd Manager](https://www.trainedcrowdmanager.com) - The Trained Crowd Manager course package is intended to train candidates who will serve, in accordan...

121. [Certifications - International Association of Venue Managers](https://iavm.org/career-learning/certifications/) - IAVM offers two certifications: the Certified Venue Executive (CVE) and the Certified Venue Professi...

122. [What is the IAVM trained crowd manager certification? - UMU](https://m.umu.com/ask/a11122301573853266861) - It's a certification program that trains individuals to effectively manage large crowds at events. I...

123. [Certified Venue Professional](https://iavm.org/career-learning/certifications/certified-venue-professional/) - The Certified Venue Professional (CVP) program was launched in 2015 by IAVM to recognize the compete...

124. [Crowd Managers and Drills - firecodesolutions.ca](https://www.firecodesolutions.ca/blog/crowd-managers-and-drills) - The requirements for drills in assembly occupancies are outlined in 12.7.7 of NFPA 101. These requir...

125. [[PDF] Far from the Madding Crowd: A Statutory Solution to Crowd Crush](https://ttu-ir.tdl.org/server/api/core/bitstreams/809a2ca3-3bff-411a-a70a-19cc420e2b64/content) - This Article argues that a statutory response to crowd crush is the most appropriate and effective w...

126. [Augmenting Physical Security with Real-Time Crowd Intelligence](https://www.linkedin.com/posts/zackklima_ai-computervision-crowdintelligence-activity-7417628365538480128-sB3i) - WaitTime uses anonymous pixel tracking, no faces stored. Axis masking blurs video live. Adoption fli...

