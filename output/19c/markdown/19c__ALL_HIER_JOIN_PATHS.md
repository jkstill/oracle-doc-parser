---
id: 19c__ALL_HIER_JOIN_PATHS
name: ALL_HIER_JOIN_PATHS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_HIER_JOIN_PATHS.html
---

# ALL_HIER_JOIN_PATHS

ALL_HIER_JOIN_PATHS describes the join paths for the hierarchies accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the hierarchy |
| HIER_NAME | VARCHAR2(128) | Name of the hierarchy |
| JOIN_PATH_NAME | VARCHAR2(128) | Name of the join path |
| ORDER_NUM | NUMBER | Order of the classification in the list of join paths associated with the hierarchy |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root). |

## Usage Notes

Related Views DBA_HIER_JOIN_PATHS describes the join paths for all hierarchies in the database. USER_HIER_JOIN_PATHS describes the join paths for the hierarchies owned by the current user. This view does not display the OWNER column. See Also: " DBA_HIER_JOIN_PATHS " " USER_HIER_JOIN_PATHS " See Also: " DBA_HIER_JOIN_PATHS " " USER_HIER_JOIN_PATHS "