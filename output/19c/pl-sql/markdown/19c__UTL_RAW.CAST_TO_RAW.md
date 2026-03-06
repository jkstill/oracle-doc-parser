---
id: 19c__UTL_RAW.CAST_TO_RAW
name: UTL_RAW.CAST_TO_RAW
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_TO_RAW

This function converts a VARCHAR2 value represented using some number of data bytes into a RAW value with that number of data bytes. The data itself is not modified in any way, but its datatype is recast to a RAW datatype.

## Syntax

```sql
UTL_RAW.CAST_TO_RAW (
   c  IN VARCHAR2) 
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| c | VARCHAR2) | IN | VARCHAR2 to be changed to a RAW |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.CAST_TO_RAW ( c IN VARCHAR2) RETURN RAW; Pragmas pragma restrict_references(cast_to_raw, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-20 CAST_TO_RAW Function Parameters Parameter Description c VARCHAR2 to be changed to a RAW Return Values Table 272-21 CAST_TO_RAW Function Return Values Return Description RAW Containing the same data as the input VARCHAR2 and equal byte length as the input VARCHAR2 and without a leading length field NULL If c input parameter was NULL