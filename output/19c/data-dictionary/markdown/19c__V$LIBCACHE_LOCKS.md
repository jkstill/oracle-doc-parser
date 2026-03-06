---
id: 19c__V$LIBCACHE_LOCKS
name: V$LIBCACHE_LOCKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LIBCACHE_LOCKS.html
---

# V$LIBCACHE_LOCKS

V$LIBCACHE_LOCKS displays information about the library cache locks and pins. Locks and pins are distinguished based on the value of the TYPE column.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TYPE | VARCHAR2(4) |  |
| ADDR | RAW(4 | 8) |  |
| HOLDING_USER_SESSION | RAW(4 | 8) |  |
| HOLDING_SESSION | RAW(4 | 8) |  |
| OBJECT_HANDLE | RAW(4 | 8) |  |
| LOCK_HELD | RAW(4 | 8) |  |
| REFCOUNT | NUMBER |  |
| MODE_HELD | NUMBER |  |
| MODE_REQUESTED | NUMBER |  |
| SAVEPOINT_NUMBER | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content