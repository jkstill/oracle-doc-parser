---
id: 19c__ALL_SCHEDULER_WINDOW_LOG
name: ALL_SCHEDULER_WINDOW_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [all]
source_file: ALL_SCHEDULER_WINDOW_LOG.html
---

# ALL_SCHEDULER_WINDOW_LOG

ALL_SCHEDULER_WINDOW_LOG displays log information for the Scheduler windows accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LOG_ID | NUMBER | Unique identifier of the log entry |
| LOG_DATE | TIMESTAMP(6) WITH TIME ZONE | Date of the log entry |
| OWNER | VARCHAR2(128) | Owner of the Scheduler window |
| WINDOW_NAME | VARCHAR2(261) | Name of the Scheduler window |
| OPERATION | VARCHAR2(30) | Operation corresponding to the log entry |
| STATUS | VARCHAR2(30) | Status of the operation, if applicable |
| USER_NAME | VARCHAR2(128) | Name of the user who performed the operation, if applicable |
| CLIENT_ID | VARCHAR2(64) | Client identifier of the user who performed the operation, if applicable |
| GLOBAL_UID | VARCHAR2(32) | Global user identifier of the user who performed the operation, if applicable |
| ADDITIONAL_INFO | CLOB | Additional information on the entry, if applicable |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_SCHEDULER_WINDOW_LOG displays log information for all Scheduler windows in the database. See Also: " DBA_SCHEDULER_WINDOW_LOG " See Also: " DBA_SCHEDULER_WINDOW_LOG "