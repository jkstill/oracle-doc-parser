---
id: 19c__UTL_ENCODE.QUOTED_PRINTABLE_ENCODE
name: UTL_ENCODE.QUOTED_PRINTABLE_ENCODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.QUOTED_PRINTABLE_ENCODE

This function reads the RAW input string and encodes it to the corresponding quoted printable format string.

## Syntax

```sql
UTL_ENCODE.QUOTED_PRINTABLE_ENCODE (
   r  IN RAW)
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | The RAW string. There are no defaults or optional parameters. |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_ENCODE.QUOTED_PRINTABLE_ENCODE ( r IN RAW) RETURN RAW; Pragmas pragma RESTRICT_REFERENCES(quoted_printable_encode, WNDS, RNDS,WNPS, RNPS); Parameters Table 262-12 QUOTED_PRINTABLE_ENCODE Function Parameters Parameter Description r The RAW string. There are no defaults or optional parameters. Return Values Table 262-13 QUOTED_PRINTABLE_ENCODE Function Return Values Return Description RAW Contains the quoted printable string