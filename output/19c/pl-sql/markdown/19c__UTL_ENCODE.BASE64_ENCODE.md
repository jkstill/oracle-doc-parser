---
id: 19c__UTL_ENCODE.BASE64_ENCODE
name: UTL_ENCODE.BASE64_ENCODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.BASE64_ENCODE

This function encodes the binary representation of the RAW value into base 64 elements and returns it in the form of a RAW string.

## Syntax

```sql
UTL_ENCODE.BASE64_ENCODE (
   r  IN RAW) 
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | The RAW value to be encoded. There are no defaults or optional parameters. |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_ENCODE.BASE64_ENCODE ( r IN RAW) RETURN RAW; Pragmas pragma RESTRICT_REFERENCES(base64_encode, WNDS, RNDS, WNPS, RNPS); Parameters Table 262-4 BASE64_ENCODE Function Parameters Parameter Description r The RAW value to be encoded. There are no defaults or optional parameters. Return Values Table 262-5 BASE64_ENCODE Function Return Values Return Description RAW Contains the encoded base 64 elements