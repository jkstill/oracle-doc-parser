---
id: 19c__ALL_USTATS
name: ALL_USTATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_USTATS.html
---

# ALL_USTATS

ALL_USTATS describes the user-defined statistics collected on the tables and indexes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_OWNER | VARCHAR2(128) | Owner of the table or index for which the statistics have been collected |
| OBJECT_NAME | VARCHAR2(128) | Name of the table or index for which the statistics have been collected |
| PARTITION_NAME | VARCHAR2(128) | Partition name of a table; NULL if the table is either nonpartitioned or the entry corresponds to the aggregate statistics for the table |
| OBJECT_TYPE | VARCHAR2(6) | Type of the object for which statistics have been collected: INDEX COLUMN |
| ASSOCIATION | VARCHAR2(8) | Statistics type association: DIRECT Direct association with the object for which the statistics have been collected IMPLICIT - Association for which the statistics have been collected is with the column type or index type, and the object is an instance of that column type or index type |
| COLUMN_NAME | VARCHAR2(128) | Column name, if OBJECT_TYPE is COLUMN , for which statistics have been collected |
| STATSTYPE_SCHEMA | VARCHAR2(128) | Schema of the statistics type which was used to collect the statistics |
| STATSTYPE_NAME | VARCHAR2(128) | Name of the statistics type which was used to collect statistics |
| STATISTICS | RAW(2000) | User-collected statistics for the object |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_USTATS describes the user-defined statistics collected on all tables and indexes in the database. USER_USTATS describes the user-defined statistics collected on the tables and indexes owned by the current user. See Also: " DBA_USTATS " " USER_USTATS " See Also: " DBA_USTATS " " USER_USTATS "