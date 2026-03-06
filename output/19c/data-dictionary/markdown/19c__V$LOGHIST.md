---
id: 19c__V$LOGHIST
name: V$LOGHIST
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
tags: [dynamic_performance]
source_file: V-LOGHIST.html
---

# V$LOGHIST

V$LOGHIST contains log history information from the control file. This view is retained for historical compatibility. Oracle recommends that you use V$LOG_HISTORY instead.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| THREAD# | NUMBER |  |
| SEQUENCE# | NUMBER |  |
| FIRST_CHANGE# | NUMBER |  |
| FIRST_TIME | DATE |  |
| SWITCH_CHANGE# | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$LOG_HISTORY " See Also: " V$LOG_HISTORY "