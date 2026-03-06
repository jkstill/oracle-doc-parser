---
id: 19c__DBMS_RESCONFIG.GETREPOSITORYRESCONFIGPATHS
name: DBMS_RESCONFIG.GETREPOSITORYRESCONFIGPATHS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.GETREPOSITORYRESCONFIGPATHS

This function returns a list of resource configuration paths defined for the repository.

## Syntax

```sql
DBMS_RESCONFIG.GETREPOSITORYRESCONFIGPATHS
 RETURN XDB$STRING_LIST_T;
```

**Returns:** `XDB$STRING_LIST_T`

## Usage Notes

Syntax DBMS_RESCONFIG.GETREPOSITORYRESCONFIGPATHS RETURN XDB$STRING_LIST_T; Usage Notes Users must be able to access all the referenced resource configurations; otherwise, an error is returned.