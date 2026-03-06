---
id: 19c__ALL_HIVE_DATABASES
name: ALL_HIVE_DATABASES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_HIVE_DATABASES.html
---

# ALL_HIVE_DATABASES

ALL_HIVE_DATABASES describes all the Hive schemas accessible to the current user in a Hadoop cluster.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLUSTER_ID | VARCHAR2(4000) | Hadoop cluster name |
| DATABASE_NAME | VARCHAR2(4000) | Name of the Hive database |
| DESCRIPTION | VARCHAR2(4000) | Description of the Hive database |
| DB_LOCATION | VARCHAR2(4000) | Physical location of the Hive database |
| HIVE_URI | VARCHAR2(4000) | The connection string (URI and port number) for the metastore database |

## Usage Notes

Related Views DBA_HIVE_DATABASES describes all the Hive schemas in a Hadoop cluster. USER_HIVE_DATABASES describes all the Hive schemas owned by the current user in a Hadoop cluster. See Also: " DBA_HIVE_DATABASES " " USER_HIVE_DATABASES " See Also: " DBA_HIVE_DATABASES " " USER_HIVE_DATABASES "