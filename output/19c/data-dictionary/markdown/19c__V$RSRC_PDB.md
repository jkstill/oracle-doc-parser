---
id: 19c__V$RSRC_PDB
name: V$RSRC_PDB
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RSRC_PDB.html
---

# V$RSRC_PDB

V$RSRC_PDB displays data related to currently active resource consumer groups by pluggable database (PDB).

## Columns

| Column | Type | Description |
|--------|------|-------------|
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
| CURRENT_PQS_ACTIVE | NUMBER |  |
| CURRENT_PQ_SERVERS_ACTIVE | NUMBER |  |
| CURRENT_PQS_QUEUED | NUMBER |  |
| SGA_BYTES | NUMBER |  |
| BUFFER_CACHE_BYTES | NUMBER |  |
| SHARED_POOL_BYTES | NUMBER |  |
| PGA_BYTES | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content When the STATISTICS_LEVEL is set to TYPICAL or ALL , this view contains information about CPU utilization and wait times even when no Resource Manager plan is set or when the Resource Manager plan does not monitor CPU or session resources. Statistics in V$RSRC_PDB are reset when a multitenant container database (CDB) changes its resource plan. They are not impacted by PDB resource plan changes. V$RSRC_PDB covers the same time period for all PDBs. This view is specifically designed for comparing statistics across different PDBs. Since V$RSRC_PDB does not contain information at the consumer group level, it is not useful for comparing consumer groups inside a PDB. See Also: " V$RSRC_CONSUMER_GROUP " See Also: " V$RSRC_CONSUMER_GROUP "