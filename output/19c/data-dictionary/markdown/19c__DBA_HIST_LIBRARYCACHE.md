---
id: 19c__DBA_HIST_LIBRARYCACHE
name: DBA_HIST_LIBRARYCACHE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_LIBRARYCACHE.html
---

# DBA_HIST_LIBRARYCACHE

DBA_HIST_LIBRARYCACHE displays historical statistics about library cache performance and activity.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| NAMESPACE | VARCHAR2(15) | Library cache namespace |
| GETS | NUMBER | Number of times a lock was requested for objects of the namespace |
| GETHITS | NUMBER | Number of times an object's handle was found in memory |
| PINS | NUMBER | Number of times a PIN was requested for objects of the namespace |
| PINHITS | NUMBER | Number of times all of the metadata pieces of the library object were found in memory |
| RELOADS | NUMBER | Any PIN of an object that is not the first PIN performed since the object handle was created, and which requires loading the object from disk |
| INVALIDATIONS | NUMBER | Total number of times objects in the namespace were marked invalid because a dependent object was modified |
| DLM_LOCK_REQUESTS | NUMBER | Number of GET requests lock instance locks |
| DLM_PIN_REQUESTS | NUMBER | Number of PIN requests lock instance locks |
| DLM_PIN_RELEASES | NUMBER | Number of release requests PIN instance locks |
| DLM_INVALIDATION_REQUESTS | NUMBER | Number of GET requests for invalidation instance locks |
| DLM_INVALIDATIONS | NUMBER | Number of invalidation pings received from other instances |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$LIBRARYCACHE . See Also: " V$LIBRARYCACHE " See Also: " V$LIBRARYCACHE "