---
id: 19c__DBMS_XDB.CHANGEPRIVILEGES
name: DBMS_XDB.CHANGEPRIVILEGES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB
tags: [dbms_xdb]
source_file: DBMS_XDB.html
---

# DBMS_XDB.CHANGEPRIVILEGES

This function adds a specified ACE to a specified resource's ACL. This procedure is deprecated in Release 12 c .

## Syntax

```sql
DBMS_XDB.CHANGEPRIVILEGES(
   res_path   IN    VARCHAR2,
   ace        IN    xmltype)
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| res_path | VARCHAR2 | IN | Path name of the resource for which privileges need to be changed |
| ace | xmltype) | IN | An XMLType instance of the <ace> element which specifies the <principal> , the operation <grant> and the list of privileges |

**Returns:** `PLS_INTEGER`

## Usage Notes

Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CHANGEPRIVILEGES Function . Note: This procedure is deprecated in Release 12 c . This functionality is replaced by a subprogram of the same name in the DBMS_XDB_REPOS package - the CHANGEPRIVILEGES Function . Syntax DBMS_XDB.CHANGEPRIVILEGES( res_path IN VARCHAR2, ace IN xmltype) RETURN PLS_INTEGER; Parameters Table 194-6 CHANGEPRIVILEGES Function Parameters Parameter Description res_path Path name of the resource for which privileges need to be changed ace An XMLType instance of the <ace> element which specifies the <principal> , the operation <grant> and the list of privileges Return Values A positive integer if the ACL was successfully modified.