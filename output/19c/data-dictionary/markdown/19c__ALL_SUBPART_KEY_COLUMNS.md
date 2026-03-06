---
id: 19c__ALL_SUBPART_KEY_COLUMNS
name: ALL_SUBPART_KEY_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_SUBPART_KEY_COLUMNS.html
---

# ALL_SUBPART_KEY_COLUMNS

ALL_SUBPART_KEY_COLUMNS displays subpartitioning key columns for composite-partitioned tables (and local indexes on composite-partitioned tables) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the partitioned table or index |
| NAME | VARCHAR2(128) | Name of the partitioned table or index |
| OBJECT_TYPE | CHAR(5) | Object type: TABLE INDEX |
| COLUMN_NAME | VARCHAR2(4000) | Column name |
| COLUMN_POSITION | NUMBER | Position of the column within the subpartitioning key |
| COLLATED_COLUMN_ID | NUMBER | Internal sequence number of the column for which this column provides linguistic ordering |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SUBPART_KEY_COLUMNS displays this information for all subpartitions in the database. USER_SUBPART_KEY_COLUMNS displays this information for subpartitions of all partitioned objects owned by the current user. This view does not display the OWNER column. See Also: " DBA_SUBPART_KEY_COLUMNS " " USER_SUBPART_KEY_COLUMNS " See Also: " DBA_SUBPART_KEY_COLUMNS " " USER_SUBPART_KEY_COLUMNS "