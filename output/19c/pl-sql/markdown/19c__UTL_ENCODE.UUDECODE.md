---
id: 19c__UTL_ENCODE.UUDECODE
name: UTL_ENCODE.UUDECODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.UUDECODE

This function reads the RAW uuencode format input string and decodes it to the corresponding RAW string.

## Syntax

```sql
UTL_ENCODE.UUDECODE (
   r  IN RAW) 
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW) | IN | The RAW string containing the uuencoded data string. There are no defaults or optional parameters. |

**Returns:** `RAW`

## Usage Notes

See " UUENCODE Function " for discussion of the cumulative nature of UUENCODE and UUDECODE for data streams. Syntax UTL_ENCODE.UUDECODE ( r IN RAW) RETURN RAW; Pragmas pragma RESTRICT_REFERENCES(uudecode, WNDS, RNDS, WNPS, RNPS); Parameters Table 262-18 UUDECODE Function Parameters Parameter Description r The RAW string containing the uuencoded data string. There are no defaults or optional parameters. Return Values Table 262-19 UUDECODE Function Return Values Return Description RAW The decoded RAW string