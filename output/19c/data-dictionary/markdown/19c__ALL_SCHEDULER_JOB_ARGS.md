---
id: 19c__ALL_SCHEDULER_JOB_ARGS
name: ALL_SCHEDULER_JOB_ARGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_JOB_ARGS.html
---

# ALL_SCHEDULER_JOB_ARGS

ALL_SCHEDULER_JOB_ARGS displays information about the arguments of the Scheduler jobs accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the job to which the argument belongs |
| JOB_NAME | VARCHAR2(128) | Name of the job to which the argument belongs |
| ARGUMENT_NAME | VARCHAR2(128) | Optional name of the argument |
| ARGUMENT_POSITION | NUMBER | Position of the argument in the argument list |
| ARGUMENT_TYPE | VARCHAR2(257) | Data type of the argument |
| VALUE | VARCHAR2(4000) | Value of the argument (in string format) if the argument is a string |
| ANYDATA_VALUE | ANYDATA | Value of the argument (in AnyData format) |
| OUT_ARGUMENT | VARCHAR2(5) | Reserved for future use |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SCHEDULER_JOB_ARGS displays information about the arguments of all Scheduler jobs in the database. USER_SCHEDULER_JOB_ARGS displays information about the arguments of the Scheduler jobs owned by the current user. This view does not display the OWNER column. See Also: " DBA_SCHEDULER_JOB_ARGS " " USER_SCHEDULER_JOB_ARGS " See Also: " DBA_SCHEDULER_JOB_ARGS " " USER_SCHEDULER_JOB_ARGS "