---
id: 19c__DBMS_STATS.GET_PARAM
name: DBMS_STATS.GET_PARAM
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.GET_PARAM

This function returns the default value of parameters of DBMS_STATS procedures.

## Syntax

```sql
DBMS_STATS.GET_PARAM (
   pname     IN   VARCHAR2)
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pname | VARCHAR2) | IN | Parameter name |

**Returns:** `VARCHAR2`

## Usage Notes

Note: This subprogram has been replaced by improved technology and is maintained only for purposes of backward compatibility. In this case, use the GET_PREFS Function . See also DBMS_STATS Deprecated Subprograms . Note: This subprogram has been replaced by improved technology and is maintained only for purposes of backward compatibility. In this case, use the GET_PREFS Function . See also DBMS_STATS Deprecated Subprograms . Syntax DBMS_STATS.GET_PARAM ( pname IN VARCHAR2) RETURN VARCHAR2; Parameters Table 171-65 GET_PARAM Function Parameters Parameter Description pname Parameter name Exceptions ORA-20001 : Invalid input values