---
id: 19c__V$QMON_SERVER_STATS
name: V$QMON_SERVER_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-QMON_SERVER_STATS.html
---

# V$QMON_SERVER_STATS

Non-sharded queue master process ID

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QMNC_PID | VARCHAR2(24) |  |
| SERVER_PID | VARCHAR2(24) |  |
| SERVER_NAME | VARCHAR2(48) |  |
| STATUS | VARCHAR2(40) |  |
| SERVER_START_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| TASK_NAME | VARCHAR2(32) |  |
| TASK_NUMBER | NUMBER |  |
| TASK_START_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_WAIT_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| MAX_LATENCY | NUMBER |  |
| MIN_LATENCY | NUMBER |  |
| TOTAL_LATENCY | NUMBER |  |
| NUM_TASKS | NUMBER |  |
| LAST_FAILURE | VARCHAR2(128) |  |
| LAST_FAILURE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_FAILURE_TASK | VARCHAR2(32) |  |
| LAST_FAILURE_TASKNUM | NUMBER |  |
| CON_ID | NUMBER |  |