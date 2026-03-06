---
id: 19c__UTL_RAW.CAST_TO_VARCHAR2
name: UTL_RAW.CAST_TO_VARCHAR2
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_TO_VARCHAR2

This function converts a RAW value represented using some number of data bytes into a VARCHAR2 value with that number of data bytes.

## Syntax

```sql
UTL_RAW.CAST_TO_VARCHAR2 (
   r IN RAW) 
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | RAW (without leading length field) to be changed to a VARCHAR2 |

**Returns:** `VARCHAR2`

## Usage Notes

Note: When casting to a VARCHAR2 , the current Globalization Support character set is used for the characters within that VARCHAR2 . Note: When casting to a VARCHAR2 , the current Globalization Support character set is used for the characters within that VARCHAR2 . Syntax UTL_RAW.CAST_TO_VARCHAR2 ( r IN RAW) RETURN VARCHAR2; Pragmas pragma restrict_references(cast_to_VARCHAR2, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-22 CAST_TO_VARCHAR2 Function Parameters Parameter Description r RAW (without leading length field) to be changed to a VARCHAR2