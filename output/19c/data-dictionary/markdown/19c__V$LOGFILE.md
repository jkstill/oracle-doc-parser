---
id: 19c__V$LOGFILE
name: V$LOGFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGFILE.html
---

# V$LOGFILE

V$LOGFILE contains information about redo log files.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP# | NUMBER |  |
| STATUS | VARCHAR2(7) |  |
| TYPE | VARCHAR2(7) |  |
| MEMBER | VARCHAR2(513) |  |
| IS_RECOVERY_DEST_FILE | VARCHAR2(3) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content