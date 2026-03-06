---
id: 19c__DBMS_XDB.GETPRIVILEGES
name: DBMS_XDB.GETPRIVILEGES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.GETPRIVILEGES

This deprecated function gets all privileges granted to the current user on a specified resource.

## Syntax

```sql
DBMS_XDB.GETPRIVILEGES(
   res_path    IN     VARCHAR2)
 RETURN sys.xmltype;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res_path | VARCHAR2) | IN | Absolute path in the hierarchy of the resource |

**Returns:** `sys.xmltype`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETPRIVILEGES Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the GETPRIVILEGES Function . Syntax DBMS_XDB.GETPRIVILEGES( res_path IN VARCHAR2) RETURN sys.xmltype; Parameters Table 194-22 GETPRIVILEGES Function Parameters Parameter Description res_path Absolute path in the hierarchy of the resource Return Values An XMLType instance of <privilege> element, which contains the list of all leaf privileges granted on this resource to the current user.