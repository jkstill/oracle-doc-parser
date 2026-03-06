---
id: 19c__V$RSRC_CONS_GROUP_HISTORY
name: V$RSRC_CONS_GROUP_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RSRC_CONS_GROUP_HISTORY.html
---

# V$RSRC_CONS_GROUP_HISTORY

V$RSRC_CONS_GROUP_HISTORY displays a history of consumer group statistics for each entry in V$RSRC_PLAN_HISTORY that has a non-NULL plan.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SEQUENCE# | NUMBER |  |
| ID | NUMBER |  |
| NAME | VARCHAR2(30) |  |
| REQUESTS | NUMBER |  |
| CPU_WAIT_TIME | NUMBER |  |
| CPU_WAITS | NUMBER |  |
| CONSUMED_CPU_TIME | NUMBER |  |
| YIELDS | NUMBER |  |
| CPU_DECISIONS | NUMBER |  |
| CPU_DECISIONS_EXCLUSIVE | NUMBER |  |
| CPU_DECISIONS_WON | NUMBER |  |
| ACTIVE_SESS_LIMIT_HIT | NUMBER |  |
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
| ACTIVE_SESS_KILLED | NUMBER |  |
| IDLE_SESS_KILLED | NUMBER |  |
| IDLE_BLKR_SESS_KILLED | NUMBER |  |
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
| PQS_COMPLETED | NUMBER |  |
| PQ_SERVERS_USED | NUMBER |  |
| PQS_QUEUED | NUMBER |  |
| PQ_ACTIVE_TIME | NUMBER |  |
| PQ_QUEUED_TIME | NUMBER |  |
| PQ_QUEUE_TIME_OUTS | NUMBER |  |
| PGA_LIMIT_SESSIONS_KILLED | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content When the STATISTICS_LEVEL is set to TYPICAL or ALL , this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources. A new window is created in V$RSRC_CON_GROUP_HISTORY when a pluggable database (PDB) changes its resource plan. The plan windows inside a PDB are not impacted by a multitenant container database (CDB) resource plan change. Since PDB plans can be set independently across different PDBs, V$RSRC_CON_GROUP_HISTORY will not cover the same time period across different PDBs. Therefore, this view is not useful for comparing statistics across different PDBs. See Also: " V$RSRC_PDB_HISTORY " " V$RSRC_PLAN_HISTORY " " STATISTICS_LEVEL " See Also: " V$RSRC_PDB_HISTORY " " V$RSRC_PLAN_HISTORY " " STATISTICS_LEVEL "