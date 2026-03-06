---
id: 19c__V$DATAFILE_HEADER
name: V$DATAFILE_HEADER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DATAFILE_HEADER.html
---

# V$DATAFILE_HEADER

V$DATAFILE_HEADER displays data file information from the data file headers.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| STATUS | VARCHAR2(7) |  |
| ERROR | VARCHAR2(18) |  |
| FORMAT | NUMBER |  |
| RECOVER | VARCHAR2(3) |  |
| FUZZY | VARCHAR2(3) |  |
| CREATION_CHANGE# | NUMBER |  |
| CREATION_TIME | DATE |  |
| TABLESPACE_NAME | VARCHAR2(30) |  |
| TS# | NUMBER |  |
| RFILE# | NUMBER |  |
| RESETLOGS_CHANGE# | NUMBER |  |
| RESETLOGS_TIME | DATE |  |
| CHECKPOINT_CHANGE# | NUMBER |  |
| CHECKPOINT_TIME | DATE |  |
| CHECKPOINT_COUNT | NUMBER |  |
| BYTES | NUMBER |  |
| BLOCKS | NUMBER |  |
| NAME | VARCHAR2(513) |  |
| SPACE_HEADER | VARCHAR2(40) |  |
| LAST_DEALLOC_CHANGE# | VARCHAR2(16) |  |
| UNDO_OPT_CURRENT_CHANGE# | VARCHAR2(40) |  |
| CON_ID | NUMBER |  |
| IS_SPARSE | VARCHAR2(3) |  |
| ENCRYPTED | VARCHAR2(3) |  |