---
id: 19c__V$LOGSTDBY_STATS
name: V$LOGSTDBY_STATS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-LOGSTDBY_STATS.html
---

# V$LOGSTDBY_STATS

The script content on this page is for navigation purposes only and does not alter the content in any way.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAME | VARCHAR2(64) |  |
| VALUE | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content No rows are returned from this view when SQL Apply is not running. This view is only meaningful in the context of a logical standby database. All statistics shown in this view are reinitialized at each SQL Apply start.