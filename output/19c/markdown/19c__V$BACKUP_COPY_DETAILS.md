---
id: 19c__V$BACKUP_COPY_DETAILS
name: V$BACKUP_COPY_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_COPY_DETAILS.html
---

# V$BACKUP_COPY_DETAILS

V$BACKUP_COPY_DETAILS contains information about all available control file and data file copies.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SESSION_KEY | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| COPY_KEY | NUMBER |  |
| FILE# | NUMBER |  |
| NAME | VARCHAR2(513) |  |
| TAG | VARCHAR2(32) |  |
| CREATION_CHANGE# | NUMBER |  |
| CREATION_TIME | DATE |  |
| CHECKPOINT_CHANGE# | NUMBER |  |
| CHECKPOINT_TIME | DATE |  |
| MARKED_CORRUPT | NUMBER |  |
| OUTPUT_BYTES | NUMBER |  |
| COMPLETION_TIME | DATE |  |
| CONTROLFILE_TYPE | VARCHAR2(1) |  |
| KEEP | VARCHAR2(3) |  |
| KEEP_UNTIL | DATE |  |
| KEEP_OPTIONS | VARCHAR2(11) |  |
| IS_RECOVERY_DEST_FILE | VARCHAR2(3) |  |
| SPARSE_BACKUP | VARCHAR2(3) |  |
| OUTPUT_BYTES_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |