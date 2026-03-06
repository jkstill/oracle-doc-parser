---
id: 19c__DBA_UMF_SERVICE
name: DBA_UMF_SERVICE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_UMF_SERVICE.html
---

# DBA_UMF_SERVICE

DBA_UMF_SERVICE displays information about the registered services in the Remote Management Framework (RMF).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TOPOLOGY_NAME | VARCHAR2(128) | Topology name for the service |
| NODE_ID | NUMBER | Node ID of the node providing the service |
| SERVICE_ID | VARCHAR2(7) | Service Identifier. Possible values: 1 : Automatic Workload Repository 2 : SQL Tuning |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view returns no rows if you are querying on an RMF source node. It returns all the registered services in the topology if you are querying on a target node See Also: Oracle Database Performance Tuning Guide for information about configuring the Remote Management Framework (RMF) architecture See Also: Oracle Database Performance Tuning Guide for information about configuring the Remote Management Framework (RMF) architecture