---
id: 19c__DBA_ADVISOR_EXECUTION_TYPES
name: DBA_ADVISOR_EXECUTION_TYPES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_ADVISOR_EXECUTION_TYPES.html
---

# DBA_ADVISOR_EXECUTION_TYPES

DBA_ADVISOR_EXECUTION_TYPES displays possible execution action for a given advisor.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADVISOR_NAME | VARCHAR2(128) | Name of the advisor |
| EXECUTION_TYPE | VARCHAR2(128) | Execution type supported by the advisor |
| EXECUTION_DESCRIPTION | VARCHAR2(4000) | Optional description of the execution type |

## Usage Notes

Only advisors that support multiple executions of their tasks have entries in this view.