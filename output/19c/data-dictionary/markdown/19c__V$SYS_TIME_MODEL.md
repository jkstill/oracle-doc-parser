---
id: 19c__V$SYS_TIME_MODEL
name: V$SYS_TIME_MODEL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: internal
tags: [dynamic_performance]
source_file: V-SYS_TIME_MODEL.html
---

# V$SYS_TIME_MODEL

The time values are 8-byte integers and can therefore hold approximately 580,000 years worth of time before wrapping. Background process time is not included in a statistic value unless the statistic is specifically for background processes.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| STAT_ID | NUMBER |  |
| STAT_NAME | VARCHAR2(64) |  |
| VALUE | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view returns instance-wide data and a value of 0 in the CON_ID column when queried from the root of a CDB. Note: This view returns instance-wide data and a value of 0 in the CON_ID column when queried from the root of a CDB.