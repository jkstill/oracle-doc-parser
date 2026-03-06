---
id: 19c__ALL_SCHEDULER_PROGRAM_ARGS
name: ALL_SCHEDULER_PROGRAM_ARGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_PROGRAM_ARGS.html
---

# ALL_SCHEDULER_PROGRAM_ARGS

ALL_SCHEDULER_PROGRAM_ARGS displays information about the arguments of the Scheduler programs accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the program to which the argument belongs |
| PROGRAM_NAME | VARCHAR2(128) | Name of the program to which the argument belongs |
| ARGUMENT_NAME | VARCHAR2(128) | Optional name of the argument |
| ARGUMENT_POSITION | NUMBER | Position of the argument in the argument list |
| ARGUMENT_TYPE | VARCHAR2(257) | Data type of the argument |
| METADATA_ATTRIBUTE | VARCHAR2(19) | Metadata attribute: JOB_NAME JOB_OWNER JOB_START WINDOW_START WINDOW_END JOB_SUBNAME EVENT_MESSAGE JOB_SCHEDULED_START |
| DEFAULT_VALUE | VARCHAR2(4000) | Default value taken by the argument (in string format) if the argument is a string |
| DEFAULT_ANYDATA_VALUE | ANYDATA | Default value taken by the argument (in AnyData format) |
| OUT_ARGUMENT | VARCHAR2(5) | Reserved for future use |

## Usage Notes

Related Views DBA_SCHEDULER_PROGRAM_ARGS displays information about the arguments of all Scheduler programs in the database. USER_SCHEDULER_PROGRAM_ARGS displays information about the arguments of the Scheduler programs owned by the current user. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_PROGRAM_ARGS " " USER_SCHEDULER_PROGRAM_ARGS " See Also: " DBA_SCHEDULER_PROGRAM_ARGS " " USER_SCHEDULER_PROGRAM_ARGS "