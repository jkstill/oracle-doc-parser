---
id: 19c__V$ENQUEUE_LOCK
name: V$ENQUEUE_LOCK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ENQUEUE_LOCK.html
---

# V$ENQUEUE_LOCK

V$ENQUEUE_LOCK displays all locks owned by enqueue state objects. The columns in this view are identical to the columns in V$LOCK .

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

See Also: " V$LOCK " See Also: " V$LOCK "