---
id: 19c__ALL_HIVE_TAB_PARTITIONS
name: ALL_HIVE_TAB_PARTITIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: partitioning
tags: [all]
source_file: ALL_HIVE_TAB_PARTITIONS.html
---

# ALL_HIVE_TAB_PARTITIONS

ALL_HIVE_TAB_PARTITIONS provides information about all Hive table partitions accessible to the current user in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLUSTER_ID | VARCHAR2(4000) | Hadoop cluster name |
| DATABASE_NAME | VARCHAR2(4000) | Hive database where the Hive table resides |
| TABLE_NAME | VARCHAR2(4000) | Hive table name |
| LOCATION | VARCHAR2(4000) | Physical location of the Hive partition |
| OWNER | VARCHAR2(4000) | Owner of the Hive table |
| PARTITION_SPECS | VARCHAR2(4000) | The current Hive partition specification |
| PART_SIZE | NUMBER | Partition size in bytes |
| CREATION_TIME | DATE | Time that the partition was created |

## Usage Notes

Related Views DBA_HIVE_TAB_PARTITIONS provides information about all Hive table partitions in the database. USER_HIVE_TAB_PARTITIONS provides information about all Hive table partitions owned by the current user in the database. See Also: " DBA_HIVE_TAB_PARTITIONS " " USER_HIVE_TAB_PARTITIONS " See Also: " DBA_HIVE_TAB_PARTITIONS " " USER_HIVE_TAB_PARTITIONS "