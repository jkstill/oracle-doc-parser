---
id: 19c__USER_TAB_COLUMNS
name: USER_TAB_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [user]
source_file: USER_TAB_COLUMNS.html
---

# USER_TAB_COLUMNS

USER_TAB_COLUMNS describes the columns of the tables, views, and clusters owned by the current user.

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Its columns (except for OWNER ) are the same as those in ALL_TAB_COLUMNS . To gather statistics for this view, use the DBMS_STATS package. This view filters out system-generated hidden columns. The USER_TAB_COLS view does not filter out system-generated hidden columns. See Also: " ALL_TAB_COLUMNS " " USER_TAB_COLS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package See Also: " ALL_TAB_COLUMNS " " USER_TAB_COLS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package