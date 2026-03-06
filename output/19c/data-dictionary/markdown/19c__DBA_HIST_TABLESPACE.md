---
id: 19c__DBA_HIST_TABLESPACE
name: DBA_HIST_TABLESPACE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dba]
source_file: DBA_HIST_TABLESPACE.html
---

# DBA_HIST_TABLESPACE

DBA_HIST_TABLESPACE displays tablespace information contained in the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| TS# | NUMBER | Tablespace number |
| TSNAME | VARCHAR2(30) | Tablespace name |
| CONTENTS | VARCHAR2(30) | Tablespace contents: UNDO PERMANENT TEMPORARY |
| SEGMENT_SPACE_MANAGEMENT | VARCHAR2(30) | Indicates whether the free and used space in the tablespace is managed using free lists ( MANUAL ) or bitmaps ( AUTO ) |
| EXTENT_MANAGEMENT | VARCHAR2(30) | Indicates whether the extents in the tablespace are dictionary managed ( DICTIONARY ) or locally managed ( LOCAL ) |
| BLOCK_SIZE | NUMBER | Block size of the tablespace |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content