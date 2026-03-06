---
id: 19c__DBMS_XDB.PURGERESOURCEMETADATA
name: DBMS_XDB.PURGERESOURCEMETADATA
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.PURGERESOURCEMETADATA

This deprecated procedure deletes all user metadata from a resource. Schema-based metadata is removed in cascade mode, rows being deleted from the corresponding metadata tables.

## Syntax

```sql
DBMS_XDB.PURGERESOURCEMETADATA(  
 abspath  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2) | IN | Absolute path of the resource |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the PURGERESOURCEMETADATA Procedure . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the PURGERESOURCEMETADATA Procedure . Syntax DBMS_XDB.PURGERESOURCEMETADATA( abspath IN VARCHAR2); Parameters Table 194-32 PURGERESOURCEMETADATA Procedure Parameters Parameter Description abspath Absolute path of the resource