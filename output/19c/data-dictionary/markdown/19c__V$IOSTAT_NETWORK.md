---
id: 19c__V$IOSTAT_NETWORK
name: V$IOSTAT_NETWORK
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-IOSTAT_NETWORK.html
---

# V$IOSTAT_NETWORK

V$IOSTAT_NETWORK displays information about network I/O statistics that were caused by accessing files on a remote database instance.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| CLIENT | VARCHAR2(32) |  |
| READS# | NUMBER |  |
| WRITES# | NUMBER |  |
| KBYTES_READ | NUMBER |  |
| KBYTES_WRITTEN | NUMBER |  |
| READ_LATENCY | NUMBER |  |
| WRITE_LATENCY | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content