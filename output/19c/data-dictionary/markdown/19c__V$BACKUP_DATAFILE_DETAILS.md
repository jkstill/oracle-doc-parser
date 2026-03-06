---
id: 19c__V$BACKUP_DATAFILE_DETAILS
name: V$BACKUP_DATAFILE_DETAILS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_DATAFILE_DETAILS.html
---

# V$BACKUP_DATAFILE_DETAILS

V$BACKUP_DATAFILE_DETAILS contains information about restorable data files.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BTYPE | CHAR(9) |  |
| BTYPE_KEY | NUMBER |  |
| SESSION_KEY | NUMBER |  |
| SESSION_RECID | NUMBER |  |
| SESSION_STAMP | NUMBER |  |
| ID1 | NUMBER |  |
| ID2 | NUMBER |  |
| FILE# | NUMBER |  |
| CREATION_CHANGE# | NUMBER |  |
| CREATION_TIME | DATE |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| INCREMENTAL_LEVEL | NUMBER |  |
| INCREMENTAL_CHANGE# | NUMBER |  |
| CHECKPOINT_CHANGE# | NUMBER |  |
| CHECKPOINT_TIME | DATE |  |
| MARKED_CORRUPT | NUMBER |  |
| FILESIZE | NUMBER |  |
| COMPRESSION_RATIO | NUMBER |  |
| SPARSE_BACKUP | VARCHAR2(3) |  |
| TS# | NUMBER |  |
| TSNAME | VARCHAR2(30) |  |
| FILESIZE_DISPLAY | VARCHAR2(4000) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content It will include all data files backed in the backup set, image copies, and proxy copies.