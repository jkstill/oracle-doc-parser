---
id: 19c__UTL_RAW.SUBSTR
name: UTL_RAW.SUBSTR
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_RAW
tags: [utl_raw]
source_file: UTL_RAW.html
---

# UTL_RAW.SUBSTR

This function returns len bytes, starting at pos from RAW r .

## Syntax

```sql
UTL_RAW.SUBSTR (
   r   IN RAW,
   pos IN BINARY_INTEGER,
   len IN BINARY_INTEGER DEFAULT NULL) 
  RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW | IN | RAW byte-string from which a portion is extracted |
| pos | BINARY_INTEGER | IN | Byte position in r at which to begin extraction |
| len | BINARY_INTEGER | IN | Number of bytes from pos to extract from r (optional) |

**Returns:** `RAW`

## Usage Notes

Syntax UTL_RAW.SUBSTR ( r IN RAW, pos IN BINARY_INTEGER, len IN BINARY_INTEGER DEFAULT NULL) RETURN RAW; Pragmas pragma restrict_references(substr, WNDS, RNDS, WNPS, RNPS); Parameters Table 272-41 SUBSTR Function Parameters Parameter Description r RAW byte-string from which a portion is extracted pos Byte position in r at which to begin extraction len Number of bytes from pos to extract from r (optional) Defaults and Optional Parameters Table 272-42 SUBSTR Function Optional Parameter Optional Parameter Description len Position pos through to the end of r Return Values Table 272-43 SUBSTR Function Return Values Return Description portion of r Beginning at pos for len bytes long NULL r input parameter was NULL