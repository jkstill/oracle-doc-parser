---
id: 19c__DBMS_SPACE_ADMIN.ASSM_TABLESPACE_VERIFY
name: DBMS_SPACE_ADMIN.ASSM_TABLESPACE_VERIFY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.ASSM_TABLESPACE_VERIFY

This procedures verifies all the segments created in an ASSM tablespace. The verification for each segment performs basic consistency checks of the space metadata blocks as well as consistency checks between space metadata and segment data blocks.

## Syntax

```sql
DBMS_SPACE_ADMIN.ASSM_TABLESPACE_VERIFY (
   tablespace_name   IN VARCHAR2,
   ts_option         IN POSITIVE,
   segment_option    IN POSITIVE DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2 | IN | Name of the tablespace to verify. The tablespace must be an ASSM tablespace. |
| ts_option | POSITIVE | IN | TS_VERIFY_BITMAPS := 19. The bitmaps are verified against the extents. This detects bits that are marked used or free wrongly and detects multiple allocation of extents. The file metadata is validated against file$ and control file. TS_VERIFY_DEEP := 20. This option is used to verify the file bitmaps as well perform checks on all the segments. TS_VERIFY_SEGMENTS := 21. This option is used to invoke SEGMENT_VERIFY on all the segments in the tablespace. Optionally you can write a script that queries all the segments in the tablespace and invoke SEGMENT_VERIFY . |
| segment_option | POSITIVE | IN | When TS_VERIFY_SEGMENTS is specified, segment_option can be one of the following: SEGMENT_VERIFY_BASIC := 9 SEGMENT_VERIFY_DEEP := 10 The value of segment_option is NULL when TS_VERIFY_DEEP or TS_VERIFY_BITMAPS is specified. |

## Usage Notes

Syntax DBMS_SPACE_ADMIN.ASSM_TABLESPACE_VERIFY ( tablespace_name IN VARCHAR2, ts_option IN POSITIVE, segment_option IN POSITIVE DEFAULT NULL); Parameters Table 159-4 ASSM_TABLESPACE_VERIFY Procedure Parameters Parameter Description tablespace_name Name of the tablespace to verify. The tablespace must be an ASSM tablespace. ts_option TS_VERIFY_BITMAPS := 19. The bitmaps are verified against the extents. This detects bits that are marked used or free wrongly and detects multiple allocation of extents. The file metadata is validated against file$ and control file. TS_VERIFY_DEEP := 20. This option is used to verify the file bitmaps as well perform checks on all the segments. TS_VERIFY_SEGMENTS := 21. This option is used to invoke SEGMENT_VERIFY on all the segments in the tablespace. Optionally you can write a script that queries all the segments in the tablespace and invoke SEGMENT_VERIFY . segment_option When TS_VERIFY_SEGMENTS is specified, segment_option can be one of the following: SEGMENT_VERIFY_BASIC := 9 SEGMENT_VERIFY_DEEP := 10 The value of segment_option is NULL when TS_VERIFY_DEEP or TS_VERIFY_BITMAPS is specified. Usage Notes Using this procedure requires SYSDBA privileges. This procedure outputs a dump file named sid_ora_ process_ID . trc to the location specified in the USER_DUMP_DEST initialization parameter.