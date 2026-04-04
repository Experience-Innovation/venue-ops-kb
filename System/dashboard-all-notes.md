---
title: "Dashboard — All Notes"
note_type: map
status: draft
created: 2026-04-03
updated: 2026-04-03
scope: "Vault-wide dashboard"
description: "Dataview queries for vault health and navigation"
children: []
tags:
  - system
  - dashboard
ai_disclosure: "Generated through Human/AI collaboration using Claude. Sources verified. Human accountability: Alex Jackson, Experience Innovation Inc."
---

# Dashboard — All Notes

## By Status

```dataview
TABLE length(rows) as "Count"
FROM "01_Domains" OR "02_Standards" OR "03_Technology" OR "04_Organizations" OR "05_People" OR "06_Sources"
GROUP BY status
SORT status ASC
```

## By Domain

```dataview
TABLE length(rows) as "Count"
FROM "01_Domains"
WHERE note_type = "concept"
GROUP BY domain
SORT domain ASC
```

## Recent Updates (Last 7 Days)

```dataview
TABLE note_type, status, domain
FROM "01_Domains" OR "02_Standards" OR "03_Technology" OR "04_Organizations" OR "05_People"
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 25
```

## Orphan Notes (No Inlinks)

```dataview
LIST
FROM "01_Domains" OR "02_Standards" OR "03_Technology" OR "04_Organizations" OR "05_People"
WHERE length(file.inlinks) = 0
SORT file.ctime DESC
```

## Missing Sources (Concept Notes Without Citations)

```dataview
LIST
FROM "01_Domains"
WHERE note_type = "concept" AND (!sources OR length(sources) = 0)
SORT file.name ASC
```

## Draft Notes Pending Review

```dataview
TABLE note_type, domain, confidence
FROM "01_Domains" OR "02_Standards" OR "03_Technology" OR "04_Organizations" OR "05_People"
WHERE status = "draft"
SORT domain ASC, file.name ASC
```

## Confidence Distribution

```dataview
TABLE confidence, length(rows) as "Count"
FROM "01_Domains"
WHERE note_type = "concept"
GROUP BY confidence
```

## Relationship Density

```dataview
TABLE
  length(file.outlinks) as "Outlinks",
  length(file.inlinks) as "Inlinks"
FROM "01_Domains"
WHERE note_type = "concept"
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 25
```
