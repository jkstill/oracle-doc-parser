---
id: 19c__DBA_SSCR_RESTORE
name: DBA_SSCR_RESTORE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_SSCR_RESTORE.html
---

# DBA_SSCR_RESTORE

DBA_SSCR_RESTORE displays session state restore statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DB_NAME | VARCHAR2(4000) | Database name of restored session |
| INST_NAME | VARCHAR2(4000) | Instance name of restored session |
| INST_ID | NUMBER | Instance ID of restored session |
| SESSION_ID | NUMBER | Session ID of restored session |
| SESSION_SERIAL# | NUMBER | Session serial number of restored session |
| USER_NAME | VARCHAR2(128) | User name of restored session |
| SCHEMA_NAME | VARCHAR2(128) | Schema name of restored session |
| SEQUENCE# | NUMBER | Sequence number of restore operation |
| RESTORE_MODE | VARCHAR2(7) | Mode of restore operation |
| RESTORE_SCOPE | VARCHAR2(7) | Scope of restore operation |
| RESTORE_FORMAT | VARCHAR2(9) | Format of restore files |
| RESTORE_DIR | VARCHAR2(128) | Directory object of restore files |
| RESTORE_LOCATOR | RAW(64) | Locator of master restore file |
| RESTORE_TIME | TIMESTAMP(6) | Timestamp of restore operation |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content