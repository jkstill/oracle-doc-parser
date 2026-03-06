---
id: 19c__DBMS_SPM.DROP_SQL_PLAN_BASELINE
name: DBMS_SPM.DROP_SQL_PLAN_BASELINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.DROP_SQL_PLAN_BASELINE

This function drops a single plan, or all plans associated with a SQL statement.

## Syntax

```sql
DBMS_SPM.DROP_SQL_PLAN_BASELINE (
   sql_handle     IN VARCHAR2 := NULL,
   plan_name      IN VARCHAR2 := NULL)
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_handle | VARCHAR2 | IN | SQL statement handle. It identifies plans associated with a SQL statement that are to be dropped. If NULL then plan_name must be specified. |
| plan_name | VARCHAR2 | IN | Plan name. It identifies a specific plan. Default NULL means to drop all plans associated with the SQL statement identified by sql_handle . |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_SPM.DROP_SQL_PLAN_BASELINE ( sql_handle IN VARCHAR2 := NULL, plan_name IN VARCHAR2 := NULL) RETURN PLS_INTEGER; Parameters Table 161-13 DROP_SQL_PLAN_BASELINE Function Parameters Parameter Description sql_handle SQL statement handle. It identifies plans associated with a SQL statement that are to be dropped. If NULL then plan_name must be specified. plan_name Plan name. It identifies a specific plan. Default NULL means to drop all plans associated with the SQL statement identified by sql_handle . Return Values The number of plans dropped