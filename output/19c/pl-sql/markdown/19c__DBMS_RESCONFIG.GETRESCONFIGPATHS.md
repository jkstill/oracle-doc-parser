---
id: 19c__DBMS_RESCONFIG.GETRESCONFIGPATHS
name: DBMS_RESCONFIG.GETRESCONFIGPATHS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.GETRESCONFIGPATHS

This function returns a list of resource configuration paths defined in the target resource's configuration list.

## Syntax

```sql
DBMS_RESCONFIG.GETRESCONFIGPATHS(
   respath IN VARCHAR2)  
 RETURN XDB$STRING_LIST_T;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| respath | VARCHAR2) | IN | Absolute path of the target resource |

**Returns:** `XDB$STRING_LIST_T`

## Usage Notes

Syntax DBMS_RESCONFIG.GETRESCONFIGPATHS( respath IN VARCHAR2) RETURN XDB$STRING_LIST_T; Parameters Table 141-10 GETRESCONFIGPATHS Function Parameters Parameter Description respath Absolute path of the target resource Usage Notes Users must be able to access all the referenced resource configurations; otherwise, an error is returned.