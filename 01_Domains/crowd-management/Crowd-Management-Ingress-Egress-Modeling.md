---
title: "Ingress/Egress Modeling and Simulation"
note_type: concept
status: draft
created: 2026-04-06
updated: 2026-04-06
domain: crowd-management
description: "Computational simulation tools and methodologies for modeling pedestrian flow, predicting bottlenecks, and optimizing ingress/egress design in public assembly venues using agent-based and fluid dynamics approaches."
tags:
  - simulation
  - modeling
  - egress
  - ingress
  - pedestrian-flow
confidence: high
venue_types:
  - all
vef_alignment:
  - ai-and-digital-transformation
  - systems-processes-clarity-of-roles
sources:
  - "[[Source-0421-Helbing-Crowd-Turbulence]]"
  - "[[Source-0422-Keith-Still-Crowd-Science]]"
research_batch: dr-d2-r14-crowd-management
extraction_model: claude-opus-4-6
child_of: "[[Domain-Crowd-Management]]"
related_to:
  - "[[Crowd-Management-Fruins-Level-of-Service]]"
  - "[[Technology-And-Digital-IoT-Smart-Building]]"
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# Ingress/Egress Modeling and Simulation

Ingress/egress modeling uses computational simulation to predict pedestrian flow patterns, identify bottlenecks, and optimize venue design before construction or event execution. Two primary modeling paradigms are used: agent-based microsimulation (each pedestrian modeled as an autonomous agent) and fluid dynamics macrosimulation (crowd treated as a continuous flow) [[Source-0421-Helbing-Crowd-Turbulence]].

## Agent-Based Microsimulation

Agent-based models assign each simulated pedestrian individual parameters (walking speed, body size, destination, reaction time) and behavioral rules (obstacle avoidance, following behavior, social forces). The Social Force Model developed by Helbing uses attractive and repulsive forces between pedestrians and between pedestrians and obstacles to generate emergent crowd behavior including lane formation, oscillation at bottlenecks, and the transition to turbulence at extreme densities [[Source-0421-Helbing-Crowd-Turbulence]].

## Simulation Platforms

Commercial platforms include Oasys MassMotion (used for transportation hubs and large venue design), Pathfinder (Thunderhead Engineering, NFPA-validated for egress analysis), STEPS (Mott MacDonald), and Legion SpacePlan. These tools import architectural models, define population parameters, and run thousands of simulated scenarios to identify the statistical distribution of evacuation times and density hotspots [[Source-0422-Keith-Still-Crowd-Science]].

## DIM-ICE Framework Integration

Prof. Keith Still's DIM-ICE risk model provides the analytical framework connecting simulation outputs to operational planning: Design capacity validated through simulation, Information strategy informing agent behavior assumptions, Management interventions tested as scenario variables. The RAMP Analysis (Routes, Areas, Movement, People/profile) complements simulation by structuring the physical assessment that defines simulation inputs [[Source-0422-Keith-Still-Crowd-Science]].

## Practical Application

Simulation is most valuable during venue design (testing gate configurations, concourse widths, stairwell capacity), event planning (testing gate opening sequences, phased ingress strategies), and post-incident analysis (reconstructing crowd dynamics from surveillance footage). Density thresholds in simulation should be calibrated to Fruin's LOS framework with intervention triggers set at 4-5 persons/m² — well before the critical 6-7 persons/m² where turbulence onset occurs [[Source-0421-Helbing-Crowd-Turbulence]].
