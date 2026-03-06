---
id: 19c__DBA_HIST_TABLESPACE_STAT
name: DBA_HIST_TABLESPACE_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dba]
source_file: DBA_HIST_TABLESPACE_STAT.html
---

# DBA_HIST_TABLESPACE_STAT

DBA_HIST_TABLESPACE_STAT displays tablespace information from the control file.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| TS# | NUMBER | Tablespace number |
| TSNAME | VARCHAR2(30) | Tablespace name |
| CONTENTS | VARCHAR2(9) | Tablespace contents: PERMANENT TEMPORARY |
| STATUS | VARCHAR2(9) | Tablespace status: ONLINE OFFLINE READ ONLY |
| SEGMENT_SPACE_MANAGEMENT | VARCHAR2(6) | Indicates whether the free and used segment space in the tablespace is managed using free lists ( MANUAL ) or bitmaps ( AUTO ) |
| EXTENT_MANAGEMENT | VARCHAR2(10) | Indicates whether the extents in the tablespace are dictionary managed ( DICTIONARY ) or locally managed ( LOCAL ) |
| IS_BACKUP | VARCHAR2(5) | Indicates whether the tablespace is part of a backup |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$TABLESPACE and DBA_TABLESPACES . See Also: " V$TABLESPACE " " DBA_TABLESPACES " See Also: " V$TABLESPACE " " DBA_TABLESPACES "