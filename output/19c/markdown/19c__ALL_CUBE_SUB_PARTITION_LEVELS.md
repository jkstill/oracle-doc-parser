---
id: 19c__ALL_CUBE_SUB_PARTITION_LEVELS
name: ALL_CUBE_SUB_PARTITION_LEVELS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: partitioning
tags: [all]
source_file: ALL_CUBE_SUB_PARTITION_LEVELS.html
---

# ALL_CUBE_SUB_PARTITION_LEVELS

ALL_CUBE_SUB_PARTITION_LEVELS describes the OLAP secondary partition levels in the database that are accessible by the user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the OLAP secondary partition level |
| CUBE_NAME | VARCHAR2(128) | Name of the OLAP cube |
| SUB_PARTITION_LEVEL_NAME | VARCHAR2(200) | Name of the secondary partition level of the OLAP cube |
| PRECOMPUTE_PERCENT | NUMBER | Precompute percent of the secondary partition level of the OLAP cube |
| PARTITION_DIMENSION_NAME | VARCHAR2(128) | Name of the cube dimension for which there is a secondary partition level on the OLAP cube |
| PARTITION_HIERARCHY_NAME | VARCHAR2(128) | Name of the hierarchy for which there is a secondary partition level on the OLAP cube |
| PARTITION_LEVEL_NAME | VARCHAR2(128) | Name of the hierarchy level for which there is a secondary partition level on the OLAP cube |
| SUB_PARTITION_LEVEL_ORDER | NUMBER | Order number of the secondary partition level on the OLAP cube |

## Usage Notes

Related Views DBA_CUBE_SUB_PARTITION_LEVELS describes the OLAP secondary partition levels in the database. USER_CUBE_SUB_PARTITION_LEVELS describes the OLAP secondary partition levels in the database that are owned by the current user. This view does not display the OWNER column. See Also: " DBA_CUBE_SUB_PARTITION_LEVELS " " USER_CUBE_SUB_PARTITION_LEVELS " See Also: " DBA_CUBE_SUB_PARTITION_LEVELS " " USER_CUBE_SUB_PARTITION_LEVELS "