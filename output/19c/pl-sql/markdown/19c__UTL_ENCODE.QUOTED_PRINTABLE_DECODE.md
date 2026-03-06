---
id: 19c__UTL_ENCODE.QUOTED_PRINTABLE_DECODE
name: UTL_ENCODE.QUOTED_PRINTABLE_DECODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.QUOTED_PRINTABLE_DECODE

This function reads the varchar2 quoted printable format input string and decodes it to the corresponding RAW string.

## Syntax

```sql
UTL_ENCODE.QUOTED_PRINTABLE_DECODE (
   r  IN RAW)
RETURN RAW;
```

**Returns:** `RAW`

## Usage Notes

Syntax UTL_ENCODE.QUOTED_PRINTABLE_DECODE ( r IN RAW) RETURN RAW; Pragmas pragma RESTRICT_REFERENCES(quoted_printable_decode, WNDS, RNDS, WNPS, RNPS); Parameters Table 262-10 QUOTED_PRINTABLE_DECODE Function Parameters Parameters Description r The RAW string containing a quoted printable data string. There are no defaults or optional parameters. Return Values Table 262-11 QUOTED_PRINTABLE_DECODE Function Return Values Return Description RAW The decoded string