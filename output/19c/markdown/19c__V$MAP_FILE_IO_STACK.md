---
id: 19c__V$MAP_FILE_IO_STACK
name: V$MAP_FILE_IO_STACK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-MAP_FILE_IO_STACK.html
---

# V$MAP_FILE_IO_STACK

V$MAP_FILE_IO_STACK displays the hierarchical arrangement of storage containers for files. Each row in the view represents a level in the hierarchy.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_MAP_IDX | NUMBER |  |
| DEPTH | NUMBER |  |
| ELEM_IDX | NUMBER |  |
| CU_SIZE | NUMBER |  |
| STRIDE | NUMBER |  |
| NUM_CU | NUMBER |  |
| ELEM_OFFSET | NUMBER |  |
| FILE_OFFSET | NUMBER |  |
| DATA_TYPE | VARCHAR2(15) |  |
| PARITY_POS | NUMBER |  |
| PARITY_PERIOD | NUMBER |  |
| ID | NUMBER |  |
| PARENT_ID | NUMBER |  |
| CON_ID | NUMBER |  |