---
id: 19c__DBMS_XDB.GETCONTENTVARCHAR2
name: DBMS_XDB.GETCONTENTVARCHAR2
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.GETCONTENTVARCHAR2

This deprecated function gets the contents of a resource returned as a string.

## Syntax

```sql
DBMS_XDB.GETCONTENTVARCHAR2(
     abspath    IN     VARCHAR2,
  RETURN BLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |

**Returns:** `BLOB`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETCONTENTVARCHAR2 Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETCONTENTVARCHAR2 Function . Syntax DBMS_XDB.GETCONTENTVARCHAR2( abspath IN VARCHAR2, RETURN BLOB; Parameters Table 194-17 GETCONTENTVARCHAR2 Function Parameters Parameter Description abspath Absolute path of the resource Return Values The contents of the resource as a string.