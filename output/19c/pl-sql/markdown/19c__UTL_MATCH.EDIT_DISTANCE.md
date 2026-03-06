---
id: 19c__UTL_MATCH.EDIT_DISTANCE
name: UTL_MATCH.EDIT_DISTANCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_MATCH
tags: [utl_match]
source_file: UTL_MATCH.html
---

# UTL_MATCH.EDIT_DISTANCE

This function calculates the number of insertions, deletions or substitutions required to transform string-1 into string-2.

## Syntax

```sql
UTL_MATCH.EDIT_DISTANCE (
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

Syntax UTL_MATCH.EDIT_DISTANCE ( s1 IN VARCHAR2, s2 IN VARCHAR2) RETURN PLS_INTEGER; Parameters Table 270-3 EDIT_DISTANCE Function Parameters Parameter Description s1 The string to be transformed s2 The string into which s1 is to be transformed Examples SELECT UTL_MATCH.EDIT_DISTANCE('shackleford', 'shackelford') FROM DUAL; ------------- returns 2