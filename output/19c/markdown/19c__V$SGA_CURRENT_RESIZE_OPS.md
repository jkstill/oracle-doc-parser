---
id: 19c__V$SGA_CURRENT_RESIZE_OPS
name: V$SGA_CURRENT_RESIZE_OPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-SGA_CURRENT_RESIZE_OPS.html
---

# V$SGA_CURRENT_RESIZE_OPS

Name of the parameter for the resize operation

## Columns

| Column | Type | Description |
|--------|------|-------------|
| COMPONENT | VARCHAR2(64) |  |
| OPER_TYPE | VARCHAR2(13) |  |
| OPER_MODE | VARCHAR2(9) |  |
| PARAMETER | VARCHAR2(80) |  |
| INITIAL_SIZE | NUMBER |  |
| TARGET_SIZE | NUMBER |  |
| CURRENT_SIZE | NUMBER |  |
| START_TIME | DATE |  |
| LAST_UPDATE_TIME | DATE |  |
| CON_ID | NUMBER |  |