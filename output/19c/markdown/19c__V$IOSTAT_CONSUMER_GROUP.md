---
id: 19c__V$IOSTAT_CONSUMER_GROUP
name: V$IOSTAT_CONSUMER_GROUP
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-IOSTAT_CONSUMER_GROUP.html
---

# V$IOSTAT_CONSUMER_GROUP

V$IOSTAT_CONSUMER_GROUP displays disk I/O statistics for consumer groups.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CONSUMER_GROUP_ID | NUMBER |  |
| SMALL_READ_MEGABYTES | NUMBER |  |
| SMALL_WRITE_MEGABYTES | NUMBER |  |
| LARGE_READ_MEGABYTES | NUMBER |  |
| LARGE_WRITE_MEGABYTES | NUMBER |  |
| SMALL_READ_REQS | NUMBER |  |
| SMALL_WRITE_REQS | NUMBER |  |
| LARGE_READ_REQS | NUMBER |  |
| LARGE_WRITE_REQS | NUMBER |  |
| NUMBER_OF_WAITS | NUMBER |  |
| WAIT_TIME | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

If the resource manager is enabled, then I/O statistics for all consumer groups that are part of the currently enabled resource plan are captured.