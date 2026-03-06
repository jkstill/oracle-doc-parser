---
id: 19c__V$GLOBAL_BLOCKED_LOCKS
name: V$GLOBAL_BLOCKED_LOCKS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-GLOBAL_BLOCKED_LOCKS.html
---

# V$GLOBAL_BLOCKED_LOCKS

V$GLOBAL_BLOCKED_LOCKS displays global blocked locks.

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
| CON_ID | NUMBER |  |