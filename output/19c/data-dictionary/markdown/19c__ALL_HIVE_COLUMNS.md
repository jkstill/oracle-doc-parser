---
id: 19c__ALL_HIVE_COLUMNS
name: ALL_HIVE_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_HIVE_COLUMNS.html
---

# ALL_HIVE_COLUMNS

ALL_HIVE_COLUMNS describes all Hive columns accessible to the current user in a Hive metastore.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLUSTER_ID | VARCHAR2(4000) | Identifier for the Hadoop cluster |
| DATABASE_NAME | VARCHAR2(4000) | Hive database where the owning Hive table resides |
| TABLE_NAME | VARCHAR2(4000) | Hive table name that the column belongs to |
| COLUMN_NAME | VARCHAR2(4000) | Hive column name |
| HIVE_COLUMN_TYPE | VARCHAR2(4000) | Data type of the Hive column |
| ORACLE_COLUMN_TYPE | VARCHAR2(4000) | Equivalent Oracle data type of the Hive column |
| LOCATION | VARCHAR2(4000) | Physical location of the Hive table |
| OWNER | VARCHAR2(4000) | Owner of the Hive table |
| CREATION_TIME | DATE | Time that the Hive column was created |
| HIVE_URI | VARCHAR2(4000) | The connection string (URI and port number) for the metastore database |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_HIVE_COLUMNS describes all Hive columns in a Hive metastore. USER_HIVE_COLUMNS describes all Hive columns owned by the current user in a Hive metastore. See Also: " DBA_HIVE_COLUMNS " " USER_HIVE_COLUMNS " See Also: " DBA_HIVE_COLUMNS " " USER_HIVE_COLUMNS "