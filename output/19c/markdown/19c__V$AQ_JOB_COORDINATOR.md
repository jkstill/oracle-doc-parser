---
id: 19c__V$AQ_JOB_COORDINATOR
name: V$AQ_JOB_COORDINATOR
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-AQ_JOB_COORDINATOR.html
---

# V$AQ_JOB_COORDINATOR

V$AQ_JOB_COORDINATOR lists performance statistics per coordinator, for every AQ coordinator controlled by the Oracle Database Advanced Queueing master coordinator.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COORDINATOR_ID | NUMBER |  |
| PROCESS_ID | VARCHAR2(24) |  |
| PROCESS_NAME | VARCHAR2(48) |  |
| JOB_NAME | VARCHAR2(32) |  |
| JOB_TYPE | NUMBER |  |
| SERVER_COUNT | NUMBER |  |
| MAX_SERVER_COUNT | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing See Also: Oracle Database Advanced Queuing User's Guide for more information about Oracle Database Advanced Queueing