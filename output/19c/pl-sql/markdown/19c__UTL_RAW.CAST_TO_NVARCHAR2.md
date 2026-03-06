---
id: 19c__UTL_RAW.CAST_TO_NVARCHAR2
name: UTL_RAW.CAST_TO_NVARCHAR2
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_TO_NVARCHAR2

This function converts a RAW value represented using some number of data bytes into an NVARCHAR2 value with that number of data bytes.

## Syntax

```sql
UTL_RAW.CAST_TO_NVARCHAR2 (
   r IN RAW) 
RETURN NVARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | RAW (without leading length field) to be changed to a NVARCHAR2 ) |

**Returns:** `NVARCHAR2`

## Usage Notes

Note: When casting to a NVARCHAR2 , the current Globalization Support character set is used for the characters within that NVARCHAR2 value. Note: When casting to a NVARCHAR2 , the current Globalization Support character set is used for the characters within that NVARCHAR2 value. Syntax UTL_RAW.CAST_TO_NVARCHAR2 ( r IN RAW) RETURN NVARCHAR2; Pragmas pragma restrict_references(cast_to_NVARCHAR2, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-18 CAST_TO_NVARCHAR2 Function Parameters Parameter Description r RAW (without leading length field) to be changed to a NVARCHAR2 )