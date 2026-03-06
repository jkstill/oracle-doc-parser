---
id: 19c__ALL_SCHEDULER_SCHEDULES
name: ALL_SCHEDULER_SCHEDULES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_SCHEDULES.html
---

# ALL_SCHEDULER_SCHEDULES

ALL_SCHEDULER_SCHEDULES displays information about the Scheduler schedules accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the schedule |
| SCHEDULE_NAME | VARCHAR2(128) | Name of the schedule |
| SCHEDULE_TYPE | VARCHAR2(12) | Type of the schedule: ONCE - Repeat interval is NULL CALENDAR - Oracle calendaring expression used as schedule EVENT - Event schedule |
| START_DATE | TIMESTAMP(6) WITH TIME ZONE | Start date for the repeat interval |
| REPEAT_INTERVAL | VARCHAR2(4000) | Calendar syntax expression for the schedule |
| EVENT_QUEUE_OWNER | VARCHAR2(128) | Owner of the source queue into which the event will be raised |
| EVENT_QUEUE_NAME | VARCHAR2(128) | Name of the source queue into which the event will be raised |
| EVENT_QUEUE_AGENT | VARCHAR2(523) | Name of the AQ agent used by the user on the event source queue (if it is a secure queue) |
| EVENT_CONDITION | VARCHAR2(4000) | Boolean expression used as the subscription rule for the event on the source queue |
| FILE_WATCHER_OWNER | VARCHAR2(261) | Owner of the file watcher on which this schedule is based |
| FILE_WATCHER_NAME | VARCHAR2(261) | Name of the file watcher on which this schedule is based |
| END_DATE | TIMESTAMP(6) WITH TIME ZONE | Cutoff date after which the schedule will not specify any dates |
| COMMENTS | VARCHAR2(4000) | Comments on the schedule |

## Usage Notes

Related Views DBA_SCHEDULER_SCHEDULES displays information about all Scheduler schedules in the database. USER_SCHEDULER_SCHEDULES displays information about the Scheduler schedules owned by the current user. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_SCHEDULES " " USER_SCHEDULER_SCHEDULES " See Also: " DBA_SCHEDULER_SCHEDULES " " USER_SCHEDULER_SCHEDULES "