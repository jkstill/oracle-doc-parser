---
id: 19c__UTL_RAW.REVERSE
name: UTL_RAW.REVERSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.REVERSE

This function reverses a byte sequence in RAW r from end to end.

## Syntax

```sql
UTL_RAW.REVERSE (
   r IN RAW) 
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | RAW to reverse |

**Returns:** `RAW`

## Usage Notes

For example, x'0102F3' would be reversed to x'F30201', and 'xyz' would be reversed to 'zyx'.The result length is the same as the input RAW length. Syntax UTL_RAW.REVERSE ( r IN RAW) RETURN RAW; Pragmas pragma restrict_references(reverse, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-38 REVERSE Function Parameters Parameter Description r RAW to reverse Return Values Table 272-39 REVERSE Function Return Values Return Description RAW Containing the "reverse" of r