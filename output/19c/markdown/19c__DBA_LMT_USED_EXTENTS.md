---
id: 19c__DBA_LMT_USED_EXTENTS
name: DBA_LMT_USED_EXTENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dba]
source_file: DBA_LMT_USED_EXTENTS.html
---

# DBA_LMT_USED_EXTENTS

DBA_LMT_USED_EXTENTS describes the extents comprising the segments in all locally managed tablespaces in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SEGMENT_FILEID | NUMBER | File number of the segment header of the extent |
| SEGMENT_BLOCK | NUMBER | Block number of the segment header of the extent |
| TABLESPACE_ID | NUMBER | Identifier number of the tablespace containing the extent |
| EXTENT_ID | NUMBER | Extent number in the segment |
| FILEID | NUMBER | File identifier number of the file containing the extent |
| BLOCK | NUMBER | Starting block number of the extent |
| LENGTH | NUMBER | Number of blocks in the extent |