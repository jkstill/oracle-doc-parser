---
id: 19c__DBA_UMF_TOPOLOGY
name: DBA_UMF_TOPOLOGY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dba]
source_file: DBA_UMF_TOPOLOGY.html
---

# DBA_UMF_TOPOLOGY

DBA_UMF_TOPOLOGY displays information about the registered topologies in the Remote Management Framework (RMF).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TOPOLOGY_NAME | VARCHAR2(128) | Unique topology name |
| TARGET_ID | NUMBER | Node ID of the target node |
| TOPOLOGY_VERSION | NUMBER | Topology version number |
| TOPOLOGY_STATE | VARCHAR2(8) | Possible values: ACTIVE : Topology can be used for RMF operations INACTIVE : Topology cannot be used for RMF operations |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view returns no rows if you are querying on an RMF source node. It returns one row per registered topology if you are querying on a target node. See Also: Oracle Database Performance Tuning Guide for information about configuring the Remote Management Framework (RMF) architecture See Also: Oracle Database Performance Tuning Guide for information about configuring the Remote Management Framework (RMF) architecture