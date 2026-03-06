---
id: 19c__DBMS_RESCONFIG.GETRESCONFIG
name: DBMS_RESCONFIG.GETRESCONFIG
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESCONFIG
tags: [dbms_resconfig]
source_file: DBMS_RESCONFIG.html
---

# DBMS_RESCONFIG.GETRESCONFIG

This function returns the resource configuration at the specified position of the target resource's configuration list.

## Syntax

```sql
DBMS_RESCONFIG.GETRESCONFIG(
   respath IN VARCHAR2,  
   pos IN PLS_INTEGER)
 RETURN XMLTYPE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| respath | VARCHAR2 | IN | Absolute path of the target resource |
| pos | PLS_INTEGER) | IN | Index of element to return. An exception is raised if the index is out of range ( pos < 0 or pos >= the size of the target resource's configuration list). |

**Returns:** `XMLTYPE`

## Usage Notes

Syntax DBMS_RESCONFIG.GETRESCONFIG( respath IN VARCHAR2, pos IN PLS_INTEGER) RETURN XMLTYPE; Parameters Table 141-9 GETRESCONFIG Function Parameters Parameter Description respath Absolute path of the target resource pos Index of element to return. An exception is raised if the index is out of range ( pos < 0 or pos >= the size of the target resource's configuration list). Usage Notes Users must have the required read privilege on the requested resource configuration; otherwise, an error is returned.