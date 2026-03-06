---
id: 19c__DBMS_XDB.EXISTSRESOURCE
name: DBMS_XDB.EXISTSRESOURCE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.EXISTSRESOURCE

This deprecated function indicates if a resource is in the hierarchy. Matches resource by a string that represents its absolute path.

## Syntax

```sql
DBMS_XDB.EXISTSRESOURCE(
   abspath    IN    VARCHAR2)
 RETURN BOOLEAN;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2) | IN | Path name of the resource whose ACL document is required |

**Returns:** `BOOLEAN`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the EXISTSRESOURCE Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the EXISTSRESOURCE Function . Syntax DBMS_XDB.EXISTSRESOURCE( abspath IN VARCHAR2) RETURN BOOLEAN; Parameters Table 194-13 EXISTSRESOURCE Function Parameters Parameter Description abspath Path name of the resource whose ACL document is required Return Values TRUE if the resource is found.