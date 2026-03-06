---
id: 19c__ALL_CAPTURE_PARAMETERS
name: ALL_CAPTURE_PARAMETERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [all]
source_file: ALL_CAPTURE_PARAMETERS.html
---

# ALL_CAPTURE_PARAMETERS

ALL_CAPTURE_PARAMETERS displays information about the parameters for the capture processes that enqueue the captured changes into queues accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CAPTURE_NAME | VARCHAR2(128) | Name of the capture process |
| PARAMETER | VARCHAR2(128) | Name of the parameter |
| VALUE | VARCHAR2(4000) | Parameter value |
| SET_BY_USER | VARCHAR2(3) | Indicates whether the parameter value was set by the user ( YES ) or was not set by the user ( NO ). If NO , then the parameter is set to its default value. If YES , then the parameter may or may not be set to its default value. |
| SOURCE_DATABASE | VARCHAR2(128) | Global name of the container for which the capture parameter is defined |

## Usage Notes

Related View DBA_CAPTURE_PARAMETERS displays information about the parameters for all capture processes in the database. See Also: " DBA_CAPTURE_PARAMETERS " See Also: " DBA_CAPTURE_PARAMETERS "