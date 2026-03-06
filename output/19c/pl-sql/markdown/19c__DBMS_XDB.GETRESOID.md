---
id: 19c__DBMS_XDB.GETRESOID
name: DBMS_XDB.GETRESOID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.GETRESOID

This deprecated procedure returns the object ID of the resource from its absolute path.

## Syntax

```sql
DBMS_XDB.GETRESOID(
   abspath IN VARCHAR2)
RETURN RAW;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath_path |  |  | Absolute path of the resource |

**Returns:** `RAW`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETRESOID Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETRESOID Function . Syntax DBMS_XDB.GETRESOID( abspath IN VARCHAR2) RETURN RAW; Parameters Table 194-23 GETRESOID Function Parameters Parameter Description abspath_path Absolute path of the resource Return Values NULL if the resource is not present.