---
id: 19c__V$PROCESS_MEMORY_DETAIL
name: V$PROCESS_MEMORY_DETAIL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PROCESS_MEMORY_DETAIL.html
---

# V$PROCESS_MEMORY_DETAIL

V$PROCESS_MEMORY_DETAIL provides detailed information on dynamic PGA memory usage for each automatically captured snapshot.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PID | NUMBER |  |
| SERIAL# | NUMBER |  |
| CATEGORY | VARCHAR2(15) |  |
| NAME | VARCHAR2(26) |  |
| HEAP_NAME | VARCHAR2(15) |  |
| BYTES | NUMBER |  |
| ALLOCATION_COUNT | NUMBER |  |
| HEAP_DESCRIPTOR | RAW(4 | 8) |  |
| PARENT_HEAP_DESCRIPTOR | RAW(4 | 8) |  |
| CON_ID | NUMBER |  |