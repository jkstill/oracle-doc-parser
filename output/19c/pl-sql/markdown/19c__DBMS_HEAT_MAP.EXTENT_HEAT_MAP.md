---
id: 19c__DBMS_HEAT_MAP.EXTENT_HEAT_MAP
name: DBMS_HEAT_MAP.EXTENT_HEAT_MAP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HEAT_MAP
tags: [dbms_heat_map]
source_file: DBMS_HEAT_MAP.html
---

# DBMS_HEAT_MAP.EXTENT_HEAT_MAP

This table function returns the extent level Heat Map statistics for a table segment. It returns no information for segment types that are not data. Aggregates at extent level, including minimum modification time and maximum modification time, are included.

## Syntax

```sql
DBMS_HEAT_MAP.EXTENT_HEAT_MAP (
   owner             IN VARCHAR2,
   segment_name      IN VARCHAR2,
   partition_name    IN VARCHAR2 DEFAULT NULL,
RETURN hm_els_row PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner | VARCHAR2 | IN | Owner of the segment |
| segment_name | VARCHAR2 | IN | Table name of a non-partitioned table or (sub)partition of partitioned table. Returns no rows when table name is specified for a partitioned table. |
| partition_name | VARCHAR2 | IN | Defaults to NULL . For a partitioned table, specify the partition or subpartition segment name. |

**Returns:** `hm_els_row`

## Usage Notes

Syntax DBMS_HEAT_MAP.EXTENT_HEAT_MAP ( owner IN VARCHAR2, segment_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL, RETURN hm_els_row PIPELINED; Parameters Table 80-4 EXTENT_HEAT_MAP Function Parameters Parameter Description owner Owner of the segment segment_name Table name of a non-partitioned table or (sub)partition of partitioned table. Returns no rows when table name is specified for a partitioned table. partition_name Defaults to NULL . For a partitioned table, specify the partition or subpartition segment name. Return Values Table 80-5 EXTENT_HEAT_MAP Function Return Values (Output Parameters ) Parameter Description owner Owner of the segment segment_name Segment name of the non-partitioned table partition_name Partition or subpartition name tablespace_name Tablespace containing the segment file_id Absolute file number of the block in the segment relative_fno Relative file number of the block in the segment block_id Block number of the block blocks Number of blocks in the extent bytes Number of bytes in the extent min_writetime Minimum of last modification time of the block max_writetime Maximum of last modification time of the block avg_writetime Average of last modification time of the block