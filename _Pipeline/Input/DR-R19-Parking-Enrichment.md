# R-19: Parking & Transportation Domain — Source Enrichment Report

**Purpose:** Provide independent, non-vendor corroboration for existing medium-confidence concept notes in the parking-and-transportation knowledge base. This report specifically targets the four concepts flagged at medium confidence (Technology-Systems, Pre-Paid-Reserved, Self-Operated-Vs-Contracted, Transit-Multimodal), fills the two DELTA-019 gaps (TNC/ride-share zone management and MUTCD special events citations), and adds structured sourcing for AV readiness and sustainability topics.

**Source Priority Applied:** Government regulatory (P1) > Professional association standards (P2) > Academic transportation research (P3) > Industry data with methodology disclosure (P4). Vendor marketing materials are excluded throughout.

***

## 1. TNC / Ride-Share Zone Design Standards

### 1.1 NACTO Curb Management Framework

The National Association of City Transportation Officials (NACTO) is the primary non-vendor authority on curbside pickup/dropoff design. The **NACTO "Curb Appeal" publication (2017)** provides policy foundations for curbside management, establishing that transit protection, commercial loading, and accessible passenger loading must be assigned to prevent bus blockages, with remaining curb dedicated to uses including "pick-up and drop-off areas for for-hire and private vehicles." This document is FHWA-endorsed and is the appropriate anchor citation for TNC/ride-share zone policy.[^1][^2]

The **NACTO Urban Street Design Guide — Curbside Activity section** provides specific geometric parameters for passenger loading zones:

- Far-side space: minimum **20 ft (6 m)** for a single-vehicle loading area
- Near-side space: minimum **40 ft (12 m)**
- Midblock space: minimum **60 ft (18 m)**
- Each additional vehicle anticipated in the queue adds **20 ft (6 m)**[^3]

These dimensions are the authoritative non-vendor source for lane geometry in TNC pickup/dropoff zone design at venues.

### 1.2 ITE Curbside Management Practitioners Guide

The **ITE Curbside Management Practitioners Guide** (published by the Institute of Transportation Engineers) explicitly addresses TNC pick-up and drop-off at high-demand destinations including stadiums and performing arts venues. The guide discusses geofencing to direct for-hire vehicle drivers and riders to designated pick-up and drop-off zones, call attention to restricted areas, and addresses PLZ (Passenger Loading Zone) design for events. This is a P2-category professional association source (ITE) with transparent methodology, distinct from vendor documentation.[^4][^5]

The ITE also maintains the **Curbside Management Tool**, built on the ITE Curbside Practitioners Guide and the FHWA Curbside Inventory Report, providing spatial and temporal prioritization frameworks for curb allocation using ArcGIS Pro.[^5]

### 1.3 ADA Requirements for Passenger Loading Zones

The **U.S. Access Board Technical Guide on Passenger Loading Zones (§503)** provides federal accessibility standards that apply to all venue pickup/dropoff infrastructure:[^6]

| Element | Requirement |
|---|---|
| Vehicle pull-up space width | Minimum 96 inches |
| Vehicle pull-up space length | Minimum 20 feet |
| Access aisle width | Minimum 60 inches |
| Vertical clearance | 114 inches throughout vehicular route |
| Accessible zone frequency | 1 per every 100 linear feet of PLZ |

These requirements apply to any "areas specifically designed or designated for passenger loading," which includes all formal TNC zones at public assembly facilities.[^6]

### 1.4 Independent Research on TNC Zone Effectiveness

The **University of Washington Urban Freight Lab (2023)** conducted field research testing curbside management strategies including increased PLZ allocation combined with geofencing. Results showed that the combined strategy reduced the number of TNC pick-ups/drop-offs occurring in travel lanes, reduced dwell times, increased curb use compliance, and increased TNC passenger satisfaction — though no observable effect on travel speeds was detected in the study area.[^7]

A **Bureau of Transportation Statistics / ROSAP report on Curb Management** (available via ROSA P/National Transportation Library) examined TNC PUDO zone design criteria derived from taxi stand design research, identifying that users prefer locations with good lighting, shelter, seating, proximity to retail options, and safe sightlines.[^8]

### 1.5 Municipal TNC Zone Implementations (Regulatory Evidence)

**Nashville, TN (NDOT):** The Nashville Department of Transportation and Multimodal Infrastructure conducted a formal rideshare zone pilot program at the Tennessee Performing Arts Center beginning January 2025, with Phase 2 extended through December 28, 2025. NDOT used metered parking spaces as designated rideshare and taxi pick-up/drop-off zones. The stated goals were to "develop a rideshare zone framework guide that can be used to stage other pick-up and drop-off zones throughout downtown as part of the Connect Downtown Action Plan." NDOT negotiated contract provisions with Uber and Lyft specifying designated staging locations.[^9][^10]

**Las Vegas, NV (Nevada Taxicab Authority):** The Las Vegas Grand Prix (LVGP) Rideshare & Taxi Plan, filed with the Nevada Taxicab Authority, documents formal event-specific TNC zone operations from 6:00 PM – 3:00 AM. Zones were established at the Sphere, multiple Strip properties (Park MGM, The Mirage, Wynn), and peripheral staging areas. Each zone included "traffic equipment, event staff, and wayfinding signage" to ensure smooth traffic flow. Inner-circuit hotels deployed dedicated courtesy shuttles during hot track hours when rideshare access was restricted.[^11]

**Data Gap — Trip Volumes:** No publicly accessible, peer-reviewed study providing MLB/NFL/NHL/MLS game-day TNC trip volume data was found. NDOT's pilot program is designed to generate such data; results from Phase 2 (ending December 2025) would be a future independent source.

***

## 2. MUTCD Traffic Management for Special Events

### 2.1 MUTCD 11th Edition — Applicable Sections (December 2023)

The **Manual on Uniform Traffic Control Devices for Streets and Highways, 11th Edition (FHWA, December 2023)** is the primary federal regulatory source. Key sections applicable to public assembly venue operations:

**Part 6 — Temporary Traffic Control:**
- **Section 6A (Fundamental Principles of TTC):** Paragraph 10 states: *"For any planned special event that will have an impact on the traffic on any street or highway, a TTC plan should be developed in conjunction with and be approved by the agency or agencies that have jurisdiction over the affected roadways."* This is the operative standard linking MUTCD Part 6 to event-day operations.[^12]
- **Section 6A, Paragraph 7:** TTC plans must be prepared by "persons knowledgeable (for example, trained and/or certified) about the fundamental principles of TTC and work activities to be performed." This establishes the training/certification requirement for traffic control personnel at venue events.[^12]
- **Chapter 6O — Traffic Incident Management Areas** (renumbered from Chapter 6I in the 2009 Edition): Governs temporary traffic controls at incident scenes; applicable to unplanned disruptions during events such as post-event queue spillback, crashes, or stalled vehicles. The 2003 Edition Chapter 6I referenced the same material under that designation.[^13][^14]

**Note on Edition References:** The 2009 and 2003 MUTCD editions used "Chapter 6I" for Traffic Incident Management Areas. The 11th Edition (2023) renumbered this content to Chapter 6O. Any existing KB citations referencing MUTCD Chapter 6I should be clarified as referencing pre-11th Edition text.[^14][^15][^13]

### 2.2 FHWA Planned Special Events Handbook (Primary Independent Source)

The **FHWA "Managing Travel for Planned Special Events" Handbook (Publication FHWA-OP-04-010)** is a 448-page, 15-chapter federal guidance document constituting the primary independent operational reference for special event traffic management. The companion **Executive Summary (FHWA-HOP-07-108)** and **Checklists for Practitioners (FHWA-HOP-08-005)** cover chapters 4–10 of the handbook.[^16][^17][^18][^19]

Key Traffic Management Plan (TMP) components identified in **Chapter 6 (Table 6-2)**:[^20]

