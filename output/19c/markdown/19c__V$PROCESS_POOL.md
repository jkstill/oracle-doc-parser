---
id: 19c__V$PROCESS_POOL
name: V$PROCESS_POOL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-PROCESS_POOL.html
---

# V$PROCESS_POOL

V$PROCESS_POOL provides information about process pools.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| POOL_NAME | VARCHAR2(512) |  |
| ENABLED | VARCHAR2(5) |  |
| MIN_COUNT | NUMBER |  |
| BATCH_COUNT | NUMBER |  |
| INIT_COUNT | NUMBER |  |
| CUR_COUNT | NUMBER |  |
| MAX_COUNT | NUMBER |  |
| CON_ID | NUMBER |  |