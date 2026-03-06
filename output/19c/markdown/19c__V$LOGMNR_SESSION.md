---
id: 19c__V$LOGMNR_SESSION
name: V$LOGMNR_SESSION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-LOGMNR_SESSION.html
---

# V$LOGMNR_SESSION

V$LOGMNR_SESSION displays information about active LogMiner persistent sessions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| SESSION_NAME | VARCHAR2(32) |  |
| SESSION_STATE | VARCHAR2(9) |  |
| DB_NAME | VARCHAR2(128) |  |
| DB_ID | NUMBER |  |
| RESET_SCN | NUMBER |  |
| RESET_TIMESTAMP | NUMBER |  |
| RESET_TIME | DATE |  |
| NUM_PROCESS | NUMBER |  |
| CHUNK_SIZE | NUMBER |  |
| START_SCN | NUMBER |  |
| END_SCN | NUMBER |  |
| SPILL_SCN | NUMBER |  |
| PROCESSED_SCN | NUMBER |  |
| PROCESSED_TIME | DATE |  |
| PREPARED_SCN | NUMBER |  |
| READ_SCN | NUMBER |  |
| LOW_MARK_SCN | NUMBER |  |
| CONSUMED_SCN | NUMBER |  |
| MAX_MEMORY_SIZE | NUMBER |  |
| USED_MEMORY_SIZE | NUMBER |  |
| BUILDER_WORK_SIZE | NUMBER |  |
| PREPARED_WORK_SIZE | NUMBER |  |
| AVAILABLE_WORK_SIZE | NUMBER |  |
| AVAILABLE_TXN | NUMBER |  |
| AVAILABLE_COMMITTED_TXN | NUMBER |  |
| DELIVERED_TXN | NUMBER |  |
| DELIVERED_COMMITTED_TXN | NUMBER |  |
| PINNED_TXN | NUMBER |  |
| PINNED_COMMITTED_TXN | NUMBER |  |
| CHECKPOINT_INTERVAL | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

(A LogMiner persistent session is created either by starting Data Guard SQL Apply on a logical standby database for the first time or by creating Replication capture.) Transient LogMiner sessions (those created as a result of querying the V$LOGMNR_CONTENTS view) do not show up in the V$LOGMNR_SESSION view. The statistics shown in this view correspond to snapshots of the system and are not cumulative in nature. See Also: " V$LOGMNR_CONTENTS " See Also: " V$LOGMNR_CONTENTS "