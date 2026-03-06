---
id: 19c__UTL_RAW.CAST_FROM_NUMBER
name: UTL_RAW.CAST_FROM_NUMBER
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CAST_FROM_NUMBER

This function returns the RAW binary representation of a NUMBER value.

## Syntax

```sql
UTL_RAW.CAST_FROM_NUMBER (
   n  IN NUMBER)
 RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| n | NUMBER) | IN | NUMBER value |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.CAST_FROM_NUMBER ( n IN NUMBER) RETURN RAW; Pragmas pragma restrict_references(cast_from_number, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-13 CAST_FROM_NUMBER Function Parameters Parameter Description n NUMBER value Return Values The binary representation of the NUMBER value.