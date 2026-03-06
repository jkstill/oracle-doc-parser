---
id: 19c__V$ARCHIVE_DEST
name: V$ARCHIVE_DEST
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-ARCHIVE_DEST.html
---

# V$ARCHIVE_DEST

V$ARCHIVE_DEST displays, for the current instance, all of the destinations in the Data Guard configuration, including each destination's current value, mode, and status.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DEST_ID | NUMBER |  |
| DEST_NAME | VARCHAR2(256) |  |
| STATUS | VARCHAR2(9) |  |
| BINDING | VARCHAR2(9) |  |
| NAME_SPACE | VARCHAR2(7) |  |
| TARGET | VARCHAR2(7) |  |
| ARCHIVER | VARCHAR2(10) |  |
| SCHEDULE | VARCHAR2(8) |  |
| DESTINATION | VARCHAR2(256) |  |
| LOG_SEQUENCE | NUMBER |  |
| REOPEN_SECS | NUMBER |  |
| DELAY_MINS | NUMBER |  |
| MAX_CONNECTIONS Foot 1 | NUMBER |  |
| NET_TIMEOUT | NUMBER |  |
| PROCESS | VARCHAR2(10) |  |
| REGISTER | VARCHAR2(3) |  |
| FAIL_DATE | DATE |  |
| FAIL_SEQUENCE | NUMBER |  |
| FAIL_BLOCK | NUMBER |  |
| FAILURE_COUNT | NUMBER |  |
| MAX_FAILURE | NUMBER |  |
| ERROR | VARCHAR2(256) |  |
| ALTERNATE | VARCHAR2(256) |  |
| DEPENDENCY | VARCHAR2(256) |  |
| REMOTE_TEMPLATE | VARCHAR2(256) |  |
| QUOTA_SIZE | NUMBER |  |
| QUOTA_USED | NUMBER |  |
| MOUNTID | NUMBER |  |
| TRANSMIT_MODE | VARCHAR2(12) |  |
| ASYNC_BLOCKS | NUMBER |  |
| AFFIRM | VARCHAR2(3) |  |
| TYPE | VARCHAR2(7) |  |
| VALID_NOW | VARCHAR2(16) |  |
| VALID_TYPE | VARCHAR2(15) |  |
| VALID_ROLE | VARCHAR2(12) |  |
| DB_UNIQUE_NAME | VARCHAR2(30) |  |
| VERIFY | VARCHAR2(3) |  |
| COMPRESSION | VARCHAR2(7) |  |
| APPLIED_SCN | NUMBER |  |
| CON_ID | NUMBER |  |
| ENCRYPTION | VARCHAR2(7) |  |

## Usage Notes

See Also: Zero Data Loss Recovery Appliance Administrator's Guide for introductory information about Recovery Appliance " LOG_ARCHIVE_DEST " and " LOG_ARCHIVE_DEST_n " " LOG_ARCHIVE_DUPLEX_DEST " and " LOG_ARCHIVE_DEST_STATE_n " " LOG_ARCHIVE_MIN_SUCCEED_DEST " See Also: Zero Data Loss Recovery Appliance Administrator's Guide for introductory information about Recovery Appliance " LOG_ARCHIVE_DEST " and " LOG_ARCHIVE_DEST_n " " LOG_ARCHIVE_DUPLEX_DEST " and " LOG_ARCHIVE_DEST_STATE_n " " LOG_ARCHIVE_MIN_SUCCEED_DEST "