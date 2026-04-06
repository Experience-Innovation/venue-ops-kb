---
title: "DR Prompt R-10 — Safety, Emergency Medicine, and Regulatory Standards for Mass Gathering Venues"
prompt_id: R-10
session: S19
created: 2026-04-06
target_domains:
  - safety-and-risk
gap_reference: "DELTA-014 (HIGH severity): 6 safety-and-risk concepts with structural traceability gaps. Single-source concepts (Lightning, MCI, Medical Staffing) need supplementary authoritative sources. Multi-claim regulatory concepts (Emergency Action Plans, Fire Watch, Heat Illness) need specific standard/regulation sources not in the existing corpus."
lifecycle: active
---

DR PROMPT R-10 — Safety, Emergency Medicine, and Regulatory Standards for Mass Gathering Venues

CONTEXT: The KB's safety-and-risk domain has 14 concept notes but the worst traceability score of any domain (93% gap rate, A-04 audit). Six concepts are HIGH-severity: Lightning-Severe-Weather (single source, 6 unsupported claims), Mass-Casualty-Incident-Planning (single source, START triage origin unverified), Medical-Staffing-Models (single source, "Saunders et al." not cited, 95.97% statistic unsourced), Emergency-Action-Plans (Alberta OHS Code not sourced), Fire-Watch-Protocols (5 specific thresholds without attribution), Heat-Illness-Protocols (Taylor Swift concert casualty claim unsourced). The existing source corpus has NFPA 101, CISA guides, and OSHA heat safety but lacks emergency medicine literature, FEMA safe room standards, and provincial OHS codes.

RESEARCH OBJECTIVE: Produce targeted supplementary reference on mass gathering emergency medicine, severe weather protocols, fire watch regulatory standards, and heat-related illness prevention for public assembly venues as of April 2026. This is a gap-fill prompt — not broad safety coverage (which exists), but specific sources for specific unsupported claims.

PRIMARY RESEARCH QUESTIONS:

1. MASS GATHERING MEDICINE — STAFFING RATIOS AND TRIAGE SYSTEMS: What is the evidence base for medical staffing ratios at mass gatherings? The "Saunders et al." staffing ratio framework — full citation, publication venue, year, specific ratios recommended. NIH StatPearls chapter on EMS mass gatherings — author, latest update, specific staffing formulas. START triage (Simple Triage and Rapid Treatment) — origin story (Newport Beach Fire Department and Hoag Hospital, 1983), original publication citation, current adoption statistics in North America. SALT triage (Sort, Assess, Lifesaving interventions, Treatment/Transport) — origin, how it differs from START, where it's mandated. Medical presentation rates at mass gatherings — the "0.5-2 per 1,000" benchmark and specific studies documenting it (Arbon, Zeitz, Milsten). The "95.97% mild presentations" statistic — which study produced this specific figure?

2. FEMA SAFE ROOM AND SHELTER STANDARDS: FEMA P-361 (Safe Rooms for Tornadoes and Hurricanes) — what does it require for assembly occupancies? Design wind speeds and impact criteria for safe rooms. ICC 500 (Standard for the Design and Construction of Storm Shelters) — relationship to FEMA P-361. Application to new construction vs. existing venues. Specific requirements for venues above occupant thresholds. Cost implications and case studies of safe room integration in venue projects.

3. FIRE WATCH REGULATORY STANDARDS AND THRESHOLDS: What specific codes establish fire watch trigger thresholds? NFPA 101 (Life Safety Code) and NFPA 1 (Fire Code) — sections addressing fire watch requirements when fire protection systems are impaired. "Fire alarm out of service for more than 4 hours" trigger — which code section establishes this? "Sprinkler system impaired for more than 10 hours" trigger — which code section? IFC (International Fire Code) fire watch provisions — how they differ from NFPA. NFPA 1126 (Use of Pyrotechnics Before a Proximate Audience) — mortar setback distances (25 feet concussion mortar, 15 feet minimum audience separation or 2x fallout radius) — specific section references. Fireworks Operator Certificate (FOC) under Canada's Explosives Act — requirements, issuing authority, renewal.

4. PROVINCIAL AND STATE OCCUPATIONAL HEALTH AND SAFETY CODES: Alberta OHS Code Part 7 (Emergency Preparedness and Response) — specific requirements for emergency response plans in assembly occupancies. How do other Canadian provincial OHS codes address venue emergency planning? Ontario OHSA and its regulations for assembly workplaces. BC WorkSafeBC requirements. What US state-level codes add requirements beyond federal OSHA for venue emergency planning? California, New York, Nevada as examples of enhanced requirements.

