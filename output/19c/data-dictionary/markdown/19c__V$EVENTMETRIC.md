---
id: 19c__V$EVENTMETRIC
name: V$EVENTMETRIC
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-EVENTMETRIC.html
---

# V$EVENTMETRIC

V$EVENTMETRIC displays values of wait event metrics for the most recent 60-second interval.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| BEGIN_TIME | DATE |  |
| END_TIME | DATE |  |
| INTSIZE_CSEC | NUMBER |  |
| EVENT# | NUMBER |  |
| EVENT_ID | NUMBER |  |
| NUM_SESS_WAITING | NUMBER |  |
| TIME_WAITED | NUMBER |  |
| WAIT_COUNT | NUMBER |  |
| TIME_WAITED_FG | NUMBER |  |
| WAIT_COUNT_FG | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content