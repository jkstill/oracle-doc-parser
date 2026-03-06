---
id: 19c__V$MUTEX_SLEEP_HISTORY
name: V$MUTEX_SLEEP_HISTORY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-MUTEX_SLEEP_HISTORY.html
---

# V$MUTEX_SLEEP_HISTORY

V$MUTEX_SLEEP_HISTORY displays time-series data.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MUTEX_IDENTIFIER | NUMBER |  |
| SLEEP_TIMESTAMP | TIMESTAMP(6) |  |
| MUTEX_TYPE | VARCHAR2(32) |  |
| GETS | NUMBER |  |
| SLEEPS | NUMBER |  |
| REQUESTING_SESSION | NUMBER |  |
| BLOCKING_SESSION | NUMBER |  |
| LOCATION | VARCHAR2(40) |  |
| MUTEX_VALUE | RAW(4 | 8) |  |
| P1 | NUMBER |  |
| P1RAW | RAW(4 | 8) |  |
| P2 | NUMBER |  |
| P3 | NUMBER |  |
| P4 | NUMBER |  |
| P5 | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Each row in this view is for a specific time, mutex type, location, requesting session and blocking session combination. That is, it shows data related to a specific session (requesting session) that slept while requesting a specific mutex type and location, because it was being held by a specific blocking session. The data in this view is contained within a circular buffer, with the most recent sleeps shown.