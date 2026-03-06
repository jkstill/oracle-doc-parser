---
id: 19c__ALL_PART_KEY_COLUMNS
name: ALL_PART_KEY_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_PART_KEY_COLUMNS.html
---

# ALL_PART_KEY_COLUMNS

ALL_PART_KEY_COLUMNS describes the partitioning key columns for the partitioned objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the partitioned table or index |
| NAME | VARCHAR2(128) | Name of the partitioned table or index |
| OBJECT_TYPE | CHAR(5) | Object type: TABLE INDEX |
| COLUMN_NAME | VARCHAR2(4000) | Name of the column |
| COLUMN_POSITION | NUMBER | Position of the column within the partitioning key |
| COLLATED_COLUMN_ID | NUMBER | Internal sequence number of the column for which this column provides linguistic ordering |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_PART_KEY_COLUMNS describes the partitioning key columns for all partitioned objects in the database. USER_PART_KEY_COLUMNS describes the partitioning key columns for the partitioned objects owned by the current user. This view does not display the OWNER column. See Also: " DBA_PART_KEY_COLUMNS " " USER_PART_KEY_COLUMNS " See Also: " DBA_PART_KEY_COLUMNS " " USER_PART_KEY_COLUMNS "