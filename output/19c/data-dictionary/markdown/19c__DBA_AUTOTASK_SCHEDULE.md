---
id: 19c__DBA_AUTOTASK_SCHEDULE
name: DBA_AUTOTASK_SCHEDULE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_AUTOTASK_SCHEDULE.html
---

# DBA_AUTOTASK_SCHEDULE

DBA_AUTOTASK_SCHEDULE displays the schedule of maintenance windows for the next 32 days for each client.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WINDOW_NAME | VARCHAR2(128) | Name of the maintenance window |
| START_TIME | TIMESTAMP(6) WITH TIME ZONE | Projected start time of the window |
| DURATION | INTERVAL DAY(3) TO SECOND(0) | Currently defined duration of the window (NULL for the currently open window) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content