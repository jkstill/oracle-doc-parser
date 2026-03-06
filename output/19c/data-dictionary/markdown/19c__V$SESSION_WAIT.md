---
id: 19c__V$SESSION_WAIT
name: V$SESSION_WAIT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_WAIT.html
---

# V$SESSION_WAIT

The script content on this page is for navigation purposes only and does not alter the content in any way.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SEQ# | NUMBER |  |
| EVENT | VARCHAR2(64) |  |
| P1TEXT | VARCHAR2(64) |  |
| P1 | NUMBER |  |
| P1RAW | RAW(8) |  |
| P2TEXT | VARCHAR2(64) |  |
| P2 | NUMBER |  |
| P2RAW | RAW(8) |  |
| P3TEXT | VARCHAR2(64) |  |
| P3 | NUMBER |  |
| P3RAW | RAW(8) |  |
| WAIT_CLASS_ID | NUMBER |  |
| WAIT_CLASS# | NUMBER |  |
| WAIT_CLASS | VARCHAR2(64) |  |
| WAIT_TIME | NUMBER |  |
| SECONDS_IN_WAIT | NUMBER |  |
| STATE | VARCHAR2(19) |  |
| WAIT_TIME_MICRO | NUMBER |  |
| TIME_REMAINING_MICRO | NUMBER |  |
| TIME_SINCE_LAST_WAIT_MICRO | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " TIMED_STATISTICS " and " Oracle Wait Events " See Also: " TIMED_STATISTICS " and " Oracle Wait Events "