| TMP Component | Description |
|---|---|
| Site Access and Parking Plan | Venue entry/exit routing, parking allocation |
| Traffic Flow Plan | Corridor/route assignments, freeway/arterial lane designations |
| En-Route Traveler Information | Dynamic message signs, app/website integration |
| Traffic Incident Management Plan | References regional TIM manuals + event-specific modifications |
| Pedestrian Access Plan | ADA pathways, wayfinding |
| Traffic Control Plan | Intersection assignments, signal timing, personnel deployment |
| Traffic Surveillance Plan | Camera/sensor coverage for event-day monitoring |

**Chapter 4** addresses the special event permit process. Permit application deadlines for large-scale events generally range from 60 to 120 days prior, depending on jurisdiction:[^21]

| Jurisdiction | Permit Deadline |
|---|---|
| Ypsilanti, MI | 60 days |
| Montgomery County, MD | 60 days |
| Virginia Beach, VA | 60–90 days |
| Redmond, WA | 90 days |
| Aurora, IL | 120 days |

**Chapter 2** explicitly addresses permanent venue TMP deployment: "Stakeholders often develop transportation management plans specific to a permanent venue, such as a stadium, arena, or amphitheater. Development of site access and parking plans usually occur during venue construction."[^22]

### 2.3 State/Provincial Traffic Manual Supplements

**Ontario Traffic Manual Book 7 — Temporary Conditions (April 2022 Field Edition):** Published by the Ontario Ministry of Labour, Immigration, Training and Skills Development (MLITSD), Book 7 provides the Canadian provincial standard for traffic control in work zones and temporary conditions on public highways, including ramps and municipal roads. Appendix A covers "Temporary Traffic Control for Unplanned Events," including emergency planning, first-on-scene protocols, and situations requiring special attention. The Field Edition is the current operative reference for Traffic Control Person (TCP) qualification and authority requirements in Ontario.[^23][^24][^25]

**Key TCP requirements under OTM Book 7:** TCPs shall not direct traffic for more than one lane in the same direction; shall not direct traffic where the posted speed limit exceeds 90 km/h; shall be a "competent worker"; and shall not perform other work while setting up or directing traffic.[^23]

**California MUTCD:** A 2026 draft edition of the California MUTCD Chapter 6G Figures has been circulated by the California Transportation Commission (CTCDC) for review. The current operative California MUTCD supplements federal MUTCD for state and local roadways; practitioners should verify current adopted edition via Caltrans.[^26]

**Alberta Special Events Guide (3rd Edition, updated July 2025):** Published by Alberta Infrastructure and Transportation, this guide addresses event permitting within the provincial highway right-of-way and is directly applicable to Alberta-based operations.[^27]

### 2.4 Traffic Control Personnel Training

MUTCD 11th Edition Section 6A, Paragraph 7 establishes that TTC plan designers must be trained and/or certified. The FHWA handbook reinforces that traffic engineers and law enforcement constitute the core planning team. At the provincial level, OTM Book 7 defines "competent worker" qualification for TCP roles. In the U.S., the **American Traffic Safety Services Association (ATSSA)** and state DOT programs administer TTC training and certification, though the MUTCD itself does not mandate a specific national certification program — it requires competence.[^16][^12][^23]

***

## 3. Parking Operational Models — Independent Sources

### 3.1 Municipal Parking Authority Published Data

**Toronto Parking Authority (TPA):** The TPA is a municipally owned, fully self-funded entity that receives no operating funding from the City of Toronto. The **2016 TPA Operating Budget (City of Toronto Council-approved)** documents total gross cost of $84.7 million against revenues of $137.0 million, with 299–302 staff and an approved 10-year capital plan of approximately $345 million (2011–2020). This represents a high-quality independent benchmark for municipal self-operated parking at scale.[^28][^29][^30]

The **Toronto Auditor General's 2016 audit of TPA revenue operations** (audit report published January 12, 2016) produced 12 recommendations to enhance operational efficiency, focusing on: (1) reporting to demonstrate alignment of parking rates with policy, (2) expanding automation to enhance efficiency, and (3) updating policies and procedures. This government audit report is a P1/P4-category source documenting the operational structure of a self-operated municipal parking authority distinct from vendor claims.[^31]

**Chicago Parking Meters Concession:** The Chicago P3 case offers direct comparative evidence on self-operated versus contracted models. In 2008, Chicago leased ~36,000 on-street meters to Chicago Parking Meters LLC for $1.15 billion over 75 years. By 2025, the consortium had earned approximately $2 billion — nearly double the purchase price. A NACTO-published analysis of the concession details pricing zones, rate schedules, "true-up" provisions, and the city's retained enforcement revenue. Independent analysis by the Metropolitan Planning Council documented that the 2013 renegotiation saved $25 million/year, or $1 billion over the contract life. A 2025 settlement required Chicago to pay $15.5 million to the consortium for pandemic enforcement shortfalls.[^32][^33][^34]

**Nashville Metro Traffic & Parking Commission:** The February 2024 staff analysis documents the Nashville meter rate formula: *Revenue = (T × D) × U*, where T = established hourly rate (CBD: $2.25/hr; Non-CBD: $1.75/hr), D = hours in a day, U = flat utilization rate of 65%. This yields published rates of $35/day (CBD) and $28/day (Non-CBD). The commission also documents valet parking permit fee structures for public right-of-way. This is an official municipal document, not vendor-sourced.[^35]

### 3.2 Independent Academic and Policy Research

**VTPI Comprehensive Parking Supply, Cost and Price Analysis (2023):** Todd Litman of the Victoria Transport Policy Institute, published in the *Journal of Transportation and Statistics*, documents that commercial parking spaces typically rent for $50–$250/month in U.S. city centers, and establishes methodological frameworks for revenue-per-space analysis that distinguish between commercial, institutional, and government operators.[^36]

**VTPI TDM Encyclopedia — Parking Pricing:** Documents that parking price elasticity of vehicle trips is typically -0.1 to -0.3 (a 10% price increase reduces parking demand by 1–3%). These figures are widely used in event parking pricing analysis and derive from multiple independent studies reviewed by Litman, not from vendor data.[^37][^38]

**UBC Sustainability — Best Practices & Recommendations on Parking Management (2021):** Describes Vancouver's payment-in-lieu program, with private sector underground parking construction costs of $40,000–$50,000/space (2017), updated to $195–$270/sq.ft by 2022 per Altus Group data.[^39][^40]

### 3.3 IPMI Benchmarking (Association Source with Transparent Methodology)

The **IPMI (formerly IPI) Parking Analytics: An Industry Snapshot (2017)** launched an expanded benchmarking initiative tracking KPIs including revenue per FTE personnel, offering operators the ability to contribute data at parking.org/kpis. IPMI is an association, not a vendor; its benchmarks involve member-contributed operational data with disclosed methodology. While IPMI has vendor members, its benchmarking and publications (Parking & Mobility Magazine, certification programs) represent the P2 standard for this domain.[^41]

The **Parksmart certification program** (co-developed by IPMI/Green Parking Council, now administered by GBCI/USGBC) documents that certified garages average up to a 25% reduction in operational costs compared to the national average. This represents independently verified operational performance data from a third-party certification body.[^42]

***

## 4. Pre-Paid and Reserved Parking Programs — Non-Vendor Evidence Base

### 4.1 Pricing Elasticity (Academic Sources)

**Meta-Analysis of Parking Price Elasticities (Transportation Research Part A, 2019):** A peer-reviewed study published in *Transportation Research Part A: Policy and Practice* (ScienceDirect) conducted a meta-analysis of 50 parking price elasticity studies using seemingly unrelated regression models. The primary finding: the baseline price elasticity for non-commuting trips is **-0.63** (95% CI: -0.72 to -0.54). This is the most rigorous available academic benchmark for event parking price sensitivity and directly corroborates the range cited in the VTPI guidelines.[^43]

**VTPI Parking Pricing Implementation Guidelines:** Litman documents trip-level elasticity at -0.1 to -0.3 for vehicle trips with respect to parking price. These figures are appropriate for event parking demand modeling and are independent of any vendor claims.[^37]

