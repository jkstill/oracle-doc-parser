---
id: 19c__UTL_RAW.BIT_AND
name: UTL_RAW.BIT_AND
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.BIT_AND

This function performs bitwise logical "and" of the values in RAW r1 with RAW r2 and returns the "anded" result RAW .

## Syntax

```sql
UTL_RAW.BIT_AND (
   r1 IN RAW,
   r2 IN RAW) 
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r1 | RAW | IN | RAW to "and" with r2 |
| r2 | RAW) | IN | RAW to "and" with r1 |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.BIT_AND ( r1 IN RAW, r2 IN RAW) RETURN RAW; Pragmas pragma restrict_references(bit_and, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-2 BIT_AND Function Parameters Parameter Description r1 RAW to "and" with r2 r2 RAW to "and" with r1 Return Values Table 272-3 BIT_AND Function Return Values Return Description RAW Containing the "and" of r1 and r2 NULL Either r1 or r2 input parameter was NULL Usage Notes If r1 and r2 differ in length, the and operation is terminated after the last byte of the shorter of the two RAWs , and the unprocessed portion of the longer RAW is appended to the partial result. The result length equals the longer of the two input RAWs .