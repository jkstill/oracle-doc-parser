---
id: 19c__V$INDEX_USAGE_INFO
name: V$INDEX_USAGE_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: index
tags: [dynamic_performance]
source_file: V-INDEX_USAGE_INFO.html
---

# V$INDEX_USAGE_INFO

V$INDEX_USAGE_INFO keeps track of index usage since the last flush. A flush occurs every 15 minutes. After each flush, ACTIVE_ELEM_COUNT is reset to 0 and LAST_FLUSH_TIME is updated to the current time.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INDEX_STATS_ENABLED | NUMBER |  |
| INDEX_STATS_COLLECTION_TYPE | NUMBER |  |
| ACTIVE_ELEM_COUNT | NUMBER |  |
| ALLOC_ELEM_COUNT | NUMBER |  |
| MAX_ELEM_COUNT | NUMBER |  |
| FLUSH_COUNT | NUMBER |  |
| TOTAL_FLUSH_DURATION | NUMBER |  |
| LAST_FLUSH_TIME | TIMESTAMP(3) |  |
| STATUS_MSG | VARCHAR2(256) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " DBA_INDEX_USAGE " See Also: " DBA_INDEX_USAGE "