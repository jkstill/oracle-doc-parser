---
id: 19c__DBMS_XDB.RENAMERESOURCE
name: DBMS_XDB.RENAMERESOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.RENAMERESOURCE

This deprecated procedure renames the XDB resource.

## Syntax

```sql
DBMS_XDB.RENAMERESOURCE(
   srcpath    IN  VARCHAR2,
   destfolder IN  CARCHAR2,
   newname    IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| srcpath | VARCHAR2 | IN | Absolute path in the Hierarchy for the source resource destination folder |
| destfolder | CARCHAR2 | IN | Absolute path in the Hierarchy for the destination folder |
| newname | VARCHAR2) | IN | Name of the child in the destination folder |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the RENAMERESOURCE Procedure . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the RENAMERESOURCE Procedure . Syntax DBMS_XDB.RENAMERESOURCE( srcpath IN VARCHAR2, destfolder IN CARCHAR2, newname IN VARCHAR2); Parameters Table 194-33 RENAMERESOURCE Procedure Parameters Parameter Description srcpath Absolute path in the Hierarchy for the source resource destination folder destfolder Absolute path in the Hierarchy for the destination folder newname Name of the child in the destination folder