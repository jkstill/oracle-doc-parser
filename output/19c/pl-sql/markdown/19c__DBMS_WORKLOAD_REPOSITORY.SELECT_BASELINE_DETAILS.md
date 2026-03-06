---
id: 19c__DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_DETAILS
name: DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_DETAILS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_DETAILS

This table function shows the values of the metrics corresponding to a baseline for a range of snapshots.

## Syntax

```sql
DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_DETAILS(
   l_baseline_id   IN  NUMBER,   
   l_begin_snap    IN  NUMBER DEFAULT NULL,
   l_end_snap      IN  NUMBER DEFAULT NULL,
   l_dbid          IN  NUMBER DEFAULT NULL)
 RETURN awrbl_details_type_table PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| l_baseline_id | NUMBER | IN | ID of the baseline for which the statistics need to be retrieved. Specifying the value 0 returns the statistics for the moving window baseline. |
| l_begin_snap | NUMBER | IN | Start snapshot sequence number for the baseline. |
| l_end_snap | NUMBER | IN | End snapshot sequence number for the baseline. |
| l_dbid | NUMBER | IN | Database identifier for the baseline. If its value is set to NULL , then the database identifier for the local database is used. Its default value is NULL . |

**Returns:** `awrbl_details_type_table`

## Usage Notes

This table function returns an object of AWR_BASELINE_METRIC_TYPE Object Type . Syntax DBMS_WORKLOAD_REPOSITORY.SELECT_BASELINE_DETAILS( l_baseline_id IN NUMBER, l_begin_snap IN NUMBER DEFAULT NULL, l_end_snap IN NUMBER DEFAULT NULL, l_dbid IN NUMBER DEFAULT NULL) RETURN awrbl_details_type_table PIPELINED; Parameters Table 192-40 SELECT_BASELINE_DETAILS Function Parameters Parameter Description l_baseline_id ID of the baseline for which the statistics need to be retrieved. Specifying the value 0 returns the statistics for the moving window baseline. l_begin_snap Start snapshot sequence number for the baseline. l_end_snap End snapshot sequence number for the baseline. l_dbid Database identifier for the baseline. If its value is set to NULL , then the database identifier for the local database is used. Its default value is NULL .