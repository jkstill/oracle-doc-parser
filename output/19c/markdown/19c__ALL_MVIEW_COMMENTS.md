---
id: 19c__ALL_MVIEW_COMMENTS
name: ALL_MVIEW_COMMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: objects
tags: [all]
source_file: ALL_MVIEW_COMMENTS.html
---

# ALL_MVIEW_COMMENTS

ALL_MVIEW_COMMENTS displays comments on the materialized views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the materialized view |
| MVIEW_NAME | VARCHAR2(128) | Name of the materialized view |
| COMMENTS | VARCHAR2(4000) | Comment on the materialized view |

## Usage Notes

Related Views DBA_MVIEW_COMMENTS displays comments on the materialized views in the database. USER_MVIEW_COMMENTS displays comments on the materialized views owned by the current user. This view does not display the OWNER column. See Also: " DBA_MVIEW_COMMENTS " " USER_MVIEW_COMMENTS " See Also: " DBA_MVIEW_COMMENTS " " USER_MVIEW_COMMENTS "