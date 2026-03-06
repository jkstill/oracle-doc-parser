---
id: 19c__DBA_SR_OBJ_STATUS
name: DBA_SR_OBJ_STATUS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dba]
source_file: DBA_SR_OBJ_STATUS.html
---

# DBA_SR_OBJ_STATUS

DBA_SR_OBJ_STATUS provides information on the status of objects registered for synchronous refresh for the current refresh operations for the current synchronous refresh groups in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the synchronous refresh object |
| NAME | VARCHAR2(128) | Name of the synchronous refresh object |
| TYPE | VARCHAR2(5) | Type of synchronous refresh object: MVIEW TABLE |
| GROUP_ID | NUMBER | Group ID of the synchronous refresh group to which this object belongs |
| STATUS | VARCHAR2(13) | Status of the synchronous refresh object: NOT PROCESSED COMPLETE ABORT |
| ERROR_NUMBER | NUMBER | Error number of the run (if any) |
| ERROR_MESSAGE | VARCHAR2(4000) | Error message of the run (if any) |
| LAST_MODIFIED_TIME | DATE | Last modification time of the synchronous refresh object |

## Usage Notes

To see information on the status of objects registered for synchronous refresh, use the DBA_SR_OBJ_STATUS_ALL view. Related View USER_SR_OBJ_STATUS provides information on the status of objects registered for synchronous refresh for the current refresh operations for the current synchronous refresh groups in the database which are owned by the current user. Its columns are the same as those in DBA_SR_OBJ_STATUS . See Also: " USER_SR_OBJ_STATUS " See Also: " USER_SR_OBJ_STATUS "