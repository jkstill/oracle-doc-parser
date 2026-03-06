---
id: 19c__DBA_MVIEW_LOG_FILTER_COLS
name: DBA_MVIEW_LOG_FILTER_COLS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_MVIEW_LOG_FILTER_COLS.html
---

# DBA_MVIEW_LOG_FILTER_COLS

DBA_MVIEW_LOG_FILTER_COLS displays all columns (excluding primary key columns) being logged in the materialized view logs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the master table being logged |
| NAME | VARCHAR2(128) | Name of the master table being logged |
| COLUMN_NAME | VARCHAR2(128) | Column being logged |