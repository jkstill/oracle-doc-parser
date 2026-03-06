---
id: 19c__DBMS_WORKLOAD_REPOSITORY
name: DBMS_WORKLOAD_REPOSITORY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPOSITORY
tags: [dbms_workload_repository]
source_file: DBMS_WORKLOAD_REPOSITORY.html
---

# DBMS_WORKLOAD_REPOSITORY

The DBMS_WORKLOAD_REPOSITORY package defines an object and associated table types.

## Syntax

```sql
TYPE awr_baseline_metric_type AS OBJECT (
   baseline_name      VARCHAR2(64),
   dbid               NUMBER NOT NULL,
   instance_number    NUMBER NOT NULL,
   beg_time           DATE NOT NULL,
   end_time           DATE NOT NULL,
   metric_id          NUMBER NOT NULL,
   metric_name        VARCHAR2(64) NOT NULL,
   metric_unit        VARCHAR2(64) NOT NULL,
   num_interval       NUMBER NOT NULL,
   interval_size      NUMBER NOT NULL,
   average            NUMBER NOT NULL,
   minimum            NUMBER NOT NULL,
   maximum            NUMBER NOT NULL);
```

## Usage Notes

OBJECT Types AWR_BASELINE_METRIC_TYPE Object Type TABLE Types AWR_BASELINE_METRIC_TYPE_TABLE Table Type AWRRPT_INSTANCE_LIST_TYPE Table Type Syntax TYPE awr_baseline_metric_type AS OBJECT ( baseline_name VARCHAR2(64), dbid NUMBER NOT NULL, instance_number NUMBER NOT NULL, beg_time DATE NOT NULL, end_time DATE NOT NULL, metric_id NUMBER NOT NULL, metric_name VARCHAR2(64) NOT NULL, metric_unit VARCHAR2(64) NOT NULL, num_interval NUMBER NOT NULL, interval_size NUMBER NOT NULL, average NUMBER NOT NULL, minimum NUMBER NOT NULL, maximum NUMBER NOT NULL); Fields Table 192-1 AWR_BASELINE_METRIC_TYPE Fields Field Description baseline_name Name of the Baseline dbid Database ID for the snapshot instance_number Instance number for the snapshot beg_time Begin time of the interval end_time End time of the interval metric_id Metric ID metric_name Metric name metric_unit Unit of measurement num_interval Number of intervals observed interval_size Interval size (in hundredths of a second) average Average over the period minimum Minimum value observed maximum Maximum value observed Syntax CREATE TYPE awr_baseline_metric_type_table AS TABLE OF awr_baseline_metric_type;