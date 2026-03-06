---
id: 19c__DBA_HIST_PGASTAT
name: DBA_HIST_PGASTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_PGASTAT.html
---

# DBA_HIST_PGASTAT

DBA_HIST_PGASTAT displays historical PGA memory usage statistics as well as statistics about the automatic PGA memory manager when it is enabled.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Database instance number |
| NAME | VARCHAR2(64) | Name of the statistic: aggregate PGA auto target aggregate PGA target parameter bytes processed cache hit percentage extra bytes read/written global memory bound max processes count maximum PGA allocated maximum PGA used for auto workareas maximum PGA used for manual workareas over allocation count PGA memory freed back to OS process count recompute count (total) total freeable PGA memory total PGA allocated total PGA inuse total PGA used for auto workareas total PGA used for manual workareas See Also: V$PGASTAT for descriptions of the statistics |
| VALUE | NUMBER | Statistic value |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$PGASTAT . See Also: " V$PGASTAT " See Also: " V$PGASTAT "