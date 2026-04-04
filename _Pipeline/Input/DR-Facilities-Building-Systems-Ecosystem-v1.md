# Facilities Management & Building Systems Ecosystem for Large Entertainment and Convention Venues
**April 2026 | Research Report**

***

## Executive Summary

Large entertainment and convention venues — encompassing convention centres, arenas, stadiums, performing arts centres, and integrated resorts — operate among the most operationally complex building types in existence. Each category generates extreme swings in occupancy (near-zero to tens of thousands within hours), demands full technical reliability during events, and increasingly faces stakeholder pressure to demonstrate sustainability leadership. As of 2026, the industry is in a period of rapid convergence: Building Management Systems (BMS) platforms have matured into AI-assisted, open-architecture enterprise tools; predictive maintenance powered by IoT sensors is displacing the last pockets of purely reactive repair; sustainability certifications have multiplied; and venue management software has evolved into integrated IWMS and digital-twin environments. This report organizes the current state of the art across seven operational domains, cross-references venue-type differences where they are material, and catalogs the key technology platforms, standards, and certifying bodies in use today.

***

## 1. Building Management Systems (BMS)

### Platform Landscape

The BMS market for large venues is dominated by four major platform families, all now embracing open protocols, cloud connectivity, and AI-driven analytics:

- **Johnson Controls Metasys** — The flagship BAS released Metasys 15.0 in November 2025, scaling to 50,000 objects and 1,000 IP devices per server (60% more than comparable systems) with multi-server redundancy for mission-critical environments. It integrates HVAC, lighting, fire, and security systems and includes an advanced energy management suite for emissions tracking, benchmarking, and budgeting. Metasys is in active use at professional sports and entertainment venues, including a prominent case at a major tennis stadium where it links HVAC, lighting, and energy management with real-time performance dashboards.[^1][^2]

- **Siemens Desigo CC** — A structured-model BMS platform engineered upstream in ABT (Advanced Building Technology) tools, which produces a persistent digital plant model that drives navigation, alarms, graphics, and workflows. Desigo CC integrates with Dell Technologies hardware for large campus deployments and supports classroom/event schedule pull-through to align building control schedules with occupancy data.[^3][^4]

- **Honeywell Optimizer Supervisor (Niagara N4.14)** — Honeywell's open-framework BMS middleware, now at version N4.14, uses HTML5 for interface rendering and role-based access control (RBAC). As a framework rather than a full platform, it is widely deployed as an integration layer across mixed-vendor environments.[^5][^3]

- **Schneider Electric EcoStruxure Building Operation** — A comprehensive BMS that provides integration, visibility, and control across building systems with open, scalable, data-centric architecture. Used in historic building retrofits and large commercial portfolios targeting decarbonization.[^6]

All four platforms support the major interoperability protocols: **BACnet/IP**, **Modbus**, and **LonWorks**. For venues with legacy equipment, Niagara is frequently deployed as a middleware integration layer to normalize disparate systems.[^7]

### HVAC Control in Large Assemblies

Convention centres, arenas, and stadiums present unique HVAC engineering challenges: occupancy swings from near-zero (off hours) to maximum rated capacity over a period as short as one to two hours. The industry's response is **demand-controlled ventilation (DCV)** using CO₂ sensors as the primary sensing modality. ASHRAE Standard 62.1-2022 mandates DCV for spaces larger than 500 sq ft with a design occupancy ≥ 25 people per 1,000 sq ft served by variable-flow systems. CO₂-based DCV achieves energy reductions of **10–30%** over constant-air-volume baselines by eliminating over-ventilation during low-occupancy periods. Modern systems integrate DCV sensor networks directly into the BMS for remote monitoring, scheduling, and automated demand response participation.[^8][^9]

Variable Air Volume (VAV) systems dominate large convention and arena HVAC design. For ice arenas, the refrigeration plant introduces an additional layer of environmental control: humidity must be held at 50–55% relative humidity to prevent fogging and degradation of ice quality, adding a tight coupling between the refrigeration control system and the broader BMS.[^10]

### BMS Integration with Event Scheduling

The most operationally mature venues have integrated their BMS with venue management and event scheduling software so that building system setpoints — HVAC pre-conditioning, lighting levels, escalator activation — are automatically triggered by the event calendar. Siemens Desigo CC demonstrated this integration by pulling classroom schedules via API to align building control schedules with actual occupancy. This integration eliminates manual setpoint changes, reduces energy waste during load-in/load-out periods, and ensures the venue reaches target conditions precisely at occupancy.[^4]

***

## 2. Mechanical, Electrical, and Plumbing (MEP) Systems

### Preventive vs. Predictive Maintenance

The industry has shifted from a primarily **preventive maintenance (PM)** posture toward a **predictive/condition-based maintenance (CBM)** posture enabled by IoT sensor networks integrated with CMMS software. The practical outcome is significant: Deloitte analysis cited by industry sources indicates AI-based predictive maintenance can cut maintenance costs by up to 25% and reduce unexpected breakdowns by as much as 70%. For venues where refrigeration, HVAC, and lighting systems dominate the operating budget, these gains are material.[^11]

The technology stack enabling CBM typically includes:

- **Vibration sensors** on HVAC motors, compressors, and pumps
- **Thermal imaging cameras** on electrical panels and switchgear
- **CO₂ and environmental sensors** throughout occupied spaces
- **Cloud-based CMMS** with AI/ML algorithms analyzing sensor data to generate automated work orders

IBM Maximo Application Suite is the leading enterprise EAM/CMMS platform deployed at major venues, offering AI-driven maintenance, IoT integration, asset lifecycle management, and condition-based monitoring. IBM data indicates Maximo implementations reduce labor, inventory, and equipment costs by 10–25%. Other CMMS platforms targeting arenas and stadiums include **Snapfix**, **ClickMaint**, and **ioX-CMMS**.[^12][^13][^14][^15][^16]

### ASHRAE Standards Governing MEP Operations

| Standard | Scope | Relevance to Venues |
|----------|-------|---------------------|
| ASHRAE 180-2018 | HVAC inspection and maintenance, commercial buildings | Sets minimum inspection/maintenance requirements preserving energy efficiency and IAQ [^17] |
| ASHRAE 211-2018 | Commercial building energy audits (Levels 1, 2, 3) | Framework for audit rigor at large venues seeking energy benchmarking or LEED prereqs [^17] |
| ASHRAE 62.1-2022 | Minimum ventilation rates and IAQ | DCV mandate for high-occupancy spaces; critical for arena/convention HVAC design [^18] |
| ASHRAE Standard 100 | Energy efficiency in existing buildings | Used in jurisdictions adopting performance standards for large existing venues [^19] |
| ASHRAE TC 7.3 | O&M and lifecycle cost management | Lifecycle cost analysis methodology for HVAC capital decisions [^20] |

### Ice Arena Refrigeration Plants — A Venue-Specific System

Ice arenas introduce a specialized MEP subsystem absent from all other venue types: the **refrigeration plant**. Modern systems use natural refrigerants — principally **ammonia (R-717)** and **CO₂ (R-744)** — favored for both environmental compliance (zero GWP or very low GWP) and thermodynamic efficiency. Automated control systems continuously monitor slab temperature, surface ice temperature, brine/glycol flow, compressor cycles, humidity, and dew point, adjusting in real time to maintain ice quality and minimize energy waste.[^21]

