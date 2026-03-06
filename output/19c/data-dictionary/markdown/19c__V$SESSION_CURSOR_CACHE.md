---
id: 19c__V$SESSION_CURSOR_CACHE
name: V$SESSION_CURSOR_CACHE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_CURSOR_CACHE.html
---

# V$SESSION_CURSOR_CACHE

V$SESSION_CURSOR_CACHE displays information on cursor usage for the current session.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MAXIMUM | NUMBER |  |
| COUNT | NUMBER |  |
| OPENS | NUMBER |  |
| HITS | NUMBER |  |
| HIT_RATIO | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: The V$SESSION_CURSOR_CACHE view is not a measure of the effectiveness of the SESSION_CACHED_CURSORS initialization parameter. Note: The V$SESSION_CURSOR_CACHE view is not a measure of the effectiveness of the SESSION_CACHED_CURSORS initialization parameter. See Also: " SESSION_CACHED_CURSORS " See Also: " SESSION_CACHED_CURSORS "