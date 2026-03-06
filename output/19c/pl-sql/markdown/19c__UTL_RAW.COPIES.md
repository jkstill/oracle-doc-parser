---
id: 19c__UTL_RAW.COPIES
name: UTL_RAW.COPIES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.COPIES

This function returns n copies of r concatenated together.

## Syntax

```sql
UTL_RAW.COPIES (
   r IN RAW,
   n IN NUMBER) 
  RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.COPIES ( r IN RAW, n IN NUMBER) RETURN RAW; Pragmas pragma restrict_references(copies, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-30 COPIES Function Parameters Parameters Description r RAW to be copied n Number of times to copy the RAW (must be positive) Return Values This returns the RAW copied n times. Exceptions Table 272-31 COPIES Function Exceptions Error Description VALUE_ERROR Either: - r is missing, NULL or 0 length - n < 1 - Length of result exceeds maximum length of a RAW