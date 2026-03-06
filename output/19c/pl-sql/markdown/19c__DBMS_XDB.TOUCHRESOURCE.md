---
id: 19c__DBMS_XDB.TOUCHRESOURCE
name: DBMS_XDB.TOUCHRESOURCE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.TOUCHRESOURCE

This deprecated procedure changes the modification time of the resource to the current time.

## Syntax

```sql
DBMS_XDB.TOUCHRESOURCE 
     abspath    IN     VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| abspath_path |  |  | Absolute path of the resource |

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the TOUCHRESOURCE Procedure . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the TOUCHRESOURCE Procedure . Syntax DBMS_XDB.TOUCHRESOURCE abspath IN VARCHAR2); Parameters Table 194-36 DBMS_XDB.TOUCHRESOURCE Procedure Parameters Parameter Description abspath_path Absolute path of the resource