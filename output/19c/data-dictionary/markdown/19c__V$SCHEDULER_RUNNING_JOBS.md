---
id: 19c__V$SCHEDULER_RUNNING_JOBS
name: V$SCHEDULER_RUNNING_JOBS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-SCHEDULER_RUNNING_JOBS.html
---

# V$SCHEDULER_RUNNING_JOBS

V$SCHEDULER_RUNNING_JOBS displays information about running Scheduler jobs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_ID | NUMBER |  |
| SESSION_SERIAL_NUM | NUMBER |  |
| JOB_ID | NUMBER |  |
| PADDR | RAW(4 | 8) |  |
| OS_PROCESS_ID | VARCHAR2(12) |  |
| SESSION_STAT_CPU | INTERVAL DAY(2) TO SECOND(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content