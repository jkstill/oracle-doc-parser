---
id: 19c__DBA_UMF_REGISTRATION
name: DBA_UMF_REGISTRATION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_UMF_REGISTRATION.html
---

# DBA_UMF_REGISTRATION

DBA_UMF_REGISTRATION displays information about the registered nodes in the Remote Management Framework (RMF).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TOPOLOGY_NAME | VARCHAR2(128) | Topology name for the node |
| NODE_NAME | VARCHAR2(128) | Unique node name in the topology |
| NODE_ID | NUMBER | Unique node ID in the topology |
| NODE_TYPE | NUMBER | Node type. Possible value: 0 : RDBMS node |
| AS_SOURCE | VARCHAR2(5) | Indicates whether the node is a source node. Possible values: TRUE : The node is a source node, and it can provide remote services FALSE : The node is not a source node, and it cannot provide remote services |
| AS_CANDIDATE_TARGET | VARCHAR2(5) | Node is a candidate target. Possible values: TRUE : Node can be promoted to target role FALSE : Node cannot be promoted to target role |
| STATE | VARCHAR2(20) | Current state of the node. Possible values: OK : Node is registered REGISTRATION_PENDING : Node registration has started, but has not been completed SYNC_FAILED : Unable to synchronize the topology with the node |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view returns no rows if you are querying on an RMF source node. It returns all the registered nodes in the topology if you are querying on a target node. See Also: Oracle Database Performance Tuning Guide for information about configuring the Remote Management Framework (RMF) architecture See Also: Oracle Database Performance Tuning Guide for information about configuring the Remote Management Framework (RMF) architecture