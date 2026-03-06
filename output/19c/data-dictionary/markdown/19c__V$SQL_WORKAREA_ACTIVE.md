---
id: 19c__V$SQL_WORKAREA_ACTIVE
name: V$SQL_WORKAREA_ACTIVE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: sql
tags: [dynamic_performance]
source_file: V-SQL_WORKAREA_ACTIVE.html
---

# V$SQL_WORKAREA_ACTIVE

The last three columns are included to enable joining V$SQL_WORKAREA_ACTIVE with V$TEMPSEG_USAGE to retrieve more information on this temporary segment.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SQL_HASH_VALUE | NUMBER |  |
| SQL_ID | VARCHAR2(13) |  |
| SQL_EXEC_START | DATE |  |
| SQL_EXEC_ID | NUMBER |  |
| WORKAREA_ADDRESS | RAW(4 | 8) |  |
| OPERATION_TYPE | VARCHAR2(160) |  |
| OPERATION_ID | NUMBER |  |
| POLICY | VARCHAR2(24) |  |
| SID | NUMBER |  |
| QCINST_ID | NUMBER |  |
| QCSID | NUMBER |  |
| ACTIVE_TIME | NUMBER |  |
| WORK_AREA_SIZE | NUMBER |  |
| EXPECTED_SIZE | NUMBER |  |
| ACTUAL_MEM_USED | NUMBER |  |
| MAX_MEM_USED | NUMBER |  |
| NUMBER_PASSES | NUMBER |  |
| TEMPSEG_SIZE | NUMBER |  |
| TABLESPACE | VARCHAR2(128) |  |
| SEGRFNO# | NUMBER |  |
| SEGBLK# | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The last three columns are included to enable joining V$SQL_WORKAREA_ACTIVE with V$TEMPSEG_USAGE to retrieve more information on this temporary segment. You can use this view to answer the following: What are the top 10 largest work areas currently allocated in the system? What percentage of memory is over-allocated ( EXPECTED_SIZE < ACTUAL_MEM_USED ) and under-allocated ( EXPECTED_SIZE > ACTUAL_MEM_USED )? What are the active work areas using more memory than what is expected by the memory manager? What are the active work areas that have spilled to disk? See Also: " V$SQL_WORKAREA " Oracle Database Concepts for more information about SQL work areas See Also: " V$SQL_WORKAREA " Oracle Database Concepts for more information about SQL work areas