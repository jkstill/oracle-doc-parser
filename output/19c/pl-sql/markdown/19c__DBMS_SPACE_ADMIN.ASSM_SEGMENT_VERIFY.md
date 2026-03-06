---
id: 19c__DBMS_SPACE_ADMIN.ASSM_SEGMENT_VERIFY
name: DBMS_SPACE_ADMIN.ASSM_SEGMENT_VERIFY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.ASSM_SEGMENT_VERIFY

Given a segment definition, the procedure verifies the basic consistency of the space metadata blocks as well as consistency between space metadata and segment data blocks. This procedure verifies segments created in Automatic Segment Space Management (ASSM) tablespaces.

## Syntax

```sql
DBMS_SPACE_ADMIN.ASSM_SEGMENT_VERIFY (
   segment_owner   IN VARCHAR2,
   segment_name    IN VARCHAR2,
   segment_type    IN VARCHAR2,
   partition_name  IN VARCHAR2,
   verify_option   IN POSITIVE  DEFAULT SEGMENT_VERIFY_BASIC,
   attrib          IN POSITIVE  DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| segment_owner | VARCHAR2 | IN | Schema that owns the segment |
| segment_name | VARCHAR2 | IN | Name of the segment to be verified |
| segment_type | VARCHAR2 | IN | Segment namespace is one of TABLE , TABLE PARTITION , TABLE SUBPARTITION , INDEX , INDEX PARTITION , INDEX SUBPARTITION , LOB , LOB PARTITION , LOB SUBPARTITION , CLUSTER |
| partition_name | VARCHAR2 | IN | Name of the partition or subpartition |
| verify_option | POSITIVE | IN | One of the following options: SEGMENT_VERIFY_BASIC := 9. Performs the basic metadata checks (Default) SEGMENT_VERIFY_DEEP := 10. Performs deep verification SEGMENT_VERIFY_SPECIFIC := 11. Performs a specific check for the segment |
| attrib | POSITIVE | IN | When option SEGMENT_VERIFY_SPECIFIC is specified as option, attrib can be one of the following: HWM_CHECK := 12. Checks whether high water mark information is accurate BMB_CHECK := 13. Checks whether space bitmap blocks have correct backpointers to the segment header SEG_DICT_CHECK := 14. Checks whether dictionary information for segment is accurate EXTENT_TS_BITMAP_CHECK := 15. Checks whether extent maps are consistent with file level bitmaps DB_BACKPOINTER_CHECK := 16. Checks whether datablocks have correct backpointers to the space metadata blocks EXTENT_SEGMENT_BITMAP_CHECK := 17. Checks whether extent map in the segment matches the bitmaps in the segment BITMAPS_CHECK := 18. Checks whether space bitmap blocks are accurate |

## Usage Notes

There is however a difference between basic verification and deep verification: Basic verification involves consistency checks of space metadata, such as integrity among level 1, level 2, level 3 bitmap blocks, consistency of segment extent map and level 1 bitmap ranges. Deep verification involves consistency checks between datablocks and space metadata blocks such as whether the datablocks point correctly to the parent level 1 bitmap blocks, and whether the freeness states in the datablocks are consistent with the freeness states of bits in level 1 bitmap blocks corresponding to the datablocks. Syntax DBMS_SPACE_ADMIN.ASSM_SEGMENT_VERIFY ( segment_owner IN VARCHAR2, segment_name IN VARCHAR2, segment_type IN VARCHAR2, partition_name IN VARCHAR2, verify_option IN POSITIVE DEFAULT SEGMENT_VERIFY_BASIC, attrib IN POSITIVE DEFAULT NULL); Parameters Table 159-3 ASSM_SEGMENT_VERIFY Procedure Parameters Parameter Description segment_owner Schema that owns the segment segment_name Name of the segment to be verified segment_type Segment namespace is one of TABLE , TABLE PARTITION , TABLE SUBPARTITION , INDEX , INDEX PARTITION , INDEX SUBPARTITION , LOB , LOB PARTITION , LOB SUBPARTITION , CLUSTER partition_name Name of the partition or subpartition verify_option One of the following options: SEGMENT_VERIFY_BASIC := 9. Performs the basic metadata checks (Default) SEGMENT_VERIFY_DEEP := 10. Performs deep verification SEGMENT_VERIFY_SPECIFIC := 11. Performs a specific check for the segment attrib When option SEGMENT_VERIFY_SPECIFIC is specified as option, attrib can be one of the following: HWM_CHECK := 12. Checks whether high water mark information is accurate BMB_CHECK := 13. Checks whether space bitmap blocks have correct backpointers to the segment header SEG_DICT_CHECK := 14. Checks whether dictionary information for segment is accurate EXTENT_TS_BITMAP_CHECK := 15. Checks whether extent maps are consistent with file level bitmaps DB_BACKPOINTER_CHECK := 16. Checks whether datablocks have correct backpointers to the space metadata blocks EXTENT_SEGMENT_BITMAP_CHECK := 17. Checks whether extent map in the segment matches the bitmaps in the segment BITMAPS_CHECK := 18. Checks whether space bitmap blocks are accurate Usage Notes Using this procedure requires SYSDBA privileges. You can determine the relative file # and header block # ( header_relative_file and header_block parameters) by querying DBA_SEGMENTS . This procedure outputs a dump file named sid_ora_ process_ID . trc to the location specified in the USER_DUMP_DEST initialization parameter.