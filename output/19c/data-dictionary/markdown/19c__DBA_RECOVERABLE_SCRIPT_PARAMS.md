---
id: 19c__DBA_RECOVERABLE_SCRIPT_PARAMS
name: DBA_RECOVERABLE_SCRIPT_PARAMS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_RECOVERABLE_SCRIPT_PARAMS.html
---

# DBA_RECOVERABLE_SCRIPT_PARAMS

DBA_RECOVERABLE_SCRIPT_PARAMS provides details about recoverable operation parameters.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCRIPT_ID | RAW(16) | Unique ID of the operation |
| PARAMETER | VARCHAR2(128) | Name of the parameter |
| PARAM_INDEX | NUMBER | Index for multi-valued parameter |
| VALUE | VARCHAR2(4000) | Value of the parameter |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content