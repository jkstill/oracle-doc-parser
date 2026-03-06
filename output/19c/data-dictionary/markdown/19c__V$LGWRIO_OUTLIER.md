---
id: 19c__V$LGWRIO_OUTLIER
name: V$LGWRIO_OUTLIER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-LGWRIO_OUTLIER.html
---

# V$LGWRIO_OUTLIER

V$LGWRIO_OUTLIER contains entries corresponding to Log Writer (LGWR) process I/Os that have taken a long time (more than 500 ms) to complete. Use this view to see if there any occasional delays in serving disk I/O requests by the storage subsystem.

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

Previous Next JavaScript must be enabled to correctly display this content See Also: " V$IO_OUTLIER " " V$KERNEL_IO_OUTLIER " See Also: " V$IO_OUTLIER " " V$KERNEL_IO_OUTLIER "