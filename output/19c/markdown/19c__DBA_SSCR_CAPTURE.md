---
id: 19c__DBA_SSCR_CAPTURE
name: DBA_SSCR_CAPTURE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_SSCR_CAPTURE.html
---

# DBA_SSCR_CAPTURE

DBA_SSCR_CAPTURE displays session state capture statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DB_NAME | VARCHAR2(4000) | Database name of captured session |
| INST_NAME | VARCHAR2(4000) | Instance name of captured session |
| INST_ID | NUMBER | Instance ID of captured session |
| SESSION_ID | NUMBER | Session ID of captured session |
| SESSION_SERIAL# | NUMBER | Session serial number of captured session |
| USER_NAME | VARCHAR2(128) | User name of captured session |
| SCHEMA_NAME | VARCHAR2(128) | Schema name of captured session |
| SEQUENCE# | NUMBER | Sequence number of captured session |
| CAPTURE_MODE | VARCHAR2(7) | Mode of capture operation |
| CAPTURE_SCOPE | VARCHAR2(7) | Scope of capture operation |
| CAPTURE_FORMAT | VARCHAR2(9) | Format of capture files |
| CAPTURE_DIR | VARCHAR2(128) | Directory object of capture files |
| CAPTURE_LOCATOR | RAW(64) | Locator of master capture file |
| CAPTURE_TIME | TIMESTAMP(6) | Timestamp of capture operation |