**SFpark Demand-Responsive Pricing (Independent Municipal Evidence):** The Nashville Metro Best Practices document on parking management describes the San Francisco Municipal Transportation Agency's SFpark program results: achieving target occupancy (60–80%) 31% of the time in pilot areas vs. 6% in non-pilot areas; garage utilization increased 11%; parking availability increased 45% on blocks with no free parking. SFpark is a government-operated program with published methodology, making this a P1 source for dynamic/demand-responsive pricing at venues.[^44]

### 4.2 Mobile Payment Adoption (Independent Financial Research)

**Federal Reserve Bank of Boston — "Solving Real Pain Points: How Parking Apps Drive Mobile Payment Adoption" (Payment Strategies group):** This Federal Reserve publication documents mobile parking payment behavior from independent consumer research. Key findings include: 19% of consumers paid for parking via mobile as of the 2015 Deloitte Global Mobile Consumer Survey; the Boston Fed's own 2012 field test found low initial adoption; by 2017, the trend showed measurable growth. The report frames mobile parking payment as a behavioral trigger for broader mobile payment adoption, supporting its independence from parking technology vendor claims.[^45][^46]

**Federal Reserve Board — Consumers and Mobile Financial Services (2015):** National annual survey tracking mobile banking and payment adoption trends, providing independent baseline data on consumer readiness for digital parking transactions.[^47][^48]

**Boston Fed — Mobile Banking and Payment Survey of New England Financial Institutions (2016):** Documents institutional mobile payment readiness alongside consumer adoption rates.[^49]

These Federal Reserve sources are appropriate P1-category (government/independent financial institution) anchors for mobile payment adoption claims, replacing or corroborating vendor white papers on parking technology adoption.

### 4.3 Consumer Behavior and Pre-Purchase Patterns

**IPMI/Parking & Mobility Magazine — "Parking as the First Touchpoint" (2025):** An IPMI-sourced article (P2) notes that consumer behavior varies significantly by event type; fans attending concerts frequently book reserved parking at the same time as purchasing event tickets. This provides an association-sourced anchor for lead-time booking behavior without relying on ParkMobile case study metrics.[^50]

**ScienceDirect — "Misinformation and Misperception in the Market for Parking" (Transportation Research):** Academic research finding that parkers demonstrate low awareness of available parking alternatives and prices, with knowledge biased toward familiar (often free or low-cost) options. This finding has direct implications for pre-paid program marketing and wayfinding strategy at venues.[^51]

**Note on No-Show Rates:** No peer-reviewed or government study specifically addressing pre-paid parking no-show rates at event venues was located. This remains a gap where vendor data (e.g., ParkMobile internal statistics) currently dominates the evidence base. Academic studies on no-show behavior in related reservation contexts (healthcare, restaurants) exist but have not been validated for event parking specifically.

***

## 5. Transit and Multimodal Integration — Catalog

### 5.1 FTA Guidance Documents

**FTA Major Event Playbook (December 2025):** Released by the Federal Transit Administration in December 2025 in advance of the 2026 FIFA World Cup, this publication fills a long-standing gap in FTA guidance for planned major events. Topics covered include:[^52][^53]

- Assessing current public transportation service capacity and frequency for venue-scale events
- Supplemental service strategies: frequency increases, route deviations with stops near venues, express service establishment
- Charter service provisions, including FTA charter regulations and third-party agreements
- Loaned vehicles from non-host transit agencies
- ADA requirements for temporary event service (FTA ADA Circular C 4710.1)
- Accessibility for visitors with disabilities, including paratransit visitor eligibility

The playbook explicitly addresses scenarios where "existing event venues already may be served by transit, but may need to be evaluated for capacity, frequency, operating hours, and accessibility in the context of expected crowd sizes."[^52]

**FTA ADA Circular C 4710.1 (November 4, 2015):** Provides ADA guidance for transit recipients including requirements for accessible transportation facilities, stations, platforms, and service. Applicable to any FTA-funded transit extension or service modification serving event venues. Specifies that accessible spaces must minimize travel distance to accessible entrances and that no exception exists for temporary event service.[^54][^55][^56]

**Special Event Transportation Service Planning (BTS/ROSAP, 2006):** Earlier federal-era best practices document for transit agency involvement in planned special events, covering planning guidelines and strategies.[^57]

### 5.2 Venue-Specific Published Ridership Data

**Wrigley Field / CTA Red Line:** The **Wrigley Field Game Day Traffic Management Plan** (City of Chicago document, available via Scribd) documents that a 2001 survey by Siim Soot estimated approximately 31% of Cubs fans used CTA Rail. Since 2001, transit ridership at Addison Station increased 29%; the report estimates CTA rail accounts for **at least 40%** of Wrigley Field attendees. In 2012, more than 3 million people entered the Addison Red Line Station annually, making it one of the busiest in the system. The **Ideas42 Behavioral Research Report on Incentivizing Commuter Behavior** (2017) corroborates intense Red Line loading around Cubs games, documenting 5–6 PM peak ridership on weekday game nights sufficient to require demand-management interventions.[^58][^59]

**MetLife Stadium / NJ Transit Meadowlands Rail Line:** NJ Transit's published fare and schedule information documents game-day rail service beginning 3.5 hours before game time, running every 10–20 minutes pre-game, hourly during, and every 10 minutes post-game from 11 NJ Transit rail lines via Hoboken Terminal and Secaucus Junction. For the 2026 FIFA World Cup, NJ Transit's MetLife Transitway — funded by a $100 million FTA grant — is designed to augment rail capacity by carrying an additional 10,000 persons per hour; the complementary bus network is planned to operate "a bus every 30 seconds for four hours" around match times.[^60][^61][^62][^63]

**Rogers Centre / GO Transit (Toronto):** Metrolinx (the provincial crown agency operating GO Transit) confirms Union Station is a 10-minute walk from Rogers Centre via the covered SkyWalk. During Blue Jays game returns in July 2021, Metrolinx deployed extra GO trains on standby with upsized trainsets, plus regular 30-minute service on Lakeshore East and Lakeshore West lines during weekend games.[^64][^65]

**Denver / RTD Event Service (Empower Field at Mile High):** RTD's published high-volume event operations documented that during the Metallica M72 World Tour (June 27–29, 2025) — with 150,000+ fans over two nights — RTD provided connections for **upwards of 50,000 riders**; one night alone saw **more than 23,000 riders** via bus and rail to the stadium. RTD begins monitoring event calendars and flagging high-ridership events weeks in advance, deploying D, E, and W rail lines plus multiple local bus routes.[^66][^67][^68]

### 5.3 Bicycle Infrastructure Standards (NACTO)

**NACTO Urban Bikeway Design Guide (3rd Edition, 2025):** The current edition is the definitive non-vendor source for bicycle facility design. Key dimensions relevant to venue bicycle parking infrastructure:[^69][^70]

- Typical bike footprint: **2 ft (0.6 m) wide × 6 ft (1.8 m) long**
- Cargo bike footprint: **3 ft (0.9 m) wide × 10 ft (3 m) long**
- Preferred rack types: inverted-U (staple/loop racks) and post-and-ring racks; all other types discouraged[^71]
- Indoor bike parking: two-tier racks with lift assist acceptable alongside ground-level inverted-U racks[^71]

The NACTO Urban Bikeway Design Guide is FHWA-endorsed and constitutes a P2 source for venue bicycle parking design.[^2]

**NACTO Urban Street Design Guide — Curbside Activity:** Specifies that accessible parking spaces must be planned alongside all bike facility projects and references the Public Right-of-Way Accessibility Guidelines (PROWAG) for accessible parking requirements adjacent to protected bikeways.[^3]

### 5.4 Pedestrian Access Standards

The **U.S. Access Board Passenger Loading Zone guide (§503)** and the **ADA Standards §402** establish accessible route requirements for outdoor pathways: walking surfaces with slope no steeper than 1:20, with connections required between accessible parking spaces and accessible venue entrances. ADA Section 502 requires accessible parking space width of at least 96 inches with firm, slip-resistant surfaces and signage at least 60 inches above the ground.[^72][^6]

The **FTA Major Event Playbook** specifies that "any designated stop and pedestrian connection used during planned major events are accessible so that persons with disabilities can reach those accessible vehicles," and that paratransit must be available to event visitors who present proof of eligibility from any transit system.[^52]

