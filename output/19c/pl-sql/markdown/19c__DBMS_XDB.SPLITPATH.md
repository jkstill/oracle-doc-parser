---
id: 19c__DBMS_XDB.SPLITPATH
name: DBMS_XDB.SPLITPATH
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.SPLITPATH

This deprecated procedure splits the path into a parentpath and childpath.

## Syntax

```sql
DBMS_XDB.SPLITPATH(
      abspath     IN  VARCHAR2,
      parentpath  OUT VARCHAR2,
     childpath    OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath | VARCHAR2 | IN | Absolute path to be split |
| parentpath | VARCHAR2 | OUT | Parentpath |
| childpath | VARCHAR2) | OUT | Childpath |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the SPLITPATH Procedure . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the SPLITPATH Procedure . Syntax DBMS_XDB.SPLITPATH( abspath IN VARCHAR2, parentpath OUT VARCHAR2, childpath OUT VARCHAR2); Parameters Table 194-35 SPLITPATH Procedure Parameters Parameter Description abspath Absolute path to be split parentpath Parentpath childpath Childpath