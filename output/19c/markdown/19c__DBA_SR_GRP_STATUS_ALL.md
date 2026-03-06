---
id: 19c__DBA_SR_GRP_STATUS_ALL
name: DBA_SR_GRP_STATUS_ALL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_SR_GRP_STATUS_ALL.html
---

# DBA_SR_GRP_STATUS_ALL

DBA_SR_GRP_STATUS_ALL provides information on the refresh operations on the synchronous refresh groups in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the refresh operation, which is the user who launched the operation |
| GROUP_ID | NUMBER | Group ID of the synchronous refresh group |
| OPERATION | VARCHAR2(7) | The phase of the refresh operation performed: PREPARE EXECUTE |
| STATUS | VARCHAR2(10) | The status of the refresh operation: RUNNING NOT PROCESSED COMPLETE ERROR-SOFT ERROR-HARD ABORT PARTIAL |
| CURRENT_RUN | VARCHAR2(1) | Indicates whether the record is for the most recent refresh-operation on the group: Y - Yes N - No |
| CURRENT_GROUP | VARCHAR2(1) | Indicates whether the record is for a current group: Y - Yes N - No |
| NUM_TBLS | NUMBER | The number of tables in the synchronous refresh group |
| NUM_MVS | NUMBER | The number of materialized views in the synchronous refresh group |
| BASE_TBLS_REFR_STATUS | VARCHAR2(13) | Indicates the refresh status of base tables in the synchronous refresh group. The possible values are: NOT PROCESSED COMPLETE ABORT |
| NUM_MVS_COMPLETED | NUMBER | The number of materialized views which have completed refresh in the synchronous refresh group |
| NUM_MVS_ABORTED | NUMBER | The number of materialized views which have aborted refresh in the synchronous refresh group |
| ERROR_NUMBER | NUMBER | Error number of the run (if any) |
| ERROR_MESSAGE | VARCHAR2(4000) | Error message of the run (if any) |
| PREPARE_START_TIME | DATE | Time that the PREPARE_REFRESH phase of the run started |
| PREPARE_END_TIME | DATE | Time that the PREPARE_REFRESH phase of the run ended |
| EXECUTE_START_TIME | DATE | Time that the EXECUTE_REFRESH phase of the run started |
| EXECUTE_END_TIME | DATE | Time that the EXECUTE_REFRESH phase of the run ended |

## Usage Notes

A refresh operation is also called a run, and it has two phases: PREPARE_REFRESH and EXECUTE_REFRESH . These phases are controlled using the DBMS_SYNC_REFRESH package. Each row in this view provides information on a run of a group, identified by its GROUP_ID . The view contains information on the status of the objects of both current and past runs of both current and defunct synchronous refresh groups. Therefore, this view can be used to examine the history of synchronous refresh operations. The current run of a group is the most recent run of a group; a current group is a currently valid group, which is capable of being refreshed. A group becomes defunct when it is unregistered for any reason, either explicitly by the user or implicitly as a side-effect when the user registers materialized views related to the materialized views in the group. To view the status of refresh operations for the most recent runs of only the current groups, use the DBA_SR_GRP_STATUS view. Related View USER_SR_GRP_STATUS_ALL provides information on the refresh operations on the synchronous refresh groups in the database which are owned by the current user. Its columns are the same as those in DBA_SR_GRP_STATUS_ALL . See Also: " USER_SR_GRP_STATUS_ALL " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SYNC_REFRESH package See Also: " USER_SR_GRP_STATUS_ALL " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_SYNC_REFRESH package