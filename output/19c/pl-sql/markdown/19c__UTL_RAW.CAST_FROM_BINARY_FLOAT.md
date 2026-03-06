---
id: 19c__UTL_RAW.CAST_FROM_BINARY_FLOAT
name: UTL_RAW.CAST_FROM_BINARY_FLOAT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_FROM_BINARY_FLOAT

This function returns the RAW binary representation of a BINARY_FLOAT value.

## Syntax

```sql
UTL_RAW.CAST_FROM_BINARY_FLOAT(
   n          IN BINARY_FLOAT,
   endianess IN PLS_INTEGER DEFAULT 1) 
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | BINARY_FLOAT | IN | BINARY_FLOAT value |
| endianess | PLS_INTEGER | IN | A BINARY_INTEGER value indicating the endianess. The function recognizes the defined constants big_endian (1), little_endian (2), and machine_endian (3). The default is big_endian . A setting of machine_endian has the same effect as big_endian on a big endian machine, or the same effect as little_endian on a little endian machine. |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.CAST_FROM_BINARY_FLOAT( n IN BINARY_FLOAT, endianess IN PLS_INTEGER DEFAULT 1) RETURN RAW; Pragmas pragma restrict_references(cast_from_binary_float, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-11 CAST_FROM_BINARY_FLOAT Function Parameters Parameter Description n BINARY_FLOAT value endianess A BINARY_INTEGER value indicating the endianess. The function recognizes the defined constants big_endian (1), little_endian (2), and machine_endian (3). The default is big_endian . A setting of machine_endian has the same effect as big_endian on a big endian machine, or the same effect as little_endian on a little endian machine. Return Values The binary representation (RAW) of the BINARY_FLOAT value, or NULL if the input is NULL . Usage Notes A 4-byte binary_float value maps to the IEEE 754 single-precision format as follows: byte 0: bit 31 ~ bit 24 byte 1: bit 23 ~ bit 16 byte 2: bit 15 ~ bit 8 byte 3: bit 7 ~ bit 0 The parameter endianess describes how the bytes of BINARY_FLOAT are mapped to the bytes of RAW . In the following matrix, rb0 ~ rb3 refer to the bytes in RAW and fb0 ~ fb3 refer to the bytes in BINARY_FLOAT . Endianess rb0 rb1 rb2 rb3 big_endian fb0 fb1 fb2 fb3 little_endian fb3 fb2 fb1 fb0 In case of machine-endian, the 4 bytes of the BINARY_FLOAT argument are copied straight across into the RAW return value. The effect is the same if the user has passed big_endian on a big-endian machine, or little_endian on a little-endian machine.