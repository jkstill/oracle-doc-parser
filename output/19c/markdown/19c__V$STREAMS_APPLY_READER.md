---
id: 19c__V$STREAMS_APPLY_READER
name: V$STREAMS_APPLY_READER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-STREAMS_APPLY_READER.html
---

# V$STREAMS_APPLY_READER

Session ID of the reader's session

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| APPLY# | NUMBER |  |
| APPLY_NAME | VARCHAR2(128) |  |
| STATE | VARCHAR2(36) |  |
| TOTAL_MESSAGES_DEQUEUED | NUMBER |  |
| TOTAL_MESSAGES_SPILLED | NUMBER |  |
| DEQUEUE_TIME | DATE |  |
| DEQUEUED_MESSAGE_NUMBER | NUMBER |  |
| DEQUEUED_MESSAGE_CREATE_TIME | DATE |  |
| SGA_USED | NUMBER |  |
| ELAPSED_DEQUEUE_TIME | NUMBER |  |
| ELAPSED_SCHEDULE_TIME | NUMBER |  |
| ELAPSED_SPILL_TIME | NUMBER |  |
| LAST_BROWSE_NUM | NUMBER |  |
| OLDEST_SCN_NUM | NUMBER |  |
| LAST_BROWSE_SEQ | NUMBER |  |
| LAST_DEQ_SEQ | NUMBER |  |
| OLDEST_XIDUSN | NUMBER |  |
| OLDEST_XIDSLT | NUMBER |  |
| OLDEST_XIDSQN | NUMBER |  |
| SPILL_LWM_SCN | NUMBER |  |
| PROXY_SID | NUMBER |  |
| PROXY_SERIAL | NUMBER |  |
| PROXY_SPID | VARCHAR2(12) |  |
| CAPTURE_BYTES_RECEIVED | NUMBER |  |
| DEQUEUED_POSITION | RAW(64) |  |
| LAST_BROWSE_POSITION | RAW(64) |  |
| OLDEST_POSITION | RAW(64) |  |
| SPILL_LWM_POSITION | RAW(64) |  |
| OLDEST_TRANSACTION_ID | VARCHAR2(128) |  |
| TOTAL_LCRS_WITH_DEP | NUMBER |  |
| TOTAL_LCRS_WITH_WMDEP | NUMBER |  |
| TOTAL_IN_MEMORY_LCRS | NUMBER |  |
| SGA_ALLOCATED | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note: The ELAPSED_DEQUEUE_TIME and ELAPSED_SCHEDULE_TIME columns are only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL " Note: The ELAPSED_DEQUEUE_TIME and ELAPSED_SCHEDULE_TIME columns are only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL "