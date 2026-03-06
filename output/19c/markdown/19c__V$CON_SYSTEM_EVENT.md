---
id: 19c__V$CON_SYSTEM_EVENT
name: V$CON_SYSTEM_EVENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-CON_SYSTEM_EVENT.html
---

# V$CON_SYSTEM_EVENT

V$CON_SYSTEM_EVENT displays information on total waits for an event in a container.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| EVENT | VARCHAR2(64) |  |
| TOTAL_WAITS | NUMBER |  |
| TOTAL_TIMEOUTS | NUMBER |  |
| TIME_WAITED | NUMBER |  |
| AVERAGE_WAIT | NUMBER |  |
| TIME_WAITED_MICRO | NUMBER |  |
| TOTAL_WAITS_FG | NUMBER |  |
| TOTAL_TIMEOUTS_FG | NUMBER |  |
| TIME_WAITED_FG | NUMBER |  |
| AVERAGE_WAIT_FG | NUMBER |  |
| TIME_WAITED_MICRO_FG | NUMBER |  |
| EVENT_ID | NUMBER |  |
| WAIT_CLASS_ID | NUMBER |  |
| WAIT_CLASS# | NUMBER |  |
| WAIT_CLASS | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Note that the TIME_WAITED and AVERAGE_WAIT columns will contain a value of zero on those platforms that do not support a fast timing mechanism. If you are running on one of these platforms and you want this column to reflect true wait times, then you must set TIMED_STATISTICS to TRUE in the parameter file; doing this will have a small negative effect on system performance. See Also: " TIMED_STATISTICS " See Also: " TIMED_STATISTICS "