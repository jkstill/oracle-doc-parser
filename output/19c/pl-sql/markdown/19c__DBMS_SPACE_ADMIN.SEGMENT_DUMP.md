---
id: 19c__DBMS_SPACE_ADMIN.SEGMENT_DUMP
name: DBMS_SPACE_ADMIN.SEGMENT_DUMP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.SEGMENT_DUMP

This procedure dumps the segment header and bitmap blocks of a specific segment to the location specified in the USER_DUMP_DEST initialization parameter.

## Syntax

```sql
DBMS_SPACE_ADMIN.SEGMENT_DUMP (
   tablespace_name         IN    VARCHAR2,
   header_relative_file    IN    POSITIVE,
   header_block            IN    NUMBER,
   dump_option             IN    POSITIVE  DEFAULT SEGMENT_DUMP_EXTENT_MAP);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2 | IN | Name of tablespace in which segment resides |
| header_relative_file | POSITIVE | IN | Relative file number of segment header |
| header_block | NUMBER | IN | Block number of segment header |
| dump_option | POSITIVE | IN | One of the following options: SEGMENT_DUMP_EXTENT_MAP SEGMENT_DUMP_BITMAP_SUMMARY |

## Usage Notes

Syntax DBMS_SPACE_ADMIN.SEGMENT_DUMP ( tablespace_name IN VARCHAR2, header_relative_file IN POSITIVE, header_block IN NUMBER, dump_option IN POSITIVE DEFAULT SEGMENT_DUMP_EXTENT_MAP); Parameters Table 159-10 SEGMENT_DUMP Procedure Parameters Parameter Description tablespace_name Name of tablespace in which segment resides header_relative_file Relative file number of segment header header_block Block number of segment header dump_option One of the following options: SEGMENT_DUMP_EXTENT_MAP SEGMENT_DUMP_BITMAP_SUMMARY Usage Notes You can produce a slightly abbreviated dump, which includes the segment header and bitmap block summaries, without percent-free states of each block if you pass SEGMENT_DUMP_BITMAP_SUMMARY as the dump_option parameter. You can determine the relative file number and block number ( header_relative_file and header_block parameter) of the segment header block by querying DBA_SEGMENTS . HEADER_FILE . If HEADER_FILE is greater than 1023 then use DBA_DATA_FILES . RELATIVE_FNO . Examples EXECUTE DBMS_SPACE_ADMIN.SEGMENT_DUMP('USERS', 4, 33);