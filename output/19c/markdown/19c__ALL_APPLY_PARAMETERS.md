---
id: 19c__ALL_APPLY_PARAMETERS
name: ALL_APPLY_PARAMETERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [all]
source_file: ALL_APPLY_PARAMETERS.html
---

# ALL_APPLY_PARAMETERS

ALL_APPLY_PARAMETERS displays information about the parameters for the apply processes that dequeue events from queues accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APPLY_NAME | VARCHAR2(128) | Name of the apply process |
| PARAMETER | VARCHAR2(128) | Name of the parameter |
| VALUE | VARCHAR2(4000) | Parameter value |
| SET_BY_USER | VARCHAR2(3) | Indicates whether the parameter value was set by the user ( YES ) or was not set by the user ( NO ). If NO for a parameter, then the parameter is set to its default value. If YES for a parameter, then the parameter may or may not be set to its default value. |

## Usage Notes

Related View DBA_APPLY_PARAMETERS displays information about the parameters for all apply processes in the database. See Also: " DBA_APPLY_PARAMETERS " See Also: " DBA_APPLY_PARAMETERS "