---
id: 19c__DBA_HIST_EVENT_HISTOGRAM
name: DBA_HIST_EVENT_HISTOGRAM
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_EVENT_HISTOGRAM.html
---

# DBA_HIST_EVENT_HISTOGRAM

DBA_HIST_EVENT_HISTOGRAM displays event histogram historical statistics information.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| EVENT_ID | NUMBER | Identifier of the wait event |
| EVENT_NAME | VARCHAR2(64) | Name of the wait event |
| WAIT_CLASS_ID | NUMBER | Identifier of the class of the wait event |
| WAIT_CLASS | VARCHAR2(64) | Name of the class of the wait event |
| WAIT_TIME_MILLI | NUMBER | Wait time (in milliseconds) |
| WAIT_COUNT | NUMBER | Wait count |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$EVENT_HISTOGRAM . See Also: " V$EVENT_HISTOGRAM " See Also: " V$EVENT_HISTOGRAM "