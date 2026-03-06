---
id: 19c__DBA_ADDM_SYSTEM_DIRECTIVES
name: DBA_ADDM_SYSTEM_DIRECTIVES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dba]
source_file: DBA_ADDM_SYSTEM_DIRECTIVES.html
---

# DBA_ADDM_SYSTEM_DIRECTIVES

DBA_ADDM_SYSTEM_DIRECTIVES displays information about global instances for ADDM system directives.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INSTANCE_ID | NUMBER | Unique ID for the directive instance. The directive management engine automatically generates ID numbers. |
| INSTANCE_NAME | VARCHAR2(128) | User-assigned name for the directive instance. |
| DIRECTIVE_NAME | VARCHAR2(128) | Any value that further classifies this directive within a domain. The domain and the name form a unique key for the directive. |
| DESCRIPTION | VARCHAR2(4000) | Description of the ADDM system directive, shown in the language used by the current session |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content