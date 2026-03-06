---
id: 19c__V$ENQUEUE_STATISTICS
name: V$ENQUEUE_STATISTICS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ENQUEUE_STATISTICS.html
---

# V$ENQUEUE_STATISTICS

V$ENQUEUE_STATISTICS displays statistics on the number of enqueue (lock) requests for each type of lock.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EQ_NAME | VARCHAR2(64) |  |
| EQ_TYPE | VARCHAR2(2) |  |
| REQ_REASON | VARCHAR2(64) |  |
| TOTAL_REQ# | NUMBER |  |
| TOTAL_WAIT# | NUMBER |  |
| SUCC_REQ# | NUMBER |  |
| FAILED_REQ# | NUMBER |  |
| CUM_WAIT_TIME | NUMBER |  |
| REQ_DESCRIPTION | VARCHAR2(4000) |  |
| EVENT# | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

V$ENQUEUE_STATISTICS encompasses V$ENQUEUE_STAT and gives more detailed information (several rows for same enqueues with different reasons). See Also: " V$ENQUEUE_STAT " See Also: " V$ENQUEUE_STAT "