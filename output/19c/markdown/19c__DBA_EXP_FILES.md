---
id: 19c__DBA_EXP_FILES
name: DBA_EXP_FILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_EXP_FILES.html
---

# DBA_EXP_FILES

DBA_EXP_FILES describes export files.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EXP_VERSION | NUMBER(3) | Version number of the export session |
| EXP_TYPE | VARCHAR2(11) | Type of export file: complete, cumulative, or incremental |
| FILE_NAME | VARCHAR2(100) | Name of the export file |
| USER_NAME | VARCHAR2(128) | Name of user who executed export |
| TIMESTAMP | DATE | Timestamp of the export session |