---
id: 19c__DBMS_WORKLOAD_REPLAY.CREATE_FILTER_SET
name: DBMS_WORKLOAD_REPLAY.CREATE_FILTER_SET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_REPLAY
tags: [dbms_workload_replay]
source_file: DBMS_WORKLOAD_REPLAY.html
---

# DBMS_WORKLOAD_REPLAY.CREATE_FILTER_SET

This procedure creates a new filter set for the replays at replay_dir .

## Syntax

```sql
DBMS_WORKLOAD_REPLAY.CREATE_FILTER_SET(
   replay_dir       IN  VARCHAR2,
   filter_set       IN  VARCHAR2,
   default_action   IN  VARCHAR2 DEFAULT 'INCLUDE');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| replay_dir | VARCHAR2 | IN | Object directory of the replay to be filtered |
| filter_set | VARCHAR2 | IN | Name of the filter set to create (to use in USE_FILTER_SET Procedure ) |
| default_action | VARCHAR2 | IN | Can be either INCLUDE or EXCLUDE . Determines whether, by default, every captured call must be replayed or not. Also determines whether the workload filters specified must be considered as INCLUSION filters or EXCLUSION filters.) If it is INCLUDE , then by default all captured calls are replayed, except for the part of the workload defined by the filters. In this case, all the filters that were specified using the ADD_SCHEDULE_ORDERING Function are treated as EXCLUSION filters, and will determine the workload that will not be replayed. If it is EXCLUDE , then by default no captured call to the database is replayed, except for the part of the workload defined by the filters. In this case, all the filters that were specified using he ADD_SCHEDULE_ORDERING Function are treated as INCLUSION filters, and will determine the workload that is replayed. Default: INCLUDE and all the filters specified are assumed to be EXCLUSION filters |

## Usage Notes

It includes all the replay filters that have already been added by the ADD_FILTER Procedure . After the procedure has completed and replay initiated, the newly-created filter set can be used to filter the replay in replay_dir by calling the USE_FILTER_SET Procedure . Syntax DBMS_WORKLOAD_REPLAY.CREATE_FILTER_SET( replay_dir IN VARCHAR2, filter_set IN VARCHAR2, default_action IN VARCHAR2 DEFAULT 'INCLUDE'); Parameters Table 191-11 CREATE_FILTER_SET Procedure Parameters Parameter Description replay_dir Object directory of the replay to be filtered filter_set Name of the filter set to create (to use in USE_FILTER_SET Procedure ) default_action Can be either INCLUDE or EXCLUDE . Determines whether, by default, every captured call must be replayed or not. Also determines whether the workload filters specified must be considered as INCLUSION filters or EXCLUSION filters.) If it is INCLUDE , then by default all captured calls are replayed, except for the part of the workload defined by the filters. In this case, all the filters that were specified using the ADD_SCHEDULE_ORDERING Function are treated as EXCLUSION filters, and will determine the workload that will not be replayed. If it is EXCLUDE , then by default no captured call to the database is replayed, except for the part of the workload defined by the filters. In this case, all the filters that were specified using he ADD_SCHEDULE_ORDERING Function are treated as INCLUSION filters, and will determine the workload that is replayed. Default: INCLUDE and all the filters specified are assumed to be EXCLUSION filters Usage Notes This operation must be invoked when no replay is initialized, prepared, or in progress.