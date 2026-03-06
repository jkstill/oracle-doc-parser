---
id: 19c__V$RECOVERY_LOG
name: V$RECOVERY_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-RECOVERY_LOG.html
---

# V$RECOVERY_LOG

V$RECOVERY_LOG lists information about archived logs that are needed to complete media recovery. This information is derived from the log history view, V$LOG_HISTORY .

## Columns

| Column | Type | Description |
|--------|------|-------------|
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| TIME | DATE |  |
| ARCHIVE_NAME | VARCHAR2(513) |  |
| CON_ID | NUMBER |  |

## Usage Notes

V$RECOVERY_LOG contains useful information only for the Oracle process doing the recovery. When Recovery Manager directs a server process to perform recovery, only Recovery Manager can view the relevant information in this view. V$RECOVERY_LOG will be empty to all other Oracle users. See Also: " V$LOG_HISTORY " and Oracle Database Backup and Recovery User’s Guide See Also: " V$LOG_HISTORY " and Oracle Database Backup and Recovery User’s Guide