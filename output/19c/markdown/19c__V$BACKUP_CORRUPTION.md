---
id: 19c__V$BACKUP_CORRUPTION
name: V$BACKUP_CORRUPTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BACKUP_CORRUPTION.html
---

# V$BACKUP_CORRUPTION

V$BACKUP_CORRUPTION displays information about corrupt block ranges in data file backups from the control file.

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
| CORRUPTION_CHANGE# | NUMBER |  |
| MARKED_CORRUPT | VARCHAR2(3) |  |
| CORRUPTION_TYPE | VARCHAR2(9) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note that corruptions are not tolerated in the control file and archived redo log backups.