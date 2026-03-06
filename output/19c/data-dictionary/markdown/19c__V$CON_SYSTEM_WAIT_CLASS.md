---
id: 19c__V$CON_SYSTEM_WAIT_CLASS
name: V$CON_SYSTEM_WAIT_CLASS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-CON_SYSTEM_WAIT_CLASS.html
---

# V$CON_SYSTEM_WAIT_CLASS

V$CON_SYSTEM_WAIT_CLASS displays the time totals for each registered wait class in a container.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| WAIT_CLASS_ID | NUMBER |  |
| WAIT_CLASS# | NUMBER |  |
| WAIT_CLASS | VARCHAR2(64) |  |
| TOTAL_WAITS | NUMBER |  |
| TIME_WAITED | NUMBER |  |
| TOTAL_WAITS_FG | NUMBER |  |
| TIME_WAITED_FG | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content