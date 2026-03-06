---
id: 19c__DBMS_XDB.CHECKPRIVILEGES
name: DBMS_XDB.CHECKPRIVILEGES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.CHECKPRIVILEGES

This function checks access privileges granted to the current user on the specified resource.

## Syntax

```sql
DBMS_XDB.CHECKPRIVILEGES(
   res_path   IN  VARCHAR2,
   privs      IN  xmltype)
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res_path | VARCHAR2 | IN | Absolute path in the Hierarchy for resource |
| privs | xmltype) | IN | An XMLType instance of the privilege element specifying the requested set of access privileges |

**Returns:** `PLS_INTEGER`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CHECKPRIVILEGES Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CHECKPRIVILEGES Function . Syntax DBMS_XDB.CHECKPRIVILEGES( res_path IN VARCHAR2, privs IN xmltype) RETURN PLS_INTEGER; Parameters Table 194-7 CHECKPRIVILEGES Function Parameters Parameter Description res_path Absolute path in the Hierarchy for resource privs An XMLType instance of the privilege element specifying the requested set of access privileges Return Values A positive integer if all requested privileges granted.