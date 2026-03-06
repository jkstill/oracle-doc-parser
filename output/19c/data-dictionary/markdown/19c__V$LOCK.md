---
id: 19c__V$LOCK
name: V$LOCK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LOCK.html
---

# V$LOCK

V$LOCK lists the locks currently held by the Oracle Database and outstanding requests for a lock or latch.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ADDR | RAW(4 | 8) |  |
| KADDR | RAW(4 | 8) |  |
| SID | NUMBER |  |
| TYPE | VARCHAR2(2) |  |
| ID1 | NUMBER |  |
| ID2 | NUMBER |  |
| LMODE | NUMBER |  |
| REQUEST | NUMBER |  |
| CTIME | NUMBER |  |
| BLOCK | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content