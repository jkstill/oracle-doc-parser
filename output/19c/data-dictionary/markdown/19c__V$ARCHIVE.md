---
id: 19c__V$ARCHIVE
name: V$ARCHIVE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-ARCHIVE.html
---

# V$ARCHIVE

V$ARCHIVE displays information about redo log files in need of archiving.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP# | NUMBER |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| ISCURRENT | VARCHAR2(3) |  |
| CURRENT | VARCHAR2(3) |  |
| FIRST_CHANGE# | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Each row displays information for one thread. This information is also available in V$LOG . Oracle recommends that you use V$LOG . See Also: " V$LOG " See Also: " V$LOG "