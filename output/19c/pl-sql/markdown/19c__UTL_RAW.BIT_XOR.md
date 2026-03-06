---
id: 19c__UTL_RAW.BIT_XOR
name: UTL_RAW.BIT_XOR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.BIT_XOR

This function performs bitwise logical "exclusive or" of the values in RAW r1 with RAW r2 and returns the xor'd result RAW .

## Syntax

```sql
UTL_RAW.BIT_XOR (
   r1 IN RAW,
   r2 IN RAW) 
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r1 | RAW | IN | RAW to "xor" with r2 |
| r2 | RAW) | IN | RAW to "xor" with r1 |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.BIT_XOR ( r1 IN RAW, r2 IN RAW) RETURN RAW; Pragmas pragma restrict_references(bit_xor, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-8 BIT_XOR Function Parameters Parameter Description r1 RAW to "xor" with r2 r2 RAW to "xor" with r1 Return Values Table 272-9 BIT_XOR Function Return Values Return Description RAW Containing the "xor" of r1 and r2 NULL If either r1 or r2 input parameter was NULL Usage Notes If r1 and r2 differ in length, then the "xor" operation is terminated after the last byte of the shorter of the two RAWs , and the unprocessed portion of the longer RAW is appended to the partial result. The result length equals the longer of the two input RAWs .