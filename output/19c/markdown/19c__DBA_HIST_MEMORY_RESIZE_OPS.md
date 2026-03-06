---
id: 19c__DBA_HIST_MEMORY_RESIZE_OPS
name: DBA_HIST_MEMORY_RESIZE_OPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_MEMORY_RESIZE_OPS.html
---

# DBA_HIST_MEMORY_RESIZE_OPS

DBA_HIST_MEMORY_RESIZE_OPS displays memory resize operations history.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| COMPONENT | VARCHAR2(64) | Component name |
| OPER_TYPE | VARCHAR2(13) | Operation type: STATIC INITIALIZING DISABLED GROW SHRINK SHRINK_CANCEL |
| START_TIME | DATE | Start time of the operation |
| END_TIME | DATE | End time of the operation |
| TARGET_SIZE | NUMBER | Requested value of the parameter after the resize |
| OPER_MODE | VARCHAR2(9) | Operation mode: MANUAL DEFERRED IMMEDIATE |
| PARAMETER | VARCHAR2(80) | Name of the parameter for the resize operation |
| INITIAL_SIZE | NUMBER | Parameter value at the start of the operation |
| FINAL_SIZE | NUMBER | Real value of the parameter after the resize |
| STATUS | VARCHAR2(9) | Completion status of the operation: INACTIVE PENDING COMPLETE CANCELLED ERROR |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

This view contains snapshots of V$MEMORY_RESIZE_OPS . See Also: " V$MEMORY_RESIZE_OPS " See Also: " V$MEMORY_RESIZE_OPS "