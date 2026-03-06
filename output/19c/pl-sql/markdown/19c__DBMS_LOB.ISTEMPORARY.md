---
id: 19c__DBMS_LOB.ISTEMPORARY
name: DBMS_LOB.ISTEMPORARY
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.ISTEMPORARY

This function determines whether a LOB instance is temporary.

## Syntax

```sql
DBMS_LOB.ISTEMPORARY (
   lob_loc IN BLOB)
  RETURN INTEGER;
 
DBMS_LOB.ISTEMPORARY (
   lob_loc IN CLOB CHARACTER SET ANY_CS)
  RETURN INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB) | IN | LOB locator. For more information, see Operational Notes . |

**Returns:** `INTEGER`

## Usage Notes

Syntax DBMS_LOB.ISTEMPORARY ( lob_loc IN BLOB) RETURN INTEGER; DBMS_LOB.ISTEMPORARY ( lob_loc IN CLOB CHARACTER SET ANY_CS) RETURN INTEGER; Pragmas PRAGMA RESTRICT_REFERENCES(istemporary, WNDS, RNDS, WNPS, RNPS); Parameters Table 99-73 ISTEMPORARY Procedure Parameters Parameter Description lob_loc LOB locator. For more information, see Operational Notes . Return Values The return value is 1 if the LOB is temporary and exists; 0 if the LOB is not temporary or does not exist; NULL if the given locator is NULL . Usage Notes When you free a Temporary LOB with FREETEMPORARY , the LOB locator is not set to NULL . Consequently, ISTEMPORARY will return 0 for a locator that has been freed but not explicitly reset to NULL .