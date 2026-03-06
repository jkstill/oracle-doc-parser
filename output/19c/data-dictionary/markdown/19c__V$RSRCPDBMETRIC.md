---
id: 19c__V$RSRCPDBMETRIC
name: V$RSRCPDBMETRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RSRCPDBMETRIC.html
---

# V$RSRCPDBMETRIC

V$RSRCPDBMETRIC displays information about resources consumed and wait times per PDB.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| CPU_CONSUMED_TIME | NUMBER |  |
| CPU_WAIT_TIME | NUMBER |  |
| NUM_CPUS | NUMBER |  |
| RUNNING_SESSIONS_LIMIT | NUMBER |  |
| AVG_RUNNING_SESSIONS | NUMBER |  |
| AVG_WAITING_SESSIONS | NUMBER |  |
| CPU_UTILIZATION_LIMIT | NUMBER |  |
| AVG_CPU_UTILIZATION | NUMBER |  |
| IOPS | NUMBER |  |
| IOMBPS | NUMBER |  |
| IOPS_THROTTLE_EXEMPT | NUMBER |  |
| IOMBPS_THROTTLE_EXEMPT | NUMBER |  |
| AVG_IO_THROTTLE | NUMBER |  |
| AVG_ACTIVE_PARALLEL_STMTS | NUMBER |  |
| AVG_QUEUED_PARALLEL_STMTS | NUMBER |  |
| AVG_ACTIVE_PARALLEL_SERVERS | NUMBER |  |
| AVG_QUEUED_PARALLEL_SERVERS | NUMBER |  |
| PARALLEL_SERVERS_LIMIT | NUMBER |  |
| SGA_BYTES | NUMBER |  |
| BUFFER_CACHE_BYTES | NUMBER |  |
| SHARED_POOL_BYTES | NUMBER |  |
| PGA_BYTES | NUMBER |  |
| PLAN_NAME | VARCHAR2(30) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content When the STATISTICS_LEVEL is set to TYPICAL or ALL , this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources. Metrics are collected and stored every minute when CPU utilization is not being monitored. See Also: " STATISTICS_LEVEL " See Also: " STATISTICS_LEVEL "