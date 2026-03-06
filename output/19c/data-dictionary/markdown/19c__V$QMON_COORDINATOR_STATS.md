---
id: 19c__V$QMON_COORDINATOR_STATS
name: V$QMON_COORDINATOR_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-QMON_COORDINATOR_STATS.html
---

# V$QMON_COORDINATOR_STATS

QMNC_PID

## Columns

| Column | Type | Description |
|--------|------|-------------|
| QMNC_PID | VARCHAR2(24) |  |
| STATUS | VARCHAR2(24) |  |
| NUM_SERVERS | NUMBER |  |
| LAST_SERVER_START_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_SERVER_PID | VARCHAR2(24) |  |
| NEXT_WAKEUP_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| NEXT_READY_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| NEXT_EXPIRY_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_WAIT_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| LAST_FAILURE | VARCHAR2(32) |  |
| LAST_FAILURE_TIME | TIMESTAMP(3) WITH TIME ZONE |  |
| MAX_TASK_LATENCY | VARCHAR2(40) |  |
| MIN_TASK_LATENCY | VARCHAR2(40) |  |
| TOTAL_TASK_LATENCY | NUMBER |  |
| TOTAL_TASKS_EXECUTED | NUMBER |  |
| MAX_SERVERS | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content