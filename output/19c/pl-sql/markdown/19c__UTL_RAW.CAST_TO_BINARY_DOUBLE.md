---
id: 19c__UTL_RAW.CAST_TO_BINARY_DOUBLE
name: UTL_RAW.CAST_TO_BINARY_DOUBLE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_TO_BINARY_DOUBLE

This function casts the RAW binary representation of a BINARY_DOUBLE into a BINARY_DOUBLE .

## Syntax

```sql
UTL_RAW.CAST_TO_BINARY_DOUBLE (
   r          IN RAW
   endianess  IN PLS_INTEGER DEFAULT 1) 
RETURN BINARY_DOUBLE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW | IN | Binary representation of a BINARY_DOUBLE |
| endianess | PLS_INTEGER | IN | A PLS_INTEGER representing big-endian or little-endian architecture. The default is big-endian. |

**Returns:** `BINARY_DOUBLE`

## Usage Notes

Syntax UTL_RAW.CAST_TO_BINARY_DOUBLE ( r IN RAW endianess IN PLS_INTEGER DEFAULT 1) RETURN BINARY_DOUBLE; Pragmas pragma restrict_references(cast_to_binary_double, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-14 CAST_TO_BINARY_DOUBLE Function Parameters Parameter Description r Binary representation of a BINARY_DOUBLE endianess A PLS_INTEGER representing big-endian or little-endian architecture. The default is big-endian. Return Values The BINARY_DOUBLE value. Usage Notes If the RAW argument is more than 8 bytes, only the first 8 bytes are used and the rest of the bytes are ignored. If the result is -0 , +0 is returned. If the result is NaN , the value BINARY_DOUBLE_NAN is returned. If the RAW argument is less than 8 bytes, a VALUE_ERROR exception is raised. An 8-byte binary_double value maps to the IEEE 754 double-precision format as follows: byte 0: bit 63 ~ bit 56 byte 1: bit 55 ~ bit 48 byte 2: bit 47 ~ bit 40 byte 3: bit 39 ~ bit 32 byte 4: bit 31 ~ bit 24 byte 5: bit 23 ~ bit 16 byte 6: bit 15 ~ bit 8 byte 7: bit 7 ~ bit 0 The parameter endianess describes how the bytes of BINARY_DOUBLE are mapped to the bytes of RAW . In the following matrix, rb0 ~ rb7 refer to the bytes in raw and db0 ~ db7 refer to the bytes in BINARY_DOUBLE. Architecture rb0 rb1 rb2 rb3 rb4 rb5 rb6 rb7 big_endian db0 db1 db2 db3 db4 db5 db6 db7 little_endian db7 db6 db5 db4 db3 db2 db1 db0 In case of machine-endian, the 8 bytes of the RAW argument are copied straight across into the BINARY_DOUBLE return value. The effect is the same if the user has passed big_endian on a big-endian machine, or little_endian on a little-endian machine.