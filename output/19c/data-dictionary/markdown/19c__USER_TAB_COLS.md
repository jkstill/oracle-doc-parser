---
id: 19c__USER_TAB_COLS
name: USER_TAB_COLS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_TAB_COLS.html
---

# USER_TAB_COLS

USER_TAB_COLS describes the columns of the tables, views, and clusters owned by the current user.

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Its columns (except for OWNER ) are the same as those in ALL_TAB_COLS . To gather statistics for this view, use the DBMS_STATS package. This view differs from USER_TAB_COLUMNS in that system-generated hidden columns are not filtered out. See Also: " ALL_TAB_COLS " " USER_TAB_COLUMNS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package See Also: " ALL_TAB_COLS " " USER_TAB_COLUMNS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package