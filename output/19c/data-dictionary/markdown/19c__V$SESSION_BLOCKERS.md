---
id: 19c__V$SESSION_BLOCKERS
name: V$SESSION_BLOCKERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_BLOCKERS.html
---

# V$SESSION_BLOCKERS

SID

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SESS_SERIAL# | NUMBER |  |
| WAIT_ID | NUMBER |  |
| WAIT_EVENT | NUMBER |  |
| WAIT_EVENT_TEXT | VARCHAR2(64) |  |
| BLOCKER_INSTANCE_ID | NUMBER |  |
| BLOCKER_SID | NUMBER |  |
| BLOCKER_SESS_SERIAL# | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content