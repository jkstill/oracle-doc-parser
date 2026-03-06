---
id: 19c__ALL_REFRESH_CHILDREN
name: ALL_REFRESH_CHILDREN
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_REFRESH_CHILDREN.html
---

# ALL_REFRESH_CHILDREN

ALL_REFRESH_CHILDREN describes all the objects in refresh groups that are accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object in the refresh group |
| NAME | VARCHAR2(128) | Name of the object in the refresh group |
| TYPE | VARCHAR2(128) | Type of the object in the refresh group |
| ROWNER | VARCHAR2(128) | Owner of the refresh group |
| RNAME | VARCHAR2(128) | Name of the refresh group |
| REFGROUP | NUMBER | Internal identifier of the refresh group |
| IMPLICIT_DESTROY | VARCHAR2(1) | Indicates whether the refresh group is destroyed when its last item is subtracted ( Y ) or not ( N ) |
| PUSH_DEFERRED_RPC | VARCHAR2(1) | Indicates whether changes are pushed from the snapshot to the master before refresh ( Y ) or not ( N ) |
| REFRESH_AFTER _ERRORS | VARCHAR2(1) | Indicates whether to proceed with refresh despite errors when pushing deferred RPCs ( Y ) or not ( N ) |
| ROLLBACK_SEG | VARCHAR2(128) | Name of the rollback segment to use while refreshing |
| JOB | NUMBER | Identifier of the job used to refresh the group automatically |
| NEXT_DATE | DATE | Date that this job will next be refreshed automatically, if not broken |
| INTERVAL | VARCHAR2(200) | A date function used to compute the next NEXT_DATE |
| BROKEN | VARCHAR2(1) | Indicates whether the job is broken and will never be run ( Y ) or not ( N ) |
| PURGE_OPTION | NUMBER(38) | Method for purging the transaction queue after each push. 1 indicates quick purge option; 2 indicates precise purge option |
| PARALLELISM | NUMBER(38) | Level of parallelism for transaction propagation |
| HEAP_SIZE | NUMBER(38) | Size of the heap |
| JOB_NAME | VARCHAR2(128) | The name of the job used to automatically refresh the group |

## Usage Notes

Related Views DBA_REFRESH_CHILDREN describes the objects in all refresh groups in the database. USER_REFRESH_CHILDREN describes the objects in all refresh groups owned by the current user. See Also: " DBA_REFRESH_CHILDREN " " USER_REFRESH_CHILDREN " See Also: " DBA_REFRESH_CHILDREN " " USER_REFRESH_CHILDREN "