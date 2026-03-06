---
id: 19c__DBA_RECOVERABLE_SCRIPT
name: DBA_RECOVERABLE_SCRIPT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RECOVERABLE_SCRIPT.html
---

# DBA_RECOVERABLE_SCRIPT

DBA_RECOVERABLE_SCRIPT provides details about recoverable operations.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCRIPT_ID | RAW(16) | Unique ID of the operation |
| CREATION_TIME | DATE | Time the operation was invoked |
| INVOKING_PACKAGE_OWNER | VARCHAR2(128) | Invoking package owner of the operation |
| INVOKING_PACKAGE | VARCHAR2(128) | Invoking package of the operation |
| INVOKING_PROCEDURE | VARCHAR2(128) | Invoking procedure of the operation |
| INVOKING_USER | VARCHAR2(128) | Script owner |
| STATUS | VARCHAR2(12) | State of the recoverable script: GENERATING, NOT EXECUTED, EXECUTING, EXECUTED, or ERROR |
| TOTAL_BLOCKS | NUMBER | Total number of blocks for the recoverable script to be executed |
| DONE_BLOCK_NUM | NUMBER | Last block executed, thus far |
| SCRIPT_COMMENT | VARCHAR2(4000) | Comment for the recoverable script |