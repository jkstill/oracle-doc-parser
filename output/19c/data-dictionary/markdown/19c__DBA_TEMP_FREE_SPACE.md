---
id: 19c__DBA_TEMP_FREE_SPACE
name: DBA_TEMP_FREE_SPACE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_TEMP_FREE_SPACE.html
---

# DBA_TEMP_FREE_SPACE

DBA_TEMP_FREE_SPACE displays temporary space usage information at tablespace level.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace |
| TABLESPACE_SIZE | NUMBER | Total size of the tablespace, in bytes |
| ALLOCATED_SPACE | NUMBER | Total allocated space, in bytes, including space that is currently allocated and used and space that is currently allocated and available for reuse |
| FREE_SPACE | NUMBER | Total free space available, in bytes, including space that is currently allocated and available for reuse and space that is currently unallocated |
| SHARED | VARCHAR2(12) | Type of tablespace this file belongs to: SHARED : For shared tablespace LOCAL_FOR_RIM : Local temporary tablespace for RIM (read-only) instances LOCAL_FOR_ALL : Local temporary tablespace for all instance types |
| INST_ID | NUMBER | Instance ID of the instance to which the tempfile belongs |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content