---
id: 19c__V$RECOVER_FILE
name: V$RECOVER_FILE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-RECOVER_FILE.html
---

# V$RECOVER_FILE

V$RECOVER_FILE displays the status of files needing media recovery.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| ONLINE | VARCHAR2(7) |  |
| ONLINE_STATUS | VARCHAR2(7) |  |
| ERROR | VARCHAR2(18) |  |
| CHANGE# | NUMBER |  |
| TIME | DATE |  |
| CON_ID | NUMBER |  |