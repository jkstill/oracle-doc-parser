---
id: 19c__UTL_RAW.CAST_TO_BINARY_FLOAT
name: UTL_RAW.CAST_TO_BINARY_FLOAT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_TO_BINARY_FLOAT

This function casts the RAW binary representation of a BINARY_FLOAT into a BINARY_FLOAT .

## Syntax

```sql
UTL_RAW.CAST_TO_BINARY_FLOAT (
   r          IN RAW
   endianess  IN PLS_INTEGER DEFAULT 1) 
RETURN BINARY_FLOAT;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW | IN | Binary representation of a BINARY_FLOAT |
| endianess | PLS_INTEGER | IN | A PLS_INTEGER representing big-endian or little-endian architecture. The default is big-endian. |

**Returns:** `BINARY_FLOAT`

## Usage Notes

Syntax UTL_RAW.CAST_TO_BINARY_FLOAT ( r IN RAW endianess IN PLS_INTEGER DEFAULT 1) RETURN BINARY_FLOAT; Pragmas pragma restrict_references(cast_to_binary_float, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-15 CAST_TO_BINARY_FLOAT Function Parameters Parameter Description r Binary representation of a BINARY_FLOAT endianess A PLS_INTEGER representing big-endian or little-endian architecture. The default is big-endian. Return Values The BINARY_FLOAT value. Usage Notes If the RAW argument is more than 4 bytes, only the first 4 bytes are used and the rest of the bytes are ignored. If the result is -0, +0 is returned. If the result is NaN, the value BINARY_FLOAT_NAN is returned. If the RAW argument is less than 4 bytes, a VALUE_ERROR exception is raised. A 4-byte binary_float value maps to the IEEE 754 single-precision format as follows: byte 0: bit 31 ~ bit 24 byte 1: bit 23 ~ bit 16 byte 2: bit 15 ~ bit 8 byte 3: bit 7 ~ bit 0 The parameter endianess describes how the bytes of BINARY_FLOAT are mapped to the bytes of RAW . In the following matrix, rb0 ~ rb3 refer to the bytes in RAW and fb0 ~ fb3 refer to the bytes in BINARY_FLOAT . Endianness rb0 rb1 rb2 rb3 big_endian fbo fb1 fb2 fb3 little_endian fb3 fb2 fb1 fb0 In case of machine-endian, the 4 bytes of the RAW argument are copied straight across into the BINARY_FLOAT return value. The effect is the same if the user has passed big_endian on a big-endian machine, or little_endian on a little-endian machine.