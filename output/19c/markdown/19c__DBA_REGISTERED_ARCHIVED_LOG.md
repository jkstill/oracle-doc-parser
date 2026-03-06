---
id: 19c__DBA_REGISTERED_ARCHIVED_LOG
name: DBA_REGISTERED_ARCHIVED_LOG
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_REGISTERED_ARCHIVED_LOG.html
---

# DBA_REGISTERED_ARCHIVED_LOG

DBA_REGISTERED_ARCHIVED_LOG displays information about all registered archived logfiles in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CONSUMER_NAME | VARCHAR2(128) | Consumer name of the archived logs |
| SOURCE_DATABASE | VARCHAR2(128) | Name of the database which generated the redo logs |
| THREAD# | NUMBER | Thread number of the archived redo log. The thread number is 1 for a single instance. For Real Application Clusters, this column will contain different numbers. |
| SEQUENCE# | NUMBER | Sequence number of the archived redo log file |
| FIRST_SCN | NUMBER | System change number (SCN) of the current archived redo log |
| NEXT_SCN | NUMBER | System change number (SCN) of the next archived redo log |
| FIRST_TIME | DATE | Date and time of the current archived redo log |
| NEXT_TIME | DATE | Date and time of the next archived redo log |
| NAME | VARCHAR2(513) | Name of the archived redo log |
| MODIFIED_TIME | DATE | Time when the archived redo log was registered |
| DICTIONARY_BEGIN | VARCHAR2(3) | Indicates whether the beginning of the dictionary build is in the archived redo log ( YES ) or not ( NO ) |
| DICTIONARY_END | VARCHAR2(3) | Indicates whether the end of the dictionary build is in the archived redo log ( YES ) or not ( NO ) |
| PURGEABLE | VARCHAR2(3) | Indicates whether the redo log can be permanently removed ( YES ) or not ( NO ) |
| RESET_LOGS_CHANGE# | NUMBER | Resetlogs change number of the database when the log was written |
| RESET_TIMESTAMP | NUMBER | Resetlogs time of the database when the log was written |