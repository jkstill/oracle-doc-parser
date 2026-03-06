---
id: 19c__DBMS_XDB.CHANGEOWNER
name: DBMS_XDB.CHANGEOWNER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.CHANGEOWNER

This procedure changes the owner of the resource/s to the specified owner. This procedure is deprecated in Release 12 c .

## Syntax

```sql
DBMS_XDB.CHANGEOWNER(
     abspath    IN   VARCHAR2,
     owner      IN   VARCHAR2,
     recurse    IN   BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource |
| owner | VARCHAR2 | IN | New owner for the resource |
| recurse | BOOLEAN | IN | If TRUE , recursively change owner of all resources in the folder tree |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CHANGEOWNER Procedure . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CHANGEOWNER Procedure . Syntax DBMS_XDB.CHANGEOWNER( abspath IN VARCHAR2, owner IN VARCHAR2, recurse IN BOOLEAN := FALSE); Parameters Table 194-5 CHANGEOWNER Procedure Parameters Parameter Description abspath Absolute path of the resource owner New owner for the resource recurse If TRUE , recursively change owner of all resources in the folder tree