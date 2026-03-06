---
id: 19c__V$BT_SCAN_OBJ_TEMPS
name: V$BT_SCAN_OBJ_TEMPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-BT_SCAN_OBJ_TEMPS.html
---

# V$BT_SCAN_OBJ_TEMPS

V$BT_SCAN_OBJ_TEMPS shows the active objects currently tracked by the big table cache.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TS# | NUMBER |  |
| DATAOBJ# | NUMBER |  |
| SIZE_IN_BLKS | NUMBER |  |
| TEMPERATURE | NUMBER |  |
| POLICY | VARCHAR2(10) |  |
| CACHED_IN_MEM | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " DB_BIG_TABLE_CACHE_PERCENT_TARGET " for more information about enabling the big table cache See Also: " DB_BIG_TABLE_CACHE_PERCENT_TARGET " for more information about enabling the big table cache