Capital One Arena (home of the Washington Capitals/Wizards) exemplifies the lifecycle replacement challenge: the venue installed a new CO₂ refrigeration system in 2025, replacing a 30-year-old ice plant. Standard maintenance protocol for ice plants includes monthly visual inspections for leaks, seasonal chemical testing of brine/glycol, refrigerant leak detection, and pump/compressor inspections with sensor calibration. The CIMCO "Net Zero Naturally" framework provides a structured pathway for arena refrigeration towards net-zero: eliminating refrigerant emissions via natural refrigerants, optimizing energy via smart controls and heat recovery, then transitioning to full electrification.[^22][^23][^21]

### Critical System Redundancy and Backup Power

Large public assembly venues are expected to operate without power interruption during events. The standard MEP redundancy architecture for critical venue systems includes:

1. **Uninterruptible Power Supply (UPS)** — Provides immediate bridge power (seconds) during the gap between grid outage and generator start
2. **Automatic Transfer Switches (ATS)** — Detect utility failure and switch to backup within seconds
3. **Diesel or Gas Generators** — Long-term backup, typically configured in **N+1 or 2N redundancy**
4. **Battery Energy Storage Systems (BESS)** — Increasingly deployed as a cleaner alternative to lead-acid UPS, and as a grid services/demand response asset[^24]

Modern generators activate in 10–30 seconds; UPS bridges the gap. For arenas and stadiums, the systems protecting life-safety functions (egress lighting, fire suppression, public address, security) are typically on separate, dedicated backup circuits from general-use systems. Integrated resorts and casino properties typically deploy the most resilient power architectures in the industry, combining CHP (combined heat and power), BESS, and renewables with multiple utility interconnection points.[^25][^26]

### Performing Arts Centre Technical Systems

Performing arts centres uniquely contain **theatrical rigging systems** — fly towers, counterweight systems, and motorized battens — that constitute life-safety MEP assets and require a specialized maintenance program. Industry safety standards (ANSI, WorkSafeBC, Ontario OHSA) require:

- **Annual inspection** of all rigging system components by a qualified competent person, with more frequent inspection for high-use items[^27][^28]
- **Cleaning, lubrication, and adjustment** at regular intervals; immediate removal from service of defective components[^27]
- A **permanent maintenance log** signed by the inspector and verified by the owner[^27]
- **Independent third-party inspection** by an outside expert at least every three to five years[^29]

Compliance standards include **NFPA 101 Life Safety Code Assembly** requirements, OSHA Entertainment Industry Safety Guidelines, **IATSE Technical Safety Standards**, and state/provincial fire marshal rigging regulations.[^30]

***

## 3. Cleaning and Environmental Services

### Housekeeping Operations and Event Turnover

Event turnover — the complete reset of a venue between events — is one of the most operationally intensive activities in venue management. For a 50,000 sq ft event venue, industry benchmarks indicate 8–12 trained crew members working in parallel zones, completing a full turnaround in 5–7 hours. The full scope of a professional turnover includes floor scrubbing and mopping across all public areas, restroom deep clean and restock, full trash pull, glass and surface wipe-down in lobbies, kitchen/concession degreasing and sanitization, loading dock cleanup, and a photo-documented final walk-through inspection.[^31]

| Venue Size | Crew Required | Turnaround Window | Equipment |
|-----------|---------------|-------------------|-----------|
| Under 10,000 sq ft | 3–4 crew | 2–3 hours | 1 autoscrubber [^31] |
| 10,000–25,000 sq ft | 4–6 crew | 3–4 hours | 1–2 autoscrubbers [^31] |
| 25,000–50,000 sq ft | 8–12 crew | 5–7 hours | 2–3 machines [^31] |
| 50,000–100,000 sq ft | 12–18 crew | 6–8 hours | 3–4 machines [^31] |

Event turnaround pricing runs approximately $3,000–$8,000 per event for venues above 50,000 sq ft, with annual contract rates significantly lower per event for venues hosting 50+ events annually.[^31]

### Specialized Cleaning — Ice Surfaces

Ice arena cleaning requires a dedicated technical protocol. The **Zamboni (ice resurfacer)** process involves three sequential actions: washing the ice surface with a heated scraper and water, shaving the surface to remove ruts, and laying a thin film of hot water that freezes into a fresh ice layer. Protocol specifics:[^32]

- NHL rink resurface: **8–10 minutes** per flood; Olympic ice: **10–12 minutes**[^33]
- Ice thickness maintained at **1¼ to 1½ inches**; humidity at **50–55%**[^10]
- Blade must be sharp at each flood; clean towel essential to ice quality[^33]
- A **5-minute window** between ice flood completion and next user group[^33]
- "Dry shaving" early morning routine removes overnight ruts without water, reducing daily water consumption[^33]

For arenas hosting NBA/NHL events, the transition from ice surface to hardwood court typically involves covering the ice with an insulated subfloor system and laying the modular hardwood — a conversion process that can take 6–12 hours depending on the venue.

### Specialized Cleaning — Playing Fields and Stage Areas

Artificial turf fields require **grooming every 40 hours of field activity** (approximately every two weeks at peak scheduling), using specialized equipment to maintain fibre orientation, redistribute infill, and remove debris. Natural turf fields require regular mowing, aeration, fertilization, and pest control, with field markings refreshed every **2–3 years** following heavy use or adverse weather.[^34][^35]

Stage areas in performing arts centres and amphitheatres require coordination between custodial staff and technical crew: cleaning of floor surfaces must occur without disturbing cable management, pit configurations, or staging setups. Pre-performance inspection checklists governed by NFPA 101 and IATSE standards cover floor condition, rigging clearances, and equipment placement safety.[^30]

### Waste Management and Zero Waste Programs

The zero waste movement in sports and entertainment venues has advanced significantly in the past five years, driven by the **TRUE (Total Resource Use and Efficiency)** certification program administered by **Green Business Certification Inc. (GBCI)**. TRUE Platinum requires a sustained waste diversion rate of 90% or higher from landfill and incineration.

Landmark certifications as of April 2026:

| Venue | Certification | Diversion Rate | Notes |
|-------|---------------|----------------|-------|
| State Farm Arena (Atlanta) | TRUE Platinum | 90%+ | World's first sports/live entertainment venue TRUE Platinum [^36] |
| Climate Pledge Arena (Seattle) | TRUE Platinum | 93% | Highest diversion rate of any sports venue globally at time of certification; first West Coast TRUE Platinum [^37] |
| Mercedes-Benz Stadium (Atlanta) | TRUE Platinum | 90% target | TRUE Platinum and LEED Platinum dual certification [^38] |
| Q2 Stadium (Austin FC) | TRUE Platinum | — | First and only soccer-specific venue in the world with TRUE certification, upgraded from Gold to Platinum Feb 2026 [^39] |
| Lumen Field (Seattle Seahawks) | TRUE Gold | — | Second NFL venue with TRUE certification, achieved Dec 2025 [^40] |

Mercedes-Benz Stadium's waste program illustrates the operational infrastructure required: zero waste stations and labeled bins throughout all concourses, compostable food containers, post-sort of non-compostable items, a **6,000 sq ft onsite resource recovery and compost compactor facility**, regular bin auditing, and annual sustainability reporting.[^41]

***

## 4. Grounds and Exterior Maintenance

### Landscaping and Playing Surfaces

Exterior grounds at large venues range from sports turf (requiring agronomic management) to ornamental landscaping, hardscaped plazas, and internal gardens (e.g., Mercedes-Benz Stadium's rooftop urban garden). For active sports fields:[^41]

- **Natural turf**: weekly mowing (no more than one-third of canopy height removed per cut), aeration, fertilization, and pest control; infield grooming to prevent compaction[^42]
- **Artificial/synthetic turf**: weekly maintenance recommended for active fields; seasonal deep maintenance; grooming every 40 hours of field use using specialized field equipment[^43][^35]
- **Water management**: smart irrigation using weather data and soil moisture sensors dramatically reduces irrigation water consumption[^44]

### Snow and Ice Removal

For venues in northern climates (a significant proportion of Canadian and northern U.S. convention centres, arenas, and stadiums), snow and ice removal is a critical operations function. Standard program elements include:

- Plowing and clearing of all parking lots, loading areas, and pedestrian zones
- Walkway clearing to ensure safe access/egress from all building entrances and exits
- Snow relocation and off-site hauling when accumulation threatens sight lines or operational areas
- Deicing of all pedestrian surfaces adjacent to building entrances
- Roof drainage management in arenas (the IIHF arena guide requires design accommodations for external rainwater drainage and snow removal from roofs)[^45]
- A minimum standard for ice rink boards: accumulated snow must be removed to a minimum clearance of 28 inches below the top of rink boards[^46]

Grounds maintenance responsibility allocation between venue operator and municipality is commonly governed by funding formula documents, particularly for public arenas.[^46]

### Exterior Lighting and Signage

Exterior lighting at venues serves safety/security, wayfinding, and branding functions. LED retrofit programs are nearly universal in new and renovated venues, with daylight-harvesting controls reducing artificial lighting demand during daytime events. Smart lighting systems from BMS vendors (Johnson Controls, Enlighted, Siemens, Honeywell, Schneider Electric) that support BACnet/IP allow exterior lighting to be integrated into the central BMS for scheduling and energy monitoring.[^47]

EV charging infrastructure is an emerging element of venue exterior operations. Venues can leverage their large electrical service capacity — typically underutilized during off-peak periods — to install EV charging stations in parking structures, creating a revenue stream and supporting community sustainability goals.[^48]

***

## 5. Capital Project Management

### Project Delivery Methods

Large venue capital projects — new construction, major renovations, and lifecycle replacements — predominantly use two delivery methods:

**Design-Build (DB):** A single entity holds both design and construction responsibility, providing schedule and cost certainty. Frequently used for components with highly specialized system integration requirements (e.g., scoreboards, distributed audio/video, AV infrastructure) where the designer and installer need to be co-responsible.

**Construction Manager at Risk (CM at Risk / CMAR):** The construction manager provides pre-construction advisory services (budgeting, scheduling, value engineering, constructability reviews) and then acts as general contractor, typically on a cost-plus or GMP (guaranteed maximum price) basis. This method is widely used for arena and convention centre projects because it allows the owner to build the design iteratively while maintaining cost control. Calgary's Scotiabank Saddledome replacement (the new Event Centre/Scotiabank Saddledome successor) used CMLC as development manager, Dialog + HOK as prime designers, and CANA Construction + Mortenson as construction managers. The Greater Sudbury Event Centre used PCL Construction in a CM at Risk structure.[^49][^50]

### Capital Reserve Planning

Industry standard capital reserve funding for arenas and public assembly venues is **a minimum of 0.5% of construction costs annually**, dedicated to major capital works and upgrades that cannot be absorbed by the annual operating budget. This reserve is separate from routine preventive maintenance, which is an operating expense. In practice, many aging venues face significant funding gaps: for example, Owen Sound's arena asset base carried a 10-year funding gap of $25 million against a $110.2 million replacement value.[^51][^52]

For lifecycle costing and capital planning, ASHRAE Technical Committee 7.3 provides the analytical framework for life-cycle cost analysis (LCCA) of building systems, covering initial cost, analysis period, discount rate, and periodic costs such as refurbishment and disposal.[^20][^53]

### BIM in Capital Project and Lifecycle Management

Building Information Modeling (BIM) has matured from a construction coordination tool into a facilities lifecycle management platform. When integrated with IoT sensors, BIM enables real-time building performance data, energy consumption tracking, and maintenance status to be visualized in spatial context. Key outcomes:[^54]

- **Asset tracking**: precise location and condition of all equipment, from HVAC units to lighting fixtures
- **Energy analysis**: BIM models linked to energy simulation support capital investment justification
- **Capital planning**: BIM-based cost analysis, asset health assessment, and lifespan projection support evidence-based capital reserve decisions[^54]

Tools like **Matterport** (3D scanning) enable rapid as-built BIM model creation from existing facilities, bridging the gap for venues built before digital documentation was standard. **OrthoGraph Operational BIM** is an emerging platform specifically designed for facility management use, enabling quick graphical asset inventory creation with mobile access.[^55][^56]

***

## 6. Energy Management and Sustainability

### Overview of the Certification Landscape

| Certification | Issuing Body | Scope | Venue Application |
|---------------|-------------|-------|-------------------|
| LEED (v4.1) | USGBC (U.S. Green Building Council) | Buildings — New Construction, O+M, ID+C, Core+Shell | Widely adopted in convention centres, arenas, stadiums; LEED v4.1 O+M for existing buildings is the pathway for operational certification [^57][^58] |
| TRUE | GBCI (Green Business Certification Inc.) | Zero waste operations — 4 levels: Certified, Silver, Gold, Platinum (90% diversion for Platinum) | Leading zero waste certification for sports/entertainment venues [^36][^37] |
| BOMA BEST 4.0 / Smart Buildings | BOMA Canada | Existing commercial buildings — Baseline to Platinum; 6 domains (Energy/Carbon, Water, IAQ, Wellness, Waste, Resilience/Site) | North America's largest existing building certification program; applicable to Canadian convention and entertainment venues [^59][^60] |
| BOMA 360 | BOMA International | Operational best practices recognition for commercial buildings | Prerequisite for TOBY awards; applicable to convention/assembly buildings [^61] |
| ISO 20121 | ISO / accredited bodies (SGS, etc.) | Sustainable event management systems — process standard | Used by event organizers, not buildings; Green Sports Alliance Summit achieved ISO 20121 in 2025 [^62][^63] |
| WELL Health-Safety Rating | IWBI (International WELL Building Institute) | Operational policies, cleaning protocols, IAQ, design strategies | IWBI launched a WELL Advisory on Sports and Entertainment Venues; applicable to arenas, convention centres [^64][^65] |
| Play to Zero | Green Sports Alliance | Net zero energy, water, zero waste — recognition platform with performance toolkit | Purpose-built for sports/entertainment industry; 230+ members; used by GEHA Field at Arrowhead Stadium, Climate Pledge Arena, and others [^66][^67] |
| ENERGY STAR (Portfolio Manager) | U.S. EPA / NRCan | Energy performance scoring | No dedicated stadium/arena ENERGY STAR score exists (development stalled); **ENERGY STAR score for indoor ice rinks** available through NRCan/EPA partnership [^68] |
| Living Future / Zero Carbon | ILFI | Zero carbon certification | Climate Pledge Arena: first ILFI Zero Carbon Certified arena [^69] |
| Net Zero Carbon Events | UNFCCC affiliate / NZCE initiative | Event carbon neutrality pledge | ASM Global signed the NZCE Pledge in July 2024 [^70] |

### Landmark Certified Venues (As of April 2026)

**LEED Platinum venues:**
- Seattle Convention Center Summit (new construction, Platinum) — among the greenest convention facilities in North America[^58]
- Mercedes-Benz Stadium — America's first LEED Platinum professional sports stadium, highest LEED score at 88 points[^71]
- Fiserv Forum (Milwaukee Bucks) — LEED Platinum v4.1 O+M score of 80, one of only two NBA arenas at LEED Platinum (alongside Portland's Moda Center), first LEED Platinum sports venue in Wisconsin, May 2025[^72][^73]
- Climate Pledge Arena — LEED Platinum and ILFI Zero Carbon Certified[^74]

**LEED Gold** convention centres include: Los Angeles, Walter E. Washington (D.C.), Huntington Place (Detroit), Anaheim, Ernest N. Morial (New Orleans), Orange County (Orlando), Colorado (Denver), Georgia World Congress Center (Atlanta), San Diego, George R. Brown (Houston), The Venetian (Las Vegas), and David L. Lawrence (Pittsburgh).[^58]

### Renewable Energy and Decarbonization

- **Solar PV**: Mercedes-Benz Stadium deploys 4,000 solar panels generating enough energy to power nine NFL games or 13 MLS matches annually. Mandalay Bay (MGM Resorts) features an 8.3 MW rooftop solar array — one of the largest contiguous rooftop solar installations on a convention centre in the United States.[^75][^71]
- **Fuel cells**: Crypto.com Arena installed 500 kW of Bloom Energy fuel cells, eliminating over 10,000 tons of CO₂.[^76]
- **EV charging**: Venues increasingly deploy EV charging on surplus electrical capacity, with solar generation supporting vehicle charging during off-peak hours.[^48]
- **Demand response**: BMS platforms integrated with OpenADR 2.0b protocol enable automated demand response participation, reducing peak demand charges and providing grid services. EV charging and HVAC loads are the primary demand response assets.[^77][^78]

### Major Operator Sustainability Commitments

**ASM Global** (world's largest venue management company) has committed to: reducing energy consumption 25% by 2030 (vs. 2023 baseline), sourcing 100% electricity from renewables from 2024, achieving carbon neutrality by 2050, diverting 50%+ of total waste by 2025, and eliminating single-use plastic in front-of-house by 2025. ASM Global partnered with **WeTrack** for sustainability goals and operations tracking.[^79]

**Oak View Group** launched the industry's first sustainability recognition and measurement platform following Climate Pledge Arena's success, expanding the Play to Zero sustainability network.[^80]

**MGM Resorts** reduced energy use intensity by nearly 25% between 2007 and 2024, uses smart energy analytics and fault detection/diagnostics systems for ongoing commissioning, and pursues LED optimization across all properties.[^81][^75]

### Water Conservation

Water conservation strategies at large venues include multiple layers:[^82][^44]
- **Smart irrigation systems** — weather data and soil moisture sensors reduce landscape water waste
- **Low-flow fixtures** — restrooms, concession sinks, urinals
- **Rainwater harvesting** — Mercedes-Benz Stadium cistern system achieves 47% potable water reduction[^41]
- **Greywater recycling** — treating sink/shower water for irrigation and toilet flushing
- **Leak monitoring** — real-time water meter add-ons provide consumption pattern data
- **Water performance tracking** — LEED O+M, BOMA BEST, and Green Sports Alliance Play to Zero all include water as a tracked metric

***

## 7. Space Management

### Space Allocation Systems and Venue Management Software

Large venues require dedicated software to manage the complexity of multi-use, multi-configuration spaces. The leading platforms in this domain are:

| Platform | Vendor | Category | Key Capabilities |
|----------|--------|----------|-----------------|
| Momentus Technologies (formerly Ungerboeck) | Momentus | VMS/IWMS | Booking, CRM, space utilization, sustainability tracking, room diagramming, AI-powered analytics (Feb 2026 release), API integration; 60,000+ users globally [^83][^84] |
| IBM TRIRIGA | IBM | IWMS | Space management, stacking diagrams, floor plans, real-time utilization, capital projects, real estate portfolio, AI/analytics, BIM integration [^85][^86] |
| Archibus | SpaceIQ/Eptura | IWMS | Strategic space planning, asset management, building operations [^85] |
| Planon | Planon | IWMS | Real estate lifecycle, space utilization, facility operations [^85] |
| Accruent EMS | Accruent | Room/event scheduling | Desk and room reservation, event scheduling, campus/workplace management [^87] |
| EventPro | EventPro | Venue/event | Booking, event planning, catering, staffing, budgeting; modular architecture [^88] |

Momentus specifically tracks **space usages** including Event, Move-In (load-in), Move-Out (load-out), and Dark (space ready but not in use — common for theatrical set pre-rigging). This granularity enables accurate utilization metrics that separate actual event occupancy from setup and turnover time.[^89]

### CAD/BIM for Venue Operations

BIM-based digital twin environments are increasingly used not just for capital projects but for day-to-day venue operations. As of 2025–2026, approximately 70% of technology leaders prioritize digital twins in their facility strategy (Hexagon, 2025). Operational outcomes include:[^90]

- **Event layout simulation** — planners walk through 3D models weeks in advance to test configurations, verify sight lines, and approve sponsor placements
- **Real-time crowd monitoring** — IoT sensors fed into the digital twin display live heatmaps and crowd density indicators
- **Changeover planning** — digital twins simulate the conversion sequence between event configurations (e.g., hockey to concert), identifying logistical conflicts before physical setup
- **Infrastructure monitoring** — MEP asset status, energy consumption, and maintenance alerts visualized in spatial context[^91][^90]

**Matterport** LiDAR scanning and **3D venue mapping** are used to create precise digital replicas of existing facilities, providing the geometric foundation for operational BIM workflows.[^92]

### Space Utilization Tracking and Changeover Management

For venues hosting multiple event types and configurations, changeover management is a distinct operations discipline. Multi-configuration venues (arena bowl, flat-floor theatre, banquet, trade show, concert) must manage:

- **Configuration inventory**: detailed documentation of each configuration's floor plan, furniture, AV, lighting, and MEP settings
- **Changeover sequences**: step-by-step operational procedures linking crew, equipment, and time windows
- **BMS schedule alignment**: automatic pre-conditioning and setpoint changes keyed to each configuration
- **Utilization analytics**: Momentus Analytics and similar platforms provide dashboards tracking revenue per booking, space utilization rates, and conversion efficiency[^83]

For convention centres and arenas with multi-day trade shows followed by same-day concerts, the changeover schedule is often the binding constraint on event calendar density and directly impacts revenue yield.

***

## 8. Venue-Type Operational Comparison

| Operational Domain | Convention Centre | Arena / Stadium | Performing Arts Centre | Integrated Resort |
|-------------------|-------------------|-----------------|----------------------|-------------------|
| **BMS Complexity** | High — large HVAC for variable occupancy assemblies | High — includes ice plant controls (arenas) | Moderate — stage/backstage areas add complexity | Very High — gaming floor, hotel, convention, F&B all integrated |
| **HVAC Signature** | DCV for large assembly spaces; high fresh air demand | DCV + ice plant humidity control (arenas); high-occupancy bowl ventilation | HVAC for audience and backstage; acoustic constraints on mechanical design | Multiple zones; gaming floor air quality, kitchen exhaust |
| **Specialized MEP** | Large chiller plants, cooling towers | Ice refrigeration plant (arenas), Zamboni melting pit | Theatrical dimmer racks, fly motor power, stage sound power | CHP systems, extensive F&B MEP, high-security power |
| **Cleaning Approach** | Hall-to-hall turnovers between shows; exhibit hall power wash | Ice surface resurfacing (arenas); turf maintenance (stadiums); rapid seat-level cleaning | Stage area coordination with tech crew; orchestra pit cleaning | 24/7 continuous housekeeping; gaming floor never closes |
| **Critical Redundancy** | N+1 generators; UPS for IT/AV | N+1 generators; scoreboard/timing on UPS; ice plant on dedicated power | UPS on stage dimmer and fly motor systems; dimmer room on generator | 2N or 2N+1 power; multiple utility feeds; CHP as primary power |
| **Capital Planning** | Long-term renovation cycles; trade show floor load ratings | Ice plant 25–30 year replacement cycle; scoreboard/AV 10–15 years; seat replacement 20+ years | Rigging system 25–30 year cycles; counterweight replacement | Hotel FF&E 7–10 year cycle; gaming equipment rapid refresh |
| **Energy Dominance** | Lighting and HVAC | Refrigeration (arenas ~40% of energy); HVAC | Theatrical lighting (LED replacing tungsten) | Hotel HVAC + gaming floor + F&B kitchen exhaust |
| **Sustainability Lead** | LEED Gold/Platinum convention centres | TRUE zero waste leaders (State Farm Arena, Climate Pledge Arena); LEED Platinum arenas | Smaller footprint; fewer certifications pursued | LEED for hotel components; large resort campus sustainability programs |
| **Space Mgmt Tool** | Momentus, IBM TRIRIGA, Archibus for hall/meeting room booking | Sports CRM for suite/seat management + Momentus for non-sports events | Production management software + VMS for rental bookings | Hospitality PMS + event management integration |

***

## Emerging Trends Shaping the Ecosystem (2025–2026)

**AI and generative AI in venue operations** are beginning to transition from pilot projects to production deployment. AI is embedded in modern CMMS platforms for work order triage, equipment failure forecasting, and automated vendor dispatch. Generative AI is being explored for maintenance documentation, compliance reporting, and operational procedure generation.[^11]

**Digital twins as operational infrastructure** — rather than just a design tool — are achieving mainstream adoption. Venues that invested in digital twins during construction are deriving ongoing value from real-time monitoring, predictive maintenance, and virtual event planning.[^91][^90]

**Carbon tracking and ESG reporting** are now required capabilities for large venue operators. ASM Global's partnership with WeTrack and the IAVM sustainability research program reflect the institutionalization of ESG measurement as a core FM function, not a marketing initiative.[^93][^79]

**Smart stadium market growth** is projected at a CAGR of approximately 16–34% (depending on the research source), from a market value of approximately $9.6–17 billion in 2025, as IoT infrastructure, 5G connectivity, and analytics platforms become embedded in venue infrastructure refresh cycles.[^94][^95]

**Natural refrigerants in ice arenas** (CO₂ and ammonia) are displacing HFC-based systems as provincial and national codes phase out high-GWP refrigerants, with Capital One Arena's 2025 CO₂ retrofit being emblematic of a generational equipment replacement wave underway across North American arenas.[^22]

***

*Sources span IAVM, USGBC, ASHRAE, GBCI, Green Sports Alliance, IFMA, BOMA International, BOMA Canada, and primary documentation from ASM Global, Oak View Group, MGM Resorts, Johnson Controls, Siemens, Honeywell, Schneider Electric, IBM, and Momentus Technologies.*

---

## References

1. [Sports and Entertainment Venues | Johnson Controls](https://www.johnsoncontrols.com/industries/sports-and-entertainment) - Through our cutting-edge solutions, we make your sports stadium smarter, safer, and highly efficient...

2. [Johnson Controls Metasys 15.0 open Building Automation System ...](https://www.johnsoncontrols.com/media-center/news/press-releases/2025/11/17/johnson-controls-metasys-150) - Metasys 15.0 simplifies deployment and can be scaled across multiple buildings and sites, bringing c...

3. [Siemens Desigo vs Niagara: Choosing the Right System - LinkedIn](https://www.linkedin.com/posts/christopher-kelly-5a6b9620_bms-bems-bas-activity-7405918154004201472-pzAQ) - Siemens is effectively unique among mainstream BMS vendors in working from a structured plant model ...

4. [Case Study: Making Buildings Smarter - Automation.com](https://www.automation.com/article/case-study-making-buildings-smarter) - Siemens leverages Dell Technologies OEM Solutions to create the smart buildings platform. While Siem...

5. [Software Solutions - Honeywell Building Management Systems](https://buildings.honeywell.com/us/en/brands/our-brands/bms/what-we-do/software-and-services/niagara) - Step into building automation with Honeywell's solutions for 24/7 remote building monitoring, diagno...

6. [Historical Building and BMS – a Schneider Electric demo case](https://www.smarteestory.eu/historical-building-and-bms-a-schneider-electric-demo-case/) - The historic hotel began its decarbonization journey with a goal of achieving 15% energy savings wit...

7. [Top 10 Building Management System Companies to Know - nanoGrid](https://www.nanogrid.com/blog/top-10-building-management-system-companies-to-know-and-how-to-compare-them) - Johnson Controls remains a global leader in building automation systems. Its flagship BMS, Metasys, ...

8. [Demand Control Ventilation (DCV) - Inovis Energy, Inc.](https://www.inovisenergy.com/solutions/hvac-upgrades/demand-control-ventilation-dcv/) - Demand Control Ventilation (DCV) is a smart HVAC strategy that adjusts fresh air intake based on rea...

9. [[PDF] Demand-Controlled Ventilation - Trane](https://www.trane.com/content/dam/Trane/Commercial/global/products-systems/education-training/continuing-education-gbci-aia-pdh/APP-CMC067-EN.pdf) - 3.8 Ventilation Controls for High-Occupancy Areas. Demand control ventilation (DCV) is required for ...

10. [Ultimate Guide to Rink Surface Maintenance - Pro Landscapes MD](https://prolandscapesmd.com/ultimate-guide-to-rink-surface-maintenance/) - Synthetic Ice Panels: Clean regularly with pH-neutral soap, vacuum debris, and apply glide-enhancers...

11. [The Future of Sports Facility Management | EZFacility](https://www.ezfacility.com/blog/future-of-sports-facility-management/) - AI is now embedded into modern CMMS (Computerized Maintenance Management Systems) to triage tickets,...

12. [CMMS for Arenas and Stadiums | Sports facilities management ...](https://www.clickmaint.com/industries/cmms-software-for-arenas-and-stadiums) - # CMMS for Arenas and Stadiums | Sports facilities management software

Shape Iconic Experiences

 N...

13. [How to Use IoT Sensors for Predictive Maintenance in CMMS](https://www.ioxcmms.com/blog/how-to-use-iot-sensors-for-predictive-maintenance-in-cmms) - Learn how IoT sensors and CMMS enable predictive maintenance, reduce downtime, and optimize asset re...

14. [Stadium Operations and Maintenance Between Events: A Guide for ...](https://snapfix.com/news/stadium-operations-and-maintenance-between-events-a-guide-for-facilities-teams) - Manage stadium maintenance, safety checks, and event turnarounds faster with Snapfix’s all-in-one pl...

15. [IBM Maximo Application Suite](https://www.ibm.com/products/maximo) - IBM Maximo helps organizations manage, maintain and optimize assets using AI insights to reduce down...

16. [Maximo CMMS Overview: What It Does, Who It's For - Camcode](https://camcode.com/blog/maximo-cmms-overview-what-it-does-who-its-for-more/) - Maximo CMMS is a powerful computerized maintenance management system that helps businesses efficient...

17. [Standards 180 and 211 - ASHRAE](https://www.ashrae.org/technical-resources/bookstore/standards-180-and-211) - Standard 180 establishes minimum HVAC inspection and maintenance requirements that preserve a system...

18. [V in HVAC - Energy Efficient HVAC Systems Design - ASHRAE](https://www.ashrae.org/professional-development/all-instructor-led-training/catalog-of-instructor-led-training/v-in-hvac-energy-efficient-hvac-systems-design-6-credits) - This seminar covers the essential aspects of ASHRAE Standard 62.1-2022 and equips students with the ...

19. [[PDF] ASHRAE 100 Users' Guide - Gov.bc.ca](https://www2.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/construction-industry/building-codes-and-standards/guides/8777014_2021_04_01_ashrae_100_users_guide-single_page_interactive.pdf) - Working together to reduce energy consumption in existing buildings in a cost-effective way will lea...

20. [ASHRAE 7.3 Operation, Maintenance and Cost Management](https://tpc.ashrae.org/Functions?cmtKey=eff611f0-c3f1-4c2b-b986-06b428e4a4b8) - TC 7.3 is concerned with the operation, maintenance, and cost management of buildings and the use of...

21. [Refrigeration for Hockey Rinks: Guide to Ice Rink Refrigeration](https://www.gaenns.com/blog/refrigeration-for-hockey-rinks) - Ice rink refrigeration comes down to managing heat transfer via chillers, refrigerants, brine or gly...

22. [Washington Capitals Install New CO2 System - CIMCO Refrigeration](https://www.cimcorefrigeration.com/resources/washington-capitals-install-new-co2-system) - Explore the new CO₂ system replacing the 30-year-old ice plant at Capital One Arena, plus a look at ...

23. [Net Zero Naturally: CIMCO's sustainable Ice Rink Solutions](https://www.cimcorefrigeration.com/industries/recreational-ice-rinks/net-zero-naturally) - Net Zero Naturally offers a 360 degree approach to getting to net-zero emissions, reducing energy co...

24. [Types of Data Centers and Backup Power Explained](https://blog.concentricusa.com/engineering-uptime/types-of-data-centers-and-backup-power-explained) - Critical Power Needs: Often feature fully customized power systems with N+1 or 2N redundancy, on-sit...

25. [Exploring complex hotels, resorts, and casinos: Electrical/lighting ...](https://www.csemag.com/exploring-complex-hotels-resorts-and-casinos-electrical-lighting-power/) - Power system-wise, the designs are heavy on resiliency including CHP, battery energy storage systems...

26. [Generators for Data Centers & Power Plants](https://www.kairuipower.com/blog/generators-key-components-for-stable-power-in-power-plants-and-data-centers) - Discover how industrial generators provide mission-critical backup power, meet ISO & Tier IV standar...

27. [Performing Arts Safety Bulletin #7](https://www.actsafe.ca/wp-content/uploads/2022/08/Rigging-Flown-Scenery-Performing-Arts-Bulletin-PDF.pdf) - d) The maintenance of a rigging system should include: • An inspection and examination, by a compete...

28. [Rigging systems and fall arrest | Safety guidelines for the live ...](http://www.ontario.ca/document/safety-guidelines-live-performance-industry/rigging-systems-and-fall-arrest) - The maintenance of a rigging system should include: an inspection and examination by a competent per...

29. [Theater Maintenance | UCOP](https://www.ucop.edu/safety-and-loss-prevention/environmental/program-resources/performing-arts/theater-maintenance.html) - Counterweight Fly System – Complete annual fly system inspection and servicing by competent Performi...

30. [Live Theater Stage Safety Inspection Checklist [FREE PDF]](https://www.popprobe.com/checklist-library/entertainment/performing-arts/live-theater-stage-safety-inspection-checklist) - # Live Theater Stage Safety Inspection Checklist [FREE PDF]

This live theater stage safety inspecti...

31. [Event Venue Turnaround: Resetting 50000 Sq Ft Overnight](https://millfac.com/blog/event-venue-turnaround-cleaning) - The Short Answer. A full event venue turnaround covers floor scrubbing, restroom deep clean, trash r...

32. [How It Works - Zamboni](https://zamboni.com/about/how-it-works/) - The resurfacer needs to wash the ice, shave the ice and leave behind a layer of fresh ice making wat...

33. [Resurfacing the Ice Rink - REALice®](https://realice.ca/resurfacing-ice-rink/) - Drive consistently and keep at the same pace when resurfacing an ice rink. Make sure the blade is sh...

34. [10 Essential Tips for Your Outdoor Football Field Maintenance](https://hallturf.com/10-essential-tips-for-your-outdoor-football-field-maintenance/) - Regular practices such as mowing, aeration, fertilization, and are essential. Weekly inspections pla...

35. [What are the Top 5 Turf Field Maintenance Practices? - Motz](https://themotzgroup.com/sport_blog/what-are-the-top-5-turf-field-maintenance-practices/) - Our artificial turf infill options help provide a consistent, safe surface to ensure your synthetic ...

36. [State Farm Arena Becomes World's First Sports and Live ... - IAVM](http://blog.iavm.org/state-farm-arena-becomes-worlds-first-sports-and-live-entertainment-venue-to-earn-true-certification-for-zero-waste/) - State Farm Arena Becomes World's First Sports and Live Entertainment Venue to Earn TRUE Certificatio...

37. [CLIMATE PLEDGE ARENA ACHIEVES RECORD-BREAKING ...](https://climatepledgearena.com/cpa-achieves-true-certification/) - Seattle's Climate Pledge Arena has achieved the highest waste diversion rate of any sports venue glo...

38. [Ecoworks - Facebook](https://www.facebook.com/ecoworksstudio/photos/mercedesbenzstadium-truly-sets-the-gold-standard-with-its-leed-platinum-and-true/1366812334891867/) - @mercedesbenzstadium truly sets the gold standard with its #LEED Platinum and #TRUE Platinum certifi...

39. [Q2 Stadium Earns TRUE Platinum Certification - Austin FC](https://www.austinfc.com/news/q2-stadium-earns-true-platinum-certification) - Q2 Stadium initially earned TRUE Gold certification in 2024 and remains the first and only soccer-sp...

40. [Lumen Field, home of the Seattle Seahawks, achieves TRUE Gold ...](https://www.lumenfield.com/venue-info-news/true-certification-2025) - Dec 02, 2025 Lumen Field becomes only the second NFL venue to achieve TRUE Certification for zero-wa...

41. [Sustainability at Scale: What Mercedes-Benz Stadium Teaches Us ...](https://www.campwren.com/blog/mercedes-benz-stadium) - The stadium is LEED Platinum certified, the highest level awarded by the U.S. Green Building Council...

42. [Essential Maintenance for Sports Fields | Guelph Turfgrass Institute](https://guelphturfgrass.ca/essential-maintenance-sports-fields) - Operations should attempt to mow frequently enough to not remove more than 1/3 the height of the can...

43. [Essential Turf Field Maintenance: Best Practices for Long-Lasting ...](https://www.yellowstonelandscape.com/blog/essential-turf-field-maintenance-best-practices-for-long-lasting-performance) - Ensure a safe, durable, and attractive sports field with expert turf maintenance. Learn best practic...

44. [Water Conservation Strategies for Large Venues - Rockvolt](https://www.rockvolt.co.uk/water-conservation-strategies-for-large-venues) - How can large venues and stadiums improve their water consumption? · Smart Irrigation Systems · Low ...

45. [[PDF] iihf official- ice arena guide 2024](https://blob.iihf.com/iihf-media/iihfmvc/media/downloads/projects/ice%20rink%20guide/240926_iihf_ice_arena_guide_2024-september_12_fin.pdf) - Auxiliary spaces are mainly planned at the ends of the arena, leaving the long sides of the space fr...

46. [[PDF] Universal Funding Formula Responsibilities Document](https://www.gcwcc.mb.ca/site/assets/files/1049/universal_funding_formula_responsiblities_document_-_january_1-_2020.pdf) - Parking Lots. Clear and remove snow and litter. Repairs and replacement to pre-cast parking curbs an...

47. [The Rising Demand for Integrated Building Systems: How Lighting + ...](https://autani.com/2025/05/14/the-rising-demand-for-integrated-building-systems-how-lighting-hvac-work-together/) - The Rising Demand for Integrated Building Systems: How Lighting + HVAC Work Together · Why manage tw...

48. [Sports Venues Can Revolutionize EV Charging and Boost Revenue](https://www.bryceenergyservices.com/2024/01/13/sports-venues-ev-charging-boost-revenue/) - This article delves into how these venues, such as football stadiums, can harness their underutilize...

49. [CMLC REVEALS PROJECT TEAM FOR CALGARY'S NEW EVENT ...](https://calgaryroughnecks.com/cmlc-reveals-project-team-for-calgarys-new-event-centre/) - CMLC announced the Prime Design Consultant (PDC), Construction Management (CM) and specialty firms s...

50. [City of Greater Sudbury, ON selects PCL construction for downtown ...](https://www.facebook.com/groups/valleyeasttoday/posts/10163989195892328/) - The CM at Risk arrangement blends the advisory and management role of a Construction Manager with th...

51. [[PDF] Nanaimo Events Centre](https://www.nanaimo.ca/docs/your-government/event-centre-information/nanaimo-events-centre---draft-business-plan.pdf) - The Base Case developed by Stafford Sports incorporated a Capital Reserve Fund contribution based on...

52. [[PDF] Asset Management Plan - Arenas and Recreation Centres .docx](https://www.owensound.ca/media/5ejdoeq1/attachment-2-asset-management-plan-arenas-and-recreation-centres.pdf) - The below chart outlines the 10-year lifecycle costs of arena and recreation ... Replacement costs h...

53. [[PDF] ECONOMIC ANALYSES AND LIFE-CYCLE COSTS - ASHRAE](https://xp20.ashrae.org/SupplementalFiles/PHVAC9/Economic_Analyses_and_LCC.pdf) - The following elements must be established to calculate annual owning costs: (1) initial cost, (2) a...

54. [How BIM Transforms Facility Management for a Sustainable Future](https://maintenanceworld.com/2025/02/25/how-bim-transforms-facility-management-for-a-sustainable-future/) - BIM enhances facility management in many ways. This digital tool revolutionizes how projects are des...

55. [7 BIM Trends Defining Modern Construction & Facility Management](https://matterport.com/blog/bim-trends) - The following seven BIM trends highlight where this practice is headed in 2025 and what it means for...

56. [Revolutionizing Industrial Operations and Facility Management with ...](https://www.orthograph.com/revolutionizing-industrial-operations-and-facility-management-with-operational-bim-insights-from-bim-world-munich-2024/) - Adam demonstrated how OrthoGraph's Operational BIM concept bridges this gap, offering a solution des...

57. [Applying LEED to hospitality and venue projects](https://support.usgbc.org/hc/en-us/articles/12127181820435-Applying-LEED-to-hospitality-and-venue-projects) - As of December 2025, there are 4,407 LEED‐certified and registered lodging and hotel projects repres...

58. [LEED Certification at U.S. Convention Centers Ticks Up](https://www.prevuemeetings.com/meeting-planner-resources/sustainability-csr/leed-certification-at-us-convention-centers-ticks-up/) - Many of the largest convention centers in the US are LEED (Leadership in Energy and Environmental De...

59. [BOMA BEST - Sustainable & Smart Building Certification Program](https://bomabest.org) - BOMA BEST is a leading sustainability certification program for commercial buildings in Canada, help...

60. [ESG building certification | Canadian Bar Association](https://cba.org/Sections/Construction-and-Infrastructure-Law/Member-Articles/ESG-building-certification) - For example, builders concerned with sustainability could pursue BOMA BEST 4.0 Sustainable Buildings...

61. [[PDF] 2024-2025 ENTRY REQUIREMENTS - BOMA Canada](https://bomacanada.ca/wp-content/uploads/2024/02/2024.02.09-2025-TOBY-Criteria-Industrial.pdf) - a. Include training for security standards for property management, staff, and tenants. 2.3 Explain ...

62. [3R Supports Green Sports Alliance in Achieving ISO 20121 ...](https://www.3rsustainability.com/3r-supports-green-sports-alliance-iso-20121-certification/) - The Alliance's ISO 20121 certification is a testament to its commitment to sustainability. By achiev...

63. [Your guide to ISO 20121 2024 Event sustainability management ...](https://www.sgs.com/en-sa/news/2024/04/mastering-sustainable-event-management-your-complete-guide-to-iso-20121-2024-certification) - Our guide helps Middle East event organizers implement ISO 20121, integrating sustainability into al...

64. [International WELL Building Institute Launches WELL Health-Safety ...](https://via.tt.se/pressmeddelande/3276943/international-well-building-institute-launches-well-health-safety-rating-for-facility-operations-and-management-of-sports-and-entertainment-venues?publisherId=259167) - IWBI mobilizes the wellness community through management of the WELL AP credential, the pursuit of a...

65. [WELL Certification - International WELL Building Institute | IWBI](https://www.wellcertified.com/certification/v2/) - WELL Certification helps organizations demonstrate their commitment to well-being by earning the hig...

66. [Play to Zero Initiative by Green Sports Alliance](https://www.greensportsalliance.org/playtozero) - Explore the Play to Zero initiative. Learn about our tracking platform and partnerships driving sust...

67. [Sustainability in Sport Organizations in the United States - Emerald](https://www.emerald.com/books/edited-volume/21309/chapter/109558731/Sustainability-in-Sport-Organizations-in-the) - Certain venues, such as the GEHA Field at Arrowhead Stadium in Kansas City, Missouri, use the “play ...

68. [ENERGY STAR Score for Indoor Ice Rinks](https://natural-resources.canada.ca/energy-efficiency/energy-star/buildings/technical-reference-documents/energy-star-score-indoor-ice-rinks) - To be eligible for the ENERGY STAR score for indoor ice rink, less than 25% of facility space must b...

69. [Climate Pledge Arena | LinkedIn](https://au.linkedin.com/company/climatepledgearena) - The world's first Zero Carbon Certified arena, located in the heart of Seattle. Dedicated to bringin...

70. [[PDF] ASM Global Signs the Net Zero Carbon Events Pledge in Support of ...](https://www.netzerocarbonevents.org/wp-content/uploads/ASM-Global-signs-NZCE-Pledge-final.pdf) - Brussels, 29 July 2024 – The Net Zero Carbon Events (NZCE) initiative announced today. ASM Global, t...

71. [US's First LEED Stadium - Project | ODS - Outdoor Design](https://www.outdoordesign.com.au/news-info/uss-first-leed-stadium/5717.htm) - The Mercedes-Benz Stadium in Atlanta, USA, has received official certification as America's first LE...

72. [Fiserv Forum Awarded Prestigious LEED Platinum Certification - NBA](https://bucks.com/news/fiserv-forum-awarded-prestigious-leed-platinum-certification) - Fiserv Forum achieved LEED Platinum certification with a score of 80, which puts it among the leader...

73. [FISERV FORUM AWARDED PRESTIGIOUS LEED® PLATINUM ...](https://www.fiservforum.com/news/detail/fiserv-forum-awarded-prestigious-leed-platinum-certification) - Fiserv Forum becomes one of only two NBA arenas to earn LEED v4.1 Platinum certification for operati...

74. [Sustainability - Climate Pledge Arena](https://climatepledgearena.com/sustainability/) - Climate Pledge Arena serves as a long-lasting and regular reminder of the urgent need for climate ac...

75. [[PDF] 2024 TCFD Report-2026-01-21-15-18 - Contentstack](https://assets.contentstack.io/v3/assets/bltc6ce635bc4868eb2/bltb012a61e51f4b558/mgm-resorts-tcfd-report-2024.pdf) - Fuel Conservation and Fugitive Emissions Management - MGM Resorts has taken strides to reduce Scope ...

76. [Environmental Sustainability | Crypto.com Arena](https://www.cryptoarena.com/arena-info/environmental-sustainability) - In 2015 Crypto.com Arena installed a 500 kW bank of Bloom Energy fuel cells, which generate electric...

77. [Demand Response in Commercial Energy Management](https://www.commercialintegrator.com/insights/demand-response-in-commercial-energy-management/140929/) - Integrators who understand demand response and its interaction with energy management & AV systems c...

78. [Demand Response and Building Automation | Enel North America](https://www.enelnorthamerica.com/insights/blogs/building-automation-makes-demand-response-effortless) - Leveraging a building automation system (BMS) to orchestrate demand response participation is vital ...

79. [ASM Global Unveils Ambitious Plan Transforming Its Global Venue ...](https://www.sttinfo.fi/tiedote/69970912/asm-global-unveils-ambitious-plan-transforming-its-global-venue-portfolio-into-worlds-most-sustainable-collection?publisherId=58763726) - Increase plant-based menu options by 35% by 2024 within Savor (ASM Global's food division) venues. D...

80. [Sustainability - Oak View Group](https://www.oakviewgroup.com/our-solutions/sustainability/) - Join the industry's first sustainability recognition and measurement platform. In 2021, following th...

81. [Energy - MGM Resorts](https://www.mgmresorts.com/en/company/focused/investing-in-environmental-stewardship/energy.html) - We have adopted a culture of innovation in energy management by testing a wide range of energy techn...

82. [How to Achieve LEED Certification for Event Venues - Guidebook](https://www.guidebook.com/post/achieve-leed-certification-event-venues) - By focusing on energy-efficient design, conserving water, and using sustainable materials, your venu...

83. [Momentus Technologies Announces AI-Powered Platform ...](https://www.prnewswire.com/news-releases/momentus-technologies-announces-ai-powered-platform-enhancements-for-venue-and-event-operations-302676378.html) - Momentus Analytics provides built-in visibility into sales, revenue, pipeline, and space utilization...

84. [Momentus Technologies Pricing, Reviews & Features](https://www.capterra.ca/software/2403/momentus-technologies) - 18 years helping Canadian businesses

choose better software

## What Is Momentus Technologies?

Mom...

85. [Top 10 Best Space Management Software of 2026 - WifiTalents](https://wifitalents.com/best/space-management-software/) - 5#5: IBM TRIRIGA - Enterprise IWMS platform for managing real estate, facilities, capital projects, ...

86. [Space Management - IBM TRIRIGA](https://www.ibm.com/products/tririga/space-management) - IBM TRIRIGA provides comprehensive reservation tools to reserve flexible space and ensure that space...

87. [EMS Software: Workplace Management Made Easy - Accruent](https://www.accruent.com/products/ems) - Manage desks, rooms, events, workspace, and resources in one platform. Accruent EMS helps teams run ...

88. [EventPro: Venue Management Software](https://www.eventpro.net) - All-in-one venue, event & catering management software. EventPro streamlines bookings, planning, cat...

89. [Manage Space Usages - Momentus Support Center](https://elitesupportcenter.ungerboeck.com/hc/en-us/articles/17443339054103-Manage-Space-Usages) - Navigate to Space Usages. Click on your name in the upper left corner and select System Admin to acc...

90. [Digital Twins in Event Management | Smart Spatial Blog](https://smartspatial.com/post/how-digital-twins-are-transforming-event-management) - 70% of technology leaders now prioritize digital twins in their strategy (Hexagon, 2025). 15% averag...

91. [Digital Twin Technology: Revolutionizing Stadium Management](https://www.simio.com/blog/digital-twin-technology-revolutionizing-stadium-management) - Digital twin tech boosts stadium operations by optimizing security, concessions, and fan engagement ...

92. [Digital Twin Events for Smarter Corporate Planning - White Massif](https://whitemassif.com/blog/digital-twin-events) - This guide explains digital twin events and how pre-testing corporate events improves planning accur...

93. [Resources - International Association of Venue Managers](https://iavm.org/resources/) - VenueDataSource is the research program of IAVM and is a valuable resource for its members, partners...

94. [Smart Stadium Market Size, Share & Growth Analysis, 2034](https://www.fortunebusinessinsights.com/smart-stadium-market-110452) - The global smart stadium market size was valued at USD 9.57 billion in 2025 and is projected to grow...

95. [Smart Stadium Market Size, Share & Growth Report 2035](https://www.researchnester.com/reports/smart-stadium-market/6468) - The global smart stadium market size crossed USD 17.26 billion in 2025 and is likely to expand at a ...

