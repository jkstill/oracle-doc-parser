---
id: 19c__DBA_AUTOTASK_WINDOW_CLIENTS
name: DBA_AUTOTASK_WINDOW_CLIENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_AUTOTASK_WINDOW_CLIENTS.html
---

# DBA_AUTOTASK_WINDOW_CLIENTS

DBA_AUTOTASK_WINDOW_CLIENTS displays the windows that belong to MAINTENANCE_WINDOW_GROUP , along with the Enabled or Disabled status for the window for each maintenance task.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WINDOW_NAME | VARCHAR2(128) | Name of the maintenance window |
| WINDOW_NEXT_TIME | TIMESTAMP(6) WITH TIME ZONE | Next scheduled window open time unless the window is disabled |
| WINDOW_ACTIVE | VARCHAR2(5) | Indicates whether the window is currently active (open) ( TRUE ) or not ( FALSE ) |
| AUTOTASK_STATUS | VARCHAR2(8) | Status of the automated maintenance task subsystem: ENABLED DISABLED |
| OPTIMIZER_STATS | VARCHAR2(8) | Status of optimizer statistics gathering: ENABLED DISABLED |
| SEGMENT_ADVISOR | VARCHAR2(8) | Status of Segment Advisor: ENABLED DISABLED |
| SQL_TUNE_ADVISOR | VARCHAR2(8) | Status of SQL Tuning Advisor: ENABLED DISABLED |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content DBA_AUTOTASK_WINDOW_CLIENTS is primarily used by Enterprise Manager.