---
id: 19c__V$ASM_VOLUME_STAT
name: V$ASM_VOLUME_STAT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-ASM_VOLUME_STAT.html
---

# V$ASM_VOLUME_STAT

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_VOLUME_STAT displays information about statistics for each Oracle ADVM volume.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| VOLUME_NAME | VARCHAR2(30) |  |
| COMPOUND_INDEX | NUMBER |  |
| VOLUME_NUMBER | NUMBER |  |
| READS | NUMBER |  |
| WRITES | NUMBER |  |
| READ_ERRS | NUMBER |  |
| WRITE_ERRS | NUMBER |  |
| READ_TIME | NUMBER |  |
| WRITE_TIME | NUMBER |  |
| BYTES_READ | NUMBER |  |
| BYTES_WRITTEN | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information