---
id: 19c__ALL_IND_PENDING_STATS
name: ALL_IND_PENDING_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [all]
source_file: ALL_IND_PENDING_STATS.html
---

# ALL_IND_PENDING_STATS

ALL_IND_PENDING_STATS describes the pending statistics for tables, partitions, and subpartitions accessible to the current user collected using the DBMS_STATS package.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Name of the index owner |
| INDEX_NAME | VARCHAR2(128) | Index name |
| TABLE_OWNER | VARCHAR2(128) | Table owner name |
| TABLE_NAME | VARCHAR2(128) | Name of the table |
| PARTITION_NAME | VARCHAR2(128) | Name of the partition |
| SUBPARTITION_NAME | VARCHAR2(128) | Name of the subpartition |
| BLEVEL | NUMBER | Number of levels in the index |
| LEAF_BLOCKS | NUMBER | Number of leaf blocks in the index |
| DISTINCT_KEYS | NUMBER | Number of distinct keys in the index |
| AVG_LEAF_BLOCKS_PER_KEY | NUMBER | Average number of leaf blocks per key |
| AVG_DATA_BLOCKS_PER_KEY | NUMBER | Average number of data blocks per key |
| CLUSTERING_FACTOR | NUMBER | Clustering factor |
| NUM_ROWS | NUMBER | Number of rows in the index |
| SAMPLE_SIZE | NUMBER | Sample size |
| LAST_ANALYZED | DATE | Time of the last analysis |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_IND_PENDING_STATS describes pending statistics for all tables, partitions, and subpartitions in the database. USER_IND_PENDING_STATS describes pending statistics for tables, partitions, and subpartitions owned by the current user. This view does not display the OWNER column. See Also: " DBA_IND_PENDING_STATS " " USER_IND_PENDING_STATS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package See Also: " DBA_IND_PENDING_STATS " " USER_IND_PENDING_STATS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_STATS package