---
id: 19c__DBA_RECOVERABLE_SCRIPT_HIST
name: DBA_RECOVERABLE_SCRIPT_HIST
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RECOVERABLE_SCRIPT_HIST.html
---

# DBA_RECOVERABLE_SCRIPT_HIST

DBA_RECOVERABLE_SCRIPT_HIST displays details about executed or purged recoverable operations.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCRIPT_ID | RAW(16) | Unique id of the operation |
| CREATION_TIME | DATE | Time the operation was invoked |
| INVOKING_PACKAGE_OWNER | VARCHAR2(128) | Invoking package owner of the operation |
| INVOKING_PACKAGE | VARCHAR2(128) | Invoking package of the operation |
| INVOKING_PROCEDURE | VARCHAR2(128) | Invoking procedure of the operation |
| INVOKING_USER | VARCHAR2(128) | Script owner |
| STATUS | VARCHAR2(8) | state of the recoverable script: EXECUTED, PURGED |
| TOTAL_BLOCKS | NUMBER | total number of blocks for the recoverable script to be executed |
| DONE_BLOCK_NUM | NUMBER | last block so far executed |
| SCRIPT_COMMENT | VARCHAR2(4000) | comment for the recoverable script |