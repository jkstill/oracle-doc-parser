---
id: 19c__V$SESSION_WAIT_CLASS
name: V$SESSION_WAIT_CLASS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_WAIT_CLASS.html
---

# V$SESSION_WAIT_CLASS

V$SESSION_WAIT_CLASS displays the time spent in various wait event operations on a per-session basis.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| WAIT_CLASS_ID | NUMBER |  |
| WAIT_CLASS# | NUMBER |  |
| WAIT_CLASS | VARCHAR2(64) |  |
| TOTAL_WAITS | NUMBER |  |
| TIME_WAITED | NUMBER |  |
| CON_ID | NUMBER |  |