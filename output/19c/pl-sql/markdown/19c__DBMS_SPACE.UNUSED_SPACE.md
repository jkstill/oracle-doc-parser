---
id: 19c__DBMS_SPACE.UNUSED_SPACE
name: DBMS_SPACE.UNUSED_SPACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE
tags: [dbms_space]
source_file: DBMS_SPACE.html
---

# DBMS_SPACE.UNUSED_SPACE

This procedure returns information about unused space in an object (table, index, or cluster).

## Syntax

```sql
DBMS_SPACE.UNUSED_SPACE (
   segment_owner              IN  VARCHAR2, 
   segment_name               IN  VARCHAR2,
   segment_type               IN  VARCHAR2,
   total_blocks               OUT NUMBER,
   total_bytes                OUT NUMBER,
   unused_blocks              OUT NUMBER,
   unused_bytes               OUT NUMBER,
   last_used_extent_file_id   OUT NUMBER,
   last_used_extent_block_id  OUT NUMBER,
   last_used_block            OUT NUMBER, 
   partition_name             IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| segment_owner | VARCHAR2 | IN | Schema name of the segment to be analyzed |
| segment_name | VARCHAR2 | IN | Segment name of the segment to be analyzed |
| segment_type | VARCHAR2 | IN | Type of the segment to be analyzed ( TABLE , INDEX , or CLUSTER ): TABLE TABLE PARTITION TABLE SUBPARTITION INDEX INDEX PARTITION INDEX SUBPARTITION CLUSTER LOB LOB PARTITION LOB SUBPARTITION |
| total_blocks | NUMBER | OUT | Returns total number of blocks in the segment |
| total_bytes | NUMBER | OUT | Returns total number of blocks in the segment, in bytes |
| unused_blocks | NUMBER | OUT | Returns number of blocks which are not used |
| unused_bytes | NUMBER | OUT | Returns, in bytes, number of blocks which are not used |
| last_used_extent_file_id | NUMBER | OUT | Returns the file ID of the last extent which contains data |
| last_used_extent_block_id | NUMBER | OUT | Returns the starting block ID of the last extent which contains data |
| last_used_block | NUMBER | OUT | Returns the last block within this extent which contains data |
| partition_name | VARCHAR2 | IN | Partition name of the segment to be analyzed. This is only used for partitioned tables; the name of subpartition should be used when partitioning is compose. |

## Usage Notes

Syntax DBMS_SPACE.UNUSED_SPACE ( segment_owner IN VARCHAR2, segment_name IN VARCHAR2, segment_type IN VARCHAR2, total_blocks OUT NUMBER, total_bytes OUT NUMBER, unused_blocks OUT NUMBER, unused_bytes OUT NUMBER, last_used_extent_file_id OUT NUMBER, last_used_extent_block_id OUT NUMBER, last_used_block OUT NUMBER, partition_name IN VARCHAR2 DEFAULT NULL); Parameters Table 158-15 UNUSED_SPACE Procedure Parameters Parameter Description segment_owner Schema name of the segment to be analyzed segment_name Segment name of the segment to be analyzed segment_type Type of the segment to be analyzed ( TABLE , INDEX , or CLUSTER ): TABLE TABLE PARTITION TABLE SUBPARTITION INDEX INDEX PARTITION INDEX SUBPARTITION CLUSTER LOB LOB PARTITION LOB SUBPARTITION total_blocks Returns total number of blocks in the segment total_bytes Returns total number of blocks in the segment, in bytes unused_blocks Returns number of blocks which are not used unused_bytes Returns, in bytes, number of blocks which are not used last_used_extent_file_id Returns the file ID of the last extent which contains data last_used_extent_block_id Returns the starting block ID of the last extent which contains data last_used_block Returns the last block within this extent which contains data partition_name Partition name of the segment to be analyzed. This is only used for partitioned tables; the name of subpartition should be used when partitioning is compose. Examples The following declares the necessary bind variables and executes. DBMS_SPACE.UNUSED_SPACE('SCOTT', 'EMP', 'TABLE', :total_blocks, :total_bytes,:unused_blocks, :unused_bytes, :lastextf, :last_extb, :lastusedblock);