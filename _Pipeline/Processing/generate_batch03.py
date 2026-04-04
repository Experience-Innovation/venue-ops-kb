#!/usr/bin/env python3
"""Generate batch-03 source notes (Source-0061 through Source-0090) and 23 concept notes."""

import os

BASE = "/Users/bubblegumpshrimpco/Library/CloudStorage/GoogleDrive-alex@experienceinnovation.consulting/Shared drives/Venue Excellence Podcast/Venue Excellence Podcast/venue-ops-kb/.claude/worktrees/session-13-batch-processing"
SOURCES_DIR = os.path.join(BASE, "06_Sources")
DOMAINS_DIR = os.path.join(BASE, "01_Domains")

created_count = 0

# =============================================================================
# SOURCE NOTES
# =============================================================================

sources = [
    {
        "num": "0061",
        "slug": "FDA-Food-Code-2022",
        "title": "FDA Food Code 2022",
        "source_type": "regulatory-document",
        "url": "https://www.fda.gov/food/fda-food-code/food-code-2022",
        "description": "The FDA Food Code is a model code published by the U.S. Food and Drug Administration that provides a scientifically sound technical and legal basis for regulating the retail and food service industries. The 2022 edition covers food safety principles, HACCP, temperature controls, and employee health standards.",
        "domains": ["food-and-beverage", "legal-compliance-and-licensing"],
    },
    {
        "num": "0062",
        "slug": "FSMA-204-Traceability-Rule",
        "title": "FSMA Section 204 Food Traceability Final Rule",
        "source_type": "regulatory-document",
        "url": "https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods",
        "description": "The FSMA Section 204 final rule establishes additional traceability recordkeeping requirements for persons who manufacture, process, pack, or hold foods on the Food Traceability List. Requires tracking Key Data Elements at Critical Tracking Events with a compliance deadline of January 20, 2026.",
        "domains": ["supply-chain-and-procurement", "food-and-beverage", "legal-compliance-and-licensing"],
    },
    {
        "num": "0063",
        "slug": "SFCR-Canada-Safe-Food-Regulations",
        "title": "Safe Food for Canadians Regulations (SFCR)",
        "source_type": "regulatory-document",
        "url": "https://laws-lois.justice.gc.ca/eng/regulations/SOR-2018-108/",
        "description": "The Safe Food for Canadians Regulations (SFCR) consolidate multiple Canadian food commodity regulations into a single framework. They establish requirements for licensing, preventive controls (including Preventive Control Plans), and traceability across the Canadian food supply chain.",
        "domains": ["food-and-beverage", "supply-chain-and-procurement", "legal-compliance-and-licensing"],
    },
    {
        "num": "0064",
        "slug": "ServSafe-Food-Safety-Certification",
        "title": "ServSafe Food Safety Training and Certification",
        "source_type": "trade-association",
        "url": "https://www.servsafe.com/",
        "description": "ServSafe is the food and beverage safety training and certification program administered by the National Restaurant Association. It is the most widely recognized food safety certification in the United States, covering food handler, manager, and allergen training programs.",
        "domains": ["food-and-beverage", "people-and-culture"],
    },
    {
        "num": "0065",
        "slug": "FDA-HACCP-Principles-Guidelines",
        "title": "HACCP Principles and Application Guidelines",
        "source_type": "regulatory-document",
        "url": "https://www.fda.gov/food/hazard-analysis-critical-control-point-haccp/haccp-principles-application-guidelines",
        "description": "The FDA's comprehensive guide to the seven HACCP principles: hazard analysis, critical control point identification, critical limit establishment, monitoring procedures, corrective actions, verification procedures, and record-keeping. Foundational framework for systematic food safety management.",
        "domains": ["food-and-beverage", "safety-and-risk"],
    },
    {
        "num": "0066",
        "slug": "Aramark-Sports-Entertainment",
        "title": "Aramark Sports and Entertainment Division",
        "source_type": "vendor-documentation",
        "url": "https://www.aramark.com/industries/sports-entertainment",
        "description": "Aramark's Sports and Entertainment division provides food service, hospitality, and facilities management for stadiums, arenas, convention centres, and entertainment venues across North America. One of the six major contract catering operators in the venue sector.",
        "domains": ["food-and-beverage", "supply-chain-and-procurement"],
    },
    {
        "num": "0067",
        "slug": "Delaware-North-Hospitality",
        "title": "Delaware North Hospitality and Food Service",
        "source_type": "vendor-documentation",
        "url": "https://www.delawarenorth.com/",
        "description": "Delaware North is a global hospitality and food service company operating at sports venues, entertainment destinations, airports, and national parks. A privately held company and one of the six major contract food service operators in the North American venue market.",
        "domains": ["food-and-beverage", "supply-chain-and-procurement"],
    },
    {
        "num": "0068",
        "slug": "Sodexo-Live-Venue-Hospitality",
        "title": "Sodexo Live! Venue Hospitality",
        "source_type": "vendor-documentation",
        "url": "https://www.sodexolive.com/",
        "description": "Sodexo Live! (formerly Sodexo Sports and Leisure) is the live events and venue hospitality division of Sodexo Group. Provides food and beverage, premium hospitality, and guest services at stadiums, arenas, convention centres, and cultural venues worldwide.",
        "domains": ["food-and-beverage", "guest-experience"],
    },
    {
        "num": "0069",
        "slug": "Levy-Restaurants-Compass-Group",
        "title": "Levy Restaurants (Compass Group)",
        "source_type": "vendor-documentation",
        "url": "https://www.levyrestaurants.com/",
        "description": "Levy is the food and beverage division of Compass Group focused on sports, entertainment, and convention venues. Known for chef-driven dining programs and pioneering the premium food service model in major venues across North America.",
        "domains": ["food-and-beverage", "premium-and-vip"],
    },
    {
        "num": "0070",
        "slug": "OVG-Hospitality",
        "title": "Oak View Group Hospitality",
        "source_type": "vendor-documentation",
        "url": "https://www.oakviewgroup.com/hospitality",
        "description": "OVG Hospitality is the food and beverage arm of Oak View Group, a venue development and management company. Provides food service and premium hospitality operations at arenas, stadiums, and convention centres with a focus on locally sourced and chef-driven programs.",
        "domains": ["food-and-beverage", "commercial-and-revenue"],
    },
    {
        "num": "0071",
        "slug": "Legends-Hospitality",
        "title": "Legends Hospitality",
        "source_type": "vendor-documentation",
        "url": "https://www.legends.net/hospitality",
        "description": "Legends is a hospitality and entertainment company providing food and beverage, merchandise, and technology solutions for sports and entertainment venues. Co-founded by the ownership groups of the Dallas Cowboys and New York Yankees.",
        "domains": ["food-and-beverage", "commercial-and-revenue"],
    },
    {
        "num": "0072",
        "slug": "NAFEM-Foodservice-Equipment",
        "title": "NAFEM — North American Association of Food Equipment Manufacturers",
        "source_type": "trade-association",
        "url": "https://www.nafem.org/",
        "description": "NAFEM is the trade association representing food equipment manufacturers in the United States and Canada. Publishes industry data on commercial kitchen equipment, hosts the NAFEM Show, and provides resources on equipment specifications, energy efficiency, and food service facility design.",
        "domains": ["food-and-beverage", "facilities-and-building-systems"],
    },
    {
        "num": "0073",
        "slug": "IFMA-Foodservice-Manufacturers",
        "title": "IFMA — International Foodservice Manufacturers Association",
        "source_type": "trade-association",
        "url": "https://www.ifmaworld.com/",
        "description": "IFMA represents food and beverage manufacturers serving the away-from-home foodservice market. Publishes industry research, operator trends, and supply chain intelligence relevant to commercial foodservice including venue and institutional segments.",
        "domains": ["food-and-beverage", "supply-chain-and-procurement"],
    },
    {
        "num": "0074",
        "slug": "ACF-American-Culinary-Federation",
        "title": "American Culinary Federation",
        "source_type": "trade-association",
        "url": "https://www.acfchefs.org/",
        "description": "The American Culinary Federation is the largest professional chefs organization in North America. Administers a 13-level certification framework from Certified Fundamental Cook through Certified Master Chef, accredits culinary programs, and promotes professional standards in the culinary industry.",
        "domains": ["food-and-beverage", "people-and-culture"],
    },
    {
        "num": "0075",
        "slug": "GCCA-Global-Cold-Chain-Alliance",
        "title": "Global Cold Chain Alliance",
        "source_type": "trade-association",
        "url": "https://www.gcca.org/",
        "description": "The Global Cold Chain Alliance is the industry organization for companies involved in temperature-controlled logistics, including warehousing, transportation, and cold chain technology. Publishes cold chain best practices, certification programs, and compliance guidance.",
        "domains": ["logistics-and-warehouse", "supply-chain-and-procurement"],
    },
    {
        "num": "0076",
        "slug": "GFSI-Global-Food-Safety-Initiative",
        "title": "Global Food Safety Initiative (GFSI)",
        "source_type": "trade-association",
        "url": "https://mygfsi.com/",
        "description": "GFSI is a private sector coalition managed by The Consumer Goods Forum that benchmarks food safety management schemes worldwide. GFSI-recognized schemes include SQF, BRC, FSSC 22000, and IFS, providing a common framework for supplier qualification and food safety audit standards.",
        "domains": ["supply-chain-and-procurement", "food-and-beverage"],
    },
    {
        "num": "0077",
        "slug": "SQF-Institute-Food-Safety",
        "title": "SQF Institute — Safe Quality Food Program",
        "source_type": "trade-association",
        "url": "https://www.sqfi.com/",
        "description": "The SQF Institute administers the Safe Quality Food certification program, a GFSI-benchmarked food safety and quality management system. SQF certification is widely used by food manufacturers, distributors, and processors as evidence of food safety compliance in supply chain qualification.",
        "domains": ["supply-chain-and-procurement", "food-and-beverage"],
    },
    {
        "num": "0078",
        "slug": "Green-Restaurant-Association",
        "title": "Green Restaurant Association",
        "source_type": "trade-association",
        "url": "https://www.dinegreen.com/",
        "description": "The Green Restaurant Association provides a certification framework for environmentally sustainable restaurant and food service operations. Evaluates across categories including energy, water, waste, food, chemicals, disposables, and building materials.",
        "domains": ["food-and-beverage", "sustainability-and-environmental"],
    },
    {
        "num": "0079",
        "slug": "FDA-FALCPA-FASTER-Act-Allergens",
        "title": "FDA Food Allergen Labeling — FALCPA and FASTER Act",
        "source_type": "regulatory-document",
        "url": "https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies",
        "description": "FDA resources on food allergen labeling requirements under the Food Allergen Labeling and Consumer Protection Act (FALCPA, 2004) and the FASTER Act (2021), which added sesame as the ninth major allergen. Covers labeling, cross-contact advisory statements, and food service allergen management.",
        "domains": ["food-and-beverage", "legal-compliance-and-licensing"],
    },
    {
        "num": "0080",
        "slug": "CFIA-Allergen-Management",
        "title": "CFIA Priority Allergen Labelling and Management",
        "source_type": "regulatory-document",
        "url": "https://inspection.canada.ca/en/food-safety-industry/food-labelling/allergen-labelling",
        "description": "Canadian Food Inspection Agency guidance on Canada's 14 priority food allergens (including mustard, sulphites, and others beyond the US list), precautionary labelling requirements, and allergen management controls for food service establishments under Canadian food safety regulations.",
        "domains": ["food-and-beverage", "legal-compliance-and-licensing"],
    },
    {
        "num": "0081",
        "slug": "Menus-of-Change-CIA",
        "title": "Menus of Change — Culinary Institute of America",
        "source_type": "industry-publication",
        "url": "https://www.menusofchange.org/",
        "description": "Menus of Change is a research initiative by the Culinary Institute of America and Harvard T.H. Chan School of Public Health focused on plant-forward, sustainable menu strategies for food service operations. Publishes annual principles of healthy, sustainable menus for institutional and commercial food service.",
        "domains": ["food-and-beverage", "sustainability-and-environmental"],
    },
    {
        "num": "0082",
        "slug": "Second-Harvest-Food-Rescue",
        "title": "Second Harvest — Food Rescue and Waste Reduction",
        "source_type": "trade-association",
        "url": "https://www.secondharvest.ca/",
        "description": "Second Harvest is Canada's largest food rescue organization, connecting surplus food from commercial and institutional food service operations with community organizations. Publishes research on food waste reduction in commercial food service, including venue and event catering operations.",
        "domains": ["food-and-beverage", "sustainability-and-environmental"],
    },
    {
        "num": "0083",
        "slug": "DOL-FLSA-Tip-Regulations",
        "title": "DOL FLSA Tip Regulations and Guidance",
        "source_type": "regulatory-document",
        "url": "https://www.dol.gov/agencies/whd/flsa/tips",
        "description": "U.S. Department of Labor guidance on the Fair Labor Standards Act tip credit provisions, tip pooling rules, service charge distribution, and minimum wage requirements for tipped employees. Directly applicable to venue food and beverage service operations.",
        "domains": ["people-and-culture", "legal-compliance-and-licensing", "food-and-beverage"],
    },
    {
        "num": "0084",
        "slug": "UNITE-HERE-Union",
        "title": "UNITE HERE — Hospitality Workers Union",
        "source_type": "trade-association",
        "url": "https://unitehere.org/",
        "description": "UNITE HERE is the labor union representing workers in the hotel, gaming, food service, manufacturing, textile, distribution, laundry, and airport industries across North America. Represents food and beverage workers at many major venues and convention centres through collective bargaining agreements.",
        "domains": ["people-and-culture", "food-and-beverage"],
    },
    {
        "num": "0085",
        "slug": "FoodLogiQ-Traceability-Platform",
        "title": "FoodLogiQ Traceability and Compliance Platform",
        "source_type": "vendor-documentation",
        "url": "https://www.foodlogiq.com/",
        "description": "FoodLogiQ (now part of Trustwell) provides a cloud-based food traceability, supplier management, and regulatory compliance platform. Used by food service operators and their suppliers for FSMA 204 traceability compliance, supplier qualification, and recall management.",
        "domains": ["supply-chain-and-procurement", "technology-and-digital"],
    },
    {
        "num": "0086",
        "slug": "BlueCart-Procurement-Platform",
        "title": "BlueCart Procurement Platform",
        "source_type": "vendor-documentation",
        "url": "https://www.bluecart.com/",
        "description": "BlueCart is a procurement and order management platform for the food service industry, enabling digital ordering between buyers and suppliers. Provides tools for inventory management, order tracking, and supplier communication used by restaurants and food service operations.",
        "domains": ["supply-chain-and-procurement", "technology-and-digital"],
    },
    {
        "num": "0087",
        "slug": "Oracle-Simphony-POS",
        "title": "Oracle MICROS Simphony POS System",
        "source_type": "vendor-documentation",
        "url": "https://www.oracle.com/food-beverage/restaurant-pos-systems/",
        "description": "Oracle MICROS Simphony is an enterprise cloud POS platform designed for food and beverage operations, widely deployed in large-scale venues including stadiums, arenas, and convention centres. Supports multi-location management, mobile ordering, kitchen display integration, and real-time analytics.",
        "domains": ["food-and-beverage", "technology-and-digital"],
    },
    {
        "num": "0088",
        "slug": "Toast-POS-Platform",
        "title": "Toast POS and Restaurant Management Platform",
        "source_type": "vendor-documentation",
        "url": "https://pos.toasttab.com/",
        "description": "Toast is a cloud-based restaurant management and POS platform serving food and beverage operations. Provides POS, online ordering, kitchen display systems, inventory management, and workforce management tools used across restaurant and food service operations.",
        "domains": ["food-and-beverage", "technology-and-digital"],
    },
    {
        "num": "0089",
        "slug": "Winnow-AI-Food-Waste",
        "title": "Winnow Solutions — AI Food Waste Tracking",
        "source_type": "vendor-documentation",
        "url": "https://www.winnowsolutions.com/",
        "description": "Winnow provides AI-powered food waste tracking and reduction technology for commercial kitchens. Uses computer vision and machine learning to identify, measure, and categorize food waste, enabling food service operations to reduce waste by up to 50% through data-driven production adjustments.",
        "domains": ["food-and-beverage", "sustainability-and-environmental", "technology-and-digital"],
    },
    {
        "num": "0090",
        "slug": "Leanpath-Food-Waste-Prevention",
        "title": "Leanpath Food Waste Prevention Platform",
        "source_type": "vendor-documentation",
        "url": "https://www.leanpath.com/",
        "description": "Leanpath provides food waste tracking and prevention technology for commercial food service operations. Combines hardware (scales, cameras) with analytics software to measure pre-consumer food waste, identify waste patterns, and drive behavioral change in kitchen operations.",
        "domains": ["food-and-beverage", "sustainability-and-environmental", "technology-and-digital"],
    },
]

