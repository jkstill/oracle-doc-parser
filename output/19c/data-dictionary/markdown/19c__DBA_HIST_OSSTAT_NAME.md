---
id: 19c__DBA_HIST_OSSTAT_NAME
name: DBA_HIST_OSSTAT_NAME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_OSSTAT_NAME.html
---

# DBA_HIST_OSSTAT_NAME

DBA_HIST_OSSTAT_NAME displays the names of the operating system statistics.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| DBID | NUMBER | Database ID |
| STAT_ID | NUMBER | Statistic ID |
| STAT_NAME | VARCHAR2(64) | Statistic name |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view is used with DBA_HIST_OSSTAT . See Also: " DBA_HIST_OSSTAT " See Also: " DBA_HIST_OSSTAT "