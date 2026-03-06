---
id: 19c__ALL_SCHEDULER_JOB_CLASSES
name: ALL_SCHEDULER_JOB_CLASSES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_JOB_CLASSES.html
---

# ALL_SCHEDULER_JOB_CLASSES

ALL_SCHEDULER_JOB_CLASSES displays information about the Scheduler job classes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Scheduler job class |
| JOB_CLASS_NAME | VARCHAR2(128) | Name of the Scheduler job class |
| RESOURCE_CONSUMER_GROUP | VARCHAR2(128) | Resource consumer group associated with the class |
| SERVICE | VARCHAR2(64) | Name of the service the class is associated with |
| LOGGING_LEVEL | VARCHAR2(11) | Amount of logging that will be done pertaining to the class: OFF RUNS FAILED RUNS FULL |
| LOG_HISTORY | NUMBER | History (in days) to maintain in the job log for the class |
| COMMENTS | VARCHAR2(4000) | Comments on the class |

## Usage Notes

Related View DBA_SCHEDULER_JOB_CLASSES displays information about all Scheduler job classes in the database. See Also: " DBA_SCHEDULER_JOB_CLASSES " See Also: " DBA_SCHEDULER_JOB_CLASSES "