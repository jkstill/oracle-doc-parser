---
id: 19c__V$LOGMNR_DICTIONARY
name: V$LOGMNR_DICTIONARY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGMNR_DICTIONARY.html
---

# V$LOGMNR_DICTIONARY

V$LOGMNR_DICTIONARY contains log history information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DB_NAME | VARCHAR2(9) |  |
| DB_ID | NUMBER |  |
| DB_CREATED | DATE |  |
| TIMESTAMP | DATE |  |
| RESET_SCN | NUMBER |  |
| RESET_SCN_TIME | DATE |  |
| DB_VERSION_TIME | DATE |  |
| DB_CHARACTER_SET | VARCHAR2(30) |  |
| DB_VERSION | VARCHAR2(64) |  |
| DB_STATUS | VARCHAR2(64) |  |
| DICTIONARY_SCN | NUMBER |  |
| ENABLED_THREAD_MAP | RAW(16) |  |
| DB_TXN_SCN | NUMBER |  |
| FILENAME | VARCHAR2(512) |  |
| INFO | VARCHAR2(32) |  |
| STATUS | NUMBER |  |
| CON_ID | NUMBER |  |