---
id: 19c__DBA_HIST_SGA_TARGET_ADVICE
name: DBA_HIST_SGA_TARGET_ADVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_SGA_TARGET_ADVICE.html
---

# DBA_HIST_SGA_TARGET_ADVICE

DBA_HIST_SGA_TARGET_ADVICE provides historical information about the SGA_TARGET initialization parameter.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| SGA_SIZE | NUMBER | Size of the SGA |
| SGA_SIZE_FACTOR | NUMBER | Ratio between the SGA_SIZE and the current size of the SGA |
| ESTD_DB_TIME | NUMBER | Estimated DB_TIME for this SGA_SIZE |
| ESTD_PHYSICAL_READS | NUMBER | Estimated number of physical reads |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

See Also: " SGA_TARGET " See Also: " SGA_TARGET "