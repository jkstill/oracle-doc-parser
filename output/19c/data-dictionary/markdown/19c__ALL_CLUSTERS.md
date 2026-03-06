---
id: 19c__ALL_CLUSTERS
name: ALL_CLUSTERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_CLUSTERS.html
---

# ALL_CLUSTERS

ALL_CLUSTERS describes all clusters accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the cluster |
| CLUSTER_NAME | VARCHAR2(128) | Name of the cluster |
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace containing the cluster |
| PCT_FREE | NUMBER | Minimum percentage of free space in a block |
| PCT_USED | NUMBER | Minimum percentage of used space in a block |
| KEY_SIZE | NUMBER | Estimated size of cluster key plus associated rows |
| INI_TRANS | NUMBER | Initial number of transactions |
| MAX_TRANS | NUMBER | Maximum number of transactions |
| INITIAL_EXTENT | NUMBER | Size of the initial extent in bytes |
| NEXT_EXTENT | NUMBER | Size of secondary extents in bytes |
| MIN_EXTENTS | NUMBER | Minimum number of extents allowed in the segment |
| MAX_EXTENTS | NUMBER | Maximum number of extents allowed in the segment |
| PCT_INCREASE | NUMBER | Percentage increase in extent size |
| FREELISTS | NUMBER | Number of process freelists allocated to this segment |
| FREELIST_GROUPS | NUMBER | Number of freelist groups allocated to this segment |
| AVG_BLOCKS_PER_KEY | NUMBER | Number of blocks in the table divided by number of cluster keys |
| CLUSTER_TYPE | VARCHAR2(5) | Type of the cluster: INDEX - B*-Tree index HASH - Hash |
| FUNCTION | VARCHAR2(15) | If the cluster is a hash cluster, the hash function |
| HASHKEYS | NUMBER | If the cluster is a hash cluster, the number of hash keys (hash buckets) |
| DEGREE | VARCHAR2(10) | Number of threads per instance for scanning the cluster, or DEFAULT |
| INSTANCES | VARCHAR2(10) | Number of instances across which the cluster is to be scanned , or DEFAULT |
| CACHE | VARCHAR2(5) | Indicates whether the cluster is to be cached in the buffer cache ( Y ) or not ( N ) |
| BUFFER_POOL | VARCHAR2(7) | Buffer pool to be used for cluster blocks: DEFAULT KEEP RECYCLE NULL |
| FLASH_CACHE | VARCHAR2(7) | Database Smart Flash Cache hint to be used for cluster blocks: DEFAULT KEEP NONE Solaris and Oracle Linux functionality only. |
| CELL_FLASH_CACHE | VARCHAR2(7) | Cell flash cache hint to be used for cluster blocks: DEFAULT KEEP NONE See Also: Oracle Exadata Storage Server Software documentation for more information |
| SINGLE_TABLE | VARCHAR2(5) | Indicates whether this is a single-table cluster ( Y ) or not ( N ) |
| DEPENDENCIES | VARCHAR2(8) | Indicates whether row-level dependency tracking is enabled ( ENABLED ) or disabled ( DISABLED ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_CLUSTERS describes all clusters in the database. USER_CLUSTERS describes all clusters owned by the current user. This view does not display the OWNER column. See Also: " DBA_CLUSTERS " " USER_CLUSTERS " See Also: " DBA_CLUSTERS " " USER_CLUSTERS "