---
id: 19c__V$ENQUEUE_STAT
name: V$ENQUEUE_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ENQUEUE_STAT.html
---

# V$ENQUEUE_STAT

V$ENQUEUE_STAT displays statistics on the number of enqueue (lock) requests for each type of lock.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INST_ID | NUMBER |  |
| EQ_TYPE | VARCHAR2(2) |  |
| TOTAL_REQ# | NUMBER |  |
| TOTAL_WAIT# | NUMBER |  |
| SUCC_REQ# | NUMBER |  |
| FAILED_REQ# | NUMBER |  |
| CUM_WAIT_TIME | NUMBER |  |
| CON_ID | NUMBER |  |