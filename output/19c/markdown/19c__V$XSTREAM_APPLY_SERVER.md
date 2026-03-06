---
id: 19c__V$XSTREAM_APPLY_SERVER
name: V$XSTREAM_APPLY_SERVER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-XSTREAM_APPLY_SERVER.html
---

# V$XSTREAM_APPLY_SERVER

Session ID of the apply server's session

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| APPLY# | NUMBER |  |
| APPLY_NAME | VARCHAR2(128) |  |
| SERVER_ID | NUMBER |  |
| STATE | VARCHAR2(20) |  |
| XIDUSN | NUMBER |  |
| XIDSLT | NUMBER |  |
| XIDSQN | NUMBER |  |
| COMMITSCN | NUMBER |  |
| DEP_XIDUSN | NUMBER |  |
| DEP_XIDSLT | NUMBER |  |
| DEP_XIDSQN | NUMBER |  |
| DEP_COMMITSCN | NUMBER |  |
| MESSAGE_SEQUENCE | NUMBER |  |
| TOTAL_ASSIGNED | NUMBER |  |
| TOTAL_ADMIN | NUMBER |  |
| TOTAL_ROLLBACKS | NUMBER |  |
| TOTAL_MESSAGES_APPLIED | NUMBER |  |
| APPLY_TIME | DATE |  |
| APPLIED_MESSAGE_NUMBER | NUMBER |  |
| APPLIED_MESSAGE_CREATE_TIME | DATE |  |
| ELAPSED_DEQUEUE_TIME | NUMBER |  |
| ELAPSED_APPLY_TIME | NUMBER |  |
| COMMIT_POSITION | RAW(64) |  |
| DEP_COMMIT_POSITION | RAW(64) |  |
| LAST_APPLY_POSITION | RAW(64) |  |
| TRANSACTION_ID | VARCHAR2(128) |  |
| DEP_TRANSACTION_ID | VARCHAR2(128) |  |
| CON_ID | NUMBER |  |
| TOTAL_LCRS_RETRIED | NUMBER |  |
| LCR_RETRY_ITERATION | NUMBER |  |
| TOTAL_TXNS_RETRIED | NUMBER |  |
| TXN_RETRY_ITERATION | NUMBER |  |
| TOTAL_TXNS_RECORDED | NUMBER |  |

## Usage Notes

Note: The ELAPSED_SCHEDULE_TIME column is only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL " Note: The ELAPSED_SCHEDULE_TIME column is only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL "