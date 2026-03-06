---
id: 19c__V$ARCHIVE_DEST_STATUS
name: V$ARCHIVE_DEST_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ARCHIVE_DEST_STATUS.html
---

# V$ARCHIVE_DEST_STATUS

V$ARCHIVE_DEST_STATUS displays run time and configuration information for the archived redo log destinations.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DEST_ID | NUMBER |  |
| DEST_NAME | VARCHAR2(256) |  |
| STATUS | VARCHAR2(9) |  |
| TYPE | VARCHAR2(14) |  |
| DATABASE_MODE | VARCHAR2(15) |  |
| RECOVERY_MODE | VARCHAR2(23) |  |
| PROTECTION_MODE | VARCHAR2(20) |  |
| DESTINATION | VARCHAR2(256) |  |
| STANDBY_LOGFILE_COUNT | NUMBER |  |
| STANDBY_LOGFILE_ACTIVE | NUMBER |  |
| ARCHIVED_THREAD# | NUMBER |  |
| ARCHIVED_SEQ# | NUMBER |  |
| APPLIED_THREAD# | NUMBER |  |
| APPLIED_SEQ# | NUMBER |  |
| ERROR | VARCHAR2(256) |  |
| SRL | VARCHAR2(3) |  |
| DB_UNIQUE_NAME | VARCHAR2(30) |  |
| SYNCHRONIZATION_STATUS | VARCHAR2(22) |  |
| SYNCHRONIZED | VARCHAR2(3) |  |
| GAP_STATUS | VARCHAR2(24) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The information in this view does not persist across an instance shutdown.