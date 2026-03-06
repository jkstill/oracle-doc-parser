---
id: 19c__DBMS_XPLAN.DISPLAY_SQL_PLAN_BASELINE
name: DBMS_XPLAN.DISPLAY_SQL_PLAN_BASELINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XPLAN
tags: [dbms_xplan]
source_file: DBMS_XPLAN.html
---

# DBMS_XPLAN.DISPLAY_SQL_PLAN_BASELINE

This table function displays one or more execution plans for the specified SQL handle of a SQL plan baseline.

## Syntax

```sql
DBMS_XPLAN.DISPLAY_SQL_PLAN_BASELINE (
   sql_handle      IN VARCHAR2 := NULL,
   plan_name       IN VARCHAR2 := NULL,
   format          IN VARCHAR2 := 'TYPICAL')
 RETURN dbms_xplan_type_table;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_handle | VARCHAR2 | IN | SQL statement handle. It identifies a SQL statement whose plans are to be displayed. |
| plan_name | VARCHAR2 | IN | Plan name. It identifies a specific plan. Default NULL means all plans associated with identified SQL statement are explained and displayed. |
| format | VARCHAR2 | IN | Format string determines what information stored in the plan displayed. The following format values are possible, each representing a common use case: BASIC , TYPICAL , and ALL . |

**Returns:** `dbms_xplan_type_table`

## Usage Notes

Syntax DBMS_XPLAN.DISPLAY_SQL_PLAN_BASELINE ( sql_handle IN VARCHAR2 := NULL, plan_name IN VARCHAR2 := NULL, format IN VARCHAR2 := 'TYPICAL') RETURN dbms_xplan_type_table; Parameters Table 215-9 DISPLAY_SQL_PLAN_BASELINE Function Parameters Parameter Description sql_handle SQL statement handle. It identifies a SQL statement whose plans are to be displayed. plan_name Plan name. It identifies a specific plan. Default NULL means all plans associated with identified SQL statement are explained and displayed. format Format string determines what information stored in the plan displayed. The following format values are possible, each representing a common use case: BASIC , TYPICAL , and ALL . Return Values A PL/SQL type table Usage Notes This function uses plan information stored in the plan baseline to explain and display the plans. The plan_id stored in the SQL management base may not match the plan_id of the generated plan. A mismatch between the stored plan_id and generated plan_id means that it is a non-reproducible plan. Such a plan is deemed invalid and is bypassed by the optimizer during SQL compilation. Examples Display all plans of a SQL statement identified by the SQL handle SYS_SQL_b1d49f6074ab95af using TYPICAL format SET LINESIZE 150 SET PAGESIZE 2000 SELECT t.* FROM TABLE(DBMS_XPLAN.DISPLAY_SQL_PLAN_BASELINE('SYS_SQL_b1d49f6074ab95af')) t; Display all plans of one or more SQL statements containing the string HR2 using BASIC format: SET LINESIZE 150 SET PAGESIZE 2000 SELECT t.* FROM (SELECT DISTINCT sql_handle FROM dba_sql_plan_baselines WHERE sql_text LIKE '%HR2%') pb, TABLE(DBMS_XPLAN.DISPLAY_SQL_PLAN_BASELINE(pb.sql_handle, NULL, 'BASIC')) t;