---
id: 19c__V$GG_APPLY_READER
name: V$GG_APPLY_READER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GG_APPLY_READER.html
---

# V$GG_APPLY_READER

V$GG_APPLY_READER displays information about each GoldenGate apply reader.

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
| DEQUEUED_MESSAGE_CREATE_TIME | DATE |  |
| SGA_USED | NUMBER |  |
| ELAPSED_DEQUEUE_TIME | NUMBER |  |
| ELAPSED_SCHEDULE_TIME | NUMBER |  |
| ELAPSED_SPILL_TIME | NUMBER |  |
| SPILL_LWM_SCN | NUMBER |  |
| PROXY_SID | NUMBER |  |
| PROXY_SERIAL | NUMBER |  |
| PROXY_SPID | VARCHAR2(12) |  |
| BYTES_RECEIVED | NUMBER |  |
| DEQUEUED_POSITION | RAW(64) |  |
| SPILL_LWM_POSITION | RAW(64) |  |
| OLDEST_TRANSACTION_ID | VARCHAR2(128) |  |
| TOTAL_LCRS_WITH_DEP | NUMBER |  |
| TOTAL_LCRS_WITH_WMDEP | NUMBER |  |
| TOTAL_IN_MEMORY_LCRS | NUMBER |  |
| SGA_ALLOCATED | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The apply reader is a process which reads (dequeues) messages from the queue, computes message dependencies, and builds transactions. It passes the transactions on to the coordinator in commit order for assignment to the apply servers. An apply reader is a subcomponent of an apply process used by Oracle GoldenGate Integrated Replicat. Note: The ELAPSED_SCHEDULE_TIME column is only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL " Note: The ELAPSED_SCHEDULE_TIME column is only populated if the TIMED_STATISTICS initialization parameter is set to true , or if the STATISTICS_LEVEL initialization parameter is set to TYPICAL or ALL . See Also: " TIMED_STATISTICS " " STATISTICS_LEVEL "