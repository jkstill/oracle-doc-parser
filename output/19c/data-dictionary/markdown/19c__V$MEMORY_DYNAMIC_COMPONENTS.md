---
id: 19c__V$MEMORY_DYNAMIC_COMPONENTS
name: V$MEMORY_DYNAMIC_COMPONENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-MEMORY_DYNAMIC_COMPONENTS.html
---

# V$MEMORY_DYNAMIC_COMPONENTS

V$MEMORY_DYNAMIC_COMPONENTS displays information about the dynamic SGA components.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMPONENT | VARCHAR2(64) |  |
| CURRENT_SIZE | NUMBER |  |
| MIN_SIZE | NUMBER |  |
| MAX_SIZE | NUMBER |  |
| USER_SPECIFIED_SIZE | NUMBER |  |
| OPER_COUNT | NUMBER |  |
| LAST_OPER_TYPE | VARCHAR2(13) |  |
| LAST_OPER_MODE | VARCHAR2(9) |  |
| LAST_OPER_TIME | DATE |  |
| GRANULE_SIZE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view summarizes information based on all completed SGA resize operations since instance startup. All sizes are expressed in bytes.