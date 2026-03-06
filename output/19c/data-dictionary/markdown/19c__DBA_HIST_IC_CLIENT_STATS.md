---
id: 19c__DBA_HIST_IC_CLIENT_STATS
name: DBA_HIST_IC_CLIENT_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_HIST_IC_CLIENT_STATS.html
---

# DBA_HIST_IC_CLIENT_STATS

DBA_HIST_IC_CLIENT_STATS displays information about the usage of an interconnect device by the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| NAME | VARCHAR2(9) | Identifies the area of the Oracle Database: ipq - Parallel query communications dlm - Database lock management cache - Global cache communications All other values are internal to Oracle and are not expected to have high usage. |
| BYTES_SENT | NUMBER | Number of bytes sent by the instance since instance startup for the software area identified by NAME . This information is aggregated across all devices used by the instance. |
| BYTES_RECEIVED | NUMBER | Number of bytes received by the instance since instance startup for the software area identified by NAME . This information is aggregated across all devices used by the instance. |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The information is divided into several areas of the Oracle Database, each identified by the NAME value.