---
id: 19c__V$RSRC_PDB_HISTORY
name: V$RSRC_PDB_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RSRC_PDB_HISTORY.html
---

# V$RSRC_PDB_HISTORY

V$RSRC_PDB_HISTORY displays a history of consumer group statistics for each entry in V$RSRC_PDB that has a non-NULL plan by pluggable database (PDB).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SEQUENCE# | NUMBER |  |
| PDB_NAME | VARCHAR2(32) |  |
| CPU_WAIT_TIME | NUMBER |  |
| CPU_WAITS | NUMBER |  |
| CONSUMED_CPU_TIME | NUMBER |  |
| YIELDS | NUMBER |  |
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
| CON_ID | NUMBER |  |

## Usage Notes

When the STATISTICS_LEVEL is set to TYPICAL or ALL , this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources. A new window is created in V$RSRC_PDB_HISTORY when a multitenant container database (CDB) changes its resource plan. The plan windows for the CDB are not impacted by a PDB resource plan change. V$RSRC_PDB_HISTORY covers the same time period for all PDBs. This view is specifically designed for comparing statistics across different PDBs. Since V$RSRC_PDB_HISTORY does not contain information at the consumer group level, it is not useful for comparing consumer groups inside a PDB. See Also: " V$RSRC_CONS_GROUP_HISTORY " See Also: " V$RSRC_CONS_GROUP_HISTORY "