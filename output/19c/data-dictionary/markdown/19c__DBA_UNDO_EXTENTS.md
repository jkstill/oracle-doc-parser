---
id: 19c__DBA_UNDO_EXTENTS
name: DBA_UNDO_EXTENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dba]
source_file: DBA_UNDO_EXTENTS.html
---

# DBA_UNDO_EXTENTS

DBA_UNDO_EXTENTS describes the extents comprising the segments in all undo tablespaces in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | CHAR(3) | Owner of the undo tablespace |
| SEGMENT_NAME | VARCHAR2(128) | Name of the undo segment |
| TABLESPACE_NAME | VARCHAR2(128) | Name of the undo tablespace |
| EXTENT_ID | NUMBER | ID of the extent |
| FILE_ID | NUMBER | Absolute file number of the data file containing the extent |
| BLOCK_ID | NUMBER | Start block number of the extent |
| BYTES | NUMBER | Size of the extent (in bytes) |
| BLOCKS | NUMBER | Size of the extent (in blocks) |
| RELATIVE_FNO | NUMBER | Relative number of the file containing the segment header |
| COMMIT_JTIME | NUMBER | Commit time of the undo in the extent expressed as Julian time. This column is deprecated, but retained for backward compatibility reasons. |
| COMMIT_WTIME | VARCHAR2(20) | Commit time of the undo in the extent expressed as Wallclock time.This column is deprecated, but retained for backward compatibility reasons. |
| STATUS | VARCHAR2(9) | Transaction Status of the undo in the extent: ACTIVE EXPIRED UNEXPIRED |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: The status of the undo space distribution reported by DBA_UNDO_EXTENTS is correct for the undo tablespace that is active on the instance on which DBA_UNDO_EXTENTS is queried. However, due to the use of in-memory information that is different on each instance, there can be a discrepancy in the status of the undo space distribution of undo tablespaces active on other instances when queried from one instance. This does not affect undo functionality and is only a reporting discrepancy for other instances' undo tablespace space distribution status. As a best practice, query the space distribution for an undo tablespace from the instance on which it is active. Note: The status of the undo space distribution reported by DBA_UNDO_EXTENTS is correct for the undo tablespace that is active on the instance on which DBA_UNDO_EXTENTS is queried. However, due to the use of in-memory information that is different on each instance, there can be a discrepancy in the status of the undo space distribution of undo tablespaces active on other instances when queried from one instance. This does not affect undo functionality and is only a reporting discrepancy for other instances' undo tablespace space distribution status. As a best practice, query the space distribution for an undo tablespace from the instance on which it is active.