# =============================================================================
# CONCEPT NOTES
# =============================================================================

concepts = [
    {
        "filename": "Food-And-Beverage-Contract-Catering-Market.md",
        "domain_dir": "food-and-beverage",
        "title": "Contract Catering Market Structure in Venue Operations",
        "domain": "food-and-beverage",
        "description": "The six major outsourced food and beverage operators dominating venue hospitality (Aramark, Delaware North, Sodexo Live!, Levy/Compass Group, OVG Hospitality, and Legends), their market positioning, commission-based contract models, and competitive dynamics.",
        "venue_types": ["convention-centre", "arena", "stadium", "amphitheatre", "fairground-exhibition"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "strategy-and-effective-change-leadership", "guest-experience"],
        "confidence": "high",
        "sources": [
            "[[Source-0066-Aramark-Sports-Entertainment]]",
            "[[Source-0067-Delaware-North-Hospitality]]",
            "[[Source-0068-Sodexo-Live-Venue-Hospitality]]",
            "[[Source-0069-Levy-Restaurants-Compass-Group]]",
            "[[Source-0070-OVG-Hospitality]]",
            "[[Source-0071-Legends-Hospitality]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-In-House-vs-Contracted-Decision]]",
            "[[Food-And-Beverage-Premium-Dining-Suite-Service]]",
        ],
        "delivery_model": ["outsourced"],
        "body": """## Major Contract Operators

The North American venue food and beverage market is dominated by six major contract catering operators:

1. **Aramark Sports and Entertainment** — One of the largest food service companies globally, operating across stadiums, arenas, convention centres, and entertainment venues. Provides integrated food service, hospitality management, and facilities services.

2. **Delaware North** — A privately held global hospitality company with venue food service operations spanning sports, entertainment, airports, and national and state parks.

3. **Sodexo Live!** — The live events division of Sodexo Group (formerly Sodexo Sports and Leisure), operating food and beverage and premium hospitality at venues worldwide.

4. **Levy (Compass Group)** — Pioneer of chef-driven venue dining, known for elevating stadium and arena food quality. Operates as the venue food service arm of Compass Group.

5. **OVG Hospitality** — The food and beverage division of Oak View Group, combining venue development expertise with hospitality operations focused on locally sourced programs.

6. **Legends** — Co-founded by Dallas Cowboys and New York Yankees ownership, providing food service, merchandise, and technology solutions at premier venues.

## Contract Models

Venue-operator contracts typically follow commission-based structures where the venue receives a percentage of gross food and beverage revenue. Contract terms commonly range from 5 to 10 years, with capital investment requirements, minimum revenue guarantees, and performance benchmarks tied to guest satisfaction scores and per-capita spending targets.

## Market Dynamics

Competition among these operators centers on culinary program quality, capital investment commitments, technology integration (mobile ordering, cashless payment), and the ability to deliver premium dining experiences alongside high-volume concession operations. The trend toward locally sourced, chef-driven menus has raised the bar across the sector.""",
    },
    {
        "filename": "Food-And-Beverage-In-House-vs-Contracted-Decision.md",
        "domain_dir": "food-and-beverage",
        "title": "In-House vs. Contracted F&B Operations Decision",
        "domain": "food-and-beverage",
        "description": "The strategic make-vs-buy decision for venue food and beverage operations, evaluating factors such as capital requirements, operational control, revenue share models, and hybrid approaches.",
        "venue_types": ["convention-centre", "arena", "stadium", "performing-arts-centre", "fairground-exhibition"],
        "vef_alignment": ["strategy-and-effective-change-leadership", "operational-efficiency-productivity-creativity"],
        "confidence": "high",
        "sources": [
            "[[Source-0066-Aramark-Sports-Entertainment]]",
            "[[Source-0069-Levy-Restaurants-Compass-Group]]",
            "[[Source-0070-OVG-Hospitality]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-Contract-Catering-Market]]",
            "[[Food-And-Beverage-Concessions-Management]]",
        ],
        "delivery_model": ["in-house", "outsourced", "hybrid"],
        "body": """## Decision Framework

The in-house versus contracted food and beverage decision is one of the most consequential operational choices a venue makes. It affects revenue retention, guest experience quality, operational flexibility, capital requirements, and labor relations.

### Factors Favoring In-House Operations
- Full revenue retention (no commission split with a third-party operator)
- Direct control over menu design, pricing, quality standards, and guest experience
- Ability to build a distinctive culinary identity aligned with the venue brand
- Greater flexibility to adjust operations for different event types
- Direct relationship with food and beverage staff

### Factors Favoring Contracted Operations
- Access to operator capital investment for kitchen buildouts and equipment
- Leverage of operator purchasing power through group purchasing organizations (GPOs)
- Reduced operational risk — the operator absorbs labor management complexity
- Access to established supply chains, training programs, and technology platforms
- Industry expertise and benchmarking data from multi-venue portfolios

## Hybrid Models

Many venues adopt hybrid approaches, such as contracting concession operations while running premium dining in-house, or managing catering sales internally while outsourcing production. These models attempt to balance revenue retention with operational efficiency.

## Financial Considerations

The commission model typically sees venues receiving 30-50% of gross F&B revenue from contracted operators, compared to retaining 100% of revenue (but absorbing 100% of costs) with in-house operations. The break-even analysis depends heavily on venue size, event frequency, labor market conditions, and capital investment capacity.""",
    },
    {
        "filename": "Food-And-Beverage-Commissary-Hub-Spoke-Kitchen.md",
        "domain_dir": "food-and-beverage",
        "title": "Commissary and Hub-and-Spoke Kitchen Operations",
        "domain": "food-and-beverage",
        "description": "Centralized production kitchen (commissary) models and hub-and-spoke distribution systems used in high-volume venue catering to achieve consistency, efficiency, and food safety compliance across multiple service points.",
        "venue_types": ["convention-centre", "stadium", "arena", "fairground-exhibition", "theme-park"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "medium",
        "sources": [
            "[[Source-0066-Aramark-Sports-Entertainment]]",
            "[[Source-0065-FDA-HACCP-Principles-Guidelines]]",
            "[[Source-0072-NAFEM-Foodservice-Equipment]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-Concessions-Management]]",
            "[[Logistics-And-Warehouse-Inventory-Storage]]",
        ],
        "body": """## Commissary Kitchen Model

A commissary kitchen is a centralized food production facility that prepares food items for distribution to multiple service points within a venue or across a venue portfolio. This model is standard practice for large convention centres, stadiums, and fairgrounds where dozens of concession stands, banquet halls, and premium dining areas must be served simultaneously.

### Advantages
- Centralized quality control and HACCP compliance monitoring
- Efficient use of specialized equipment and skilled labor
- Consistent product quality across all service points
- Reduced equipment duplication — satellite locations need only finishing and holding equipment
- Simplified inventory management and receiving operations

### Design Considerations
- Adequate cold and dry storage capacity to support peak event production volumes
- Efficient workflow layout following food safety principles (clean-to-dirty flow separation)
- Loading dock access for receiving and internal distribution logistics
- Blast chilling and hot-holding capacity matched to production scale

## Hub-and-Spoke Distribution

In the hub-and-spoke model, the central commissary (hub) produces and portions food items that are transported to satellite service points (spokes) using insulated transport equipment, hot carts, and cold chain-compliant containers. Timing and temperature control during transport are critical food safety requirements.

## Scalability

The commissary model scales with venue size and event complexity. Convention centres with 500,000+ square feet of event space may operate multiple commissary kitchens, while stadiums typically centralize production in a single main kitchen with distributed finishing stations.""",
    },
    {
        "filename": "Food-And-Beverage-Concessions-Management.md",
        "domain_dir": "food-and-beverage",
        "title": "Concession Operations Management",
        "domain": "food-and-beverage",
        "description": "Walk-up concession stand operations in venues, including speed-of-service optimization, menu engineering for throughput, staffing models, and the balance between food quality and service velocity during peak demand.",
        "venue_types": ["arena", "stadium", "amphitheatre", "fairground-exhibition", "theme-park"],
        "vef_alignment": ["guest-experience", "operational-efficiency-productivity-creativity"],
        "confidence": "high",
        "sources": [
            "[[Source-0066-Aramark-Sports-Entertainment]]",
            "[[Source-0069-Levy-Restaurants-Compass-Group]]",
            "[[Source-0087-Oracle-Simphony-POS]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-Menu-Engineering-Dietary-Accommodation]]",
            "[[Food-And-Beverage-Technology-Stack]]",
            "[[Food-And-Beverage-Contract-Catering-Market]]",
        ],
        "body": """## Operations Overview

Concession operations are the highest-volume, fastest-paced food service channel in venue operations. During peak periods (halftime, intermission, pre-show), concession stands must serve thousands of guests within compressed time windows, making speed of service a primary operational metric alongside food quality and safety.

## Speed-of-Service Optimization

Key strategies for maximizing concession throughput include:
- **Menu simplification** — Limiting menu items to those that can be served in under 60 seconds per transaction
- **Pre-staging and batch production** — Preparing grab-and-go items in advance of peak periods
- **Cashless payment systems** — Reducing transaction time by eliminating cash handling
- **Mobile ordering** — Allowing guests to order ahead and pick up at designated windows, reducing queue length
- **Express lanes** — Dedicated service points for high-frequency items (beer, water, hot dogs)

## Menu Optimization

Concession menus are engineered for a balance of margin contribution, preparation speed, and guest appeal. The traditional model of hot dogs, nachos, and beer is evolving toward diverse offerings including local food concepts, premium options, and dietary-inclusive items, though speed-of-service remains the governing constraint.

## Staffing Models

Concession staffing relies heavily on event-day labor, including part-time employees, temporary workers, and in some jurisdictions, volunteer organizations operating stands as fundraisers. Staff training focuses on speed, accuracy, food safety basics, responsible alcohol service, and point-of-sale system operation.""",
    },
    {
        "filename": "Food-And-Beverage-Premium-Dining-Suite-Service.md",
        "domain_dir": "food-and-beverage",
        "title": "Premium Dining and Suite Service Programs",
        "domain": "food-and-beverage",
        "description": "Club-level dining, luxury suite catering, chef's table experiences, and premium food and beverage programs that drive high per-capita spending and differentiate the venue's hospitality offering.",
        "venue_types": ["arena", "stadium", "convention-centre", "performing-arts-centre"],
        "vef_alignment": ["guest-experience", "operational-efficiency-productivity-creativity", "innovation-and-continuous-improvement"],
        "confidence": "high",
        "sources": [
            "[[Source-0069-Levy-Restaurants-Compass-Group]]",
            "[[Source-0070-OVG-Hospitality]]",
            "[[Source-0071-Legends-Hospitality]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-Contract-Catering-Market]]",
            "[[Food-And-Beverage-Craft-Local-Beverage]]",
            "[[Food-And-Beverage-Menu-Engineering-Dietary-Accommodation]]",
        ],
        "body": """## Premium F&B Tiers

Premium food and beverage programs in venues typically operate across multiple tiers:

- **Luxury Suites** — Private or shared suites with dedicated catering service, pre-ordered menus, and in-suite attendants. Suites generate the highest per-capita F&B spend in any venue.
- **Club Levels** — Enclosed or semi-enclosed premium seating areas with access to dedicated restaurants, bars, and buffet stations. Club-level service bridges the gap between general admission concessions and suite-level hospitality.
- **Chef Stations and Action Cooking** — Live cooking stations where chefs prepare items to order in front of guests, creating a theatrical dining experience within the venue environment.
- **Premium Grab-and-Go** — Elevated quick-service options available in premium areas, offering higher-quality items than general concessions.

## Revenue Significance

Premium dining programs are disproportionately important to venue F&B revenue. Suite and club catering can account for 30-50% of total F&B revenue while serving a fraction of total attendance, making per-capita spending in premium areas a critical financial metric.

## Culinary Programming

Premium venues increasingly invest in culinary programming that mirrors fine-dining restaurant standards, including seasonal menu rotations, locally sourced ingredients, wine and spirits curation, and collaboration with recognized chefs. This trend has been driven by competition among contract operators to differentiate their offerings.

## Operational Complexity

Suite and club service adds operational complexity compared to concessions: individualized orders, dietary accommodation, multi-course timing, in-seat delivery logistics, and the need for trained service staff rather than concession workers.""",
    },
    {
        "filename": "Food-And-Beverage-Menu-Engineering-Dietary-Accommodation.md",
        "domain_dir": "food-and-beverage",
        "title": "Menu Engineering and Dietary Accommodation",
        "domain": "food-and-beverage",
        "description": "Menu mix optimization using contribution margin and popularity analysis, combined with dietary accommodation strategies including allergen management, plant-forward menus, and culturally inclusive food offerings in venue operations.",
        "venue_types": ["convention-centre", "arena", "stadium", "performing-arts-centre", "all"],
        "vef_alignment": ["guest-experience", "operational-efficiency-productivity-creativity", "innovation-and-continuous-improvement"],
        "confidence": "high",
        "sources": [
            "[[Source-0061-FDA-Food-Code-2022]]",
            "[[Source-0079-FDA-FALCPA-FASTER-Act-Allergens]]",
            "[[Source-0081-Menus-of-Change-CIA]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-Allergen-Management]]",
            "[[Food-And-Beverage-Concessions-Management]]",
            "[[Food-And-Beverage-Craft-Local-Beverage]]",
        ],
        "body": """## Menu Engineering Methodology

Menu engineering is the systematic analysis of menu item performance using two dimensions: contribution margin (profitability) and popularity (sales volume). Items are classified into four categories:

- **Stars** — High margin, high popularity. Maintain and promote these items.
- **Plowhorses** — Low margin, high popularity. Reengineer to improve margins.
- **Puzzles** — High margin, low popularity. Reposition or promote to increase sales.
- **Dogs** — Low margin, low popularity. Candidates for replacement.

In venue operations, menu engineering must also account for speed of preparation, ingredient overlap across items (for inventory efficiency), and suitability for the service format (concession, catered, premium).

## Dietary Accommodation

Venues serve increasingly diverse audiences with varied dietary requirements:

- **Allergen management** — The US recognizes 9 major allergens under FALCPA/FASTER Act; Canada identifies 14 priority allergens under SFCR
- **Plant-forward menus** — The Culinary Institute of America's Menus of Change initiative promotes plant-forward strategies that reduce environmental impact while meeting guest expectations
- **Cultural and religious dietary needs** — Halal, kosher, Hindu vegetarian, and other culturally significant food requirements
- **Medical dietary needs** — Gluten-free (celiac disease), low-sodium, diabetic-friendly options

## Implementation in Venues

Convention centres face particular complexity because each event may bring different dietary demographics. Banquet menus must accommodate dietary needs at scale, while concession operations must clearly label allergens and provide inclusive options without sacrificing speed of service.""",
    },
    {
        "filename": "Food-And-Beverage-HACCP-Implementation.md",
        "domain_dir": "food-and-beverage",
        "title": "HACCP Implementation in Venue Food Service",
        "domain": "food-and-beverage",
        "description": "Application of the seven HACCP principles to venue food service operations, including Preventive Control Plans (PCP) required under Canada's Safe Food for Canadians Regulations, and the adaptation of HACCP for high-volume, multi-point venue environments.",
        "venue_types": ["convention-centre", "arena", "stadium", "fairground-exhibition", "all"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "high",
        "sources": [
            "[[Source-0065-FDA-HACCP-Principles-Guidelines]]",
            "[[Source-0061-FDA-Food-Code-2022]]",
            "[[Source-0063-SFCR-Canada-Safe-Food-Regulations]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-Health-Inspection-Permitting]]",
            "[[Food-And-Beverage-Safety-Training-Certification]]",
            "[[Food-And-Beverage-Allergen-Management]]",
        ],
        "governed_by": [
            "[[Source-0065-FDA-HACCP-Principles-Guidelines]]",
            "[[Source-0063-SFCR-Canada-Safe-Food-Regulations]]",
        ],
        "body": """## The Seven HACCP Principles

Hazard Analysis and Critical Control Points (HACCP) is a systematic preventive approach to food safety that addresses physical, chemical, and biological hazards through prevention rather than finished-product inspection:

1. **Conduct a hazard analysis** — Identify potential food safety hazards at each step of the food handling process
2. **Determine Critical Control Points (CCPs)** — Identify points in the process where control can be applied to prevent, eliminate, or reduce hazards
3. **Establish critical limits** — Set measurable boundaries (e.g., minimum cooking temperatures) for each CCP
4. **Establish monitoring procedures** — Define how CCPs will be monitored (who, what, when, how)
5. **Establish corrective actions** — Define actions to take when monitoring indicates a critical limit has been exceeded
6. **Establish verification procedures** — Confirm the HACCP system is working as intended
7. **Establish record-keeping and documentation** — Maintain records of all HACCP-related activities

## Venue-Specific Adaptations

Venue food service presents unique HACCP challenges:
- Multiple production and service points requiring independent CCP monitoring
- High-volume production compressed into short pre-event windows
- Temperature control during transport from commissary to satellite service points
- Temporary food establishments at outdoor events and fairgrounds requiring adapted HACCP plans
- Mixed service formats (concession, banquet, premium dining) each requiring distinct hazard analyses

## Canadian PCP Requirements

Under Canada's Safe Food for Canadians Regulations (SFCR), food businesses must develop and maintain a written Preventive Control Plan (PCP) that incorporates HACCP principles. PCPs go beyond traditional HACCP to include preventive controls for allergens, sanitation, and supplier verification.""",
    },
    {
        "filename": "Food-And-Beverage-Allergen-Management.md",
        "domain_dir": "food-and-beverage",
        "title": "Food Allergen Management in Venue Operations",
        "domain": "food-and-beverage",
        "description": "Allergen management protocols for venue food service covering the US nine major allergens (FALCPA/FASTER Act) and Canada's 14 priority allergens, cross-contact prevention, staff training, and guest communication systems.",
        "venue_types": ["convention-centre", "arena", "stadium", "performing-arts-centre", "all"],
        "vef_alignment": ["guest-experience", "systems-processes-clarity-of-roles", "operational-efficiency-productivity-creativity"],
        "confidence": "high",
        "sources": [
            "[[Source-0079-FDA-FALCPA-FASTER-Act-Allergens]]",
            "[[Source-0080-CFIA-Allergen-Management]]",
            "[[Source-0064-ServSafe-Food-Safety-Certification]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-Menu-Engineering-Dietary-Accommodation]]",
            "[[Food-And-Beverage-HACCP-Implementation]]",
            "[[Food-And-Beverage-Safety-Training-Certification]]",
        ],
        "governed_by": [
            "[[Source-0079-FDA-FALCPA-FASTER-Act-Allergens]]",
            "[[Source-0080-CFIA-Allergen-Management]]",
        ],
        "jurisdiction": ["us-federal", "canada-federal"],
        "body": """## Regulatory Framework

### United States — Nine Major Allergens
The Food Allergen Labeling and Consumer Protection Act (FALCPA, 2004) identified eight major allergens. The FASTER Act (2021) added sesame as the ninth, effective January 1, 2023:
1. Milk, 2. Eggs, 3. Fish, 4. Crustacean shellfish, 5. Tree nuts, 6. Peanuts, 7. Wheat, 8. Soybeans, 9. Sesame

### Canada — 14 Priority Allergens
Canada's allergen list under SFCR includes all US allergens plus mustard, sulphites, and additional specificity. Venues operating in Canada must manage a broader allergen scope than US-only operations.

## Cross-Contact Prevention

Cross-contact (different from cross-contamination) occurs when a food allergen is unintentionally transferred from a food containing the allergen to a food that does not. Venue-specific cross-contact controls include:
- Dedicated preparation areas and utensils for allergen-free items
- Color-coded equipment systems to prevent shared-use errors
- Ingredient verification protocols for all received products
- Separate storage for allergen-free ingredients
- Staff hand-washing and glove-change procedures between allergen and non-allergen preparation

## Guest Communication

Venues must provide allergen information to guests through menu labeling, digital allergen guides (often accessible via QR code), trained staff who can answer allergen questions, and clear signage at concession and buffet service points. Convention centres hosting events with pre-set menus must coordinate allergen communication with event planners.

## Training Requirements

ServSafe offers a dedicated Allergen Awareness training program. All food-handling staff in venues should receive allergen training covering identification of major allergens, cross-contact prevention, emergency response procedures for allergic reactions, and communication protocols.""",
    },
    {
        "filename": "Food-And-Beverage-Safety-Training-Certification.md",
        "domain_dir": "food-and-beverage",
        "title": "Food Safety Training and Certification Programs",
        "domain": "food-and-beverage",
        "description": "Food safety training and certification programs applicable to venue food service operations, including ServSafe (US), FOODSAFE (British Columbia), food handler certification requirements, and ACF professional culinary certifications.",
        "venue_types": ["all"],
        "vef_alignment": ["employee-experience", "systems-processes-clarity-of-roles", "operational-efficiency-productivity-creativity"],
        "confidence": "high",
        "sources": [
            "[[Source-0064-ServSafe-Food-Safety-Certification]]",
            "[[Source-0074-ACF-American-Culinary-Federation]]",
            "[[Source-0061-FDA-Food-Code-2022]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-HACCP-Implementation]]",
            "[[Food-And-Beverage-Allergen-Management]]",
            "[[People-And-Culture-Culinary-Professional-Certification]]",
        ],
        "body": """## ServSafe Certification (United States)

ServSafe, administered by the National Restaurant Association, is the most widely recognized food safety certification in the US. Programs include:
- **ServSafe Food Handler** — Entry-level certification covering basic food safety principles for line-level food service employees
- **ServSafe Manager** — Comprehensive certification required by many jurisdictions for at least one certified manager on-site during food service operations
- **ServSafe Allergen** — Specialized training on allergen identification, cross-contact prevention, and guest communication

## Canadian Certifications

Canadian food safety certification varies by province:
- **FOODSAFE Level 1 and 2** (British Columbia) — Province-specific food safety training
- **Food Handler Certification** (Ontario, Alberta, and other provinces) — Required for food service workers, with province-specific approved training providers
- Requirements vary significantly by jurisdiction, complicating multi-province venue operations

## FDA Food Code Requirements

The FDA Food Code 2022 recommends that food establishments have at least one certified food protection manager (CFPM) on-site during operating hours. While the Food Code is a model code (adopted and enforced at the state and local level), the majority of US jurisdictions have adopted some version of this requirement.

## Venue-Specific Considerations

Venues face unique training challenges due to high reliance on event-day temporary staff. Training programs must be efficient enough to onboard temporary workers while ensuring minimum food safety competency. Digital training platforms and abbreviated food handler courses address this operational reality.""",
    },
    {
        "filename": "Food-And-Beverage-Health-Inspection-Permitting.md",
        "domain_dir": "food-and-beverage",
        "title": "Health Inspection and Food Service Permitting",
        "domain": "food-and-beverage",
        "description": "Health department inspection processes, food service permitting requirements, temporary food establishment (TFE) permits for events, and multi-point compliance management for venues with numerous food service locations operating under a single facility.",
        "venue_types": ["convention-centre", "arena", "stadium", "fairground-exhibition", "all"],
        "vef_alignment": ["systems-processes-clarity-of-roles", "operational-efficiency-productivity-creativity"],
        "confidence": "high",
        "sources": [
            "[[Source-0061-FDA-Food-Code-2022]]",
            "[[Source-0063-SFCR-Canada-Safe-Food-Regulations]]",
            "[[Source-0065-FDA-HACCP-Principles-Guidelines]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-HACCP-Implementation]]",
            "[[Legal-Compliance-And-Licensing-Liquor-Licensing-Venues]]",
        ],
        "governed_by": [
            "[[Source-0061-FDA-Food-Code-2022]]",
        ],
        "body": """## Health Inspection Framework

Health inspections for food service operations in venues are conducted by local or regional health authorities. In the US, inspections are typically based on the state or local adoption of the FDA Food Code. In Canada, the CFIA and provincial health authorities share jurisdiction depending on the type of food operation.

### Inspection Categories
- **Routine inspections** — Scheduled periodic inspections of permanent food service operations
- **Event-based inspections** — Inspections triggered by large events, particularly at fairgrounds and outdoor venues
- **Complaint-driven inspections** — Unscheduled inspections resulting from consumer complaints
- **Follow-up inspections** — Re-inspections to verify correction of previously cited violations

## Multi-Point Compliance

Large venues present a unique inspection challenge: a single stadium or convention centre may have 30-100+ individual food service points (concession stands, restaurants, bars, kitchens, catering prep areas), each subject to inspection. Managing compliance across all points requires:
- Standardized operating procedures across all service locations
- Internal self-inspection programs that supplement health authority inspections
- Centralized record-keeping for temperature logs, cleaning schedules, and corrective actions
- Designated food safety coordinators responsible for venue-wide compliance

## Temporary Food Establishment (TFE) Permits

Events at fairgrounds, outdoor amphitheatres, and convention centres often require TFE permits for food vendors operating on a temporary basis. TFE permitting requirements vary significantly by jurisdiction and typically include requirements for handwashing facilities, temperature control equipment, waste disposal, and food handler certification.""",
    },
    {
        "filename": "Food-And-Beverage-Technology-Stack.md",
        "domain_dir": "food-and-beverage",
        "title": "Food and Beverage Technology Stack",
        "domain": "food-and-beverage",
        "description": "Technology systems supporting venue food and beverage operations, including point-of-sale platforms (Oracle Simphony, Toast), mobile ordering, kitchen display systems, AI-powered food waste tracking (Winnow, Leanpath), and integrated procurement platforms.",
        "venue_types": ["convention-centre", "arena", "stadium", "all"],
        "vef_alignment": ["ai-and-digital-transformation", "operational-efficiency-productivity-creativity", "data-management-and-architecture"],
        "confidence": "high",
        "sources": [
            "[[Source-0087-Oracle-Simphony-POS]]",
            "[[Source-0088-Toast-POS-Platform]]",
            "[[Source-0089-Winnow-AI-Food-Waste]]",
            "[[Source-0090-Leanpath-Food-Waste-Prevention]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-Concessions-Management]]",
            "[[Supply-Chain-And-Procurement-GPO-Purchasing]]",
        ],
        "supported_by": [
            "[[Source-0087-Oracle-Simphony-POS]]",
            "[[Source-0088-Toast-POS-Platform]]",
        ],
        "body": """## Point-of-Sale Systems

POS systems are the operational backbone of venue F&B, handling transactions, inventory tracking, and reporting across multiple service points.

- **Oracle MICROS Simphony** — The enterprise standard for large-scale venue operations. Cloud-based, supports multi-location management, real-time reporting across hundreds of terminals, mobile ordering integration, and kitchen display system (KDS) connectivity. Widely deployed in stadiums, arenas, and convention centres.
- **Toast** — Cloud-based restaurant management platform with POS, online ordering, KDS, and workforce management. More common in smaller venue operations and individual restaurant concepts within venues.

## Mobile Ordering

Mobile ordering has become a standard feature at major venues, allowing guests to order from their seats via smartphone app and pick up at designated locations. This reduces queue times at concession stands and increases per-capita spending by lowering the friction of purchasing.

## Kitchen Display Systems (KDS)

KDS replace paper ticket printers in kitchen operations, displaying orders digitally with preparation timing, routing, and priority management. In high-volume venue kitchens, KDS enables better order sequencing and reduces errors.

## AI-Powered Food Waste Tracking

- **Winnow** — Uses computer vision to identify and categorize food waste as it is discarded, providing real-time data on waste patterns and enabling production adjustments
- **Leanpath** — Combines hardware (scales, cameras) with analytics to measure pre-consumer food waste, track trends, and drive behavioral change in kitchen operations

Both platforms provide data that supports sustainability reporting and cost reduction in venue food service operations.""",
    },
    {
        "filename": "Food-And-Beverage-Craft-Local-Beverage.md",
        "domain_dir": "food-and-beverage",
        "title": "Craft and Local Beverage Programs",
        "domain": "food-and-beverage",
        "description": "Local brewery, distillery, and winery partnerships in venue food and beverage programs, craft beverage curation strategies, and terroir-driven menu concepts that connect food and drink programs to regional identity.",
        "venue_types": ["arena", "stadium", "convention-centre", "performing-arts-centre", "amphitheatre"],
        "vef_alignment": ["guest-experience", "innovation-and-continuous-improvement"],
        "confidence": "medium",
        "sources": [
            "[[Source-0069-Levy-Restaurants-Compass-Group]]",
            "[[Source-0070-OVG-Hospitality]]",
            "[[Source-0081-Menus-of-Change-CIA]]",
        ],
        "child_of": "[[Domain-Food-And-Beverage]]",
        "related_to": [
            "[[Food-And-Beverage-Premium-Dining-Suite-Service]]",
            "[[Food-And-Beverage-Menu-Engineering-Dietary-Accommodation]]",
            "[[Supply-Chain-And-Procurement-Pouring-Rights]]",
        ],
        "body": """## Local Beverage Integration

The integration of local and craft beverages into venue programs has become a significant differentiator in venue hospitality. Venues are increasingly partnering with regional breweries, distilleries, wineries, and cideries to offer products that reflect the local community and create a sense of place.

### Program Structures
- **Branded concession stands** — Dedicated points of sale featuring a local brewery or distillery as the anchor brand
- **Rotating taps** — Draft systems featuring seasonal and rotating selections from regional producers
- **Signature cocktail programs** — Custom cocktails developed with local spirits for premium areas
- **Wine curation** — Regional wine selections for club levels and suite catering

## Navigating Pouring Rights

Craft and local beverage programs must operate within the constraints of exclusive pouring rights agreements with major beverage companies. Most large venues have contracts with Coca-Cola or PepsiCo (for non-alcoholic beverages) and may have beer sponsorship agreements with major brewers. Local craft programs are typically carved out as exceptions within these agreements, requiring careful contract negotiation.

## Terroir-Driven Menus

The concept of terroir — using locally sourced ingredients to express regional identity — extends beyond beverages to food programs. Venues are partnering with local farms, artisan producers, and regional food brands to create menus that tell the story of the community. This approach resonates with guests and supports local economic development.

## Operational Considerations

Local and craft products typically have shorter shelf lives, smaller production runs, and less predictable supply chains than products from major manufacturers. Venue operators must manage these constraints through careful forecasting, flexible tap management, and strong supplier relationships.""",
    },
    # --- SUPPLY CHAIN AND PROCUREMENT ---
    {
        "filename": "Supply-Chain-And-Procurement-GPO-Purchasing.md",
        "domain_dir": "supply-chain-and-procurement",
        "title": "Group Purchasing Organizations in Venue Procurement",
        "domain": "supply-chain-and-procurement",
        "description": "Group purchasing organizations (GPOs) used by venue operators to leverage collective purchasing power, including major GPOs like Entegra (Sodexo), Foodbuy (Compass/Levy), and Premier, and their role in cost management and supplier standardization.",
        "venue_types": ["convention-centre", "arena", "stadium", "all"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "strategy-and-effective-change-leadership"],
        "confidence": "medium",
        "sources": [
            "[[Source-0073-IFMA-Foodservice-Manufacturers]]",
            "[[Source-0066-Aramark-Sports-Entertainment]]",
            "[[Source-0069-Levy-Restaurants-Compass-Group]]",
        ],
        "child_of": "[[Domain-Supply-Chain-And-Procurement]]",
        "related_to": [
            "[[Supply-Chain-And-Procurement-Supplier-Qualification]]",
            "[[Food-And-Beverage-Contract-Catering-Market]]",
            "[[Food-And-Beverage-In-House-vs-Contracted-Decision]]",
        ],
        "body": """## GPO Model

Group purchasing organizations aggregate the buying power of multiple operators to negotiate volume-based pricing, rebates, and favorable contract terms with food and supply manufacturers and distributors. In the venue sector, GPO membership is one of the primary financial advantages that contract food service operators offer venues.

### Major Venue-Sector GPOs
- **Entegra Procurement Services** — The GPO affiliated with Sodexo, serving Sodexo-managed venues and available to independent operators
- **Foodbuy** — The purchasing arm of Compass Group, serving Levy-managed venues and other Compass divisions
- **Premier Inc.** — A GPO serving healthcare, hospitality, and foodservice sectors, available to independent operators
- **Aramark Supply Chain** — Aramark's integrated procurement function serving its managed venues

## Value Proposition

GPO membership delivers value through:
- Contracted pricing below individual-operator rates due to volume aggregation
- Supplier qualification and vetting (reducing the burden on individual venues)
- Rebate programs that return a percentage of spend to the operator
- Access to market intelligence on commodity pricing and supply trends
- Standardized product specifications that simplify ordering and receiving

## Implications for In-House Operations

Venues that operate food and beverage in-house lose access to the GPO pricing available to contracted operators. This cost disadvantage is one of the key factors in the in-house vs. contracted decision. Some independent GPOs offer membership to non-contracted venues, though the pricing leverage is typically less than what major operator-affiliated GPOs provide.

## Procurement Technology

GPOs increasingly provide digital procurement platforms that integrate with venue inventory management and POS systems, enabling automated reordering, spend analytics, and contract compliance monitoring.""",
    },
    {
        "filename": "Supply-Chain-And-Procurement-Pouring-Rights.md",
        "domain_dir": "supply-chain-and-procurement",
        "title": "Pouring Rights and Exclusive Beverage Contracts",
        "domain": "supply-chain-and-procurement",
        "description": "Exclusive beverage contracts (pouring rights) between venues and major beverage companies such as Coca-Cola and PepsiCo, including sponsorship integration, financial structures, and the operational constraints these agreements impose on food and beverage programs.",
        "venue_types": ["arena", "stadium", "convention-centre", "amphitheatre", "fairground-exhibition"],
        "vef_alignment": ["strategy-and-effective-change-leadership", "operational-efficiency-productivity-creativity"],
        "confidence": "high",
        "sources": [
            "[[Source-0066-Aramark-Sports-Entertainment]]",
            "[[Source-0071-Legends-Hospitality]]",
            "[[Source-0073-IFMA-Foodservice-Manufacturers]]",
        ],
        "child_of": "[[Domain-Supply-Chain-And-Procurement]]",
        "related_to": [
            "[[Food-And-Beverage-Craft-Local-Beverage]]",
            "[[Food-And-Beverage-Concessions-Management]]",
        ],
        "body": """## Pouring Rights Overview

Pouring rights agreements are exclusive contracts granting a single beverage company the right to be the sole provider of certain beverage categories within a venue. These agreements are a significant revenue source for venues and a major marketing platform for beverage companies.

### Contract Structure
- **Exclusivity scope** — Typically covers carbonated soft drinks, bottled water, sports drinks, and sometimes juice and tea categories. Alcoholic beverage exclusivity may be handled separately.
- **Financial terms** — Include upfront rights fees, annual payments, per-unit commissions, and marketing fund contributions. Major venue pouring rights can be worth millions of dollars over the contract term.
- **Contract duration** — Typically 5-10 years, with renewal options
- **Equipment and infrastructure** — The beverage company often provides fountain equipment, coolers, signage, and dispensing systems as part of the agreement

## Sponsorship Integration

Pouring rights are typically part of a broader sponsorship package that includes venue naming/branding opportunities, event sponsorship, digital signage, hospitality entitlements, and community marketing programs. The beverage contract is often one of the top three sponsorship deals at any major venue.

## Operational Constraints

Pouring rights agreements create operational constraints for food and beverage teams:
- All non-alcoholic beverages must come from the contracted supplier's portfolio
- Craft or local beverage offerings must be negotiated as exceptions
- Menu development must work within the supplier's product range
- Equipment specifications are determined by the supplier

## Competitive Dynamics

Coca-Cola and PepsiCo dominate the venue pouring rights market. Contract renewals and new venue openings trigger competitive bidding processes that can result in significant improvements in financial terms for the venue.""",
    },
    {
        "filename": "Supply-Chain-And-Procurement-FSMA-Traceability.md",
        "domain_dir": "supply-chain-and-procurement",
        "title": "FSMA 204 Food Traceability Compliance",
        "domain": "supply-chain-and-procurement",
        "description": "Requirements of FSMA Section 204 for food traceability, including the Food Traceability List, Key Data Elements (KDEs), Critical Tracking Events (CTEs), and compliance obligations for venue food service operations receiving foods on the traceability list.",
        "venue_types": ["convention-centre", "arena", "stadium", "all"],
        "vef_alignment": ["systems-processes-clarity-of-roles", "data-management-and-architecture"],
        "confidence": "high",
        "sources": [
            "[[Source-0062-FSMA-204-Traceability-Rule]]",
            "[[Source-0085-FoodLogiQ-Traceability-Platform]]",
            "[[Source-0061-FDA-Food-Code-2022]]",
        ],
        "child_of": "[[Domain-Supply-Chain-And-Procurement]]",
        "related_to": [
            "[[Supply-Chain-And-Procurement-Supplier-Qualification]]",
            "[[Food-And-Beverage-HACCP-Implementation]]",
            "[[Logistics-And-Warehouse-Loading-Dock-Operations]]",
        ],
        "governed_by": [
            "[[Source-0062-FSMA-204-Traceability-Rule]]",
        ],
        "jurisdiction": ["us-federal"],
        "body": """## FSMA Section 204 Overview

The FDA's FSMA Section 204 final rule (published November 2022) establishes additional traceability recordkeeping requirements for foods on the Food Traceability List (FTL). The rule requires persons who manufacture, process, pack, or hold FTL foods to maintain records containing Key Data Elements (KDEs) associated with Critical Tracking Events (CTEs).

### Food Traceability List
The FTL includes high-risk foods such as fresh-cut fruits and vegetables, shell eggs, nut butters, fresh herbs, leafy greens, certain cheeses, fresh-cut produce, smoked finfish, and crustaceans. Venues receiving these foods must comply with the rule's recordkeeping requirements.

## Key Data Elements and Critical Tracking Events

### Critical Tracking Events (CTEs)
CTEs are points in the supply chain where traceability records must be created:
- **Receiving** — When an FTL food arrives at the venue
- **Transformation** — When an FTL food is manufactured or processed into a different product
- **Shipping** — When an FTL food is sent to another location

### Key Data Elements (KDEs)
For each CTE, specific data must be recorded including traceability lot codes (TLCs), quantity, unit of measure, location identifiers, and dates.

## Venue Compliance Requirements

Venues that receive FTL foods (which includes most venues with food service operations) must:
- Maintain receiving records with required KDEs for all FTL foods
- Assign and record traceability lot codes
- Be able to provide records to FDA within 24 hours of a request during a recall or investigation
- Maintain records for two years

## Technology Solutions

Traceability compliance platforms such as FoodLogiQ provide digital tools for recording KDEs at CTEs, managing traceability lot codes, and generating required reports. Integration with existing procurement and inventory systems is essential for efficient compliance.""",
    },
    {
        "filename": "Supply-Chain-And-Procurement-Supplier-Qualification.md",
        "domain_dir": "supply-chain-and-procurement",
        "title": "Supplier Qualification and Food Safety Standards",
        "domain": "supply-chain-and-procurement",
        "description": "Supplier qualification frameworks using GFSI-benchmarked food safety certifications (SQF, BRC, FSSC 22000), approved supplier list management, and the role of third-party audits in venue supply chain risk management.",
        "venue_types": ["convention-centre", "arena", "stadium", "all"],
        "vef_alignment": ["systems-processes-clarity-of-roles", "operational-efficiency-productivity-creativity"],
        "confidence": "high",
        "sources": [
            "[[Source-0076-GFSI-Global-Food-Safety-Initiative]]",
            "[[Source-0077-SQF-Institute-Food-Safety]]",
            "[[Source-0062-FSMA-204-Traceability-Rule]]",
        ],
        "child_of": "[[Domain-Supply-Chain-And-Procurement]]",
        "related_to": [
            "[[Supply-Chain-And-Procurement-GPO-Purchasing]]",
            "[[Supply-Chain-And-Procurement-FSMA-Traceability]]",
            "[[Food-And-Beverage-HACCP-Implementation]]",
        ],
        "body": """## GFSI Benchmarking Framework

The Global Food Safety Initiative (GFSI) provides a benchmarking process for food safety management schemes. A GFSI-recognized certification demonstrates that a supplier's food safety management system meets globally accepted standards. Major GFSI-benchmarked schemes include:

- **SQF (Safe Quality Food)** — Administered by the SQF Institute; covers food safety and food quality management across primary production, manufacturing, and distribution
- **BRC Global Standard for Food Safety** — Published by the British Retail Consortium; widely used in manufacturing and processing
- **FSSC 22000** — Based on ISO 22000; combines management system requirements with prerequisite programs
- **IFS Food** — International Featured Standards; common in European supply chains

## Approved Supplier Lists

Venue operators maintain approved supplier lists (ASLs) that document which suppliers have been qualified to provide food products. Qualification criteria typically include:
- Current GFSI-benchmarked certification or equivalent third-party audit
- Certificate of insurance meeting venue requirements
- Compliance with applicable regulatory requirements (FSMA, SFCR)
- Satisfactory food safety audit results
- Product specification documentation

## GPO-Managed Qualification

Major contract food service operators conduct supplier qualification through their GPO programs, maintaining centralized approved supplier databases that individual venues can draw from. This reduces the administrative burden on individual venue procurement teams.

## Ongoing Monitoring

Supplier qualification is not a one-time event. Venues must monitor supplier performance through periodic audit reviews, product quality tracking, delivery performance metrics, and incident management. Suppliers that fail to maintain certification or experience food safety incidents may be suspended or removed from the approved list.""",
    },
    # --- LOGISTICS AND WAREHOUSE ---
    {
        "filename": "Logistics-And-Warehouse-Loading-Dock-Operations.md",
        "domain_dir": "logistics-and-warehouse",
        "title": "Loading Dock Operations and Receiving Protocols",
        "domain": "logistics-and-warehouse",
        "description": "Loading dock scheduling, receiving inspection protocols, delivery coordination during events, and the unique logistical challenges of managing dock operations in venues where event schedules, security requirements, and food safety protocols intersect.",
        "venue_types": ["convention-centre", "arena", "stadium", "fairground-exhibition"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "medium",
        "sources": [
            "[[Source-0075-GCCA-Global-Cold-Chain-Alliance]]",
            "[[Source-0062-FSMA-204-Traceability-Rule]]",
            "[[Source-0065-FDA-HACCP-Principles-Guidelines]]",
        ],
        "child_of": "[[Domain-Logistics-And-Warehouse]]",
        "related_to": [
            "[[Logistics-And-Warehouse-Cold-Chain-Compliance]]",
            "[[Logistics-And-Warehouse-Inventory-Storage]]",
            "[[Supply-Chain-And-Procurement-FSMA-Traceability]]",
        ],
        "body": """## Dock Scheduling

Large venues manage multiple deliveries daily across food and beverage, merchandise, equipment, event production materials, and facility supplies. Dock scheduling systems coordinate delivery windows to prevent congestion, prioritize time-sensitive deliveries (perishable foods, event-critical equipment), and align with security protocols.

### Key Scheduling Considerations
- **Event-day restrictions** — Many venues limit or prohibit deliveries during event load-in/load-out periods or during events themselves
- **Security clearance** — Delivery drivers and vehicles may require pre-registration and security screening
- **Temperature-sensitive scheduling** — Refrigerated deliveries must be scheduled to minimize dock exposure time
- **Dock capacity** — Physical limitations on the number of simultaneous deliveries

## Receiving Protocols

### Food Receiving
Food receiving at venues must comply with food safety requirements:
- Temperature verification of refrigerated and frozen products at the point of receiving
- Visual inspection for damage, contamination, and packaging integrity
- Verification of product specifications against purchase orders
- Recording of FSMA 204 traceability data (KDEs) for Food Traceability List items
- Rejection protocols for products that fail temperature or quality checks

### General Receiving
Non-food deliveries follow receiving protocols that include quantity verification, condition inspection, purchase order matching, and storage routing.

## Event-Day Coordination

Event days compress receiving operations into pre-event windows. Convention centres hosting simultaneous events face particular complexity, with multiple exhibitors, caterers, and service providers requiring dock access within overlapping time frames. Advanced scheduling and communication systems are essential for managing this complexity.""",
    },
    {
        "filename": "Logistics-And-Warehouse-Cold-Chain-Compliance.md",
        "domain_dir": "logistics-and-warehouse",
        "title": "Cold Chain Compliance and Temperature Monitoring",
        "domain": "logistics-and-warehouse",
        "description": "Cold chain management in venue logistics, including FSMA Sanitary Transportation Rule requirements, continuous temperature monitoring using IoT sensors, and protocols for maintaining food safety during receiving, storage, and internal distribution.",
        "venue_types": ["convention-centre", "arena", "stadium", "fairground-exhibition", "all"],
        "vef_alignment": ["systems-processes-clarity-of-roles", "operational-efficiency-productivity-creativity", "ai-and-digital-transformation"],
        "confidence": "high",
        "sources": [
            "[[Source-0075-GCCA-Global-Cold-Chain-Alliance]]",
            "[[Source-0062-FSMA-204-Traceability-Rule]]",
            "[[Source-0061-FDA-Food-Code-2022]]",
        ],
        "child_of": "[[Domain-Logistics-And-Warehouse]]",
        "related_to": [
            "[[Logistics-And-Warehouse-Loading-Dock-Operations]]",
            "[[Logistics-And-Warehouse-Inventory-Storage]]",
            "[[Food-And-Beverage-HACCP-Implementation]]",
        ],
        "governed_by": [
            "[[Source-0062-FSMA-204-Traceability-Rule]]",
        ],
        "body": """## Cold Chain Requirements

The cold chain encompasses the unbroken series of temperature-controlled logistics activities that maintain perishable food within safe temperature ranges from production through consumption. For venue food service, the cold chain includes supplier transportation, receiving, storage, internal distribution, and service.

### FSMA Sanitary Transportation Rule
The FSMA Sanitary Transportation of Human and Animal Food rule establishes requirements for vehicles and transportation equipment, transportation operations, training, and records. Venue operators receiving food shipments must ensure that carriers comply with temperature control requirements during transport.

### FDA Food Code Temperature Standards
- Cold holding: 41 degrees F (5 degrees C) or below
- Hot holding: 135 degrees F (57 degrees C) or above
- Danger zone: 41-135 degrees F — minimize time food spends in this range

## IoT Temperature Monitoring

Modern cold chain compliance increasingly relies on Internet of Things (IoT) sensor technology:
- **Walk-in cooler and freezer monitoring** — Continuous temperature sensors with automated alerting when temperatures exceed thresholds
- **Transport monitoring** — GPS-enabled temperature loggers that travel with shipments and provide receiving verification
- **Display case monitoring** — Sensors in service-area refrigeration providing real-time compliance data
- **Automated record-keeping** — IoT systems generate continuous temperature logs that satisfy regulatory documentation requirements

## Internal Distribution

Moving food from central storage to satellite service points within a venue is a cold chain event. Insulated transport containers, hot carts, cold carts, and timed delivery routes must maintain required temperatures. This is particularly challenging in large venues where service points may be hundreds of meters from central kitchens.""",
    },
    {
        "filename": "Logistics-And-Warehouse-Inventory-Storage.md",
        "domain_dir": "logistics-and-warehouse",
        "title": "Inventory Management and Storage Operations",
        "domain": "logistics-and-warehouse",
        "description": "Temperature-controlled storage management, par level systems, first-in-first-out (FIFO) inventory rotation, event-specific inventory planning, and the challenge of managing perishable and non-perishable inventory in venues with highly variable demand patterns.",
        "venue_types": ["convention-centre", "arena", "stadium", "fairground-exhibition", "all"],
        "vef_alignment": ["operational-efficiency-productivity-creativity", "systems-processes-clarity-of-roles"],
        "confidence": "medium",
        "sources": [
            "[[Source-0075-GCCA-Global-Cold-Chain-Alliance]]",
            "[[Source-0086-BlueCart-Procurement-Platform]]",
            "[[Source-0061-FDA-Food-Code-2022]]",
        ],
        "child_of": "[[Domain-Logistics-And-Warehouse]]",
        "related_to": [
            "[[Logistics-And-Warehouse-Cold-Chain-Compliance]]",
            "[[Logistics-And-Warehouse-Loading-Dock-Operations]]",
            "[[Food-And-Beverage-Commissary-Hub-Spoke-Kitchen]]",
        ],
        "body": """## Storage Categories

Venue inventory storage is divided into temperature-controlled zones:
- **Dry storage** — Ambient temperature for non-perishable items (canned goods, dry ingredients, paper goods, cleaning supplies)
- **Refrigerated storage** — 34-41 degrees F (1-5 degrees C) for perishable items requiring cold holding
- **Frozen storage** — 0 degrees F (-18 degrees C) or below for frozen products
- **Beverage storage** — Temperature-controlled or ambient depending on product type

## Par Level Management

Par levels define the minimum and maximum inventory quantities for each product, calibrated to event schedules, historical consumption data, and lead times. In venue operations, par levels must account for:
- **Event-day vs. non-event inventory** — Dramatically different consumption volumes between event and non-event days
- **Event type variability** — A concert audience consumes differently than a convention attendee or a hockey crowd
- **Seasonal variation** — Outdoor venues face seasonal demand shifts
- **Perishable shelf life** — Par levels for fresh products must balance availability against waste risk

## FIFO Rotation

First-in-first-out (FIFO) is the foundational inventory rotation principle in food service. Products received first are used first, preventing spoilage of older inventory. In practice, this requires:
- Date labeling on all received products
- Organized storage with older products positioned in front of or above newer products
- Regular inventory audits to identify expired or near-expiration items
- Staff training on FIFO principles and enforcement

## Event-Specific Inventory

Each event requires a tailored inventory plan based on expected attendance, event type, duration, audience demographics, and menu selections. Convention centre banquet operations require precise inventory against confirmed guest counts, while concession operations build inventory based on per-capita consumption estimates and historical data for similar events.""",
    },
    # --- LEGAL COMPLIANCE AND LICENSING ---
    {
        "filename": "Legal-Compliance-And-Licensing-Liquor-Licensing-Venues.md",
        "domain_dir": "legal-compliance-and-licensing",
        "title": "Liquor Licensing for Venue Operations",
        "domain": "legal-compliance-and-licensing",
        "description": "The complex landscape of liquor licensing for venues, including multi-point licenses for large facilities, catering endorsements, special event permits, and the jurisdictional fragmentation that makes alcohol compliance one of the most complex regulatory areas in venue operations.",
        "venue_types": ["convention-centre", "arena", "stadium", "performing-arts-centre", "amphitheatre", "fairground-exhibition"],
        "vef_alignment": ["systems-processes-clarity-of-roles", "operational-efficiency-productivity-creativity"],
        "confidence": "high",
        "sources": [
            "[[Source-0061-FDA-Food-Code-2022]]",
            "[[Source-0063-SFCR-Canada-Safe-Food-Regulations]]",
            "[[Source-0083-DOL-FLSA-Tip-Regulations]]",
        ],
        "child_of": "[[Domain-Legal-Compliance-And-Licensing]]",
        "related_to": [
            "[[Legal-Compliance-And-Licensing-Responsible-Beverage-Service]]",
            "[[Food-And-Beverage-Concessions-Management]]",
            "[[Food-And-Beverage-Health-Inspection-Permitting]]",
        ],
        "jurisdiction": ["us-state", "canada-provincial"],
        "body": """## Licensing Complexity

Liquor licensing for venues is governed at the state/provincial level, with significant variation across jurisdictions. A venue operating in multiple states or provinces must navigate different licensing categories, application processes, operating conditions, and enforcement frameworks.

### Common License Types for Venues
- **On-premises liquor license** — Permits sale and consumption of alcohol on the licensed premises
- **Catering endorsement/permit** — Allows a licensed establishment to provide alcohol service at events in areas beyond the primary licensed footprint
- **Special event permit** — Temporary authorization for alcohol service at specific events, often used for outdoor festivals, concerts, and fairground events
- **Multi-point or blanket license** — Some jurisdictions offer a single license covering multiple service points within a large venue

## Multi-Point Licensing Challenges

A large stadium or convention centre may have 50+ individual points of alcohol sale (concession stands, bars, restaurants, suites, hospitality areas). Jurisdictions handle this differently:
- Some require separate licenses or endorsements for each service point
- Some allow a single premises license covering all service areas within the venue footprint
- Some require a combination of permanent and temporary permits depending on the service area

## Event-Specific Permitting

Convention centres and fairgrounds hosting events with alcohol service may require event-specific permits, particularly when:
- The event operator (not the venue) is selling alcohol
- Service extends to areas not covered by the permanent license
- The event involves tastings, sampling, or self-pour systems with different regulatory requirements

## Compliance Management

Effective liquor license compliance in venues requires centralized license management, calendar systems for renewals and inspections, staff certification tracking (responsible beverage service), incident documentation, and regular self-audits against operating conditions.""",
    },
    {
        "filename": "Legal-Compliance-And-Licensing-Responsible-Beverage-Service.md",
        "domain_dir": "legal-compliance-and-licensing",
        "title": "Responsible Beverage Service Programs",
        "domain": "legal-compliance-and-licensing",
        "description": "Mandatory and voluntary responsible alcohol service training programs across North American jurisdictions, including Smart Serve (Ontario), Serving It Right (BC), ProServe (Alberta), TIPS, and California RBS, with their role in venue liability management.",
        "venue_types": ["arena", "stadium", "convention-centre", "performing-arts-centre", "amphitheatre", "all"],
        "vef_alignment": ["employee-experience", "systems-processes-clarity-of-roles"],
        "confidence": "high",
        "sources": [
            "[[Source-0064-ServSafe-Food-Safety-Certification]]",
            "[[Source-0083-DOL-FLSA-Tip-Regulations]]",
            "[[Source-0084-UNITE-HERE-Union]]",
        ],
        "child_of": "[[Domain-Legal-Compliance-And-Licensing]]",
        "related_to": [
            "[[Legal-Compliance-And-Licensing-Liquor-Licensing-Venues]]",
            "[[Food-And-Beverage-Safety-Training-Certification]]",
            "[[People-And-Culture-FB-Labor-Relations]]",
        ],
        "jurisdiction": ["us-state", "canada-provincial"],
        "body": """## Program Overview

Responsible beverage service (RBS) programs train alcohol servers to identify intoxication, prevent service to minors, manage difficult situations, and understand their legal obligations. Many jurisdictions require RBS certification as a condition of employment for anyone serving alcohol.

### Major Programs

**Canadian Programs (provincially mandated):**
- **Smart Serve** (Ontario) — Mandatory for all staff who serve, deliver, or sell alcohol
- **Serving It Right** (British Columbia) — Required certification for all liquor service staff
- **ProServe** (Alberta) — Mandatory AGLC-approved responsible service training
- **It's Good Business / Responsible Service NL** — Programs in other provinces with varying mandatory/voluntary status

**US Programs:**
- **TIPS (Training for Intervention ProcedureS)** — Widely used voluntary program accepted in many states
- **California Responsible Beverage Service (RBS)** — Mandatory statewide program effective July 2022, requiring all alcohol servers to complete training
- **ServSafe Alcohol** — National Restaurant Association program accepted in many jurisdictions

## Venue-Specific Requirements

Venues face particular RBS compliance challenges:
- High staff turnover requiring frequent certification cycles
- Event-day temporary workers who must hold valid certification before serving
- Multiple jurisdictional requirements for venue operators with locations in different states/provinces
- Documentation and verification systems to confirm all serving staff are currently certified

## Liability Management

RBS training is a key component of venue liability management. Demonstrating that all alcohol servers are trained and certified is typically required for liquor liability insurance and provides a defense in dram shop liability claims. Venues should maintain training records, conduct regular compliance audits, and implement policies that exceed minimum regulatory requirements.""",
    },
    # --- PEOPLE AND CULTURE ---
    {
        "filename": "People-And-Culture-FB-Labor-Relations.md",
        "domain_dir": "people-and-culture",
        "title": "Food and Beverage Labor Relations in Venues",
        "domain": "people-and-culture",
        "description": "Labor relations in venue food and beverage operations, including UNITE HERE and UFCW union representation, collective bargaining agreement provisions, tip pooling regulations under the FLSA, split shift management, and youth employment restrictions.",
        "venue_types": ["convention-centre", "arena", "stadium", "performing-arts-centre"],
        "vef_alignment": ["employee-experience", "systems-processes-clarity-of-roles", "strategy-and-effective-change-leadership"],
        "confidence": "medium",
        "sources": [
            "[[Source-0084-UNITE-HERE-Union]]",
            "[[Source-0083-DOL-FLSA-Tip-Regulations]]",
            "[[Source-0064-ServSafe-Food-Safety-Certification]]",
        ],
        "child_of": "[[Domain-People-And-Culture]]",
        "related_to": [
            "[[Food-And-Beverage-Contract-Catering-Market]]",
            "[[Legal-Compliance-And-Licensing-Responsible-Beverage-Service]]",
            "[[People-And-Culture-Culinary-Professional-Certification]]",
        ],
        "body": """## Union Representation

Food and beverage workers at major venues are frequently represented by labor unions, most commonly:

- **UNITE HERE** — The primary union representing hospitality workers in North America, including food service, concession, and catering workers at convention centres, arenas, and stadiums. UNITE HERE locals negotiate collective bargaining agreements covering wages, benefits, working conditions, and job protections.
- **UFCW (United Food and Commercial Workers)** — Represents workers in food processing and some food service operations, with occasional presence in venue food service.

### CBA Provisions Common in Venue F&B
- Seniority-based shift assignment and event staffing
- Minimum call-out hours (guaranteeing a minimum number of paid hours per event shift)
- Break requirements exceeding statutory minimums
- Health and welfare benefit contributions
- Grievance and arbitration procedures
- Restrictions on subcontracting food service work

## FLSA Tip Regulations

The Fair Labor Standards Act governs tip credit, tip pooling, and service charge distribution in the United States:
- **Tip credit** — Employers may pay tipped employees a reduced cash wage (currently $2.13/hour federal minimum, higher in many states) and take a credit against the full minimum wage
- **Tip pooling** — The DOL allows mandatory tip pooling among employees who customarily receive tips; rules on including back-of-house staff have changed through regulatory and judicial action
- **Service charges** — Mandatory service charges (common in banquet operations) are not tips under the FLSA and belong to the employer unless distributed to employees

## Split Shifts and Scheduling

Venue F&B operations frequently require split shifts (working a morning prep shift, breaking during the afternoon, returning for an evening event). Some jurisdictions require split-shift premiums. Scheduling challenges are intensified by the unpredictable nature of event calendars and last-minute attendance changes.

## Youth Employment

Venues employing workers under 18 must comply with federal and state child labor laws restricting hours, permitted tasks (particularly around hazardous equipment), and required supervision. These restrictions affect kitchen and concession staffing, particularly during school-year events.""",
    },
    {
        "filename": "People-And-Culture-Culinary-Professional-Certification.md",
        "domain_dir": "people-and-culture",
        "title": "Culinary Professional Certification Frameworks",
        "domain": "people-and-culture",
        "description": "Professional culinary certification systems including the ACF 13-level certification framework, Canadian Red Seal interprovincial program, WorldChefs certification, and CFSP (Certified Food Service Professional) designation and their relevance to venue culinary operations.",
        "venue_types": ["convention-centre", "arena", "stadium", "all"],
        "vef_alignment": ["employee-experience", "knowledge-management", "innovation-and-continuous-improvement"],
        "confidence": "high",
        "sources": [
            "[[Source-0074-ACF-American-Culinary-Federation]]",
            "[[Source-0064-ServSafe-Food-Safety-Certification]]",
            "[[Source-0073-IFMA-Foodservice-Manufacturers]]",
        ],
        "child_of": "[[Domain-People-And-Culture]]",
        "related_to": [
            "[[Food-And-Beverage-Safety-Training-Certification]]",
            "[[People-And-Culture-FB-Labor-Relations]]",
            "[[Food-And-Beverage-Premium-Dining-Suite-Service]]",
        ],
        "body": """## ACF Certification Framework

The American Culinary Federation administers a 13-level professional certification framework that serves as the industry standard for culinary professional development in the United States:

### Fundamental and Cooking Levels
- Certified Fundamental Cook (CFC)
- Certified Culinarian (CC)
- Certified Sous Chef (CSC)
- Certified Chef de Cuisine (CCC)

### Executive and Master Levels
- Certified Executive Chef (CEC)
- Certified Master Chef (CMC) — The highest culinary certification in the US

### Pastry Track
- Certified Pastry Culinarian (CPC)
- Certified Executive Pastry Chef (CEPC)
- Certified Master Pastry Chef (CMPC)

### Administrative Track
- Certified Culinary Administrator (CCA)
- Certified Culinary Educator (CCE)

## Canadian Red Seal Program

The Red Seal Program is Canada's interprovincial standard for skilled trades, including the Cook trade. Red Seal certification allows cooks to work across all Canadian provinces and territories without additional certification. The Red Seal endorsement is obtained by passing the Interprovincial Standards Red Seal Examination after completing an apprenticeship program.

## WorldChefs Certification

The World Association of Chefs Societies (WorldChefs) offers international certification levels that provide global recognition. WorldChefs certification complements national programs and is relevant for venues with international culinary talent.

## Relevance to Venue Operations

Professional certification in venue culinary operations serves multiple purposes: ensuring minimum competency standards, supporting career development and retention, enhancing the venue's culinary reputation, and meeting requirements specified in contract catering agreements. Premium dining programs increasingly seek certified culinary professionals to differentiate their offerings.""",
    },
]


def write_source(s):
    """Write a source note file."""
    domains_yaml = "\n".join(f"  - {d}" for d in s["domains"])
    content = f"""---
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
research_batch: v2-prompt-08-fb-supply
tags:
  - source
  - venue-ops
  - batch-03
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
extraction_model: claude-opus-4-6
---

# {s['title']}

{s['description']}

## Source Details

- **Type:** {s['source_type'].replace('-', ' ').title().replace('And', 'and')}
- **URL:** {s['url']}
- **Accessed:** 2026-04-04
- **Research Batch:** v2-prompt-08-fb-supply
"""
    filepath = os.path.join(SOURCES_DIR, f"Source-{s['num']}-{s['slug']}.md")
    with open(filepath, "w") as f:
        f.write(content)
    return filepath


def write_concept(c):
    """Write a concept note file."""
    venue_types_yaml = "\n".join(f"  - {v}" for v in c["venue_types"])
    vef_yaml = "\n".join(f"  - {v}" for v in c["vef_alignment"])
    sources_yaml = "\n".join(f'  - "{s}"' for s in c["sources"])
    related_yaml = "\n".join(f'  - "{r}"' for r in c.get("related_to", []))

    # Build optional frontmatter fields
    optional_fields = ""

    if "governed_by" in c:
        governed_yaml = "\n".join(f'  - "{g}"' for g in c["governed_by"])
        optional_fields += f"governed_by:\n{governed_yaml}\n"

    if "supported_by" in c:
        supported_yaml = "\n".join(f'  - "{s}"' for s in c["supported_by"])
        optional_fields += f"supported_by:\n{supported_yaml}\n"

    if "delivery_model" in c:
        dm_yaml = "\n".join(f"  - {d}" for d in c["delivery_model"])
        optional_fields += f"delivery_model:\n{dm_yaml}\n"

    if "jurisdiction" in c:
        j_yaml = "\n".join(f"  - {j}" for j in c["jurisdiction"])
        optional_fields += f"jurisdiction:\n{j_yaml}\n"

    # Build the sources list for the body
    body_sources = "\n".join(f"- {s}" for s in c["sources"])

    content = f"""---
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
research_batch: v2-prompt-08-fb-supply
child_of: "{c['child_of']}"
related_to:
{related_yaml}
{optional_fields}tags:
  - concept
  - venue-ops
  - {c['domain']}
  - batch-03
extraction_model: claude-opus-4-6
ai_disclosure: "Extracted by Claude (Anthropic) from deep research output. Human-reviewed by Alex Jackson, Experience Innovation Inc. Full methodology: VEP-KB-Data-Science-Methodology_v1.0.md"
---

# {c['title']}

{c['description']}

{c['body']}

## Sources

{body_sources}
"""
    domain_dir = os.path.join(DOMAINS_DIR, c["domain_dir"])
    filepath = os.path.join(domain_dir, c["filename"])
    with open(filepath, "w") as f:
        f.write(content)
    return filepath


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=== Generating Batch-03 Notes ===\n")

    # Write source notes
    print("--- Source Notes ---")
    for s in sources:
        fp = write_source(s)
        created_count += 1
        print(f"  [{created_count}] {os.path.basename(fp)}")

    # Write concept notes
    print("\n--- Concept Notes ---")
    for c in concepts:
        fp = write_concept(c)
        created_count += 1
        print(f"  [{created_count}] {os.path.basename(fp)}")

    print(f"\n=== TOTAL FILES CREATED: {created_count} ===")
