---
id: 19c__UTL_RAW.CAST_TO_NUMBER
name: UTL_RAW.CAST_TO_NUMBER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_TO_NUMBER

This function casts the RAW binary representation of a NUMBER into a NUMBER .

## Syntax

```sql
UTL_RAW.CAST_TO_NUMBER (
   r  IN RAW) 
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | Binary representation of a NUMBER |

**Returns:** `NUMBER`

## Usage Notes

Syntax UTL_RAW.CAST_TO_NUMBER ( r IN RAW) RETURN NUMBER; Pragmas pragma restrict_references(cast_to_number, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-17 CAST_TO_NUMBER function Parameters Parameter Description r Binary representation of a NUMBER Return Values The NUMBER value.