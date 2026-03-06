---
id: 19c__V$STANDBY_LOG
name: V$STANDBY_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-STANDBY_LOG.html
---

# V$STANDBY_LOG

Database ID of the primary database to which the standby redo logfile is assigned. If the standby redo logfile is unassigned, the value UNASSIGNED will be displayed.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP# | NUMBER |  |
| DBID | VARCHAR2(40) |  |
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| BYTES | NUMBER |  |
| BLOCKSIZE | NUMBER |  |
| USED | NUMBER |  |
| ARCHIVED | VARCHAR2(3) |  |
| STATUS | VARCHAR2(10) |  |
| FIRST_CHANGE# | NUMBER |  |
| FIRST_TIME | DATE |  |
| NEXT_CHANGE# | NUMBER |  |
| NEXT_TIME | DATE |  |
| LAST_CHANGE# | NUMBER |  |
| LAST_TIME | DATE |  |
| CON_ID | NUMBER |  |