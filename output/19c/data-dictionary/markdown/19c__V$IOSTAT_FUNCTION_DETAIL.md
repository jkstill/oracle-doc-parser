---
id: 19c__V$IOSTAT_FUNCTION_DETAIL
name: V$IOSTAT_FUNCTION_DETAIL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-IOSTAT_FUNCTION_DETAIL.html
---

# V$IOSTAT_FUNCTION_DETAIL

V$IOSTAT_FUNCTION_DETAIL displays disk I/O statistics for database functions (such as the LGWR and DBWR), broken down by file type.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FUNCTION_ID | NUMBER |  |
| FUNCTION_NAME | VARCHAR2(18) |  |
| FILETYPE_ID | NUMBER |  |
| FILETYPE_NAME | VARCHAR2(28) |  |
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