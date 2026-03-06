---
id: 19c__DBA_HIST_SERVICE_WAIT_CLASS
name: DBA_HIST_SERVICE_WAIT_CLASS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_SERVICE_WAIT_CLASS.html
---

# DBA_HIST_SERVICE_WAIT_CLASS

DBA_HIST_SERVICE_WAIT_CLASS displays the history of wait class information for services as tracked by the Workload Repository.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| SERVICE_NAME_HASH | NUMBER | Hash of the service name |
| SERVICE_NAME | VARCHAR2(64) | Name of the service |
| WAIT_CLASS_ID | NUMBER | Identifier for the class of the wait event |
| WAIT_CLASS | VARCHAR2(64) | Name for the class of the wait event |
| TOTAL_WAITS | NUMBER | Total number of waits for this event |
| TIME_WAITED | NUMBER | Total amount of time waited for this event (in hundredths of a second) |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains information from V$SERVICE_WAIT_CLASS . See Also: " V$SERVICE_WAIT_CLASS " See Also: " V$SERVICE_WAIT_CLASS "