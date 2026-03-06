---
id: 19c__V$COPY_NONLOGGED
name: V$COPY_NONLOGGED
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-COPY_NONLOGGED.html
---

# V$COPY_NONLOGGED

V$COPY_NONLOGGED displays information about nonlogged block ranges in data file copy blocks, recorded in the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INST_ID | NUMBER |  |
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| COPY_RECID | NUMBER |  |
| COPY_STAMP | NUMBER |  |
| FILE# | NUMBER |  |
| BLOCK# | NUMBER |  |
| BLOCKS | NUMBER |  |
| NONLOGGED_CHANGE# | NUMBER |  |
| NONLOGGED_TIME | VARCHAR2 |  |
| RESETLOGS_CHANGE# | VARCHAR2 |  |
| RESETLOGS_TIME | VARCHAR2 |  |
| OBJECT# | VARCHAR2 |  |
| REASON | CHAR(7) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content