---
id: 19c__V$KERNEL_IO_OUTLIER
name: V$KERNEL_IO_OUTLIER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-KERNEL_IO_OUTLIER.html
---

# V$KERNEL_IO_OUTLIER

V$KERNEL_IO_OUTLIER contains entries corresponding to I/Os that have taken a long time (more than 500 ms) to complete.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TIMESTAMP | NUMBER |  |
| IO_SIZE | NUMBER |  |
| IO_OFFSET | NUMBER |  |
| DEVICE_NAME | VARCHAR2(513) |  |
| PROCESS_NAME | VARCHAR2(64) |  |
| TOTAL_LATENCY | NUMBER |  |
| SETUP_LATENCY | NUMBER |  |
| QUEUE_TO_HBA_LATENCY | NUMBER |  |
| TRANSFER_LATENCY | NUMBER |  |
| CLEANUP_LATENCY | NUMBER |  |
| PID | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Use this view to see the individual kernel components of I/Os for which there are any occasional delays in serving disk I/O requests by the storage subsystem. Note: Although this view exists on all platforms in Oracle Database 12 c , it is only populated on the Solaris platform. Note: Although this view exists on all platforms in Oracle Database 12 c , it is only populated on the Solaris platform. See Also: " V$IO_OUTLIER " " V$LGWRIO_OUTLIER " See Also: " V$IO_OUTLIER " " V$LGWRIO_OUTLIER "