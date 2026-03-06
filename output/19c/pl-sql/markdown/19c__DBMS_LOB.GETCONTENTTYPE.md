---
id: 19c__DBMS_LOB.GETCONTENTTYPE
name: DBMS_LOB.GETCONTENTTYPE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_LOB
tags: [dbms_lob]
source_file: DBMS_LOB.html
---

# DBMS_LOB.GETCONTENTTYPE

This procedure returns the content type string previously set by means of the SETCONTENTTYPE Procedure.

## Syntax

```sql
DBMS_LOB.GETCONTENTTYPE (
   lob_loc  IN BLOB)
 RETURN VARCHAR2;

DBMS_LOB.GETCONTENTTYPE (
   lob_loc  IN CLOB CHARACTER SET ANY_CS)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| lob_loc | BLOB) | IN | LOB whose content type is to be retrieved |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_LOB.GETCONTENTTYPE ( lob_loc IN BLOB) RETURN VARCHAR2; DBMS_LOB.GETCONTENTTYPE ( lob_loc IN CLOB CHARACTER SET ANY_CS) RETURN VARCHAR2; Pragmas PRAGMA RESTRICT_REFERENCES(getcontenttype, WNDS, RNDS, WNPS, RNPS); Parameters Table 99-58 GETCONTENTTYPE Function Parameters Parameter Description lob_loc LOB whose content type is to be retrieved Return Values The returned content type. If the SecureFiles LOB does not have a contenttype associated with it, GETCONTENTTYPE() returns NULL . Exceptions Table 99-59 GETCONTENTTYPE Function Exceptions Exception Description SECUREFILE_BADLOB lob_loc is not a SECUREFILE