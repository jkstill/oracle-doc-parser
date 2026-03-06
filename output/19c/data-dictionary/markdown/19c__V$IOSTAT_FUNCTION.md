---
id: 19c__V$IOSTAT_FUNCTION
name: V$IOSTAT_FUNCTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-IOSTAT_FUNCTION.html
---

# V$IOSTAT_FUNCTION

V$IOSTAT_FUNCTION displays disk I/O statistics for database functions (such as the LGWR and DBWR).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FUNCTION_ID | NUMBER |  |
| FUNCTION_NAME | VARCHAR2(18) |  |
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

Previous Next JavaScript must be enabled to correctly display this content