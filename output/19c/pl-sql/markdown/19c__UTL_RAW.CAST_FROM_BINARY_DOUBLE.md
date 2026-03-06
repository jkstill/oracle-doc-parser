---
id: 19c__UTL_RAW.CAST_FROM_BINARY_DOUBLE
name: UTL_RAW.CAST_FROM_BINARY_DOUBLE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_FROM_BINARY_DOUBLE

This function returns the RAW binary representation of a BINARY_DOUBLE value.

## Syntax

```sql
UTL_RAW.CAST_FROM_BINARY_DOUBLE(
   n          IN BINARY_DOUBLE,
   endianess IN PLS_INTEGER DEFAULT 1) 
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | BINARY_DOUBLE | IN | BINARY_DOUBLE value |
| endianess | PLS_INTEGER | IN | A BINARY_INTEGER value indicating the endianess. The function recognizes the defined constants big_endian (1), little_endian (2), and machine_endian (3). The default is big_endian . A setting of machine_endian has the same effect as big_endian on a big endian machine, or the same effect as little_endian on a little endian machine. |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.CAST_FROM_BINARY_DOUBLE( n IN BINARY_DOUBLE, endianess IN PLS_INTEGER DEFAULT 1) RETURN RAW; Pragmas pragma restrict_references(cast_from_binary_double, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-10 CAST_FROM_BINARY_DOUBLE Function Parameters Parameter Description n BINARY_DOUBLE value endianess A BINARY_INTEGER value indicating the endianess. The function recognizes the defined constants big_endian (1), little_endian (2), and machine_endian (3). The default is big_endian . A setting of machine_endian has the same effect as big_endian on a big endian machine, or the same effect as little_endian on a little endian machine. Return Values The binary representation of the BINARY_DOUBLE value, or NULL if the input is NULL . Usage Notes An 8-byte binary_double value maps to the IEEE 754 double-precision format as follows: byte 0: bit 63 ~ bit 56 byte 1: bit 55 ~ bit 48 byte 2: bit 47 ~ bit 40 byte 3: bit 39 ~ bit 32 byte 4: bit 31 ~ bit 24 byte 5: bit 23 ~ bit 16 byte 6: bit 15 ~ bit 8 byte 7: bit 7 ~ bit 0 The parameter endianess describes how the bytes of BINARY_DOUBLE are mapped to the bytes of RAW . In the following matrix, rb0 ~ rb7 refer to the bytes in raw and db0 ~ db7 refer to the bytes in BINARY_DOUBLE. endianess rb0 rb1 rb2 rb3 rb4 rb5 rb6 rb7 big_endian db0 db1 db2 db3 db4 db5 db6 db7 little_endian db7 db6 db5 db4 db3 db2 db1 db0 In case of machine-endian, the 8 bytes of the BINARY_DOUBLE argument are copied straight across into the RAW return value. The effect is the same if the user has passed big_endian on a big-endian machine, or little_endian on a little-endian machine.