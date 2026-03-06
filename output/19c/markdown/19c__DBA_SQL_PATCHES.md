---
id: 19c__DBA_SQL_PATCHES
name: DBA_SQL_PATCHES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dba]
source_file: DBA_SQL_PATCHES.html
---

# DBA_SQL_PATCHES

DBA_SQL_PATCHES displays the set of SQL patches.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(128) | Name of the SQL patch |
| CATEGORY | VARCHAR2(128) | Category of the SQL patch |
| SIGNATURE | NUMBER | Unique identifier generated from normalized SQL text |
| SQL_TEXT | CLOB | Un-normalized SQL text |
| CREATED | TIMESTAMP(6) | Timestamp when the SQL patch was created |
| LAST_MODIFIED | TIMESTAMP(6) | Timestamp when the SQL patch was last modified |
| DESCRIPTION | VARCHAR2(500) | Text description provided for the SQL patch |
| STATUS | VARCHAR2(8) | Status of the SQL patch: ENABLED DISABLED |
| FORCE_MATCHING | VARCHAR2(3) | Indicates whether the signature is force matching ( YES ) or exact matching ( NO ) |
| TASK_ID | NUMBER | Advisor task ID that generated the SQL patch |
| TASK_EXEC_NAME | VARCHAR2(128) | Advisor execution name for the SQL patch |
| TASK_OBJ_ID | NUMBER | Advisor object ID for the SQL patch |
| TASK_FND_ID | NUMBER | Advisor finding ID for the SQL patch |
| TASK_REC_ID | NUMBER | Advisor recommendation ID for the SQL patch |