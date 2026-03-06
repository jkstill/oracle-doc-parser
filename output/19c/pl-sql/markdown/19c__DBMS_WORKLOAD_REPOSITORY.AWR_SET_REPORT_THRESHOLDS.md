---
id: 19c__DBMS_WORKLOAD_REPOSITORY.AWR_SET_REPORT_THRESHOLDS
name: DBMS_WORKLOAD_REPOSITORY.AWR_SET_REPORT_THRESHOLDS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.AWR_SET_REPORT_THRESHOLDS

This procedure configure specified report thresholds, including the number of rows in the report.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.AWR_SET_REPORT_THRESHOLDS(
   top_n_events         IN   NUMBER DEFAULT NULL,
   top_n_files          IN   NUMBER DEFAULT NULL,
   top_n_segments       IN   NUMBER DEFAULT NULL,
   top_n_services       IN   NUMBER DEFAULT NULL,
   top_n_sql            IN   NUMBER DEFAULT NULL,
   top_n_sql_max        IN   NUMBER DEFAULT NULL,
   top_sql_pct          IN   NUMBER DEFAULT NULL,
   shmem_threshold      IN   NUMBER DEFAULT NULL,
   versions_threshold   IN   NUMBER DEFAULT NULL,   
   top_n_disks          IN   NUMBER DEFAULT NULL,
   outlier_pct          IN   NUMBER DEFAULT NULL,
   outlier_cpu_pct      IN   NUMBER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| top_n_events | NUMBER | IN | Number of most significant wait events to be included |
| top_n_files | NUMBER | IN | Number of most active files to be included |
| top_n_segments | NUMBER | IN | Number of most active segments to be included |
| top_n_services | NUMBER | IN | Number of most active services to be included |
| top_n_sql | NUMBER | IN | Number of most significant SQL statements to be included |
| top_n_sql_max | NUMBER | IN | Number of SQL statements to be included if their activity is greater than that specified by top_sql_pct |
| top_sql_pct | NUMBER | IN | Significance threshold for SQL statements between top_n_sql and top_n_sql_max |
| shmem_threshold | NUMBER | IN | Shared memory low threshold |
| versions_threshold | NUMBER | IN | Plan version count low threshold |
| top_n_disks | NUMBER | IN | Number of cell disks with most I/O |
| outlier_pct | NUMBER | IN | Percentage of maximum capacity before displaying outliers for Exadata sections |
| outlier_cpu_pct | NUMBER | IN | Threshold for mean percentage CPU to display outliers |

## Usage Notes

Syntax DBMS_WORKLOAD_REPOSITORY.AWR_SET_REPORT_THRESHOLDS( top_n_events IN NUMBER DEFAULT NULL, top_n_files IN NUMBER DEFAULT NULL, top_n_segments IN NUMBER DEFAULT NULL, top_n_services IN NUMBER DEFAULT NULL, top_n_sql IN NUMBER DEFAULT NULL, top_n_sql_max IN NUMBER DEFAULT NULL, top_sql_pct IN NUMBER DEFAULT NULL, shmem_threshold IN NUMBER DEFAULT NULL, versions_threshold IN NUMBER DEFAULT NULL, top_n_disks IN NUMBER DEFAULT NULL, outlier_pct IN NUMBER DEFAULT NULL, outlier_cpu_pct IN NUMBER DEFAULT NULL); Parameters Table 192-23 AWR_SET_REPORT_THRESHOLDS Procedure Parameters Parameter Description top_n_events Number of most significant wait events to be included top_n_files Number of most active files to be included top_n_segments Number of most active segments to be included top_n_services Number of most active services to be included top_n_sql Number of most significant SQL statements to be included top_n_sql_max Number of SQL statements to be included if their activity is greater than that specified by top_sql_pct top_sql_pct Significance threshold for SQL statements between top_n_sql and top_n_sql_max shmem_threshold Shared memory low threshold versions_threshold Plan version count low threshold top_n_disks Number of cell disks with most I/O outlier_pct Percentage of maximum capacity before displaying outliers for Exadata sections outlier_cpu_pct Threshold for mean percentage CPU to display outliers User Notes The effect of each setting depends on the type of report being generated as well as on the underlying AWR data. Not all settings are meaningful for each report type. Invalid settings (such as negative numbers) are ignored. Settings are effective only in the context of the session that executes the AWR_SET_REPORT_THRESHOLDS procedure. For example, to get a report that lists top 12 segments as compared to the default, one can invoke as follows: DBMS_WORKLOAD_REPOSITORY.AWR_SET_REPORT_THRESHOLDS (top_n_segments=>12);