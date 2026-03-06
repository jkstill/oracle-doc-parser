---
id: 19c__UTL_RAW.BIT_OR
name: UTL_RAW.BIT_OR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.BIT_OR

This function performs bitwise logical "or" of the values in RAW r1 with RAW r2 and returns the or'd result RAW .

## Syntax

```sql
UTL_RAW.BIT_OR (
   r1 IN RAW,
   r2 IN RAW) 
  RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.BIT_OR ( r1 IN RAW, r2 IN RAW) RETURN RAW; Pragmas pragma restrict_references(bit_or, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-6 BIT_OR Function Parameters Parameters Description r1 RAW to "or" with r2 r2 RAW to "or" with r1 Return Values Table 272-7 BIT_OR Function Return Values Return Description RAW Containing the "or" of r1 and r2 NULL Either r1 or r2 input parameter was NULL Usage Notes If r1 and r2 differ in length, then the "or" operation is terminated after the last byte of the shorter of the two RAWs , and the unprocessed portion of the longer RAW is appended to the partial result. The result length equals the longer of the two input RAWs .