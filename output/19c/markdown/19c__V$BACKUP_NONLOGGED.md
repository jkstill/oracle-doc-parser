---
id: 19c__V$BACKUP_NONLOGGED
name: V$BACKUP_NONLOGGED
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-BACKUP_NONLOGGED.html
---

# V$BACKUP_NONLOGGED

V$BACKUP_NONLOGGED displays information about nonlogged block ranges in data file backups, recorded in the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| RECID | NUMBER |  |
| STAMP | NUMBER |  |
| SET_STAMP | NUMBER |  |
| SET_COUNT | NUMBER |  |
| PIECE# | NUMBER |  |
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