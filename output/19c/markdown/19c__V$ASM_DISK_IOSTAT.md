---
id: 19c__V$ASM_DISK_IOSTAT
name: V$ASM_DISK_IOSTAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ASM_DISK_IOSTAT.html
---

# V$ASM_DISK_IOSTAT

V$ASM_DISK_IOSTAT displays information about disk I/O statistics for each Oracle Automatic Storage Management (Oracle ASM) client.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| INSTNAME | VARCHAR2(64) |  |
| DBNAME | VARCHAR2(8) |  |
| CLUSTERNAME | VARCHAR2(31) |  |
| GROUP_NUMBER | NUMBER |  |
| DISK_NUMBER | NUMBER |  |
| FAILGROUP | VARCHAR2(30) |  |
| SITE_NAME | VARCHAR2(30) |  |
| READS | NUMBER |  |
| WRITES | NUMBER |  |
| READ_ERRS | NUMBER |  |
| WRITE_ERRS | NUMBER |  |
| READ_TIMEOUT | NUMBER |  |
| WRITE_TIMEOUT | NUMBER |  |
| READ_TIME | NUMBER |  |
| WRITE_TIME | NUMBER |  |
| BYTES_READ | NUMBER |  |
| BYTES_WRITTEN | NUMBER |  |
| HOT_READS | NUMBER |  |
| HOT_WRITES | NUMBER |  |
| HOT_BYTES_READ | NUMBER |  |
| HOT_BYTES_WRITTEN | NUMBER |  |
| COLD_READS | NUMBER |  |
| COLD_WRITES | NUMBER |  |
| COLD_BYTES_READ | NUMBER |  |
| COLD_BYTES_WRITTEN | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

If this view is queried from the database instance, only the rows for that instance are shown. See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information