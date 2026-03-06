---
id: 19c__OWA_PATTERN.GETPAT
name: OWA_PATTERN.GETPAT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_PATTERN
tags: [owa_pattern]
source_file: OWA_PATTERN.html
---

# OWA_PATTERN.GETPAT

This procedure converts a VARCHAR2 string into an OWA_PATTERN.PATTERN DATA TYPE .

## Syntax

```sql
OWA_PATTERN.GETPAT(
   arg      IN          VARCHAR2, 
   pat      IN OUT      pattern);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| arg | VARCHAR2 | IN | The string to convert. |
| pat | pattern) | IN OUT | the OWA_PATTERN.PATTERN DATA TYPE initialized with arg . |

## Usage Notes

Syntax OWA_PATTERN.GETPAT( arg IN VARCHAR2, pat IN OUT pattern); Parameters Table 227-7 GETPAT Procedure Parameters Parameter Description arg The string to convert. pat the OWA_PATTERN.PATTERN DATA TYPE initialized with arg .