---
id: 19c__DBA_WORKLOAD_CONNECTION_MAP
name: DBA_WORKLOAD_CONNECTION_MAP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WORKLOAD_CONNECTION_MAP.html
---

# DBA_WORKLOAD_CONNECTION_MAP

DBA_WORKLOAD_CONNECTION_MAP displays the connection mapping information for workload replay. Each row defines one connection mapping for a particular workload replay.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REPLAY_ID | NUMBER | ID of the replay (corresponds to DBA_WORKLOAD_REPLAYS.ID ) |
| CONN_ID | NUMBER | Key (ID) of the connection mapping table |
| SCHEDULE_CAP_ID | NUMBER | Schedule capture ID (corresponds to DBA_WORKLOAD_SCHEDULE_CAPTURES.SCHEDULE_CAP_ID ) |
| CAPTURE_CONN | VARCHAR2(4000) | Connection string that was used during capture |
| REPLAY_CONN | VARCHAR2(4000) | Connection string that should be used during replay |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content