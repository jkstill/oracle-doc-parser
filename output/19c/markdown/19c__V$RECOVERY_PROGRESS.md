---
id: 19c__V$RECOVERY_PROGRESS
name: V$RECOVERY_PROGRESS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RECOVERY_PROGRESS.html
---

# V$RECOVERY_PROGRESS

V$RECOVERY_PROGRESS can be used to track database recovery operations to ensure that they are not stalled, and also to estimate the time required to complete the operation in progress.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| START_TIME | DATE |  |
| TYPE | VARCHAR2(64) |  |
| ITEM | VARCHAR2(32) |  |
| UNITS | VARCHAR2(32) |  |
| SOFAR | NUMBER |  |
| TOTAL | NUMBER |  |
| TIMESTAMP | DATE |  |
| COMMENTS | VARCHAR2(248) |  |
| CON_ID | NUMBER |  |

## Usage Notes

On non-coordinator instances, V$RECOVERY_PROGRESS is not populated. On the coordinator instance (the instance where MRP0 was started to start recovery), V$RECOVERY_PROGRESS has the same set of rows as before, except the following rows in the ITEM column are always 0 (not used) with Multi-Instance Redo Apply: Active Apply Maximum Apply Rate Apply Time per Log Checkpoint Time per Log Recovery ID V$RECOVERY_PROGRESS is a subview of V$SESSION_LONGOPS . Note: This view is populated on the instance where the MRP0 process is started if recovery is running in Multi-Instance Redo Apply mode. Not all the columns will be populated. Note: This view is populated on the instance where the MRP0 process is started if recovery is running in Multi-Instance Redo Apply mode. Not all the columns will be populated. See Also: " V$SESSION_LONGOPS " " Background Processes " for more information about the MRP0 process Oracle Database Backup and Recovery User’s Guide for more information about performing database recovery See Also: " V$SESSION_LONGOPS " " Background Processes " for more information about the MRP0 process Oracle Database Backup and Recovery User’s Guide for more information about performing database recovery