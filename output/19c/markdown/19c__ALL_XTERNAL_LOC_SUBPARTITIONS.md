---
id: 19c__ALL_XTERNAL_LOC_SUBPARTITIONS
name: ALL_XTERNAL_LOC_SUBPARTITIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: partitioning
tags: [all]
source_file: ALL_XTERNAL_LOC_SUBPARTITIONS.html
---

# ALL_XTERNAL_LOC_SUBPARTITIONS

ALL_XTERNAL_LOC_SUBPARTITIONS describes subpartition-level locations accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLE_OWNER | VARCHAR2(128) | Owner of the partitioned external table |
| TABLE_NAME | VARCHAR2(128) | Name of the partitioned external table |
| PARTITION_NAME | VARCHAR2(128) | Name of the partition |
| SUBPARTITION_NAME | VARCHAR2(128) | Name of the subpartition |
| LOCATION | VARCHAR2(4000) | External table location clause for the subpartition |
| DIRECTORY_OWNER | CHAR(3) | Owner of the directory containing the external table subpartition location |
| DIRECTORY_NAME | VARCHAR2(128) | Name of the directory containing the external table subpartition location |

## Usage Notes

Related Views If an external table is partitioned, then the existing ALL_EXTERNAL_LOCATIONS , DBA_EXTERNAL_LOCATIONS , and USER_EXTERNAL_LOCATIONS views will have no rows for that table. Instead, locations will be indicated in the ALL_XTERNAL_LOC_PARTITIONS , DBA_XTERNAL_LOC_PARTITIONS , USER_XTERNAL_LOC_PARTITIONS , ALL_XTERNAL_LOC_SUBPARTITIONS , DBA_XTERNAL_LOC_SUBPARTITIONS , and USER_XTERNAL_LOC_SUBPARTITIONS views. DBA_XTERNAL_LOC_SUBPARTITIONS describes subpartition-level locations in the database. USER_XTERNAL_LOC_SUBPARTITIONS describes subpartition-level locations owned by the current user. This view does not display the TABLE_OWNER column. See Also: " DBA_XTERNAL_LOC_SUBPARTITIONS " " USER_XTERNAL_LOC_SUBPARTITIONS " See Also: " DBA_XTERNAL_LOC_SUBPARTITIONS " " USER_XTERNAL_LOC_SUBPARTITIONS "