---
id: 19c__DBMS_WORKLOAD_REPOSITORY.MODIFY_BASELINE_WINDOW_SIZE
name: DBMS_WORKLOAD_REPOSITORY.MODIFY_BASELINE_WINDOW_SIZE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.MODIFY_BASELINE_WINDOW_SIZE

This procedure modifies the window size for the Default Moving Window Baseline.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.MODIFY_BASELINE_WINDOW_SIZE(
   window_size    IN   NUMBER,
   dbid           IN   NUMBER   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| window_size | NUMBER | IN | New Window size for the default Moving Window Baseline, in number of days. |
| dbid | NUMBER | IN | Database ID (defaults to local DBID). |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.MODIFY_BASELINE_WINDOW_SIZE( window_size IN NUMBER, dbid IN NUMBER DEFAULT NULL); Parameters Table 192-34 MODIFY_BASELINE_WINDOW_SIZE Procedure Parameters Parameter Description window_size New Window size for the default Moving Window Baseline, in number of days. dbid Database ID (defaults to local DBID). Usage Notes The window size must be less than or equal to the AWR retention setting. If the window size needs to be greater than the retention setting, the MODIFY_SNAPSHOT_SETTINGS Procedures can be used to adjust the retention setting. A moving window can be set to a maximum of 13 weeks.