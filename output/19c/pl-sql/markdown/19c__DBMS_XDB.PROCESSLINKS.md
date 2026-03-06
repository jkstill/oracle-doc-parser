---
id: 19c__DBMS_XDB.PROCESSLINKS
name: DBMS_XDB.PROCESSLINKS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.PROCESSLINKS

This deprecated procedure processes document links in the specified resource.

## Syntax

```sql
DBMS_XDB.PURGERESOURCEMETADATA( 
 abspath  IN  VARCHAR2,
 recurse  IN  BOOLEAN := FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path of the resource. If the path is a folder, use the recurse flag. |
| recurse | BOOLEAN | IN | Used only if abspath specifies a folder. If TRUE , process links of all resources in the folder hierarchy rooted at the specified resource. If FALSE , process links of all documents in this folder only. |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the PROCESSLINKS Procedure . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the PROCESSLINKS Procedure . Syntax DBMS_XDB.PURGERESOURCEMETADATA( abspath IN VARCHAR2, recurse IN BOOLEAN := FALSE); Parameters Table 194-31 PROCESSLINKS Procedure Parameters Parameter Description abspath Absolute path of the resource. If the path is a folder, use the recurse flag. recurse Used only if abspath specifies a folder. If TRUE , process links of all resources in the folder hierarchy rooted at the specified resource. If FALSE , process links of all documents in this folder only.