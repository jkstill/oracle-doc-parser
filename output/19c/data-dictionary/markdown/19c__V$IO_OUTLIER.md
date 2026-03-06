---
id: 19c__V$IO_OUTLIER
name: V$IO_OUTLIER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-IO_OUTLIER.html
---

# V$IO_OUTLIER

V$IO_OUTLIER contains entries corresponding to I/Os that have taken a long time (more than 500 ms) to complete. Use this view to see if there any occasional delays in serving disk I/O requests by the storage subsystem.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FUNCTION_NAME | VARCHAR2(18) |  |
| IO_SIZE | NUMBER |  |
| WAIT_EVENT | VARCHAR2(64) |  |
| FILE_NAME | VARCHAR2(513) |  |
| IO_LATENCY | NUMBER |  |
| DISK1_NAME | VARCHAR2(255) |  |
| DISK1_LATENCY | NUMBER |  |
| DISK2_NAME | VARCHAR2(255) |  |
| DISK2_LATENCY | NUMBER |  |
| DISK3_NAME | VARCHAR2(255) |  |
| DISK3_LATENCY | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$KERNEL_IO_OUTLIER " " V$LGWRIO_OUTLIER " See Also: " V$KERNEL_IO_OUTLIER " " V$LGWRIO_OUTLIER "