---
id: 19c__ALL_BASE_TABLE_MVIEWS
name: ALL_BASE_TABLE_MVIEWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_BASE_TABLE_MVIEWS.html
---

# ALL_BASE_TABLE_MVIEWS

DBA_BASE_TABLE_MVIEWS describes all materialized views using materialized view logs in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Schema in which the master table or the master materialized view was created |
| MASTER | VARCHAR2(128) | Name of the master table or the master materialized view |
| MVIEW_LAST_REFRESH_TIME | DATE | Date when the materialized view based on the master was last refreshed |
| MVIEW_ID | NUMBER(38) | Unique identifier of the materialized view that is based on the master |

## Usage Notes

Related Views DBA_BASE_TABLE_MVIEWS describes all materialized views using materialized view logs in the database. USER_BASE_TABLE_MVIEWS describes the materialized views using materialized view logs owned by the current user. See Also: " DBA_BASE_TABLE_MVIEWS " " USER_BASE_TABLE_MVIEWS " See Also: " DBA_BASE_TABLE_MVIEWS " " USER_BASE_TABLE_MVIEWS "