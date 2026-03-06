---
id: 19c__V$SYSTEM_EVENT
name: V$SYSTEM_EVENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-SYSTEM_EVENT.html
---

# V$SYSTEM_EVENT

Name of the wait event; derived statistic name from V$EVENT_NAME

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

See Also: " TIMED_STATISTICS " See Also: " TIMED_STATISTICS " Note: This view returns instance-wide data and a value of 0 in the CON_ID column when queried from the root of a CDB. Note: This view returns instance-wide data and a value of 0 in the CON_ID column when queried from the root of a CDB.