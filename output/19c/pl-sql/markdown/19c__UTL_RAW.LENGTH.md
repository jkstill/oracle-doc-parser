---
id: 19c__UTL_RAW.LENGTH
name: UTL_RAW.LENGTH
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.LENGTH

This function returns the length in bytes of a RAW r .

## Syntax

```sql
UTL_RAW.LENGTH (
   r  IN RAW) 
RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | RAW byte stream to be measured |

**Returns:** `NUMBER`

## Usage Notes

Syntax UTL_RAW.LENGTH ( r IN RAW) RETURN NUMBER; Pragmas pragma restrict_references(length, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-32 LENGTH Function Parameters Parameter Description r RAW byte stream to be measured Return Values Table 272-33 LENGTH Function Return Values Return Description NUMBER Current length of the RAW