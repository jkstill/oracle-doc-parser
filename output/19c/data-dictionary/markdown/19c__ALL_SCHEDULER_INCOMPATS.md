---
id: 19c__ALL_SCHEDULER_INCOMPATS
name: ALL_SCHEDULER_INCOMPATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_INCOMPATS.html
---

# ALL_SCHEDULER_INCOMPATS

ALL_SCHEDULER_INCOMPATS displays all Scheduler incompatibility resource objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the incompatibility resource object |
| INCOMPATIBILITY_NAME | VARCHAR2(128) | Name of the incompatibility resource object |
| CONSTRAINT_LEVEL | VARCHAR2(13) | JOB_LEVEL or PROGRAM_LEVEL The default value JOB_LEVEL indicates that only a single job that is based on the program (or programs) mentioned in the object_name argument of the DBMS_SCHEDULER.CREATE_INCOMPATIBILITY procedure can run at one time. The value PROGRAM_LEVEL indicates that the programs are incompatible, but the jobs based on the same program are not incompatible. |
| ENABLED | VARCHAR2(5) | Indicates whether the incompatibility is enabled ( TRUE ) or not ( FALSE ) |
| JOBS_RUNNING_COUNT | NUMBER | Current number of running jobs using the incompatibility resource object |
| COMMENTS | VARCHAR2(256) | Comments for the resource incompatibility object |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SCHEDULER_INCOMPATS displays all Scheduler incompatibility resource objects in the database. USER_SCHEDULER_INCOMPATS displays all Scheduler incompatibility resource objects owned by the current user. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_INCOMPATS " " USER_SCHEDULER_INCOMPATS " See Also: " DBA_SCHEDULER_INCOMPATS " " USER_SCHEDULER_INCOMPATS "