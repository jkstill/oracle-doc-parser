---
id: 19c__V$STREAMS_APPLY_COORDINATOR
name: V$STREAMS_APPLY_COORDINATOR
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-STREAMS_APPLY_COORDINATOR.html
---

# V$STREAMS_APPLY_COORDINATOR

SID

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| STATE | VARCHAR2(21) |  |
| APPLY# | NUMBER |  |
| APPLY_NAME | VARCHAR2(128) |  |
| TOTAL_APPLIED | NUMBER |  |
| TOTAL_WAIT_DEPS | NUMBER |  |
| TOTAL_WAIT_COMMITS | NUMBER |  |
| TOTAL_ADMIN | NUMBER |  |
| TOTAL_ASSIGNED | NUMBER |  |
| TOTAL_RECEIVED | NUMBER |  |
| TOTAL_IGNORED | NUMBER |  |
| TOTAL_ROLLBACKS | NUMBER |  |
| TOTAL_ERRORS | NUMBER |  |
| UNASSIGNED_COMPLETE_TXNS | NUMBER |  |
| AUTO_TXN_BUFFER_SIZE | NUMBER |  |
| LWM_TIME | DATE |  |
| LWM_MESSAGE_NUMBER | NUMBER |  |
| LWM_MESSAGE_CREATE_TIME | DATE |  |
| HWM_TIME | DATE |  |
| HWM_MESSAGE_NUMBER | NUMBER |  |
| HWM_MESSAGE_CREATE_TIME | DATE |  |
| STARTUP_TIME | DATE |  |
| ELAPSED_SCHEDULE_TIME | NUMBER |  |
| ELAPSED_IDLE_TIME | NUMBER |  |
| LWM_POSITION | RAW(64) |  |
| HWM_POSITION | RAW(64) |  |
| PROCESSED_MESSAGE_NUMBER | NUMBER |  |
| CON_ID | NUMBER |  |
| ACTIVE_SERVER_COUNT | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: The ELAPSED_SCHEDULE_TIME column is only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL " Note: The ELAPSED_SCHEDULE_TIME column is only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL "