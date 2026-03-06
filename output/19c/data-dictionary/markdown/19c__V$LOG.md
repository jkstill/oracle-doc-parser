---
id: 19c__V$LOG
name: V$LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOG.html
---

# V$LOG

V$LOG displays log file information from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP# | NUMBER |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| BYTES | NUMBER |  |
| BLOCKSIZE | NUMBER |  |
| MEMBERS | NUMBER |  |
| ARCHIVED | VARCHAR2(3) |  |
| STATUS | VARCHAR2(16) |  |
| FIRST_CHANGE# | NUMBER |  |
| FIRST_TIME | DATE |  |
| NEXT_CHANGE# | NUMBER |  |
| NEXT_TIME | DATE |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content