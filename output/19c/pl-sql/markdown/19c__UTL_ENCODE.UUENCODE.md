---
id: 19c__UTL_ENCODE.UUENCODE
name: UTL_ENCODE.UUENCODE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_ENCODE
tags: [utl_encode]
source_file: UTL_ENCODE.html
---

# UTL_ENCODE.UUENCODE

This function reads the RAW input string and encodes it to the corresponding uuencode format string.

## Syntax

```sql
UTL_ENCODE.UUENCODE (
   r          IN RAW,
   type       IN PLS_INTEGER DEFAULT 1,
   filename   IN VARCHAR2 DEFAULT NULL,
   permission IN VARCHAR2 DEFAULT NULL) RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | RAW | IN | RAW string |
| type | PLS_INTEGER | IN | Optional number parameter containing the type of uuencoded output. Options: complete—a defined PL/SQL constant with a value of 1 . (default) header_piece ...middle_piece ...end_piece |
| filename | VARCHAR2 | IN | Optional varchar2 parameter containing the uuencode filename; the default is uuencode.txt |
| permission | VARCHAR2 | IN | Optional varchar2 parameter containing the permission mode; the default is 0 (a text string zero). |

**Returns:** `RAW`

## Usage Notes

The output of this function is cumulative, in that it can be used to encode large data streams, by splitting the data stream into acceptably sized RAW values, encoded, and concatenated into a single encoded string. Syntax UTL_ENCODE.UUENCODE ( r IN RAW, type IN PLS_INTEGER DEFAULT 1, filename IN VARCHAR2 DEFAULT NULL, permission IN VARCHAR2 DEFAULT NULL) RETURN RAW; Pragmas pragma RESTRICT_REFERENCES(uuencode, WNDS, RNDS, WNPS, RNPS); Parameters Table 262-20 UUENCODE Function Parameters Parameter Description r RAW string type Optional number parameter containing the type of uuencoded output. Options: complete—a defined PL/SQL constant with a value of 1 . (default) header_piece ...middle_piece ...end_piece filename Optional varchar2 parameter containing the uuencode filename; the default is uuencode.txt permission Optional varchar2 parameter containing the permission mode; the default is 0 (a text string zero). Return Values Table 262-21 UUENCODE Function Return Values Return Description RAW Contains the uuencode format string