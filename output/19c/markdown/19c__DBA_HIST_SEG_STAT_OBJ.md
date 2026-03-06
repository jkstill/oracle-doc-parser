---
id: 19c__DBA_HIST_SEG_STAT_OBJ
name: DBA_HIST_SEG_STAT_OBJ
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_SEG_STAT_OBJ.html
---

# DBA_HIST_SEG_STAT_OBJ

DBA_HIST_SEG_STAT_OBJ displays all the names of the segments captured in the workload repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| TS# | NUMBER | Tablespace number |
| OBJ# | NUMBER | Dictionary object number |
| DATAOBJ# | NUMBER | Data object number |
| OWNER | VARCHAR2(128) | Owner of the object |
| OBJECT_NAME | VARCHAR2(128) | Name of the object |
| SUBOBJECT_NAME | VARCHAR2(128) | Name of the subobject (for example: partition) |
| OBJECT_TYPE | VARCHAR2(18) | Type of the object for example: table, tablespace) |
| TABLESPACE_NAME | VARCHAR2(30) | Tablespace Name for the object |
| PARTITION_TYPE | VARCHAR2(8) | Partition Type, if relevant |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view is used with the DBA_HIST_SEG_STAT view. See Also: " DBA_HIST_SEG_STAT " See Also: " DBA_HIST_SEG_STAT "