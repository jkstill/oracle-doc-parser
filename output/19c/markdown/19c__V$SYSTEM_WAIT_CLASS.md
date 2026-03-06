---
id: 19c__V$SYSTEM_WAIT_CLASS
name: V$SYSTEM_WAIT_CLASS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SYSTEM_WAIT_CLASS.html
---

# V$SYSTEM_WAIT_CLASS

V$SYSTEM_WAIT_CLASS displays the instance-wide time totals for each registered wait class.

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

Note: This view returns instance-wide data and a value of 0 in the CON_ID column when queried from the root of a CDB. Note: This view returns instance-wide data and a value of 0 in the CON_ID column when queried from the root of a CDB.