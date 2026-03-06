---
id: 19c__V$SESSION_WAIT_HISTORY
name: V$SESSION_WAIT_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_WAIT_HISTORY.html
---

# V$SESSION_WAIT_HISTORY

V$SESSION_WAIT_HISTORY displays the last 10 wait events for each active session.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SEQ# | NUMBER |  |
| EVENT# | NUMBER |  |
| EVENT | VARCHAR2(64) |  |
| P1TEXT | VARCHAR2(64) |  |
| P1 | NUMBER |  |
| P2TEXT | VARCHAR2(64) |  |
| P2 | NUMBER |  |
| P3TEXT | VARCHAR2(64) |  |
| P3 | NUMBER |  |
| WAIT_TIME | NUMBER |  |
| WAIT_TIME_MICRO | NUMBER |  |
| TIME_SINCE_LAST_WAIT_MICRO | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content