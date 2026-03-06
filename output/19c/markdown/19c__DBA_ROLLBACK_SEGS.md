---
id: 19c__DBA_ROLLBACK_SEGS
name: DBA_ROLLBACK_SEGS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ROLLBACK_SEGS.html
---

# DBA_ROLLBACK_SEGS

DBA_ROLLBACK_SEGS describes rollback segments.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SEGMENT_NAME | VARCHAR2(30) | Name of the rollback segment |
| OWNER | VARCHAR2(6) | Owner of the rollback segment: PUBLIC SYS |
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace containing the rollback segment |
| SEGMENT_ID | NUMBER | ID number of the rollback segment |
| FILE_ID | NUMBER | Absolute file number of the data file containing the segment header |
| BLOCK_ID | NUMBER | ID number of the block containing the segment header |
| INITIAL_EXTENT | NUMBER | Initial extent size in bytes |
| NEXT_EXTENT | NUMBER | Secondary extent size in bytes |
| MIN_EXTENTS | NUMBER | Minimum number of extents |
| MAX_EXTENTS | NUMBER | Maximum number of extent |
| PCT_INCREASE | NUMBER | Percent increase for extent size |
| STATUS | VARCHAR2(16) | Rollback segment status: OFFLINE ONLINE NEEDS RECOVERY PARTLY AVAILABLE UNDEFINED |
| INSTANCE_NUM | VARCHAR2(40) | Rollback segment owning Oracle Real Application Clusters instance number |
| RELATIVE_FNO | NUMBER | Relative file number of the segment header |