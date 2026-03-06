---
id: 19c__V$ASM_FILESYSTEM
name: V$ASM_FILESYSTEM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-ASM_FILESYSTEM.html
---

# V$ASM_FILESYSTEM

V$ASM_FILESYSTEM displays information for every mounted Oracle ACFS.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FS_NAME | VARCHAR2(1024) |  |
| AVAILABLE_TIME | DATE |  |
| BLOCK_SIZE | NUMBER |  |
| STATE | VARCHAR2(13) |  |
| CORRUPT | VARCHAR2(5) |  |
| NUM_VOL | NUMBER |  |
| TOTAL_SIZE | NUMBER |  |
| TOTAL_FREE | NUMBER |  |
| TOTAL_SNAP_SPACE_USAGE | NUMBER |  |
| REPLSTATE | VARCHAR2(7) |  |
| RESIZE_STATE Foot 1 | VARCHAR2(5) |  |
| COMPRESS_STATE Foot 1 | VARCHAR2(7) |  |
| FROZEN_STATE Foot 1 | VARCHAR2(5) |  |
| ACFS_COMPATIBILITY Foot 1 | VARCHAR2(60) |  |
| METADATA_BLOCK_SIZE Foot 1 | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information