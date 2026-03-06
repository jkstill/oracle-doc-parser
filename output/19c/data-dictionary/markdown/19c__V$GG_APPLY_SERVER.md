---
id: 19c__V$GG_APPLY_SERVER
name: V$GG_APPLY_SERVER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GG_APPLY_SERVER.html
---

# V$GG_APPLY_SERVER

V$GG_APPLY_SERVER displays information about each GoldenGate apply server and its activities.

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

Previous Next JavaScript must be enabled to correctly display this content An apply server receives messages from the apply coordinator for an apply process. For each message received, an apply server either applies the message or sends the message to the appropriate apply handler. An apply server is a subcomponent of an apply process used by Oracle GoldenGate Integrated Replicat. Note: The ELAPSED_SCHEDULE_TIME column is only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL " Note: The ELAPSED_SCHEDULE_TIME column is only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL "