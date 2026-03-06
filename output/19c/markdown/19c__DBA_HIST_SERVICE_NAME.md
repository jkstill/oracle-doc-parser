---
id: 19c__DBA_HIST_SERVICE_NAME
name: DBA_HIST_SERVICE_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_SERVICE_NAME.html
---

# DBA_HIST_SERVICE_NAME

DBA_HIST_SERVICE_NAME displays the names of the Services tracked by the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID for the snapshot |
| SERVICE_NAME_HASH | NUMBER | Hash of the service name |
| SERVICE_NAME | VARCHAR2(64) | Name of the service |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains information for V$SERVICES . See Also: " V$SERVICES " See Also: " V$SERVICES "