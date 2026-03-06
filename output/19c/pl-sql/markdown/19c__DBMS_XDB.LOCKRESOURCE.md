---
id: 19c__DBMS_XDB.LOCKRESOURCE
name: DBMS_XDB.LOCKRESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.LOCKRESOURCE

Given a path to a resource, this deprecated function gets a WebDAV-style lock on that resource.

## Syntax

```sql
DBMS_XDB.LOCKRESOURCE(
   path      IN  VARCHAR2,
   depthzero IN  BOOLEAN,
   shared    IN  boolean)
RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Path name of the resource to lock. |
| depthzero | BOOLEAN | IN | Currently not supported |
| shared | boolean) | IN | Passing TRUE obtains a shared write lock |

**Returns:** `BOOLEAN`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the LOCKRESOURCE Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the LOCKRESOURCE Function . Syntax DBMS_XDB.LOCKRESOURCE( path IN VARCHAR2, depthzero IN BOOLEAN, shared IN boolean) RETURN BOOLEAN; Parameters Table 194-30 LOCKRESOURCE Function Parameters Parameter Description path Path name of the resource to lock. depthzero Currently not supported shared Passing TRUE obtains a shared write lock Return Values TRUE if successful.