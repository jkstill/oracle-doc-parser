---
id: 19c__V$RSRC_CONSUMER_GROUP
name: V$RSRC_CONSUMER_GROUP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RSRC_CONSUMER_GROUP.html
---

# V$RSRC_CONSUMER_GROUP

V$RSRC_CONSUMER_GROUP displays data related to currently active resource consumer groups.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| NAME | VARCHAR2(32) |  |
| ACTIVE_SESSIONS | NUMBER |  |
| EXECUTION_WAITERS | NUMBER |  |
| REQUESTS | NUMBER |  |
| CPU_WAIT_TIME | NUMBER |  |
| CPU_WAITS | NUMBER |  |
| CONSUMED_CPU_TIME | NUMBER |  |
| YIELDS | NUMBER |  |
| CPU_DECISIONS | NUMBER |  |
| CPU_DECISIONS_EXCLUSIVE | NUMBER |  |
| CPU_DECISIONS_WON | NUMBER |  |
| QUEUE_LENGTH | NUMBER |  |
| CURRENT_UNDO_CONSUMPTION | NUMBER |  |
| ACTIVE_SESSION_LIMIT_HIT | NUMBER |  |
| UNDO_LIMIT_HIT | NUMBER |  |
| SWITCHES_IN_CPU_TIME | NUMBER |  |
| SWITCHES_OUT_CPU_TIME | NUMBER |  |
| SWITCHES_IN_IO_MEGABYTES | NUMBER |  |
| SWITCHES_OUT_IO_MEGABYTES | NUMBER |  |
| SWITCHES_IN_IO_REQUESTS | NUMBER |  |
| SWITCHES_OUT_IO_REQUESTS | NUMBER |  |
| SWITCHES_IN_IO_LOGICAL | NUMBER |  |
| SWITCHES_OUT_IO_LOGICAL | NUMBER |  |
| SWITCHES_IN_ELAPSED_TIME | NUMBER |  |
| SWITCHES_OUT_ELAPSED_TIME | NUMBER |  |
| SQL_CANCELED | NUMBER |  |
| ACTIVE_SESSIONS_KILLED | NUMBER |  |
| IDLE_SESSIONS_KILLED | NUMBER |  |
| IDLE_BLKR_SESSIONS_KILLED | NUMBER |  |
| QUEUED_TIME | NUMBER |  |
| QUEUE_TIME_OUTS | NUMBER |  |
| IO_SERVICE_TIME | NUMBER |  |
| IO_SERVICE_WAITS | NUMBER |  |
| SMALL_READ_MEGABYTES | NUMBER |  |
| SMALL_WRITE_MEGABYTES | NUMBER |  |
| LARGE_READ_MEGABYTES | NUMBER |  |
| LARGE_WRITE_MEGABYTES | NUMBER |  |
| SMALL_READ_REQUESTS | NUMBER |  |
| SMALL_WRITE_REQUESTS | NUMBER |  |
| LARGE_READ_REQUESTS | NUMBER |  |
| LARGE_WRITE_REQUESTS | NUMBER |  |
| CURRENT_PQS_ACTIVE | NUMBER |  |
| CURRENT_PQ_SERVERS_ACTIVE | NUMBER |  |
| PQS_QUEUED | NUMBER |  |
| PQS_COMPLETED | NUMBER |  |
| PQ_SERVERS_USED | NUMBER |  |
| PQ_ACTIVE_TIME | NUMBER |  |
| CURRENT_PQS_QUEUED | NUMBER |  |
| PQ_QUEUED_TIME | NUMBER |  |
| PQ_QUEUE_TIME_OUTS | NUMBER |  |
| PGA_LIMIT_SESSIONS_KILLED | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content When the STATISTICS_LEVEL is set to TYPICAL or ALL , this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources. Statistics in V$RSRC_CONSUMER_GROUP are reset when a pluggable database (PDB) changes its resource plan. They are not impacted by multitenant container database (CDB) resource plan changes. Since PDB plans can be set independently across different PDBs, V$RSRC_CONSUMER_GROUP will not cover the same time period across different PDBs. Therefore, this view is not useful for comparing statistics across different PDBs. See Also: " STATISTICS_LEVEL " " V$RSRC_PDB " Oracle Database Administrator’s Guide for information on resource groups Oracle Database PL/SQL Packages and Types Reference for information on creating resource groups with the DBMS_RESOURCE_MANAGER package See Also: " STATISTICS_LEVEL " " V$RSRC_PDB " Oracle Database Administrator’s Guide for information on resource groups Oracle Database PL/SQL Packages and Types Reference for information on creating resource groups with the DBMS_RESOURCE_MANAGER package