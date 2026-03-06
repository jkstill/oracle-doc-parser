---
id: 19c__ALL_SCHEDULER_WINDOW_DETAILS
name: ALL_SCHEDULER_WINDOW_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SCHEDULER_WINDOW_DETAILS.html
---

# ALL_SCHEDULER_WINDOW_DETAILS

ALL_SCHEDULER_WINDOW_DETAILS displays log details for the Scheduler windows accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LOG_ID | NUMBER | Unique identifier of the log entry (foreign key of the *_SCHEDULER_WINDOW_LOG views) |
| LOG_DATE | TIMESTAMP(6) WITH TIME ZONE | Date of the log entry |
| OWNER | VARCHAR2(128) | Owner of the Scheduler window |
| WINDOW_NAME | VARCHAR2(261) | Name of the Scheduler window |
| REQ_START_DATE | TIMESTAMP(6) WITH TIME ZONE | Requested start date for the Scheduler window |
| ACTUAL_START_DATE | TIMESTAMP(6) WITH TIME ZONE | Actual start date of the Scheduler window |
| WINDOW_DURATION | INTERVAL DAY(3) TO SECOND(0) | Requested duration of the Scheduler window |
| ACTUAL_DURATION | INTERVAL DAY(3) TO SECOND(0) | Actual duration for which the Scheduler window lasted |
| INSTANCE_ID | NUMBER | Identifier of the instance on which the window was run |
| ADDITIONAL_INFO | VARCHAR2(4000) | Additional information on the entry, if applicable |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_SCHEDULER_WINDOW_DETAILS displays log details for all Scheduler windows in the database. See Also: " DBA_SCHEDULER_WINDOW_DETAILS " See Also: " DBA_SCHEDULER_WINDOW_DETAILS "