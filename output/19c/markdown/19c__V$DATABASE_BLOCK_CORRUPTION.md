---
id: 19c__V$DATABASE_BLOCK_CORRUPTION
name: V$DATABASE_BLOCK_CORRUPTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-DATABASE_BLOCK_CORRUPTION.html
---

# V$DATABASE_BLOCK_CORRUPTION

V$DATABASE_BLOCK_CORRUPTION displays information about database blocks that were corrupted after the last backup.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE# | NUMBER |  |
| BLOCK# | NUMBER |  |
| BLOCKS | NUMBER |  |
| CORRUPTION_CHANGE# | NUMBER |  |
| CORRUPTION_TYPE | VARCHAR2(9) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$NONLOGGED_BLOCK " for information about nonlogged blocks See Also: " V$NONLOGGED_BLOCK " for information about nonlogged blocks