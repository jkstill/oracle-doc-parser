---
id: 19c__DBA_WORKLOAD_SCHEDULE_ORDERING
name: DBA_WORKLOAD_SCHEDULE_ORDERING
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_WORKLOAD_SCHEDULE_ORDERING.html
---

# DBA_WORKLOAD_SCHEDULE_ORDERING

DBA_WORKLOAD_SCHEDULE_ORDERING displays the start ordering between workload captures in the replay schedule.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCHEDULE_NAME | VARCHAR2(128) | Name of a schedule to be replayed |
| SCHEDULE_CAP_ID | NUMBER | Identifies the workload capture that will wait |
| WAITFOR_CAP_ID | NUMBER | Identifies the workload capture for which the workload capture identified by SCHEDULE_CAP_ID needs to wait. The replay of capture SCHEDULE_CAP_ID will not start until capture WAITFOR_CAP_ID finishes its replay. If the view has multiple rows with the same SCHEDULE_CAP_ID but different WAITFOR_CAP_ID , it defines a schedule so that the replay of a capture specified by SCHEDULE_CAP_ID will not start unless all the replays of the waited captures run into completion. If the view has multiple rows with the same WAITFOR_CAP_ID but different SCHEDULE_CAP_ID , it defines a schedule so that the replay of multiple captures will not start unless the replay of the capture specified by WAITFOR_CAP_ID finishes. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Each row in the view defines one start ordering between two workload captures in the same replay schedule.