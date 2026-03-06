---
id: 19c__UTL_RAW.CAST_TO_BINARY_INTEGER
name: UTL_RAW.CAST_TO_BINARY_INTEGER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_TO_BINARY_INTEGER

This function casts the RAW binary representation of a BINARY_INTEGER into a BINARY_INTEGER .

## Syntax

```sql
UTL_RAW.CAST_TO_BINARY_INTEGER (
   r          IN RAW
   endianess  IN PLS_INTEGER DEFAULT BIG_ENDIAN) 
RETURN BINARY_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW | IN | Binary representation of a BINARY_INTEGER |
| endianess | PLS_INTEGER | IN | A PLS_INTEGER representing big-endian or little-endian architecture. The default is big-endian. |

**Returns:** `BINARY_INTEGER`

## Usage Notes

Syntax UTL_RAW.CAST_TO_BINARY_INTEGER ( r IN RAW endianess IN PLS_INTEGER DEFAULT BIG_ENDIAN) RETURN BINARY_INTEGER; Pragmas pragma restrict_references(cast_to_binary_integer, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-16 CAST_TO_BINARY_INTEGER Function Parameters Parameter Description r Binary representation of a BINARY_INTEGER endianess A PLS_INTEGER representing big-endian or little-endian architecture. The default is big-endian. Return Values The BINARY_INTEGER value