---
id: 19c__DBMS_SQLDIAG.GET_FIX_CONTROL
name: DBMS_SQLDIAG.GET_FIX_CONTROL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.GET_FIX_CONTROL

This function returns the value of fix control for a given bug number.

## Syntax

```sql
DBMS_SQLDIAG.GET_FIX_CONTROL (
    bug_number   IN    NUMBER)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| bug_number | NUMBER) | IN | Bug number |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_SQLDIAG.GET_FIX_CONTROL ( bug_number IN NUMBER) RETURN NUMBER; Parameters Table 165-23 GET_FIX_CONTROL Function Parameters Parameter Description bug_number Bug number