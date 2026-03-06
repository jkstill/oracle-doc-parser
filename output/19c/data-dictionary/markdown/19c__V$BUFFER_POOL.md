---
id: 19c__V$BUFFER_POOL
name: V$BUFFER_POOL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BUFFER_POOL.html
---

# V$BUFFER_POOL

V$BUFFER_POOL displays information about all buffer pools available for the instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER |  |
| NAME | VARCHAR2(20) |  |
| BLOCK_SIZE | NUMBER |  |
| RESIZE_STATE | VARCHAR2(10) |  |
| CURRENT_SIZE | NUMBER |  |
| BUFFERS | NUMBER |  |
| TARGET_SIZE | NUMBER |  |
| TARGET_BUFFERS | NUMBER |  |
| PREV_SIZE | NUMBER |  |
| PREV_BUFFERS | NUMBER |  |
| LO_BNUM | NUMBER |  |
| HI_BNUM | NUMBER |  |
| LO_SETID | NUMBER |  |
| HI_SETID | NUMBER |  |
| SET_COUNT | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " DB_BLOCK_SIZE " See Also: " DB_BLOCK_SIZE "