5. HEAT-RELATED ILLNESS IN OUTDOOR EVENTS: OSHA's 2025 proposed heat safety rule — specific WBGT (Wet Bulb Globe Temperature) thresholds (80F initial trigger, 90F high-heat trigger). What is the current regulatory status of this rule? Historical heat-related incidents at major events — Taylor Swift Eras Tour in Rio de Janeiro (November 2023, death of Ana Clara Benevides Machado, age 23) — official reporting sources (Brazilian government, event operator statements, news agencies with primary sourcing). Other documented heat-related mass gathering incidents at venues. NOAA/NWS heat advisory thresholds relevant to outdoor venue operations. Heat acclimatization and prevention protocols specific to venue staff and attendees.

6. LIGHTNING DETECTION AND VENUE PROTOCOLS: NWS lightning safety guidelines for outdoor venues — the three-radius monitoring system (15 miles monitoring, 12 miles preparation, 8 miles mandatory evacuation). The "30-30 rule" and "30-minute rule" for resumption of activities after last detected strike. Commercial lightning detection providers and systems used by venues (Perry Weather, DTN, Earth Networks, Vaisala/NLDN). NWS StormReady recognition program for venues — requirements and process. NFPA 780 (Standard for the Installation of Lightning Protection Systems) — application to venue structures.

7. NFPA 1026 — INCIDENT COMMANDER COMPETENCY: NFPA 1026 (Standard for Incident Management Personnel Professional Qualifications) — 2024 edition. What competency requirements does it establish for Incident Commanders at assembly occupancies? How does it relate to FEMA ICS training (IS-100, IS-200, IS-700)? Adoption status — which jurisdictions mandate NFPA 1026 compliance for venue operators?

SOURCE QUALITY:
- PRIORITY 1: Primary regulatory sources — NFPA codes (101, 1, 1126, 780, 1026) with specific section references, FEMA publications (P-361), OSHA proposed rules (Federal Register citations), Canadian OHS legislation (Alberta OHS Code, Ontario OHSA)
- PRIORITY 2: Emergency medicine literature — peer-reviewed journals (Prehospital Emergency Care, Annals of Emergency Medicine, Journal of Emergency Medical Services), NIH StatPearls chapters with author/date
- PRIORITY 3: Weather safety authorities — NOAA/NWS official guidance documents, commercial lightning detection provider technical specifications
- PRIORITY 4: Incident reporting — official government/coroner reports on heat-related event deaths, OSHA incident investigation reports, Canadian workplace safety investigation reports
- AVOID: General "event safety tips" articles. Vendor marketing for safety products. News articles without primary source citations for specific claims. Social media accounts of incidents.

OUTPUT STRUCTURE:
- Mass gathering medical staffing evidence table (study, year, ratios, context, citation)
- START/SALT triage comparison (origin, methodology, adoption, citation)
- FEMA P-361 / ICC 500 requirements summary for assembly occupancies
- Fire watch trigger threshold reference (code section, threshold, applicability)
- Provincial/state OHS code comparison for venue emergency planning
- Heat-related venue incident catalog (event, date, outcome, official source)
- Lightning protocol reference (NWS thresholds, detection systems, resumption criteria)
- NFPA 1026 competency requirements summary for venue Incident Commanders

KNOWN CONTEXT: The KB already covers: Incident-Command-System (ICS structure, FEMA training courses — 3 sources), Life-Safety-Evaluation (NFPA 101 evaluation requirements — 2 sources), Emergency-Action-Plans (3 sources but missing Alberta OHS), AED-Programs (2 sources), Business-Continuity-Planning (CISA guide — 1 source), Tabletop-Exercises (FEMA VTTX — 2 sources), GBAC-STAR-Accreditation (2 sources). This prompt targets ONLY the specific unsupported claims identified in DELTA-014 — not broad safety coverage, not security operations, not crowd management (separate domains).

CONSTRAINTS: This is a targeted gap-fill, not a comprehensive safety research prompt. Each research question maps to a specific unsupported claim in an existing concept note. Citations must include specific code section numbers, publication dates, and author names where applicable. For incident reports (Taylor Swift concert, other heat events), use official sources only — coroner reports, government investigations, or operator/venue official statements. Do not cite social media or fan accounts as sources for incident claims. Canadian OHS codes should specify the province and specific regulation/section, not just "Canadian law."
