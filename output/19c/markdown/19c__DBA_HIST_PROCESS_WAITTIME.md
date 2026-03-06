---
id: 19c__DBA_HIST_PROCESS_WAITTIME
name: DBA_HIST_PROCESS_WAITTIME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_PROCESS_WAITTIME.html
---

# DBA_HIST_PROCESS_WAITTIME

DBA_HIST_PROCESS_WAITTIME displays CPU and wait time by process types.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| PROCESS_TYPE | VARCHAR2(5) | Process type |
| DESCRIPTION | VARCHAR2(64) | Process description |
| WAIT_CLASS_TYPE | VARCHAR2(64) | Type of wait class |
| VALUE | NUMBER | Wait time or CPU used time in milliseconds |
| CON_DBID | NUMBER | The database ID of the PDB for the process |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |