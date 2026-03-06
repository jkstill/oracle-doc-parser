---
id: 19c__V$MUTEX_SLEEP
name: V$MUTEX_SLEEP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-MUTEX_SLEEP.html
---

# V$MUTEX_SLEEP

V$MUTEX_SLEEP shows the wait time, and the number of sleeps for each combination of mutex type and location.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| MUTEX_TYPE | VARCHAR2(32) |  |
| LOCATION | VARCHAR2(40) |  |
| SLEEPS | NUMBER |  |
| WAIT_TIME | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content