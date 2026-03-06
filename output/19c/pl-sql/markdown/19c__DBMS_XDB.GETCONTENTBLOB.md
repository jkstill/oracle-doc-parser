---
id: 19c__DBMS_XDB.GETCONTENTBLOB
name: DBMS_XDB.GETCONTENTBLOB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.GETCONTENTBLOB

This deprecated function retrieves the contents of a resource returned as a BLOB .

## Syntax

```sql
DBMS_XDB.GETCONTENTBLOB(
     abspath    IN     VARCHAR2, 
     csid       OUT    PLS_INTEGER,
     locksrc    IN     BOOLEAN := FALSE) 
  RETURN BLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |
| csid | PLS_INTEGER | OUT | If TRUE , lock and return the source LOB. If FALSE , return a temp LOB copy. |
| locksrc | BOOLEAN | IN | Contents of the resource as a BLOB |

**Returns:** `BLOB`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETCONTENTBLOB Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETCONTENTBLOB Function . Syntax DBMS_XDB.GETCONTENTBLOB( abspath IN VARCHAR2, csid OUT PLS_INTEGER, locksrc IN BOOLEAN := FALSE) RETURN BLOB; Parameters Table 194-15 GETCONTENTBLOB Function Parameters Parameter Description abspath Absolute path of the resource csid If TRUE , lock and return the source LOB. If FALSE , return a temp LOB copy. locksrc Contents of the resource as a BLOB Return Values The contents of the resource as a BLOB.