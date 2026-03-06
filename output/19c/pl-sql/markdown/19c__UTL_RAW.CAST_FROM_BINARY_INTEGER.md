---
id: 19c__UTL_RAW.CAST_FROM_BINARY_INTEGER
name: UTL_RAW.CAST_FROM_BINARY_INTEGER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_FROM_BINARY_INTEGER

This function returns the RAW binary representation of a BINARY_INTEGER value.

## Syntax

```sql
UTL_RAW.CAST_FROM_BINARY_INTEGER (
   n          IN BINARY_INTEGER
   endianess  IN PLS_INTEGER DEFAULT BIG_ENDIAN) 
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | BINARY_INTEGER | IN | BINARY_INTEGER value. |
| endianess | PLS_INTEGER | IN | A BINARY_INTEGER value indicating the endianess. The function recognizes the defined constants big_endian (1), little_endian (2), and machine_endian (3). The default is big_endian . A setting of machine_endian has the same effect as big_endian on a big endian machine, or the same effect as little_endian on a little endian machine. |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.CAST_FROM_BINARY_INTEGER ( n IN BINARY_INTEGER endianess IN PLS_INTEGER DEFAULT BIG_ENDIAN) RETURN RAW; Pragmas pragma restrict_references(cast_from_binary_integer, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-12 CAST_FROM_BINARY_INTEGER Function Parameters Parameter Description n BINARY_INTEGER value. endianess A BINARY_INTEGER value indicating the endianess. The function recognizes the defined constants big_endian (1), little_endian (2), and machine_endian (3). The default is big_endian . A setting of machine_endian has the same effect as big_endian on a big endian machine, or the same effect as little_endian on a little endian machine. Return Values The binary representation of the BINARY_INTEGER value.