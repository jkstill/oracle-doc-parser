---
id: 19c__V$QMON_TASKS
name: V$QMON_TASKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-QMON_TASKS.html
---

# V$QMON_TASKS

TIMESTAMP(3) WITH TIME ZONE

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TASK_NAME | VARCHAR2(32) |  |
| TASK_NUMBER | NUMBER |  |
| TASK_TYPE | VARCHAR2(40) |  |
| TASK_SUBMIT_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| TASK_READY_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| TASK_EXPIRY_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| TASK_START_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| TASK_STATUS | VARCHAR2(32) |  |
| SERVER_NAME | VARCHAR2(48) |  |
| MAX_RETRIES | NUMBER |  |
| NUM_RUNS | NUMBER |  |
| NUM_FAILURES | NUMBER |  |
| CON_ID | NUMBER |  |