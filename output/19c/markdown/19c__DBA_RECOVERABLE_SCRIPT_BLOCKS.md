---
id: 19c__DBA_RECOVERABLE_SCRIPT_BLOCKS
name: DBA_RECOVERABLE_SCRIPT_BLOCKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RECOVERABLE_SCRIPT_BLOCKS.html
---

# DBA_RECOVERABLE_SCRIPT_BLOCKS

DBA_RECOVERABLE_SCRIPT_BLOCKS provides details about recoverable script blocks.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCRIPT_ID | RAW(16) | Global unique ID of the recoverable script to which this block belongs |
| BLOCK_NUM | NUMBER | The n th block in the recoverable script to be executed |
| FORWARD_BLOCK | CLOB | Forward block to be executed |
| FORWARD_BLOCK_DBLINK | VARCHAR2(128) | Database where the forward block is executed |
| UNDO_BLOCK | CLOB | Block to roll back the forward operation |
| UNDO_BLOCK_DBLINK | VARCHAR2(128) | Database where the undo block is executed |
| STATUS | VARCHAR2(12) | Status of the block execution: GENERATING, NOT EXECUTED, EXECUTING, EXECUTED, or ERROR |
| BLOCK_COMMENT | VARCHAR2(4000) | Comment for the block |