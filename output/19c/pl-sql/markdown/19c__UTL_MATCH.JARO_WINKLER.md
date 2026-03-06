---
id: 19c__UTL_MATCH.JARO_WINKLER
name: UTL_MATCH.JARO_WINKLER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_MATCH
tags: [utl_match]
source_file: UTL_MATCH.html
---

# UTL_MATCH.JARO_WINKLER

This function calculates the measure of agreement between two strings.

## Syntax

```sql
UTL_MATCH.JARO_WINKLER (
   s1  IN  VARCHAR2, 
   s2  IN  VARCHAR2) 
 RETURN BINARY_DOUBLE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| s1 | VARCHAR2 | IN | Input |
| s2 | VARCHAR2) | IN | input |

**Returns:** `BINARY_DOUBLE`

## Usage Notes

Syntax UTL_MATCH.JARO_WINKLER ( s1 IN VARCHAR2, s2 IN VARCHAR2) RETURN BINARY_DOUBLE; Parameters Table 270-5 JARO_WINKLER Function Parameters Parameter Description s1 Input s2 input Examples SELECT UTL_MATCH.JARO_WINKLER('shackleford', 'shackelford') FROM DUAL; -------------- returns 9.818E-001