---
id: 19c__V$AQ_IPC_MSG_STATS
name: V$AQ_IPC_MSG_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-AQ_IPC_MSG_STATS.html
---

# V$AQ_IPC_MSG_STATS

V$AQ_IPC_MSG_STATS displays the statistics of each IPC message class, such as the total number of invocations of a message class, total pending message/processed message count, and last failure related data. Information like total processed message count, average pending time/average processing time gives a real-time outline of AQ IPC background state.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MSG_CLASS_NAME | VARCHAR2(30) |  |
| TOTAL_MSG_CALLS | NUMBER |  |
| TOTAL_ACTIVE_MSGS | NUMBER |  |
| TOTAL_PENDING_MSGS | NUMBER |  |
| TOTAL_PROCESSED_MSGS | NUMBER |  |
| LAST_RECEIVED_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_PROCESS_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_DONE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| AVERAGE_PENDING_TIME | NUMBER |  |
| AVERAGE_PROCESSING_TIME | NUMBER |  |
| LAST_FAILURE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_ERROR_MSG | VARCHAR2(512) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content