***

## 6. Autonomous Vehicle Staging and Future-Proofing

### 6.1 Federal AV Policy Framework

**USDOT AV 4.0 — "Ensuring American Leadership in Automated Vehicle Technologies" (January 2020):** The current federal AV policy document outlines 10 principles organized across three interests: protecting users and communities (safety, cybersecurity, privacy, accessibility), promoting efficient markets, and facilitating coordinated efforts. AV 4.0 is explicitly a framework of voluntary guidelines rather than binding regulation; it establishes multi-agency coordination posture led by the White House National Science and Technology Council.[^73][^74][^75]

The USDOT Automated Vehicles Comprehensive Plan (2021) serves as the implementation-level complement to AV 4.0, covering research, regulatory modernization, and deployment pathways.[^73]

**FHWA Research on AV Highway Infrastructure Impacts (FHWA-RD-21-015, 2021):** Documents current concerns and potential impacts of AVs on highway infrastructure, providing FHWA with an evidence base for infrastructure modifications — including pavement marking conspicuity, lane width standards, and curbside design considerations for AV sensor performance.[^76]

### 6.2 SAE J3016 Automation Levels — Venue Implications

**SAE J3016 (April 2021 revision):** The internationally recognized taxonomy defining SAE Levels 0–5 of driving automation. Levels relevant to venue parking and transportation:[^77][^78]

| SAE Level | Description | Venue Application |
|---|---|---|
| Level 1 | Driver assistance (lateral or longitudinal only) | Parking assistance (parallel parking) |
| Level 2 | Partial automation (both axes, driver supervises) | Automated parking maneuver assist |
| Level 4 | High automation (no driver required within ODD) | Automated valet parking, driverless shuttle service |
| Level 5 | Full automation (no ODD limits) | Full-autonomy shuttle/circulator |

SAE J3016 specifically provides an example where a **Level 4 automated parking feature** dispatches the vehicle in driverless operation to find a parking space in a designated parking facility, then allows user retrieval via dispatch. A **Level 4 ADS-DV (driverless vehicle)** is defined as being dispatched for ride-hailing services. These definitions are the appropriate regulatory anchor for KB concept notes on valet automation and autonomous shuttle integration.[^79]

### 6.3 NACTO Blueprint for Autonomous Urbanism (2nd Edition)

**NACTO Blueprint for Autonomous Urbanism, Second Edition:** This NACTO policy framework establishes design and policy principles for AV integration in urban streets, directly addressing curbside management. Key recommendations applicable to venue curbside design:[^80][^81]

- Real-time curbside management systems should allow AVs to "automatically reserve time slots a few minutes in advance of arrival at a site"[^82]
- AV-only lanes should be reserved for automated mass transit, not private single-occupancy AVs[^81]
- Cities should adopt curbside management plans committing any space savings from reduced parking to public use (parklets, bus/bike lanes, green infrastructure)[^81]
- Shared AVs could "significantly reduce congestion and the need for parking, opening up new options for street design"[^81]

The Blueprint is a P2 source (professional association with transparent policy rationale) applicable to venue master planning for AV-readiness.

### 6.4 ITE Curbside Management for AVs

The **ITE Curbside Management Tool** (built on the ITE Curbside Management Practitioners Guide and FHWA Curbside Inventory Report) incorporates AV-era curbside considerations in its temporal and spatial prioritization framework. ITE is developing guidance that addresses AV PUDO coordination as a distinct curbside use category alongside TNCs, freight, and transit.[^5]

**Draft ISO 25614:** An international standard under development establishing a framework for **digital PUDO orchestration** — defining message formats and transaction flows for coordinated AV curb access without exposing proprietary operator data. This is the emerging standards layer that will govern AV staging at high-demand venues.[^83]

**DOE/OSTI Research on SAV PUDO (2023):** Agent-based simulation research conducted in the Austin, TX CBD tested 18 scenarios of PUDO spacing, fleet size, and fare pricing for shared autonomous vehicles. Findings show that PUDO spacing (1 block vs. 3 blocks) has significant impact on ridership, vehicle-miles traveled, vehicle occupancy, and revenue — directly applicable to venue parking area shuttle zone design.[^84]

### 6.5 AV Shuttle Pilot Programs

**Denver RTD AV Shuttle Proposal (USDOT ADS Demonstration Grant Application):** RTD requested $6.33M in federal funds for a Level 4 EasyMile shuttle operating a 2.2-mile route from the University of Denver light rail station into campus. A prior pilot at the same location saw more than 32,000 riders, with 98% recommending the service. This is an FTA-adjudicated, USDOT-reviewed program — a P1/P4 source.[^85]

**NPS Low-Speed Automated Shuttle Evaluation (2022):** Federal evaluation report from the National Park Service documenting pilot experiences at multiple NPS sites, covering operational performance, public acceptance, and infrastructure requirements.[^86]

**Fairfax County Autonomous Electric Shuttle (Relay):** Operated by Dominion Energy / EasyMile EZ10 from 2021 through June 30, 2023; used GPS + 3D LiDAR (262 ft range) + 2D LiDAR (131 ft range) for navigation; operated on public roads as a first/last-mile service. This county-operated pilot provides government-sourced documentation of AV shuttle infrastructure requirements.[^87]

***

## 7. Parking Sustainability Practices — Catalog

### 7.1 Parksmart Certification (GBCI/USGBC)

**Parksmart** is the world's only rating system that specifically defines, measures, and recognizes high-performing sustainable parking structures. It was initially developed in 2014 by the International Parking Institute and the Green Parking Council; it is now administered by Green Business Certification Inc. (GBCI), the same body that administers LEED.[^88][^89][^42]

| Certification Tier | Requirement |
|---|---|
| Bronze | Minimum 20 points in each of 3 categories (new construction or projects commissioned within 2 years) |
| Silver | Higher point threshold across same 3 categories |
| Gold | Highest tier for new construction |
| Pioneer | Existing structures commissioned >2 years before registration |

The three certification categories are: (1) Management, (2) Programs, and (3) Technology and Structure Design. As of December 2021, over 150 new and existing projects in 10 countries have registered or certified with Parksmart. Certified garages have averaged up to a **25% reduction in operational costs** compared to the national average.[^90][^91][^88][^42]

**Critical distinction from LEED:** Per the USGBC, stand-alone parking structures are **not eligible for LEED certification**. When a venue contains a significant mixed-use component in the same footprint, LEED certification becomes possible; otherwise Parksmart is the applicable certification standard.[^92]

### 7.2 EV Charging in Parking Structures — Regulatory Standards

**U.S. Access Board Technical Assistance Document on EV Charging (2023):** Provides design guidance for accessible EV charging stations under ADA and ABA standards. Applicable requirements for parking structures:[^93]

- Minimum vehicular route vertical clearance: **98 inches** throughout the route to accessible EV spaces[^93]
- Accessible EV charging space: minimum **11 ft wide × 20 ft long**, with **5 ft access aisle**[^93]
- EV charging stations must connect to an accessible route to the accessible entrance of the parking structure[^93]
- Converting existing accessible parking spaces to EV-only spaces is not recommended and may require recalculation of minimum accessible space counts[^93]

**Proposed U.S. Access Board Rules for Accessible EV Charging (2024):** Proposes upgraded dimensions: accessible EV space at least **132 inches wide × 240 inches long × 98 inches high**; access aisle minimum **60 inches wide** extending the full length of the space.[^94]

**ASHRAE Standard 90.2-2018, Addendum N (2024):** Energy code standard for EV charging in parking facilities: each installed EVSE space must be capable of supplying not less than **7.4 kVA full continuous load**; where 10 or more spaces are installed with an EV energy management system, the distribution equipment may use load-sharing calculations.[^95]

**State/Local ADA Variances:** New York City requires up to 5% of EV spaces to be accessible; NYC also does not permit an EV space to count as one of the minimum required accessible parking spaces in a project. California, New Jersey, and jurisdictions adopting the 2021 International Building Code have added scoping requirements beyond federal minimums.[^96]

### 7.3 Solar Canopy Integration

