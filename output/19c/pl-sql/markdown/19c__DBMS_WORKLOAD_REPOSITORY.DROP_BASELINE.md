---
id: 19c__DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE
name: DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE

This procedure drops a previously-defined baseline.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE(
   baseline_name  IN  VARCHAR2,
   cascade        IN  BOOLEAN  DEFAULT FALSE,
   dbid           IN  NUMBER   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| baseline_name | VARCHAR2 | IN | Name of baseline to drop from the system |
| cascade | BOOLEAN | IN | If TRUE , the pair of snapshots associated with the baseline will also be dropped. Otherwise, only the baseline is removed. |
| dbid | NUMBER | IN | Database ID for which the baseline needs to be dropped (defaults to local DBID). |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE( baseline_name IN VARCHAR2, cascade IN BOOLEAN DEFAULT FALSE, dbid IN NUMBER DEFAULT NULL); Parameters Table 192-31 DROP_BASELINE Parameters Parameter Description baseline_name Name of baseline to drop from the system cascade If TRUE , the pair of snapshots associated with the baseline will also be dropped. Otherwise, only the baseline is removed. dbid Database ID for which the baseline needs to be dropped (defaults to local DBID). Examples This example drops the baseline ' oltp_peakload_bl ' without dropping the underlying snapshots: EXECUTE DBMS_WORKLOAD_REPOSITORY.DROP_BASELINE ( baseline_name => 'oltp_peakload_bl'); If you query the DBA_HIST_BASELINE view after the DROP_BASELINE action, you will see the specified baseline definition is removed. You can query the DBA_HIST_SNAPSHOT view to find that the underlying snapshots are left intact.