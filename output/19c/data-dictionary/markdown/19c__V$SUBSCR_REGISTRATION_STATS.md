---
id: 19c__V$SUBSCR_REGISTRATION_STATS
name: V$SUBSCR_REGISTRATION_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SUBSCR_REGISTRATION_STATS.html
---

# V$SUBSCR_REGISTRATION_STATS

The script content on this page is for navigation purposes only and does not alter the content in any way.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REG_ID | NUMBER |  |
| NUM_NTFNS | NUMBER |  |
| NUM_GROUPING_NTFNS | NUMBER |  |
| NUM_NTFNS_CURRENT_GROUP | NUMBER |  |
| LAST_NTFN_START_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_NTFN_SENT_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| TOTAL_EMON_LATENCY | NUMBER |  |
| EMON# | NUMBER |  |
| ALL_EMON_SERVERS | RAW(2000) |  |
| TOTAL_PAYLOAD_BYTES_SENT | NUMBER |  |
| SHARD_ID Foot 1 | NUMBER |  |
| NUM_RETRIES | NUMBER |  |
| TOTAL_PLSQL_EXEC_TIME | NUMBER |  |
| LAST_ERR | VARCHAR2(90) |  |
| LAST_ERR_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_UPDATE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| NUM_PENDING_NTFNS | NUMBER |  |
| TOTAL_PENDING_NTFN_BYTES | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content