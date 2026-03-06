---
id: 19c__UTL_ENCODE.BASE64_DECODE
name: UTL_ENCODE.BASE64_DECODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.BASE64_DECODE

This function reads the base 64-encoded RAW input string and decodes it to its original RAW value.

## Syntax

```sql
UTL_ENCODE.BASE64_DECODE (
   r  IN RAW) 
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | The RAW string containing base 64-encoded data. There are no defaults or optional parameters. |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_ENCODE.BASE64_DECODE ( r IN RAW) RETURN RAW; Pragmas pragma RESTRICT_REFERENCES(base64_decode, WNDS, RNDS, WNPS, RNPS); Parameters Table 262-2 BASE64_DECODE Function Parameters Parameter Description r The RAW string containing base 64-encoded data. There are no defaults or optional parameters. Return Values Table 262-3 BASE64_DECODE Function Return Values Return Description RAW Contains the decoded string