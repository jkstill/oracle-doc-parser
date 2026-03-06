---
id: 19c__DBA_HIST_IM_SEG_STAT_OBJ
name: DBA_HIST_IM_SEG_STAT_OBJ
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_IM_SEG_STAT_OBJ.html
---

# DBA_HIST_IM_SEG_STAT_OBJ

DBA_HIST_IM_SEG_STAT_OBJ displays information about object metadata for historical in-memory segments.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database id for the snapshot |
| TS# | NUMBER | Tablespace number |
| OBJ# | NUMBER | Dictionary object number |
| DATAOBJ# | NUMBER | Data object number |
| OWNER | VARCHAR2(128) | Owner of the object |
| OBJECT_NAME | VARCHAR2(128) | Name of the object |
| SUBOBJECT_NAME | VARCHAR2(128) | Name of the subobject |
| OBJECT_TYPE | VARCHAR2(128) | Type of the object |
| TABLESPACE_NAME | VARCHAR2(128) | Tablespace name for the object |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |