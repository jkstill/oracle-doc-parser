---
id: 19c__UTL_MATCH.JARO_WINKLER_SIMILARITY
name: UTL_MATCH.JARO_WINKLER_SIMILARITY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_MATCH
tags: [utl_match]
source_file: UTL_MATCH.html
---

# UTL_MATCH.JARO_WINKLER_SIMILARITY

This function calculates the measure of agreement between two strings, and returns a score between 0 (no match) and 100 (perfect match).

## Syntax

```sql
UTL_MATCH.JARO_WINKLER_SIMILARITY (
   s1  IN  VARCHAR2, 
   s2  IN  VARCHAR2) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| s1 | VARCHAR2 | IN | Input |
| s2 | VARCHAR2) | IN | input |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax UTL_MATCH.JARO_WINKLER_SIMILARITY ( s1 IN VARCHAR2, s2 IN VARCHAR2) RETURN PLS_INTEGER; Parameters Table 270-6 JARO_WINKLER_SIMILARITY Function Parameters Parameter Description s1 Input s2 input Examples SELECT UTL_MATCH.JARO_WINKLER_SIMILARITY('shackleford', 'shackelford') FROM DUAL; -------------- returns 98