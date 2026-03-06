---
id: 19c__DBMS_SPACE.SPACE_USAGE
name: DBMS_SPACE.SPACE_USAGE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE
tags: [dbms_space]
source_file: DBMS_SPACE.html
---

# DBMS_SPACE.SPACE_USAGE

This procedure has two variations to show space usage.

## Syntax

```sql
DBMS_SPACE.SPACE_USAGE(
   segment_owner           IN  VARCHAR2,
   segment_name            IN  VARCHAR2,
   segment_type            IN  VARCHAR2,
   unformatted_blocks      OUT NUMBER,
   unformatted_bytes       OUT NUMBER,
   fs1_blocks              OUT NUMBER,
   fs1_bytes               OUT NUMBER,
   fs2_blocks              OUT NUMBER,
   fs2_bytes               OUT NUMBER,
   fs3_blocks              OUT NUMBER,
   fs3_bytes               OUT NUMBER,
   fs4_blocks              OUT NUMBER,
   fs4_bytes               OUT NUMBER,
   full_blocks             OUT NUMBER,
   full_bytes              OUT NUMBER,
   partition_name          IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| segment_owner | VARCHAR2 | IN | Schema name of the segment to be analyzed |
| segment_name | VARCHAR2 | IN | Name of the segment to be analyzed |
| partition_name | VARCHAR2 | IN | Partition name of the segment to be analyzed |
| segment_type | VARCHAR2 | IN | Type of the segment to be analyzed ( TABLE , INDEX , or CLUSTER ): TABLE TABLE PARTITION TABLE SUBPARTITION INDEX INDEX PARTITION INDEX SUBPARTITION CLUSTER LOB LOB PARTITION LOB SUBPARTITION |
| unformatted_blocks | NUMBER | OUT | For LOB segments, the number of blocks that is returned from unformatted_blocks is actually the number of chunks for the LOB segment. |
| unformatted bytes |  |  | Total number of bytes unformatted |
| fs1_blocks | NUMBER | OUT | Number of blocks having at least 0 to 25% free space |
| fs1_bytes | NUMBER | OUT | Number of bytes having at least 0 to 25% free space |
| fs2_blocks | NUMBER | OUT | Number of blocks having at least 25 to 50% free space |
| fs2_bytes | NUMBER | OUT | Number of bytes having at least 25 to 50% free space |
| fs3_blocks | NUMBER | OUT | Number of blocks having at least 50 to 75% free space |
| fs3_bytes | NUMBER | OUT | Number of bytes having at least 50 to 75% free space |
| fs4_blocks | NUMBER | OUT | Number of blocks having at least 75 to 100% free space |
| fs4_bytes | NUMBER | OUT | Number of bytes having at least 75 to 100% free space |
| ful1_blocks |  |  | The number of blocks that is returned from full_blocks is actually the number of chunks for the LOB segment |
| full_bytes | NUMBER | OUT | Total number of bytes full in the segment |
| segment_size_blocks |  |  | Number of blocks allocated to the segment |
| segment_size_bytes |  |  | Number of bytes allocated to the segment |
| used_blocks |  |  | Number blocks allocated to the LOB that contains active data |
| used_bytes |  |  | Number bytes allocated to the LOB that contains active data |
| expired_blocks |  |  | Number of expired blocks used by the LOB to keep version data |
| expired_bytes |  |  | Number of expired bytes used by the LOB to keep version data |
| unexpired_blocks |  |  | Number of unexpired blocks used by the LOB to keep version data |
| unexpired_bytes |  |  | Number of unexpired bytes used by the LOB to keep version data |
| partition_name | VARCHAR2 | IN | Name of the partition ( NULL if not a partition) |

## Usage Notes

The first form of the procedure shows the space usage of data blocks under the segment High Water Mark. You can calculate usage for LOB s, LOB PARTITIONS and LOB SUBPARTITIONS . This procedure can only be used on tablespaces that are created with auto segment space management. The bitmap blocks, segment header, and extent map blocks are not accounted for by this procedure. Note that this overload cannot be used on SECUREFILE LOB s. Note: For LOB segments, the number of blocks that is returned from full_blocks and unformatted_blocks is actually the number of chunks for the LOB segment. The second form of the procedure returns information about SECUREFILE LOB space usage. It will return the amount of space in blocks being used by all the SECUREFILE LOB s in the LOB segment. The procedure displays the space actively used by the LOB column, freed space that has retention expired, and freed space that has retention unexpired. Note that this overload can be used only on SECUREFILE LOB s. Note: For LOB segments, the number of blocks that is returned from full_blocks and unformatted_blocks is actually the number of chunks for the LOB segment. Syntax DBMS_SPACE.SPACE_USAGE( segment_owner IN VARCHAR2, segment_name IN VARCHAR2, segment_type IN VARCHAR2, unformatted_blocks OUT NUMBER, unformatted_bytes OUT NUMBER, fs1_blocks OUT NUMBER, fs1_bytes OUT NUMBER, fs2_blocks OUT NUMBER, fs2_bytes OUT NUMBER, fs3_blocks OUT NUMBER, fs3_bytes OUT NUMBER, fs4_blocks OUT NUMBER, fs4_bytes OUT NUMBER, full_blocks OUT NUMBER, full_bytes OUT NUMBER, partition_name IN VARCHAR2 DEFAULT NULL); DBMS_SPACE.SPACE_USAGE( segment_owner IN VARCHAR2, segment_name IN VARCHAR2, segment_type IN VARCHAR2, segment_size_blocks OUT NUMBER, segment_size_bytes OUT NUMBER, used_blocks OUT NUMBER, used_bytes OUT NUMBER, expired_blocks OUT NUMBER, expired_bytes OUT NUMBER, unexpired_blocks OUT NUMBER, unexpired_bytes OUT NUMBER, partition_name IN VARCHAR2 DEFAULT NULL); Parameters Table 158-14 SPACE_USAGE Procedure Parameters Parameter Description segment_owner Schema name of the segment to be analyzed segment_name Name of the segment to be analyzed partition_name Partition name of the segment to be analyzed segment_type Type of the segment to be analyzed ( TABLE , INDEX , or CLUSTER ): TABLE TABLE PARTITION TABLE SUBPARTITION INDEX INDEX PARTITION INDEX SUBPARTITION CLUSTER LOB LOB PARTITION LOB SUBPARTITION unformatted_blocks For LOB segments, the number of blocks that is returned from unformatted_blocks is actually the number of chunks for the LOB segment. unformatted bytes Total number of bytes unformatted fs1_blocks Number of blocks having at least 0 to 25% free space fs1_bytes Number of bytes having at least 0 to 25% free space fs2_blocks Number of blocks having at least 25 to 50% free space fs2_bytes Number of bytes having at least 25 to 50% free space fs3_blocks Number of blocks having at least 50 to 75% free space fs3_bytes Number of bytes having at least 50 to 75% free space fs4_blocks Number of blocks having at least 75 to 100% free space fs4_bytes Number of bytes having at least 75 to 100% free space ful1_blocks The number of blocks that is returned from full_blocks is actually the number of chunks for the LOB segment full_bytes Total number of bytes full in the segment segment_size_blocks Number of blocks allocated to the segment segment_size_bytes Number of bytes allocated to the segment used_blocks Number blocks allocated to the LOB that contains active data used_bytes Number bytes allocated to the LOB that contains active data expired_blocks Number of expired blocks used by the LOB to keep version data expired_bytes Number of expired bytes used by the LOB to keep version data unexpired_blocks Number of unexpired blocks used by the LOB to keep version data unexpired_bytes Number of unexpired bytes used by the LOB to keep version data partition_name Name of the partition ( NULL if not a partition) Examples variable unf number; variable unfb number; variable fs1 number; variable fs1b number; variable fs2 number; variable fs2b number; variable fs3 number; variable fs3b number; variable fs4 number; variable fs4b number; variable full number; variable fullb number; begin dbms_space.space_usage('U1','T', 'TABLE', :unf, :unfb, :fs1, :fs1b, :fs2, :fs2b, :fs3, :fs3b, :fs4, :fs4b, :full, :fullb); end; / print unf ; print unfb ; print fs4 ; print fs4b; print fs3 ; print fs3b; print fs2 ; print fs2b; print fs1 ; print fs1b; print full; print fullb;