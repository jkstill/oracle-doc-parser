---
id: 19c__V$ROWCACHE_PARENT
name: V$ROWCACHE_PARENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ROWCACHE_PARENT.html
---

# V$ROWCACHE_PARENT

INDX

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INDX | NUMBER |  |
| HASH | NUMBER |  |
| ADDRESS | RAW(4 | 8) |  |
| CACHE# | NUMBER |  |
| CACHE_NAME | VARCHAR2(64) |  |
| EXISTENT | VARCHAR2(1) |  |
| LOCK_MODE | NUMBER |  |
| LOCK_REQUEST | NUMBER |  |
| TXN | RAW(4 | 8) |  |
| SADDR | RAW(4 | 8) |  |
| INST_LOCK_REQUEST | NUMBER |  |
| INST_LOCK_RELEASE | NUMBER |  |
| INST_LOCK_TYPE | VARCHAR2(2) |  |
| INST_LOCK_ID1 | RAW(4) |  |
| INST_LOCK_ID2 | RAW(4) |  |
| KEY | RAW(100) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content