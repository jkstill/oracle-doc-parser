---
id: 19c__V$SHARED_POOL_RESERVED
name: V$SHARED_POOL_RESERVED
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-SHARED_POOL_RESERVED.html
---

# V$SHARED_POOL_RESERVED

V$SHARED_POOL_RESERVED displays statistics that help you tune the reserved pool and space within the shared pool.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FREE_SPACE | NUMBER |  |
| AVG_FREE_SIZE | NUMBER |  |
| FREE_COUNT | NUMBER |  |
| MAX_FREE_SIZE | NUMBER |  |
| USED_SPACE | NUMBER |  |
| AVG_USED_SIZE | NUMBER |  |
| USED_COUNT | NUMBER |  |
| MAX_USED_SIZE | NUMBER |  |
| REQUESTS | NUMBER |  |
| REQUEST_MISSES | NUMBER |  |
| LAST_MISS_SIZE | NUMBER |  |
| MAX_MISS_SIZE | NUMBER |  |
| REQUEST_FAILURES | NUMBER |  |
| LAST_FAILURE_SIZE | NUMBER |  |
| ABORTED_REQUEST_THRESHOLD | NUMBER |  |
| ABORTED_REQUESTS | NUMBER |  |
| LAST_ABORTED_SIZE | NUMBER |  |
| CON_ID | NUMBER |  |