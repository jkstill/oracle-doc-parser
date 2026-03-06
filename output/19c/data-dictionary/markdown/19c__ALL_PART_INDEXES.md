---
id: 19c__ALL_PART_INDEXES
name: ALL_PART_INDEXES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [all]
source_file: ALL_PART_INDEXES.html
---

# ALL_PART_INDEXES

ALL_PART_INDEXES displays the object-level partitioning information for the partitioned indexes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the partitioned index |
| INDEX_NAME | VARCHAR2(128) | Name of the partitioned index |
| TABLE_NAME | VARCHAR2(128) | Name of the partitioned table |
| PARTITIONING_TYPE | VARCHAR2(9) | Type of the partitioning method: NONE - Not specified See Also: the *_INDEXES view RANGE HASH SYSTEM LIST REFERENCE |
| SUBPARTITIONING_TYPE | VARCHAR2(9) | Type of the composite partitioning method: NONE - Not specified See Also: the *_INDEXES view RANGE HASH SYSTEM LIST REFERENCE |
| PARTITION_COUNT | NUMBER | Number of partitions in the index |
| DEF_SUBPARTITION_COUNT | NUMBER | For a composite-partitioned index, the default number of subpartitions, if specified |
| PARTITIONING_KEY_COUNT | NUMBER | Number of columns in the partitioning key |
| SUBPARTITIONING_KEY_COUNT | NUMBER | For a composite-partitioned index, the number of columns in the subpartitioning key |
| LOCALITY | VARCHAR2(6) | Indicates whether the partitioned index is local ( LOCAL ) or global ( GLOBAL ) |
| ALIGNMENT | VARCHAR2(12) | Indicates whether the partitioned index is prefixed ( PREFIXED ) or non-prefixed ( NON_PREFIXED ) |
| DEF_TABLESPACE_NAME | VARCHAR2(30) | For a local index, the default tablespace to be used when adding or splitting a table partition |
| DEF_PCT_FREE | NUMBER | For a local index, the default PCTFREE value to be used when adding a table partition |
| DEF_INI_TRANS | NUMBER | For a local index, the default INITRANS value to be used when adding a table partition |
| DEF_MAX_TRANS | NUMBER | For a local index, the default MAXTRANS value to be used when adding a table partition |
| DEF_INITIAL_EXTENT | VARCHAR2(40) | For a local index, the default INITIAL value (in Oracle blocks) to be used when adding a table partition, or DEFAULT if no INITIAL value was specified |
| DEF_NEXT_EXTENT | VARCHAR2(40) | For a local index, the default NEXT value (in Oracle blocks) to be used when adding a table partition, or DEFAULT if no NEXT value was specified |
| DEF_MIN_EXTENTS | VARCHAR2(40) | For a local index, the default MINEXTENTS value to be used when adding a table partition, or DEFAULT if no MINEXTENTS value was specified |
| DEF_MAX_EXTENTS | VARCHAR2(40) | For a local index, the default MAXEXTENTS value to be used when adding a table partition, or DEFAULT if no MAXEXTENTS value was specified |
| DEF_MAX_SIZE | VARCHAR2(40) | For a local index, the default MAXSIZE value to be used when adding a table partition, or DEFAULT if no MAXSIZE value was specified |
| DEF_PCT_INCREASE | VARCHAR2(40) | For a local index, the default PCTINCREASE value to be used when adding a table partition, or DEFAULT if no PCTINCREASE value was specified |
| DEF_FREELISTS | NUMBER | For a local index, the default FREELISTS value to be used when adding a table partition |
| DEF_FREELIST_GROUPS | NUMBER | For a local index, the default FREELIST GROUPS value to be used when adding a table partition |
| DEF_LOGGING | VARCHAR2(7) | For a local index, the default LOGGING attribute to be used when adding a table partition: NONE - Not specified See Also: the *_INDEXES view YES NO |
| DEF_BUFFER_POOL | VARCHAR2(7) | For a local index, the default buffer pool to be used when adding a table partition: DEFAULT KEEP RECYCLE NULL |
| DEF_FLASH_CACHE | VARCHAR2(7) | For a local index, the default Database Smart Flash Cache hint to be used when adding a table partition: DEFAULT KEEP NONE Solaris and Oracle Linux functionality only. |
| DEF_CELL_FLASH_CACHE | VARCHAR2(7) | For a local index, the default cell flash cache hint to be used when adding a table partition: DEFAULT KEEP NONE See Also: Oracle Exadata Storage Server Software documentation for more information |
| DEF_PARAMETERS | VARCHAR2(1000) | Default parameter string for domain indexes |
| INTERVAL | VARCHAR2(1000) | String of the interval value |
| AUTOLIST | VARCHAR2(3) | Indicates whether a local index is partitioned by auto list partitioning ( YES ) or not ( NO ) |
| INTERVAL_SUBPARTITION | VARCHAR2(1000) | String of the subpartition interval value |
| AUTOLIST_SUBPARTITION | VARCHAR2(3) | Indicates whether a local index is subpartitioned by auto list partitioning ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_PART_INDEXES displays the object-level partitioning information for all partitioned indexes in the database. USER_PART_INDEXES displays the object-level partitioning information for the partitioned indexes owned by the current user. This view does not display the OWNER column. See Also: " DBA_PART_INDEXES " " USER_PART_INDEXES " See Also: " DBA_PART_INDEXES " " USER_PART_INDEXES "