---
id: 19c__ALL_MVIEW_REFRESH_TIMES
name: ALL_MVIEW_REFRESH_TIMES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_MVIEW_REFRESH_TIMES.html
---

# ALL_MVIEW_REFRESH_TIMES

ALL_MVIEW_REFRESH_TIMES describes refresh times of the materialized views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the materialized view |
| NAME | VARCHAR2(128) | Name of the materialized view |
| MASTER_OWNER | VARCHAR2(128) | Owner of the master table |
| MASTER | VARCHAR2(128) | Name of the master table |
| LAST_REFRESH | DATE | SYSDATE from the master site at the time of the last refresh |

## Usage Notes

Related Views DBA_MVIEW_REFRESH_TIMES describes refresh times of all materialized views in the database. USER_MVIEW_REFRESH_TIMES describes refresh times of the materialized views owned by the current user. See Also: " DBA_MVIEW_REFRESH_TIMES " " USER_MVIEW_REFRESH_TIMES " See Also: " DBA_MVIEW_REFRESH_TIMES " " USER_MVIEW_REFRESH_TIMES "