---
id: 19c__UTL_MATCH.EDIT_DISTANCE_SIMILARITY
name: UTL_MATCH.EDIT_DISTANCE_SIMILARITY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_MATCH
tags: [utl_match]
source_file: UTL_MATCH.html
---

# UTL_MATCH.EDIT_DISTANCE_SIMILARITY

This function calculates the number of insertions, deletions or substations required to transform string-1 into string-2, and returns the Normalized value of the Edit Distance between two strings.

## Syntax

```sql
UTL_MATCH.EDIT_DISTANCE_SIMILARITY (
   s1  IN  VARCHAR2, 
   s2  IN  VARCHAR2) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| s1 | VARCHAR2 | IN | The string to be transformed |
| s2 | VARCHAR2) | IN | The string into which s1 is to be transformed |

**Returns:** `PLS_INTEGER`

## Usage Notes

The value is typically between 0 (no match) and 100 (perfect match). Syntax UTL_MATCH.EDIT_DISTANCE_SIMILARITY ( s1 IN VARCHAR2, s2 IN VARCHAR2) RETURN PLS_INTEGER; Parameters Table 270-4 EDIT_DISTANCE_SIMILARITY Function Parameters Parameter Description s1 The string to be transformed s2 The string into which s1 is to be transformed Examples SELECT UTL_MATCH.EDIT_DISTANCE_SIMILARITY('shackleford', 'shackelford') FROM DUAL; -------------- returns 82