---
id: 19c__DBMS_XDB_REPOS.CHANGEPRIVILEGES
name: DBMS_XDB_REPOS.CHANGEPRIVILEGES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_REPOS
tags: [dbms_xdb_repos]
source_file: DBMS_XDB_REPOS.html
---

# DBMS_XDB_REPOS.CHANGEPRIVILEGES

This function adds a specified ACE to a specified resource's ACL.

## Syntax

```sql
DBMS_XDB_REPOS.CHANGEPRIVILEGES(
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

Syntax DBMS_XDB_REPOS.CHANGEPRIVILEGES( res_path IN VARCHAR2, ace IN xmltype) RETURN PLS_INTEGER; Parameters Table 198-6 CHANGEPRIVILEGES Function Parameters Parameter Description res_path Path name of the resource for which privileges need to be changed ace An XMLType instance of the <ace> element which specifies the <principal> , the operation <grant> and the list of privileges Return Values A positive integer if the ACL was successfully modified. Usage Notes If no ACE with the same principal and the same operation ( grant / deny ) already exists in the ACL, the new ACE is added at the end of the ACL.