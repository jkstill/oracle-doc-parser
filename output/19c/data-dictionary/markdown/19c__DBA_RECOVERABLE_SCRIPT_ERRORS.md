---
id: 19c__DBA_RECOVERABLE_SCRIPT_ERRORS
name: DBA_RECOVERABLE_SCRIPT_ERRORS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RECOVERABLE_SCRIPT_ERRORS.html
---

# DBA_RECOVERABLE_SCRIPT_ERRORS

DBA_RECOVERABLE_SCRIPT_ERRORS provides details about errors that occurred during script execution.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCRIPT_ID | RAW(16) | Global unique ID of the recoverable script |
| BLOCK_NUM | NUMBER | The n th block that failed |
| ERROR_NUMBER | NUMBER | Number of the error encountered while executing the block |
| ERROR_MESSAGE | VARCHAR2(4000) | Error message encountered while executing the block |
| ERROR_CREATION_TIME | DATE | Time that the error was created |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content