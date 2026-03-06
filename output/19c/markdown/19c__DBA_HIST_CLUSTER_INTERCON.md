---
id: 19c__DBA_HIST_CLUSTER_INTERCON
name: DBA_HIST_CLUSTER_INTERCON
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_CLUSTER_INTERCON.html
---

# DBA_HIST_CLUSTER_INTERCON

DBA_HIST_CLUSTER_INTERCON displays information about the devices used by the instance to access the interconnect (that is, communicate with other instances).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| NAME | VARCHAR2(256) | Operating system name of the device |
| IP_ADDRESS | VARCHAR2(64) | IP address of the device |
| IS_PUBLIC | VARCHAR2(3) | Indicates whether the device is a public interface ( YES ) or a private interface ( NO ) Public interfaces can be listened to by outside applications, which may be a security problem. Oracle recommends using private interfaces for interconnect. |
| SOURCE | VARCHAR2(31) | Describes the type of device |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |