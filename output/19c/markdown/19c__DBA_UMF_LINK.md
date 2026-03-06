---
id: 19c__DBA_UMF_LINK
name: DBA_UMF_LINK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_UMF_LINK.html
---

# DBA_UMF_LINK

DBA_UMF_LINK displays information about the registered database links in the Remote Management Framework (RMF).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TOPOLOGY_NAME | VARCHAR2(128) | Topology name for the link |
| FROM_NODE_ID | NUMBER | Node ID of the local node |
| TO_NODE_ID | NUMBER | Node ID of the remote node |
| LINK_NAME | VARCHAR2(128) | Fully qualified database link name |

## Usage Notes

This view returns no rows if you are querying on an RMF source node. It returns all the registered database links in the topology if you are querying on a target node. See Also: Oracle Database Performance Tuning Guide for information about configuring the Remote Management Framework (RMF) architecture See Also: Oracle Database Performance Tuning Guide for information about configuring the Remote Management Framework (RMF) architecture