---
id: 19c__DBA_HIST_RSRC_PLAN
name: DBA_HIST_RSRC_PLAN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_RSRC_PLAN.html
---

# DBA_HIST_RSRC_PLAN

DBA_HIST_RSRC_PLAN displays historical information about resource plans.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| SEQUENCE# | NUMBER | A sequential counter that uniquely describes a row. When the instance is restarted, this value is reset to zero. |
| START_TIME | DATE | Time that the resource plan was enabled |
| END_TIME | DATE | Time that the resource plan was disabled; NULL if the row contains the current resource plan information |
| PLAN_ID | NUMBER | Resource plan ID; NULL if the Resource Manager was disabled |
| PLAN_NAME | VARCHAR2(128) | Resource plan name; NULL if the Resource Manager was disabled |
| CPU_MANAGED | VARCHAR2(4) | Indicates whether the resource plan has parameters that specify a policy for how the Resource Manager should schedule sessions to manage CPU usage ( ON ) or whether Resource Manager is not managing CPU usage ( OFF ) |
| PARALLEL_EXECUTION_MANAGED | VARCHAR2(4) | State of parallel statement queuing: OFF - Parallel statement queuing is disabled STARTUP - Parallel statement queuing is enabled. This is a temporary state that can occur when an Oracle RAC database is undergoing configuration changes FIFO - Parallel statement queuing is enabled. All parallel statements are managed in a single Oracle RAC FIFO queue FULL - Parallel statement queuing is enabled. All parallel statements are managed in per-consumer group queues according to the current resource plan. This state is used when a resource plan that contains resource allocation directives ( MGMT_P* ) is enabled. |
| INSTANCE_CAGING | VARCHAR2(4) | Indicates whether instance caging is enabled ( ON ) or disabled ( OFF ). Instance caging is enabled if the CPU_COUNT initialization parameter is explicitly modified to a value other than 0 and Resource Manager is enabled. |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$RSRC_PLAN_HISTORY . See Also: " V$RSRC_PLAN_HISTORY " See Also: " V$RSRC_PLAN_HISTORY "