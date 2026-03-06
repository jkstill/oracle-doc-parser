---
id: 19c__V$FLASHBACK_DATABASE_LOGFILE
name: V$FLASHBACK_DATABASE_LOGFILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-FLASHBACK_DATABASE_LOGFILE.html
---

# V$FLASHBACK_DATABASE_LOGFILE

V$FLASHBACK_DATABASE_LOGFILE displays information about the flashback log files.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(513) |  |
| LOG# | NUMBER |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| BYTES | NUMBER |  |
| FIRST_CHANGE# | NUMBER |  |
| FIRST_TIME | DATE |  |
| TYPE | VARCHAR2(9) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content