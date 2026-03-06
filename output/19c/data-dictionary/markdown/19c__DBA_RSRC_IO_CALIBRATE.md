---
id: 19c__DBA_RSRC_IO_CALIBRATE
name: DBA_RSRC_IO_CALIBRATE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_RSRC_IO_CALIBRATE.html
---

# DBA_RSRC_IO_CALIBRATE

DBA_RSRC_IO_CALIBRATE displays I/O calibration results for the latest calibration run.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| START_TIME | TIMESTAMP(6) | Start time of the most recent I/O calibration |
| END_TIME | TIMESTAMP(6) | End time of the most recent I/O calibration |
| MAX_IOPS | NUMBER | Maximum number of data block read requests that can be sustained per second |
| MAX_MBPS | NUMBER | Maximum megabytes per second of maximum-sized read requests that can be sustained |
| MAX_PMBPS | NUMBER | Maximum megabytes per second of large I/O requests that can be sustained by a single process |
| LATENCY | NUMBER | Latency for data block read requests |
| NUM_PHYSICAL_DISKS | NUMBER | Number of physical disks in the storage subsystem (as specified by the user) |
| ADDITIONAL_INFO | VARCHAR2(1024) | Additional information about the most recent calibration run |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content