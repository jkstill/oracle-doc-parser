---
id: 19c__DBMS_XDB.GETCONTENTCLOB
name: DBMS_XDB.GETCONTENTCLOB
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.GETCONTENTCLOB

This deprecated function gets the contents of a resource returned as a CLOB .

## Syntax

```sql
DBMS_XDB.GETCONTENTCLOB(
     abspath    IN     VARCHAR2,
  RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |

**Returns:** `CLOB`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETCONTENTCLOB Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETCONTENTCLOB Function . Syntax DBMS_XDB.GETCONTENTCLOB( abspath IN VARCHAR2, RETURN CLOB; Parameters Table 194-16 GETCONTENTCLOB Function Parameters Parameter Description abspath Absolute path of the resource Return Values The contents of the resource as a CLOB.