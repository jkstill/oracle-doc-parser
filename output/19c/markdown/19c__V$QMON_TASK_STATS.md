---
id: 19c__V$QMON_TASK_STATS
name: V$QMON_TASK_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-QMON_TASK_STATS.html
---

# V$QMON_TASK_STATS

Unique task number last created for this task

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_NAME | VARCHAR2(32) |  |
| TASK_TYPE | VARCHAR2(40) |  |
| LAST_CREATED_TASKNUM | NUMBER |  |
| NUM_TASKS | NUMBER |  |
| TOTAL_TASK_RUN_TIME | NUMBER |  |
| TOTAL_TASK_RUNS | NUMBER |  |
| TOTAL_TASK_FAILURES | NUMBER |  |
| METRIC_TYPE | VARCHAR2(50) |  |
| METRIC_VALUE | NUMBER |  |
| LAST_FAILURE | VARCHAR2(32) |  |
| LAST_FAILURE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_FAILURE_TASKNUM | NUMBER |  |
| REMARK | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |