---
id: 19c__DBMS_SPM.ALTER_SQL_PLAN_BASELINE
name: DBMS_SPM.ALTER_SQL_PLAN_BASELINE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.ALTER_SQL_PLAN_BASELINE

This function changes an attribute of a single plan or all plans associated with a SQL statement using the attribute name/value format.

## Syntax

```sql
DBMS_SPM.ALTER_SQL_PLAN_BASELINE (
   sql_handle        IN VARCHAR2 := NULL,
   plan_name         IN VARCHAR2 := NULL,
   attribute_name    IN VARCHAR2,
   attribute_value   IN VARCHAR2)
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_handle | VARCHAR2 | IN | SQL statement handle. It identifies plans associated with a SQL statement for an attribute change. If NULL then plan_name must be specified. |
| plan_name | VARCHAR2 | IN | Plan name. It identifies a specific plan. Default NULL means set the attribute for all plans associated with a SQL statement identified by sql_handle . If NULL then sql_handle must be specified. |
| attribute_name | VARCHAR2 | IN | Name of plan attribute to set (see table below). |
| attribute_value | VARCHAR2) | IN | Value of plan attribute to use (see table below) |

**Returns:** `PLS_INTEGER`

## Usage Notes

Syntax DBMS_SPM.ALTER_SQL_PLAN_BASELINE ( sql_handle IN VARCHAR2 := NULL, plan_name IN VARCHAR2 := NULL, attribute_name IN VARCHAR2, attribute_value IN VARCHAR2) RETURN PLS_INTEGER; Parameters Table 161-4 ALTER_SQL_PLAN_BASELINE Function Parameters Parameter Description sql_handle SQL statement handle. It identifies plans associated with a SQL statement for an attribute change. If NULL then plan_name must be specified. plan_name Plan name. It identifies a specific plan. Default NULL means set the attribute for all plans associated with a SQL statement identified by sql_handle . If NULL then sql_handle must be specified. attribute_name Name of plan attribute to set (see table below). attribute_value Value of plan attribute to use (see table below) Table 161-5 Names & Values for ALTER_SQL_PLAN_BASELINE Function Parameters Name Description Possible Values enabled ' YES ' means the plan is available for use by the optimizer. It may or may not be used depending on accepted status. ' YES ' or ' NO ' fixed ' YES ' means the SQL plan baseline is not evolved over time. A fixed plan takes precedence over a non-fixed plan. ' YES ' or ' NO ' autopurge ' YES ' means the plan is purged if it is not used for a time period. ' NO ' means it is never purged. ' YES ' or ' NO ' plan_name Name of the plan String of up to 30 characters description Plan description. String of up to 500 bytes Return Values The number of plans altered. Usage Notes When a single plan is specified, one of various statuses, or plan name, or description can be altered. When all plans for a SQL statement are specified, one of various statuses, or description can be altered. This function can be called numerous times, each time setting a different plan attribute of same plan(s) or different plan(s).