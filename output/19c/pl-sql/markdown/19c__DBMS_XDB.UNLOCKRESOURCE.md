---
id: 19c__DBMS_XDB.UNLOCKRESOURCE
name: DBMS_XDB.UNLOCKRESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.UNLOCKRESOURCE

This deprecated function unlocks the resource given a lock token and a path to the resource.

## Syntax

```sql
DBMS_XDB.UNLOCKRESOURCE(
   path     IN  VARCHAR2,
   deltoken IN  VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| path | VARCHAR2 | IN | Path name to the resource |
| deltoken | VARCHAR2) | IN | Lock token to be removed |

**Returns:** `BOOLEAN`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the UNLOCKRESOURCE Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the UNLOCKRESOURCE Function . Syntax DBMS_XDB.UNLOCKRESOURCE( path IN VARCHAR2, deltoken IN VARCHAR2) RETURN BOOLEAN; Parameters Table 194-37 UNLOCKRESOURCE Function Parameters Parameter Description path Path name to the resource deltoken Lock token to be removed Return Values TRUE if operation successful.