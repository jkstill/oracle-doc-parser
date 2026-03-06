---
id: 19c__UTL_RAW.CONVERT
name: UTL_RAW.CONVERT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.CONVERT

This function converts RAW r from character set from_charset to character set to_charset and returns the resulting RAW .

## Syntax

```sql
UTL_RAW.CONVERT (
   r            IN RAW,
   to_charset   IN VARCHAR2,
   from_charset IN VARCHAR2) 
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW | IN | RAW byte-string to be converted |
| to_charset | VARCHAR2 | IN | Name of the character set to which r is converted |
| from_charset | VARCHAR2) | IN | Name of the character set in which r is supplied |

**Returns:** `RAW`

## Usage Notes

Both from_charset and to_charset must be supported character sets defined to the Oracle server. Syntax UTL_RAW.CONVERT ( r IN RAW, to_charset IN VARCHAR2, from_charset IN VARCHAR2) RETURN RAW; Pragmas pragma restrict_references(convert, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-27 CONVERT Function Parameters Parameter Description r RAW byte-string to be converted to_charset Name of the character set to which r is converted from_charset Name of the character set in which r is supplied Return Values Table 272-28 CONVERT Function Return Values Return Description RAW Byte string r converted according to the specified character sets.