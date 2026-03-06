---
id: 19c__DBA_HIST_RESOURCE_LIMIT
name: DBA_HIST_RESOURCE_LIMIT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_RESOURCE_LIMIT.html
---

# DBA_HIST_RESOURCE_LIMIT

DBA_HIST_RESOURCE_LIMIT displays historical information about global resource use for some of the system resource.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| RESOURCE_NAME | VARCHAR2(30) | Name of the resource |
| CURRENT_UTILIZATION | NUMBER | Number of (resources, locks, or processes) currently being used |
| MAX_UTILIZATION | NUMBER | Maximum consumption of the resource since the last instance start up |
| INITIAL_ALLOCATION | VARCHAR2(10) | Initial allocation. This will be equal to the value specified for the resource in the initialization parameter file ( UNLIMITED for infinite allocation). |
| LIMIT_VALUE | VARCHAR2(10) | Unlimited for resources and locks. This can be greater than the initial allocation value ( UNLIMITED for infinite limit). |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$RESOURCE_LIMIT . If time is of interest, join this view with DBA_HIST_SNAPSHOT.END_INTERVAL_TIME .