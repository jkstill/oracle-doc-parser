---
id: 19c__DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_METRIC
name: DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_METRIC
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_METRIC

This table function shows the values of the metrics corresponding to a baseline for all the snapshots.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_METRIC(
   l_baseline_name     IN VARCHAR2,
   l_dbid              IN NUMBER DEFAULT NULL,
   l_instance_num      IN NUMBER DEFAULT NULL)
 RETURN awr_metric_type_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| l_baseline_name | VARCHAR2 | IN | Name of the baseline for which the metrics need to be viewed. |
| l_dbid | NUMBER | IN | Database identifier for the baseline. If set to NULL , the database identifier for the local database is used. Default is NULL . |
| l_instance_num | NUMBER | IN | The instance number for which the metrics need to be viewed. If set to NULL , metrics for the local database instance are shown. Default is NULL . |

**Returns:** `awr_metric_type_table`

## Usage Notes

This table function returns an object of AWR_BASELINE_METRIC_TYPE Object Type . Syntax DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_METRIC( l_baseline_name IN VARCHAR2, l_dbid IN NUMBER DEFAULT NULL, l_instance_num IN NUMBER DEFAULT NULL) RETURN awr_metric_type_table PIPELINED; Parameters Table 192-41 SELECT_BASELINE_METRIC Function Parameters Parameter Description l_baseline_name Name of the baseline for which the metrics need to be viewed. l_dbid Database identifier for the baseline. If set to NULL , the database identifier for the local database is used. Default is NULL . l_instance_num The instance number for which the metrics need to be viewed. If set to NULL , metrics for the local database instance are shown. Default is NULL .