The **IPMI/Parking & Mobility Magazine (2025 Awards)** documents that current sustainable parking structure designs include roof levels pre-wired for future photovoltaic panels and Level 2 EV charging stations. This confirms industry-standard practice for solar-readiness in new parking structures.[^97]

Solar canopy installations serve a dual function: renewable energy generation and vehicle shade, with documented secondary benefits including stormwater management (canopy drainage systems capture and filter rainwater), mitigation of the urban heat island effect, and direct DC-coupled EV charging. The integration of solar canopies with EV charging is increasingly treated as a single infrastructure investment.[^98]

### 7.4 Stormwater Management in Parking Areas

**EPA Stormwater Best Management Practice — Permeable Pavements:** The U.S. Environmental Protection Agency's official BMP guidance classifies permeable pavements as green infrastructure under the Clean Water Act, capable of providing up to 80% total suspended solids removal. Three permeable pavement types are documented for parking applications:[^99]

- Porous asphalt
- Pervious concrete
- Permeable interlocking concrete pavers (PICP)

Each type is evaluated against conventional impervious asphalt as a control.[^99]

**EPA Edison Environmental Center Permeable Pavement Study:** EPA researchers designed a 1-acre parking lot (110 vehicles) using all three permeable pavement types plus rain gardens, with long-term monitoring of water quality, maintenance effects, and hydrologic performance. This government-operated study provides the most rigorous independent dataset on permeable pavement performance in parking applications.[^100]

**Sustainable Technologies Canada — Permeable Pavement and Bioretention Swale Performance Evaluation (2008):** Canadian government-adjacent research evaluated PICP and bioswale performance in a commercial parking lot in the Greater Toronto Area. During the largest monitored storm event (72 mm over 5.5 hours), permeable pavement overflow volume was less than 10% of runoff from conventional asphalt. The bioswale overflowed only during events exceeding approximately 20 mm, with most annual runoff infiltrating into the ground. This study is directly applicable to Canadian (Alberta) venue parking contexts.[^101]

**Minnesota Stormwater Manual — Permeable Pavement Design Criteria:** Documents the "treatment train" approach applicable to sloping venue parking sites: permeable pavement as primary filter feeding bioswales or rain gardens for additional nutrient processing. Includes maintenance requirements (vacuuming, avoidance of sanding and sealcoating) specific to parking lot applications.[^102]

***

## 8. Confidence Elevation Summary

The following table maps newly identified independent sources to existing medium-confidence concept notes:

| Concept Note | Root Cause (per A-06 audit) | Primary New Independent Sources |
|---|---|---|
| **Technology-Systems** | ParkMobile case study as sole evidence | Boston Fed mobile payments reports[^45][^46]; Federal Reserve 2015 Consumer Survey[^48]; SFpark demand-responsive pricing data[^44]; ITE Curbside Management Tool[^5] |
| **Pre-Paid-Reserved** | ParkMobile/NPA vendor data | ScienceDirect meta-analysis (50 studies, elasticity -0.63)[^43]; VTPI Parking Pricing elasticity -0.1 to -0.3[^37][^38]; Boston Fed parking mobile payments brief[^45]; SFpark occupancy data[^44] |
| **Self-Operated-Vs-Contracted** | NPA rate study as sole source | Toronto Parking Authority annual report + Auditor General audit[^31][^29][^30]; Chicago P3 concession NACTO analysis[^32][^33][^34]; Nashville rate formula (municipal document)[^35]; VTPI cost analysis[^36] |
| **Transit-Multimodal** | Limited independent ridership data | FTA Major Event Playbook (Dec 2025)[^52]; NJ Transit Meadowlands Rail service[^61]; Denver RTD 50,000-rider event data[^66]; Wrigley Field 40% transit modal split[^58]; Metrolinx Rogers Centre documentation[^64][^65] |
| **TNC-Ride-Share-Coordination** (DELTA-019 gap) | Unsourced | NACTO Curb Appeal + USDG Curbside Activity dimensions[^1][^3]; ITE Curbside Practitioners Guide[^4]; Nashville NDOT pilot program[^9][^10]; Las Vegas LVGP official TNC plan[^11]; ADA PLZ standards §503[^6]; UW Urban Freight Lab curbside research[^7] |
| **Traffic-Management-Event-Day** (DELTA-019 gap) | No specific MUTCD section citations | MUTCD 11th Ed §6A ¶10 (TTC plan requirement)[^12]; FHWA Handbook FHWA-OP-04-010 Chapter 6 TMP components[^16][^20]; OTM Book 7 April 2022[^23][^24]; FHWA Chapter 4 permit deadlines[^21] |

### Remaining Gaps

The following specific data points remain unsourced by independent non-vendor evidence and represent continuing knowledge base limitations:

1. **TNC trip volume at major venues (MLB/NFL/NHL/MLS):** No publicly accessible, peer-reviewed or government dataset found. NDOT's Nashville pilot is designed to generate such data (results expected after December 2025).
2. **Pre-paid parking no-show rates at event venues:** Academic literature on no-show behavior has not been validated for this specific use case. Vendor-held operational data (ParkMobile, etc.) remains the primary source.
3. **Direct self-operated vs. contracted operational cost comparison for venues specifically:** Published studies compare operational models for municipal on-street and off-street parking; stadium/arena-specific managed parking comparison studies were not located. IPMI's benchmarking surveys approach this gap but have not produced a publicly accessible peer-reviewed comparison specific to venue contexts.
4. **Wrigley Field game-day CTA modal split (post-2012):** The 40% estimate is derived from a pre-2012 document using 2001 survey data updated with 2012 station entry counts. A post-pandemic, directly measured figure does not appear to be in the public domain.

---

## References

