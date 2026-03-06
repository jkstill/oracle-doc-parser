---
id: 19c__DBMS_WORKLOAD_REPOSITORY.RENAME_BASELINE
name: DBMS_WORKLOAD_REPOSITORY.RENAME_BASELINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.RENAME_BASELINE

This procedure renames a baseline.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.RENAME_BASELINE(
   old_baseline_name     IN   VARCHAR2,
   new_baseline_name     IN VARCHAR2,
   dbid                  IN NUMBER   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| old_baseline_name | VARCHAR2 | IN | Old baseline name. |
| new_baseline_name | VARCHAR2 | IN | New baseline name. |
| dbid | NUMBER | IN | Database ID for which the baseline needs to be renamed (defaults to local DBID). |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.RENAME_BASELINE( old_baseline_name IN VARCHAR2, new_baseline_name IN VARCHAR2, dbid IN NUMBER DEFAULT NULL); Parameters Table 192-39 RENAME_BASELINE Procedure Parameters Parameter Description old_baseline_name Old baseline name. new_baseline_name New baseline name. dbid Database ID for which the baseline needs to be renamed (defaults to local DBID).