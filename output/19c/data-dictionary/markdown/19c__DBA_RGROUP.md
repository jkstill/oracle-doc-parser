---
id: 19c__DBA_RGROUP
name: DBA_RGROUP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RGROUP.html
---

# DBA_RGROUP

DBA_RGROUP displays all refresh groups.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| REFGROUP | NUMBER | Internal identifier of the refresh group |
| OWNER | VARCHAR2(128) | Owner of the object in the refresh group |
| NAME | VARCHAR2(128) | Name of the object in the refresh group |
| IMPLICIT_DESTROY | VARCHAR2(1) | Indicates whether the refresh group is destroyed when its last item is removed ( Y ) or not ( N ) |
| PUSH_DEFERRED_RPC | VARCHAR2(1) | Indicates whether changes are pushed from the snapshot to the master before refresh ( Y ) or not ( N ) |
| REFRESH_AFTER_ERRORS | VARCHAR2(1) | Indicates whether to proceed with refresh despite errors when pushing deferred RPCs ( Y ) or not ( N ) |
| ROLLBACK_SEG | VARCHAR2(128) | Name of the rollback segment to use while refreshing |
| JOB | NUMBER | Identifier of the job used to refresh the group automatically |
| PURGE_OPTION | NUMBER(38) | Method for purging the transaction queue after each push. 1 indicates quick purge option; 2 indicates precise purge option |
| PARALLELISM | NUMBER(38) | Level of parallelism for transaction propagation |
| HEAP_SIZE | NUMBER(38) | Size of the heap |
| JOB_NAME | VARCHAR2(128) | The name of the job used to automatically refresh the group |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content