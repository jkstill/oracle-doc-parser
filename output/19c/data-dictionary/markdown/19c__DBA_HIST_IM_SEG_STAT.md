---
id: 19c__DBA_HIST_IM_SEG_STAT
name: DBA_HIST_IM_SEG_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_IM_SEG_STAT.html
---

# DBA_HIST_IM_SEG_STAT

DBA_HIST_IM_SEG_STAT displays information about historical in-memory segment statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| TS# | NUMBER | Tablespace number |
| OBJ# | NUMBER | Dictionary object number |
| DATAOBJ# | NUMBER | Data object number |
| MEMBYTES | NUMBER | Size of in-memory version of the segment in bytes |
| SCANS | NUMBER | Count of segment statistics |
| SCANS_DELTA | NUMBER | Delta values for in-memory scans |
| DB_BLOCK_CHANGES | NUMBER | The total number of changes that were part of an update or delete operation that were made to segment blocks |
| DB_BLOCK_CHANGES_DELTA | NUMBER | Delta value for database block changes |
| POPULATE_CUS | NUMBER | Count of compression units (CUs) populated per segment |
| POPULATE_CUS_DELTA | NUMBER | Delta value for compression unit (CU) populate operations |
| REPOPULATE_CUS | NUMBER | Count of CUs repopulated per segment |
| REPOPULATE_CUS_DELTA | NUMBER | Delta value for compression unit (CU) repopulate operations |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content