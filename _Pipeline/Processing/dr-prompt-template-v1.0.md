---
title: "Deep Research Prompt Template"
version: "1.0"
created: 2026-04-06
session: S19
lifecycle: active
platform: "Perplexity Pro Enterprise Max (Comet browser, Deep Research enabled)"
authority: "Codified from exemplar R-05 (S18) per Alex directive 2026-04-06"
---

# Deep Research Prompt Template v1.0

## Purpose

Standard template for all Deep Research prompts submitted to Perplexity Pro Enterprise Max via Comet browser. Every DR prompt targeting the venue-ops-kb must follow this structure. No exceptions.

## Template

```
DR PROMPT [ID] — [Descriptive Title]

CONTEXT: [Why this research is needed. Reference the KB gap — which concept note, 
which delta entry, what's missing or thin. State the current source situation and why 
it's insufficient. This grounds the research in an actual KB need, not abstract curiosity.]

RESEARCH OBJECTIVE: [One sentence. What to produce, for what domain, as of what date. 
Include venue types if scope is narrower than "all venues."]

PRIMARY RESEARCH QUESTIONS:

1. [TOPIC AREA]: [Detailed question with sub-bullets specifying exactly what's needed.
   Include specific entities, standards, regulations, or frameworks to investigate.
   Name specific data points sought (statistics, thresholds, dates, organizations).]
2. [TOPIC AREA]: [Same structure. Each numbered question targets a distinct facet of 
   the research objective.]
...
N. [TOPIC AREA]: [As many questions as needed to fully scope the research. Typical 
   range: 5-8 questions per prompt.]

SOURCE QUALITY:
- PRIORITY 1: [Primary/authoritative sources — official documents, regulatory bodies, 
  standards organizations]
- PRIORITY 2: [Secondary authoritative — industry associations, Indigenous/community-
  led organizations, peer-reviewed research]
- PRIORITY 3: [Tertiary — industry publications, operator reports, trade press]
- PRIORITY 4: [Supporting — academic research, case studies, conference proceedings]
- AVOID: [Explicitly name source types to exclude — marketing materials, vendor claims 
  without verification, non-authoritative commentary]

OUTPUT STRUCTURE:
- [Named deliverable 1 — e.g., "Reference table with full text and status"]
- [Named deliverable 2 — e.g., "Process guide with operational steps"]
- [Named deliverable 3 — e.g., "Case study catalog (N venues with specifics)"]
...
[Each deliverable maps to a specific extraction target in the KB.]

KNOWN CONTEXT: [What the KB already covers that overlaps with this prompt's scope. 
Prevents duplicate research. Name specific concept notes, domains, or sources that 
already exist. Explicitly state what this prompt targets ONLY — and what it does NOT 
target.]

CONSTRAINTS: [Scope limits. Jurisdictional focus. Special handling rules (e.g., CS 
exemplar tagging). Disambiguation of similar entities. Hard exclusions. Any KB-specific 
policies that apply (Hard Rules, vocabulary restrictions, etc.).]
```

## Section Purposes

| Section | Purpose | Required |
|---|---|---|
| **ID + Title** | Unique identifier for audit trail. Title is human-scannable. | Yes |
| **CONTEXT** | Grounds the research in a real KB gap. References delta entries. | Yes |
| **RESEARCH OBJECTIVE** | Single-sentence scope statement. Controls scope creep. | Yes |
| **PRIMARY RESEARCH QUESTIONS** | Detailed, numbered questions. The "what to find." | Yes |
| **SOURCE QUALITY** | Priority-ranked source preferences. Controls quality bar. | Yes |
| **OUTPUT STRUCTURE** | Named deliverables. Maps to extraction targets. | Yes |
| **KNOWN CONTEXT** | Deduplication guard. Prevents re-researching existing content. | Yes |
| **CONSTRAINTS** | Scope limits and special handling. Prevents scope creep. | Yes |

## Naming Convention

- Prompt ID: `R-NN` (sequential, zero-padded)
- File naming: `dr-prompt-R-NN-short-description.md`
- Research batch tag (VOCABULARY.yaml): `dr-[purpose]-s[session]` (e.g., `dr-remediation-s18`, `dr-b1-fill-s19`)

## Prompt Design Principles

1. **Gap-driven, not curiosity-driven.** Every prompt traces to a specific KB gap (empty domain, delta entry, scaffolded domain needing depth).
2. **Named entities over generic requests.** Ask for "NFPA 101 Section 12.7" not "fire safety codes." Name the standards, organizations, and jurisdictions you need.
3. **Source quality hierarchy is mandatory.** Primary sources first. Vendor marketing last. AVOID section prevents noise.
4. **Output structure maps to extraction.** Each named deliverable becomes one or more concept notes + source notes in the KB.
5. **Known context prevents duplication.** If the KB already has 13 F&B concepts, say so — don't re-research F&B foundations.
6. **Constraints prevent scope creep.** Jurisdictional limits, entity disambiguation, and KB policy enforcement happen at prompt time, not extraction time.

## Audit Trail Requirement (CI Item — Phase D)

Every DR prompt must be tracked from inception to extraction:

```
Need identified → Prompt authored → Prompt submitted → Output received → 
Output registered → Extraction complete → Validation passed
```

**Implementation deferred to Phase D CI session.** For now: prompts are stored in `_Pipeline/Processing/`, outputs land in `_Pipeline/Input/`, and the mapping is documented in `progress.md` session logs.

---

*Codified S19 (2026-04-06) from exemplar R-05. Platform: Perplexity Pro Enterprise Max via Comet browser.*
