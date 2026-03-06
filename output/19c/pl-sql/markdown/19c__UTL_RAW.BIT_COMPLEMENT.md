---
id: 19c__UTL_RAW.BIT_COMPLEMENT
name: UTL_RAW.BIT_COMPLEMENT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.BIT_COMPLEMENT

This function performs bitwise logical "complement" of the values in RAW r and returns the complemented result RAW . The result length equals the input RAW r length.

## Syntax

```sql
UTL_RAW.BIT_COMPLEMENT (
   r IN RAW) 
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | RAW to perform "complement" operation |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.BIT_COMPLEMENT ( r IN RAW) RETURN RAW; Pragmas pragma restrict_references(bit_complement, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-4 BIT_COMPLEMENT Function Parameters Parameter Description r RAW to perform "complement" operation Return Values Table 272-5 BIT_COMPLEMENT Function Return Values Return Description RAW The "complement" of r1 NULL If r input parameter was NULL