---
id: 19c__DBMS_AUTO_TASK_ADMIN.SET_P1_RESOURCES
name: DBMS_AUTO_TASK_ADMIN.SET_P1_RESOURCES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_TASK_ADMIN
tags: [dbms_auto_task_admin]
source_file: DBMS_AUTO_TASK_ADMIN.html
---

# DBMS_AUTO_TASK_ADMIN.SET_P1_RESOURCES

This procedure sets percentage-based resource allocation for each High Priority Consumer Group used by AUTOTASK Clients.

## Syntax

```sql
DBMS_AUTO_TASK_ADMIN.SET_P1_RESOURCES(
   stats_group_pct     OUT   NUMBER,
   seg_group_pct       OUT   NUMBER,
   tune_group_pct      OUT   NUMBER,
   health_group_pct    OUT   NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| stats_group_pct | NUMBER | OUT | %resources for Statistics Gathering |
| seq_group_pct |  |  | %resources for Space Management |
| tune_group_pct | NUMBER | OUT | %resources for SQL Tuning |
| health_group_pct | NUMBER) | OUT | %resources for Health Checks |

## Usage Notes

Syntax DBMS_AUTO_TASK_ADMIN.SET_P1_RESOURCES( stats_group_pct OUT NUMBER, seg_group_pct OUT NUMBER, tune_group_pct OUT NUMBER, health_group_pct OUT NUMBER); Parameters Table 32-9 SET_P1_RESOURCES Procedure Parameters Parameter Description stats_group_pct %resources for Statistics Gathering seq_group_pct %resources for Space Management tune_group_pct %resources for SQL Tuning health_group_pct %resources for Health Checks Usage Notes Values must be integers in the range 0 to 100, and must add up to 100 (percent), otherwise, an exception is raised.