1. [[PDF] curb appeal | nacto](https://nacto.org/wp-content/uploads/NACTO-Curb-Appeal-Curbside-Management.pdf) - This policy foundation supports transit project managers and designers in making better decisions ab...

2. [Design Guides - NACTO](https://nacto.org/publications/design-guides/) - NACTO's design guides, endorsed by FHWA, represent best practices for safe, multimodal urban streets...

3. [Curbside Activity - NACTO](https://nacto.org/publication/urban-bikeway-design-guide/designing-bikeways-for-all-ages-and-abilities/curbside-activity/) - Where possible, locate loading zones at the start or end of blocks. These spaces are easier to maneu...

4. [[PDF] CURBSIDE MANAGEMENT PRACTITIONERS GUIDE](https://s23705.pcdn.co/wp-content/uploads/2019/03/ITE-Kerbside-Curbside-Management-Guide.pdf) - Geofencing can be used to direct for-hire vehicle drivers and riders to pick-up and drop-off zones, ...

5. [Curbside Management Resources - ITE.org](https://www.ite.org/technical-resources/topics/complete-streets/curbside-management-resources/) - The Curbside Management Tool contains a suite of components that facilitate data collection, analysi...

6. [[PDF] Passenger Loading Zones - Access-Board.gov](https://www.access-board.gov/files/ada/guides/plz.pdf) - Where passenger loading zones are provided, at least one accessible passenger loading zone is requir...

7. [[PDF] Testing Curbside Management Strategies to Mitigate the Impacts of ...](https://urbanfreightlab.com/wp-content/uploads/2023/04/Testing-Curbside-to-Mitigate.pdf) - Some of the quantitative measures include event type (passenger pick-up or drop-off, vehicle park or...

8. [[PDF] Understanding Curb Management and Targeted Incentive Policies ...](https://rosap.ntl.bts.gov/view/dot/60827/dot_60827_DS1.pdf) - TNC Pick-Up and Drop-Off Zones. Taxi stand design and location findings can help inform pick-up and ...

9. [NDOT Extends Rideshare Zone Pilot Program with Tennessee ...](https://www.nashville.gov/departments/transportation/news/ndot-extends-rideshare-zone-pilot-program-tennessee-performing-arts-center) - The rideshare zone pilot program will assist NDOT in developing a rideshare zone framework guide tha...

10. [Nashville proposes designated rideshare zones to ease downtown ...](https://fox17.com/news/local/2025-jan-16-nashville-tennessee-proposes-designated-rideshare-zones-to-ease-downtown-traffic-congestion-lyft-uber-broadway-entertainment-district-davidson-county) - The Nashville Department of Transportation wants to limit where rideshare companies can pick up and ...

11. [[PDF] LVGP - Rideshare & Taxi Plan - Nevada Taxicab Authority](https://taxi.nv.gov/uploadedFiles/taxinvgov/content/Rider_Info/LVGP-Rideshare-and-Taxi-Plan.pdf) - LVGP has established drop-off and pick-up zones for each Venue Space. The following Pick Up/ Drop Zo...

12. [MUTCD 11th Edition Part 6: Temporary Traffic Control Guidelines](https://www.studocu.com/en-us/document/university-of-california-berkeley/applied-structural-mechanics/mutcd-11th-edition-part-6-temporary-traffic-control-guidelines/144195873) - This document outlines the guidelines and standards for temporary traffic control (TTC) as per the M...

13. [Chapter 6I. Control of Traffic Through Traffic Incident Management ...](https://mutcd.fhwa.dot.gov/htm/2003r1/part6/part6i.htm) - A traffic incident is an emergency road user occurrence, a natural disaster, or other unplanned even...

14. [Chapter 6I - MUTCD 2009 Edition - FHWA](https://mutcd.fhwa.dot.gov/htm/2009/part6/part6i.htm) - A traffic incident management area is an area of a highway where temporary traffic controls are inst...

15. [MUTCD 11th Edition - FHWA MUTCD - Department of Transportation](https://mutcd.fhwa.dot.gov/kno_11th_Edition.htm) - The 11th Edition of the MUTCD is available only in PDF format on this Web site. PDF formatted parts ...

16. [Managing Travel for Planned Special Events - FHWA Operations](https://ops.fhwa.dot.gov/publications/fhwaop04010/chapter5_02.htm) - Initial Planning Activities handbook section pertains to transportation engineer, law enforcement of...

17. [FHWA: Planned Special Events: Checklists for Practitioners - NOCoE](https://transportationops.org/publications/fhwa-planned-special-events-checklists-practitioners) - Planned special event practitioners may apply these checklists to a specific planned special event t...

18. [Managing Travel for Planned Special Events Handbook](https://ops.fhwa.dot.gov/publications/fhwahop07108/introduction.htm) - The Federal Highway Administration (FHWA) established a program devoted to managing travel for plann...

19. [Managing Travel for Planned Special Events Handbook: Executive ...](https://ops.fhwa.dot.gov/tim/preparedness/pse/handbook.htm) - These checklists follow the order in which the topics are presented in Chapters 4, 5, 6, 7, 8, 9, an...

20. [Managing Travel for Planned Special Events Handbook](https://ops.fhwa.dot.gov/publications/fhwaop04010/chapter6_02.htm) - Managing travel for planned special events involves developing a transportation management plan that...

21. [Managing Travel for Planned Special Events - FHWA Operations](https://ops.fhwa.dot.gov/publications/fhwaop04010/chapter4_03.htm) - This section on permitting will describe special event application components, review processes, gui...

22. [Managing Travel for Planned Special Events - FHWA Operations](https://ops.fhwa.dot.gov/publications/fhwaop04010/chapter2.htm) - This chapter presents planned special event operations characteristics and associated factors defini...

23. [[PDF] otm-book-7-temporary-conditions-field-edition-april ... - Owen Sound](https://www.owensound.ca/media/wcefhy1b/otm-book-7-temporary-conditions-field-edition-april-2022.pdf) - OTM Book 7 provides practical guidance regarding the use of traffic control ... require special cons...

24. [[PDF] Ontario Traffic Manual Book 7 - IHSA](https://www.ihsa.ca/PDFs/Products/Id/W015.pdf) - The Ontario Traffic Manual Book 7 (Temporary Conditions) provides the basic requirements for traffic...

25. [Ontario Traffic Manual - Book 7 - FIELD Edition - April 2022 (Book)](https://www.bestsafetytraining.ca/product/book-7-ontario-traffic-manual/) - In stock

26. [[PDF] Chapter 6G Figures](https://dot.ca.gov/-/media/dot-media/programs/safety-programs/documents/ca-mutcd/nmutcd/part6/20251002-ctcdc-mtg-ai-25-11-att-12-camutcd-2026-6g-figure-a11y.pdf) - Chapter 6G – TTC Zone Regulatory Signs. Part 6 Temporary Traffic Control. (DRAFT – For review purpos...

27. [Special events guide. 3rd edition - Open Government program](https://open.alberta.ca/publications/special-events-guide) - This Special Events Guide has been developed to provide guidance to the public and Alberta Infrastru...

28. [[PDF] Toronto Parking Authority ANNUAL REPORT](https://parking.greenp.com/documents/annual_reports/ar_00000016.pdf) - The Authority is unique from most City bodies in that it receives no funding support from the City t...

29. [[PDF] Toronto Parking Authority](https://www.toronto.ca/wp-content/uploads/2017/12/956c-Toronto-Parking-Authority-2016-Council-Approved-Operating-Program-Summary.pdf) - Moving into 2016, the Toronto Parking Authority was facing a net pressure of $5.259 million due main...

30. [[PDF] TPA Annual Report 2016 FINAL Website - Green P Parking](https://parking.greenp.com/app/uploads/2016/09/TPA-Annual-Report-2016-FINAL.pdf) - The Authority is unique from most City bodies in that it receives no funding from the City of Toront...

31. [[PDF] Auditor General's report - Toronto Parking Authority Phase 2](https://www.toronto.ca/legdocs/mmis/2016/au/bgrd/backgroundfile-90475.pdf) - This report contains 12 recommendations to enhance operational efficiency and effectiveness of the r...

32. [[PDF] Notes on Chicago's Metered Parking Concession - NACTO](https://nacto.org/wp-content/uploads/Chicago_PPM_Concession.pdf) - of parking and transportation system. ◦ Rates had not been raised on 75+% of parking meters in over ...

33. [Let's Talk About The Chicago Parking Meter Deal](https://thoughtsaboutcities.substack.com/p/lets-talk-about-the-chicago-parking) - Put differently, Chicago was just forced, by contract that itself signed, to pay $15M more for a dea...

34. [Chicago Parking Meter Analysis: Renegotiation of ... - MyCuriousCity](http://mycuriouscity.com/home/2016/7/18/chicago-parking-meter-analysis-renegotiation-of-parking-meter-deal-saves-money-and-sets-stage-for-future-turnaround) - The 2013 agreement that the City of Chicago negotiated with private concessionaire Chicago Parking M...

35. [[PDF] Metropolitan Traffic and Parking Commission FROM - Nashville.gov](https://www.nashville.gov/sites/default/files/2024-02/Staff_Analysis_TrafficParking_Commission-Feb2024-UPDATE.pdf?ct=1707857954) - Valet parking permit applicants shall be charged an application fee plus additional fees for use of ...

36. [[PDF] Comprehensive Parking Supply, Cost and Price Analysis](https://www.vtpi.org/WCTR2023_parking.pdf) - Parking facilities are sometimes valued by dividing total retail revenues by their number of spaces ...

37. [[PDF] Parking Pricing Implementation Guidelines](https://www.vtpi.org/parkpricing.pdf) - Parking pricing must balance different objectives. Efficient parking pricing means that motorists pa...

38. [Online TDM Encyclopedia - Parking Pricing](https://www.vtpi.org/tdm/tdm26.htm) - Even modest parking fees can affect vehicle travel patterns. The price elasticity of vehicle travel ...

39. [[PDF] Best Practices & Recommendations on Parking Management at the ...](https://sustain.ubc.ca/sites/default/files/2021-048_Best%20Practices%20&%20Recommendations%20on%20Parking%20_Le.pdf) - The section below briefly describes the five successfully implemented parking programs in Vancouver,...

40. [[PDF] Appendix E Parking Research Review and Survey Analysis](https://www.richmondhill.ca/en/resources/Development-Planning/Appendix-E-_-TER---Parking-Trends-Report-October-20-2023.pdf) - The intent of this report is to provide information for the City in order to assist in making decisi...

41. [[PDF] PARKING ANALYTICS: An Industry Snapshot](https://www.parking.org/wp-content/uploads/2016/05/2017-Parking-Data-Analytics-2.pdf) - In 2017 the International Parking Institute. (IPI) launched an expanded initiative focused on parkin...

42. [[PDF] Sustainable parking structures join the built community - Parksmart](https://parksmart.gbci.org/sites/default/files/certifiably-parked-report.pdf) - Parking plays a role. Parksmart (formerly Green Garage Certification) is the world's only rating sys...

43. [The price elasticity of parking: A meta-analysis - ScienceDirect.com](https://www.sciencedirect.com/science/article/abs/pii/S0965856417308832) - We conduct a meta-analysis of parking price elasticities based on 50 studies. Using seemingly unrela...

44. [[PDF] best practices: parking management - Nashville.gov](https://www.nashville.gov/sites/default/files/2023-01/BestPractices_ParkingManagement_20220916_FINAL.pdf?ct=1674064068) - Austin's parking plans created extensive databases of parking spaces, rates, utilization, and occupa...

45. [[PDF] Solving Real Pain Points: How Parking Apps Drive Mobile Payment ...](https://www.bostonfed.org/-/media/Documents/PaymentStrategies/everyday-mobile/brief-3-mobile-parking.pdf) - Consumer adoption and implementation of mobile parking apps have been growing in large and small cit...

46. [[PDF] Everyday Mobile Payments – Finally A Feasible Reality](https://www.bostonfed.org/-/media/Documents/PaymentStrategies/everyday-mobile-payments-finally-a-feasible-reality.pdf) - When the Boston Fed's Payment Strategies group conducted its first field test of mobile payment adop...

47. [[PDF] Consumers and Mobile Financial Services 2015 - Federal Reserve](https://www.federalreserve.gov/econresdata/consumers-and-mobile-financial-services-report-201503.pdf) - The sur- vey examines trends in the adoption and use of mobile banking, payments, and shopping behav...

48. [FRB: CM: 2015 Executive Summary](https://www.federalreserve.gov/econresdata/mobile-devices/2015-executive-summary.htm) - The survey examines trends in the adoption and use of mobile banking, payments, and shopping behavio...

49. [[PDF] 2016 Mobile Banking and Payment Survey of New England ...](https://www.bostonfed.org/-/media/Documents/PaymentStrategies/2016-mobile-banking-and-payment-survey-of-new-england-financial-institutions.pdf) - This study offers insights into current mobile banking practices and mobile payment plans of banks a...

50. [Destination and Event Management | Parking as the First Touchpoint](https://parking-mobility-magazine.org/features/parking-as-the-first-touchpoint/) - Behavior also varies significantly by event type and audience. For example, fans attending concerts ...

51. [Misinformation and misperception in the market for parking](https://www.sciencedirect.com/science/article/pii/S2214367X2200031X) - We find that parkers know little about available parking alternatives and their prices, and the accu...

52. [[PDF] FTA Major Event Playbook - Federal Transit Administration](https://www.transit.dot.gov/sites/fta.dot.gov/files/2025-12/FTA-Major-Event-Playbook.pdf) - This new. FTA Major Event Playbook fills that gap and includes practical information and key conside...

53. [FTA Announces Major Event Playbook for Transit Agencies](https://content.govdelivery.com/accounts/USDOTFTA/bulletins/3fe4dac) - The new playbook offers a practical guide, strategic insights, and key considerations to help public...

54. [[PDF] Americans with Disabilities Act Circular C 4710.1, Draft Chapters for ...](https://www.apta.com/wp-content/uploads/Resources/gap/fedreg/Documents/FTA_Draft_Chapters_ADA_Circular_Amendment_2%20-%20Final.pdf) - the ADA-ABA Accessibility Guidelines (ADA-ABA AG). ... FTA notes that many transit agencies find tha...

55. [[PDF] FTA Circular 4710.1 - Americans With Disabilities Act Guidance](https://www.transit.dot.gov/sites/fta.dot.gov/files/docs/Final_FTA_ADA_Circular_C_4710.1.pdf) - This circular provides guidance to recipients and subrecipients of Federal Transit. Administration (...

56. [Rail Law Alert – FTA Announces Guidance re: Compliance with ADA](https://www.kaplankirsch.com/resources-and-news/rail-law-alert-fta-announces-guidance-re-compliance-with-ada/) - In releasing Circular 4710.1, FTA emphasizes that it is merely providing additional guidance regardi...

57. [[PDF] Special Event Transportation Service Planning - ROSA P](https://rosap.ntl.bts.gov/view/dot/38501/dot_38501_DS1.pdf) - Best practices in planning guidelines and strategies are presented for use by transit agencies to im...

58. [Wrigley Field Gameday Traffic Plan | PDF - Scribd](https://www.scribd.com/document/155346029/Wrigley-Gameday-Traffic-Management-Plan) - The document provides a traffic management plan for Wrigley Field game days. It summarizes that Wrig...

59. [[PDF] Incentivizing Commuter Behavior | Ideas42](http://www.ideas42.org/wp-content/uploads/2017/11/Incentivizing-Commuter-Behavior.FINAL_.pdf) - On days with fare rebates, only 159 would use the six Red Line stations—a 17.5% decrease in particip...

60. [NJ Transit MetLife World Cup plans for MetLife Stadium trips](https://www.railway.supply/nj-transit-metlife-world-cup-plans-for-metlife-stadium-trips/) - To deliver the added capacity, NJ Transit plans to use 100 of its larger articulated buses, each des...

61. [TAKE THE TRAIN TO THE GAME AT METLIFE STADIUM - NJ Transit](https://www.njtransit.com/press-releases/take-train-game-metlife-stadium) - Meadowlands Rail Line service for football games begins three and a half hours before game time, run...

62. [The World Cup 2026 transportation plan around MetLife Stadium is ...](https://www.instagram.com/p/DWWU3qyjeep/) - NJ Transit is opening a new bus terminal at the stadium in May 2026 with buses running every 30 seco...

63. [How to Get to MetLife for the 2026 World Cup - Time Out](https://www.timeout.com/newyork/news/the-only-way-to-get-to-metlife-during-the-2026-world-cup-will-be-through-public-transit-031926) - NJ Department of Transportation officials say they're planning for “a bus every 30 seconds for four ...

64. [Why GO Transit is your game day MVP - The Globe and Mail](https://www.theglobeandmail.com/life/adv/article-why-go-transit-is-your-game-day-mvp/) - Rogers Centre is also a quick 10-minute jaunt away, with most of the walk indoors through the SkyWal...

65. [Blue Jays grand return home means busier Union Station - Metrolinx](https://www.metrolinx.com/en/discover/blue-jays-grand-return-home-means-busier-union-station) - The building is allowing 15,000 fans in the ballpark, per game, for the first 10 home games from Jul...

66. [RTD's planning efforts for large-scale events begin several weeks in ...](https://www.rtd-denver.com/community/news/rtd-s-planning-efforts-for-large-scale-events-begin-several-weeks-in-advance) - “We provided more than 23,000 people with connections to and from the stadium on Friday night alone,...

67. [High-Volume Events | RTD-Denver](https://www.rtd-denver.com/high-volume-events) - Learn how RTD prepares for events and deploys service · Discover agency resources to support custome...

68. [RTD rail, bus services to use before, after Broncos game on Sunday](https://www.yahoo.com/news/articles/rtd-rail-bus-services-broncos-165803756.html) - RTD said it expects there will be an increase in ridership due to the game — which kicks off at 2:05...

69. [Urban Bikeway Design Guide - NACTO](https://nacto.org/publication/urban-bikeway-design-guide/) - Developed for cities, by cities, the new guide is more than a permission slip for better street desi...

70. [About the Guide - NACTO](https://nacto.org/publication/urban-bikeway-design-guide/about-the-guide/) - The NACTO Urban Bikeway Design Guide provides design guidance for the development of bike facilities...

71. [Bike and Scooter Parking - NACTO](https://nacto.org/publication/urban-bikeway-design-guide/maintenance-and-operations/bike-and-scooter-parking/) - Bike and scooter parking includes short-term and long-term parking, as well as shared micromobility ...

72. [Understanding ADA Requirements for Event Spaces](https://www.nextdayaccess.ca/blog/understanding-ada-requirements-for-event-spaces/) - Event spaces must have accessible seating that's wide enough to accommodate wheelchairs. As stated i...

73. [[PDF] Automated Vehicles - Comprehensive Plan](https://www.transportation.gov/sites/dot.gov/files/2021-01/USDOT_AVCP.pdf) - AV 4.0 complements the guidance provided to private- and public-sector stakeholders in A. Vision for...

74. [U.S. DOT releases automated vehicle guideline update, AV 4.0](https://landline.media/u-s-dot-releases-automated-vehicle-guideline-update-av-4-0/) - The Trump administration has released an updated version of what are essentially voluntary guideline...

75. [New AV 4.0 Guidance on US Government Involvement ... - Akin Gump](https://www.akingump.com/en/insights/alerts/new-av-4-0-guidance-on-us-government-involvement-in-autonomous) - AV 4.0 details current US government efforts to research, develop and deploy AVs and related technol...

76. [[PDF] Impacts of Automated Vehicles on Highway Infrastructure](https://www.fhwa.dot.gov/publications/research/operations/21015/21015.pdf) - This study covers current concerns and thoughts on the potential impacts of automated vehicles (AVs)...

77. [Levels of Driving Automation - Update - CITM](https://citm.ca/levels-of-driving-automation-update/) - The J3016 standard defines six levels of driving automation, from SAE Level Zero (no automation) to ...

78. [SAE Levels of Driving Automation™ Refined for Clarity and ...](https://www.sae.org/news/blog/sae-levels-driving-automation-clarity-refinements) - With a taxonomy for SAE's six levels of driving automation, SAE J3016 defines the SAE Levels from Le...

79. [[PDF] SAE J3016_202104.pdf - UNECE Wiki](https://wiki.unece.org/download/attachments/128418539/SAE%20J3016_202104.pdf?api=v2) - ... Level 4 automated valet parking feature—in addition to allowing the user to operate the vehicle ...

80. [Blueprint for Autonomous Urbanism - NACTO](https://nacto.org/publication/blueprint-for-autonomous-urbanism/) - The Blueprint for Autonomous Urbanism, Second Edition, lays out a vision for how autonomous vehicles...

81. [Blueprint for Autonomous Urbanism | PDF | Public Transport - Scribd](https://www.scribd.com/document/509269959/NACTO-Blueprint-2nd-Edition-singlepages-small) - The document is the second edition of the Blueprint for Autonomous Urbanism published by the Nationa...

82. [[PDF] Blueprint for Autonomous Urbanism Second Edition - NACTO](https://nacto.org/wp-content/uploads/NACTO_Blueprint_2nd_Edition_Part3.pdf) - Real-time curbside management systems could allow vehicles to automatically reserve time slots a few...

83. [Pick-up and Drop-off at the Curb - Urban Robotics Foundation](https://www.urbanroboticsfoundation.org/post/pick-up-and-drop-off-at-the-curb) - This transformation requires preparing curbs that accommodate specific automated vehicle needs while...

84. [Curb Allocation and Pick-Up Drop-Off Aggregation for a Shared ...](https://www.osti.gov/pages/biblio/1960661) - The siting and density of pick-up and drop-off (PUDO) points for SAVs, much like bus stops, can be k...

85. [[PDF] University of Denver Autonomous Vehicle Shuttle](https://www.transportation.gov/sites/dot.gov/files/docs/policy-initiatives/automated-vehicles/351416/69-university-denver.pdf) - More than 32,000 people rode the shuttle during that pilot program, and, after their experience, 98 ...

86. [[PDF] Summary Evaluation of Low-Speed Automated Shuttle Pilots at NPS ...](https://www.nps.gov/subjects/transportation/upload/NPS-Automated-Shuttle-Pilots-Evaluation-Report.pdf) - The NPS identified Yellowstone National Park as a potential location for an automated shuttle pilot ...

87. [Autonomous Electric Shuttle Pilot Project | Transportation](https://www.fairfaxcounty.gov/transportation/Autonomous-Shuttle-Pilot) - The pilot project sought to test this driverless, public transportation option to evaluate its effec...

88. [Certification | Parksmart - GBCI](https://parksmart.gbci.org/certification) - Points are awarded to parking structures for forward-thinking and sustainable practices in three cat...

89. [Parksmart | Advancing sustainable parking structures](https://parksmart.gbci.org) - Parksmart is the world's only certification system designed to advance sustainable mobility through ...

90. [[PDF] GUIDE TO PARKSMART CERTIFICATION](https://www.parking.org/wp-content/uploads/2017/07/Guide-to-Parksmart-Certification.pdf) - Parksmart awards points to parking structures for sustainability achievements in garage management, ...

91. [The guiding principles of ParkSmart certification - RJC Engineers](https://www.rjc.ca/rjc-media/blog/parking-structure-design-operation-parksmart-certification.html) - ParkSmart, Canada's first voluntary certification system created to “advance sustainable mobility th...

92. [Parksmart Certification (formerly Green Garage… - Watry Design, Inc.](https://watrydesign.com/insights/green-garage-certification) - Per the USGBC, stand-alone parking structures are not eligible for LEED certification. However, when...

93. [Design Recommendations for Accessible Electric Vehicle Charging ...](https://www.access-board.gov/tad/ev/) - A technical assistance document to assist in the design and construction of electric vehicle (EV) ch...

94. [U.S. Access Board‚Äôs Proposed Rules for Accessible EV Charging ...](https://www.callaborlaw.com/blog/u.s-access-boards-proposed-rules-for-accessible-ev-charging-station-design) - The aisle must be a minimum of 60” inches wide, extend the full length of the EV charging space, and...

95. [[PDF] Energy Efficient Design of Low-Rise Residential Buildings - ASHRAE](https://www.ashrae.org/file%20library/technical%20resources/standards%20and%20guidelines/standards%20addenda/90_2_2018_n_20240723.pdf) - Parking garages and parking lots shall comply with Section 7.6.7. [ . . . ] 7.6.7 Plug-In Electric V...

96. [Accessible Electric Vehicle Parking Spaces and Charging Stations](https://www.swinter.com/accessible-electric-vehicle-parking/) - The parking space is a minimum of 132 inches in width; · The parking space is a minimum of 20 feet i...

97. [2025 IPMI Awards | Architectural Design & Facility Design](https://parking-mobility-magazine.org/2025-ipmi-awards/architectural-design-facility-design-stand-alone/) - Sustainable elements were central to the design and include a roof level prepped for future photovol...

98. [Exploring the Environmental Impact of Parking Lot Solar Canopies](https://www.emperysolar.com/News_Details/Exploring_the_Environmental_Impact_of_Parking_Lot_Solar_Canopies_A_Sustainable_Solution_for_Urban_Spaces.html) - Parking lot solar canopies provide renewable energy, reduce urban heat, manage stormwater effectivel...

99. [[PDF] Stormwater Best Management Practice, Permeable Pavements](https://www.epa.gov/system/files/documents/2021-11/bmp-permeable-pavements.pdf) - For example, designers can use permeable pavements in parking lot lanes or parking spaces to treat s...

100. [Experimental Permeable Pavement Parking Lot and Rain Garden ...](https://www.epa.gov/water-research/experimental-permeable-pavement-parking-lot-and-rain-garden-stormwater-management) - EPA researchers took this opportunity to design a parking area using low impact development (LID) co...

101. [[PDF] Performance Evaluation of Permeable Pavement and a Bioretention ...](https://sustainabletechnologies.ca/app/uploads/2013/01/PPBS-Final-2008.pdf) - A bioretention swale (or bioswale) is a stormwater best management practice that treats stormwater r...

102. [Design criteria for permeable pavement](https://stormwater.pca.state.mn.us/design_criteria_for_permeable_pavement) - Permeable pavements without underdrains infiltrate stormwater and should follow requirements for wel...

