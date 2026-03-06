---
id: 19c__DBMS_HEAT_MAP.BLOCK_HEAT_MAP
name: DBMS_HEAT_MAP.BLOCK_HEAT_MAP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_HEAT_MAP
tags: [dbms_heat_map]
source_file: DBMS_HEAT_MAP.html
---

# DBMS_HEAT_MAP.BLOCK_HEAT_MAP

This table function returns the last modification time for each block in a table segment. It returns no information for segment types that are not data.

## Syntax

```sql
DBMS_HEAT_MAP.BLOCK_HEAT_MAP (
   owner             IN VARCHAR2,
   segment_name      IN VARCHAR2,
   partition_name    IN VARCHAR2 DEFAULT NULL,
   sort_columnid     IN NUMBER DEFAULT NULL,
   sort_order        IN VARCHAR2 DEFAULT NULL) 
RETURN hm_bls_row PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| owner | VARCHAR2 | IN | Owner of the segment |
| segment_name | VARCHAR2 | IN | Table name of a non-partitioned table or (sub)partition of partitioned table. Returns no rows when table name is specified for a partitioned table. |
| partition_name | VARCHAR2 | IN | Defaults to NULL . For a partitioned table, specify the partition or subpartition segment name. |
| sort_columnid | NUMBER | IN | ID of the column on which to sort the output. Valid values 1..9. Invalid values are ignored. |
| sort_order | VARCHAR2 | IN | Defaults to NULL . Possible values: ASC , DESC |

**Returns:** `hm_bls_row`

## Usage Notes

Syntax DBMS_HEAT_MAP.BLOCK_HEAT_MAP ( owner IN VARCHAR2, segment_name IN VARCHAR2, partition_name IN VARCHAR2 DEFAULT NULL, sort_columnid IN NUMBER DEFAULT NULL, sort_order IN VARCHAR2 DEFAULT NULL) RETURN hm_bls_row PIPELINED; Parameters Table 80-2 BLOCK_HEAT_MAP Function Parameters Parameter Description owner Owner of the segment segment_name Table name of a non-partitioned table or (sub)partition of partitioned table. Returns no rows when table name is specified for a partitioned table. partition_name Defaults to NULL . For a partitioned table, specify the partition or subpartition segment name. sort_columnid ID of the column on which to sort the output. Valid values 1..9. Invalid values are ignored. sort_order Defaults to NULL . Possible values: ASC , DESC Return Values Table 80-3 BLOCK_HEAT_MAP Function Return Values (Output Parameters ) Parameter Description owner Owner of the segment segment_name Segment name of the non-partitioned table partition_name Partition or subpartition name tablespace_name Tablespace containing the segment file_id Absolute file number of the block in the segment relative_fno Relative file number of the block in the segment block_id Block number of the block write time Last modification time of the block