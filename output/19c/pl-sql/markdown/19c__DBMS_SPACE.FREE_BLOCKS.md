---
id: 19c__DBMS_SPACE.FREE_BLOCKS
name: DBMS_SPACE.FREE_BLOCKS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE
tags: [dbms_space]
source_file: DBMS_SPACE.html
---

# DBMS_SPACE.FREE_BLOCKS

This procedure returns information about free blocks in an object (table, index, or cluster).

## Syntax

```sql
DBMS_SPACE.FREE_BLOCKS (
   segment_owner     IN  VARCHAR2, 
   segment_name      IN  VARCHAR2,
   segment_type      IN  VARCHAR2,
   freelist_group_id IN  NUMBER,
   free_blks         OUT NUMBER,
   scan_limit        IN  NUMBER DEFAULT NULL,
   partition_name    IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| segment_owner | VARCHAR2 | IN | Schema name of the segment to be analyzed |
| segment_name | VARCHAR2 | IN | Segment name of the segment to be analyzed |
| segment_type | VARCHAR2 | IN | Type of the segment to be analyzed ( TABLE , INDEX , or CLUSTER ): TABLE TABLE PARTITION TABLE SUBPARTITION INDEX INDEX PARTITION INDEX SUBPARTITION CLUSTER LOB LOB PARTITION LOB SUBPARTITION |
| freelist_group_id | NUMBER | IN | Freelist group (instance) whose free list size is to be computed |
| free_blks | NUMBER | OUT | Returns count of free blocks for the specified group |
| scan_limit | NUMBER | IN | Maximum number of free list blocks to read (optional). Use a scan limit of X you are interested only in the question, "Do I have X blocks on the free list?" |
| partition_name | VARCHAR2 | IN | Partition name of the segment to be analyzed. This is only used for partitioned tables. The name of subpartition should be used when partitioning is composite. |

## Usage Notes

See SPACE_USAGE Procedures for returning free block information in an auto segment space managed segment. Syntax DBMS_SPACE.FREE_BLOCKS ( segment_owner IN VARCHAR2, segment_name IN VARCHAR2, segment_type IN VARCHAR2, freelist_group_id IN NUMBER, free_blks OUT NUMBER, scan_limit IN NUMBER DEFAULT NULL, partition_name IN VARCHAR2 DEFAULT NULL); Pragmas pragma restrict_references(free_blocks,WNDS); Parameters Table 158-8 FREE_BLOCKS Procedure Parameters Parameter Description segment_owner Schema name of the segment to be analyzed segment_name Segment name of the segment to be analyzed segment_type Type of the segment to be analyzed ( TABLE , INDEX , or CLUSTER ): TABLE TABLE PARTITION TABLE SUBPARTITION INDEX INDEX PARTITION INDEX SUBPARTITION CLUSTER LOB LOB PARTITION LOB SUBPARTITION freelist_group_id Freelist group (instance) whose free list size is to be computed free_blks Returns count of free blocks for the specified group scan_limit Maximum number of free list blocks to read (optional). Use a scan limit of X you are interested only in the question, "Do I have X blocks on the free list?" partition_name Partition name of the segment to be analyzed. This is only used for partitioned tables. The name of subpartition should be used when partitioning is composite. Examples The following uses the CLUS cluster in SCOTT schema with 4 freelist groups. It returns the number of blocks in freelist group 3 in CLUS . DBMS_SPACE.FREE_BLOCKS('SCOTT', 'CLUS', 'CLUSTER', 3, :free_blocks); Note: An error is raised if scan_limit is not a positive number.