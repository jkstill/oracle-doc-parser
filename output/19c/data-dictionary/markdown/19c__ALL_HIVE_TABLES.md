---
id: 19c__ALL_HIVE_TABLES
name: ALL_HIVE_TABLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_HIVE_TABLES.html
---

# ALL_HIVE_TABLES

ALL_HIVE_TABLES provides information about all the Hive tables accessible to the current user in the Hive metastore.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLUSTER_ID | VARCHAR2(4000) | Hadoop cluster name |
| DATABASE_NAME | VARCHAR2(4000) | Hive database where the Hive table resides |
| TABLE_NAME | VARCHAR2(4000) | Hive table name |
| LOCATION | VARCHAR2(4000) | Physical location of the Hive table |
| NO_OF_COLS | NUMBER | Number of columns in the Hive table |
| CREATION_TIME | DATE | Creation time of the Hive table |
| LAST_ACCESSED_TIME | DATE | Time that the Hive table was last accessed |
| OWNER | VARCHAR2(4000) | Owner of the Hive table |
| TABLE_TYPE | VARCHAR2(4000) | Type of the Hive table |
| PARTITIONED | VARCHAR2(4000) | Is this Hive table partitioned? |
| NO_OF_PART_KEYS | NUMBER | Number of partition keys in the Hive table |
| INPUT_FORMAT | VARCHAR2(4000) | Hive table input format |
| OUTPUT_FORMAT | VARCHAR2(4000) | Hive table output format |
| SERIALIZATION | VARCHAR2(4000) | Hive table serialization |
| COMPRESSED | NUMBER | Is this Hive table compressed? |
| HIVE_URI | VARCHAR2(4000) | The connection string (URI and port number) for the metastore database |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_HIVE_TABLES provides information about all Hive tables in the Hive metastore. USER_HIVE_TABLES provides information about all Hive tables owned by the current user in the Hive metastore. See Also: " DBA_HIVE_TABLES " " USER_HIVE_TABLES " See Also: " DBA_HIVE_TABLES " " USER_HIVE_TABLES "