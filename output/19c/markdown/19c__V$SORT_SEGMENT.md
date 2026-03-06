---
id: 19c__V$SORT_SEGMENT
name: V$SORT_SEGMENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [dynamic_performance]
source_file: V-SORT_SEGMENT.html
---

# V$SORT_SEGMENT

V$SORT_SEGMENT displays information about every sort segment in a given instance. The view is only updated when the tablespace is of the TEMPORARY type.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TABLESPACE_NAME | VARCHAR2(30) |  |
| SEGMENT_FILE | NUMBER |  |
| SEGMENT_BLOCK | NUMBER |  |
| EXTENT_SIZE | NUMBER |  |
| CURRENT_USERS | NUMBER |  |
| TOTAL_EXTENTS | NUMBER |  |
| TOTAL_BLOCKS | NUMBER |  |
| USED_EXTENTS | NUMBER |  |
| USED_BLOCKS | NUMBER |  |
| FREE_EXTENTS | NUMBER |  |
| FREE_BLOCKS | NUMBER |  |
| ADDED_EXTENTS | NUMBER |  |
| EXTENT_HITS | NUMBER |  |
| FREED_EXTENTS | NUMBER |  |
| FREE_REQUESTS | NUMBER |  |
| MAX_SIZE | NUMBER |  |
| MAX_BLOCKS | NUMBER |  |
| MAX_USED_SIZE | NUMBER |  |
| MAX_USED_BLOCKS | NUMBER |  |
| MAX_SORT_SIZE | NUMBER |  |
| MAX_SORT_BLOCKS | NUMBER |  |
| RELATIVE_FNO | NUMBER |  |
| TS# | NUMBER |  |
| CON_ID | NUMBER |  |
| IS_LOCAL_TEMP | NUMBER |  |