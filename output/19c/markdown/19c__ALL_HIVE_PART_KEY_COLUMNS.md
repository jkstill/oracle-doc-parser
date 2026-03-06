---
id: 19c__ALL_HIVE_PART_KEY_COLUMNS
name: ALL_HIVE_PART_KEY_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_HIVE_PART_KEY_COLUMNS.html
---

# ALL_HIVE_PART_KEY_COLUMNS

ALL_HIVE_PART_KEY_COLUMNS provides information about all Hive table partition columns accessible to the current user in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLUSTER_ID | VARCHAR2(4000) | Hadoop cluster name |
| DATABASE_NAME | VARCHAR2(4000) | Hive database where the Hive table resides |
| TABLE_NAME | VARCHAR2(4000) | Hive table name |
| OWNER | VARCHAR2(4000) | Owner of the Hive table |
| COLUMN_NAME | VARCHAR2(4000) | Partition column name |
| COLUMN_TYPE | VARCHAR2(4000) | Partition column type |
| COLUMN_POSITION | NUMBER | Partition column position in the Hive partition specification |
| ORACLE_COLUMN_TYPE | VARCHAR2(4000) | Equivalent Oracle data type of the Hive column |

## Usage Notes

Related Views DBA_HIVE_PART_KEY_COLUMNS provides information about all Hive table partition columns in the database. USER_HIVE_PART_KEY_COLUMNS provides information about all Hive table partition columns owned by the current user in the database. See Also: " DBA_HIVE_PART_KEY_COLUMNS " " USER_HIVE_PART_KEY_COLUMNS " See Also: " DBA_HIVE_PART_KEY_COLUMNS " " USER_HIVE_PART_KEY_COLUMNS "