---
id: 19c__V$LOGMNR_LOGS
name: V$LOGMNR_LOGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGMNR_LOGS.html
---

# V$LOGMNR_LOGS

V$LOGMNR_LOGS contains log information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| LOG_ID | NUMBER |  |
| FILENAME | VARCHAR2(512) |  |
| LOW_TIME | DATE |  |
| HIGH_TIME | DATE |  |
| DB_ID | NUMBER |  |
| DB_NAME | VARCHAR2(8) |  |
| RESET_SCN | NUMBER |  |
| RESET_SCN_TIME | DATE |  |
| COMPATIBLE | VARCHAR2(17) |  |
| THREAD_ID | NUMBER |  |
| THREAD_SQN | NUMBER |  |
| LOW_SCN | NUMBER |  |
| NEXT_SCN | NUMBER |  |
| DICTIONARY_BEGIN | VARCHAR2(3) |  |
| DICTIONARY_END | VARCHAR2(3) |  |
| TYPE | VARCHAR2(7) |  |
| BLOCKSIZE | NUMBER |  |
| FILESIZE | NUMBER |  |
| INFO | VARCHAR2(32) |  |
| STATUS | NUMBER |  |
| CON_ID | NUMBER |  |