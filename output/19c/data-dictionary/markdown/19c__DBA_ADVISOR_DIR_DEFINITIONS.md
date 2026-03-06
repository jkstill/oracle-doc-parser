---
id: 19c__DBA_ADVISOR_DIR_DEFINITIONS
name: DBA_ADVISOR_DIR_DEFINITIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_ADVISOR_DIR_DEFINITIONS.html
---

# DBA_ADVISOR_DIR_DEFINITIONS

DBA_ADVISOR_DIR_DEFINITIONS provides a definition of the base directive.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ID | NUMBER | Unique id for directive. The directive management engine automatically generates ID numbers. The identifier is unique among all directives regardless of the domain name and directive name. |
| ADVISOR_ID | NUMBER | Identifier number of the owner advisor. |
| ADVISOR_NAME | VARCHAR2(128) | The name of the advisor to which this directive belongs. |
| DIRECTIVE_NAME | VARCHAR2(128) | Any value that further classifies this directive within a domain. The domain and the name form a unique key for the directive. |
| DOMAIN_NAME | VARCHAR2(128) | Domain or namespace name. |
| DESCRIPTION | VARCHAR2(256) | An optional description that documents the purpose of the directive. |
| TYPE | NUMBER | Further describes the use of the directive. Possible values are: Filter - An Xpath filter Single Value - Evaluation returns a single string value Multiple Values - Evaluation returns one to many string values Conditional - Evaluation returns a single value based on an input key, similar to a CASE or SWITCH statement |
| TYPE_NAME | VARCHAR2(15) | A decoded version of the TYPE column. |
| TASK_STATUS | VARCHAR2(9) | The status of the directive instances when a task is not in its initial state. Possible values are: IMMUTABLE MUTABLE |
| INSTANCES | VARCHAR2(8) | Indicates whether a directive will permit multiple instances. Possible values are: SINGLE MULTIPLE |
| METADATA | CLOB | A DTD that is used to process the directive. |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content