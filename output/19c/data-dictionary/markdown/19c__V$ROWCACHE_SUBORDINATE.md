---
id: 19c__V$ROWCACHE_SUBORDINATE
name: V$ROWCACHE_SUBORDINATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ROWCACHE_SUBORDINATE.html
---

# V$ROWCACHE_SUBORDINATE

V$ROWCACHE_SUBORDINATE displays information for subordinate objects in the data dictionary.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INDX | NUMBER |  |
| HASH | NUMBER |  |
| ADDRESS | RAW(4 | 8) |  |
| CACHE# | NUMBER |  |
| SUBCACHE# | NUMBER |  |
| SUBCACHE_NAME | VARCHAR2(64) |  |
| EXISTENT | VARCHAR2(1) |  |
| PARENT | RAW(4 | 8) |  |
| KEY | RAW(100) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content