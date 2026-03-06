---
id: 19c__DBA_HIST_MEM_DYNAMIC_COMP
name: DBA_HIST_MEM_DYNAMIC_COMP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_HIST_MEM_DYNAMIC_COMP.html
---

# DBA_HIST_MEM_DYNAMIC_COMP

DBA_HIST_MEM_DYNAMIC_COMP displays historical memory component sizes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SNAP_ID | NUMBER | Unique snapshot ID |
| DBID | NUMBER | Database ID for the snapshot |
| INSTANCE_NUMBER | NUMBER | Instance number for the snapshot |
| COMPONENT | VARCHAR2(64) | Component name |
| CURRENT_SIZE | NUMBER | Current size of the component |
| MIN_SIZE | NUMBER | Minimum size of the component since instance startup |
| MAX_SIZE | NUMBER | Maximum size of the component since instance startup |
| USER_SPECIFIED_SIZE | NUMBER | Value of the user parameter for the component |
| OPER_COUNT | NUMBER | Number of operations since instance startup |
| LAST_OPER_TYPE | VARCHAR2(13) | Last completed operation for the component: STATIC INITIALIZING DISABLED GROW SHRINK SHRINK_CANCEL |
| LAST_OPER_MODE | VARCHAR2(9) | Mode of the last completed operation: MANUAL DEFERRED IMMEDIATE |
| LAST_OPER_TIME | DATE | Start time of the last completed operation |
| GRANULE_SIZE | NUMBER | Granularity of the GROW or SHRINK operation |
| CON_DBID | NUMBER | The database ID of the PDB for the sampled session |
| CON_ID | NUMBER | The ID of the container that CON_DBID identifies. Possible values include: 0 : This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. 1 : This value is used for rows containing data that pertain to only the root n : Where n is the applicable container ID for the rows containing data |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view contains snapshots of V$MEMORY_DYNAMIC_COMPONENTS . See Also: " V$MEMORY_DYNAMIC_COMPONENTS " See Also: " V$MEMORY_DYNAMIC_COMPONENTS "