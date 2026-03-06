---
id: 19c__V$ASM_VOLUME
name: V$ASM_VOLUME
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dynamic_performance]
source_file: V-ASM_VOLUME.html
---

# V$ASM_VOLUME

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_VOLUME displays information about each Oracle ADVM volume.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GROUP_NUMBER | NUMBER |  |
| VOLUME_NAME | VARCHAR2(30) |  |
| COMPOUND_INDEX | NUMBER |  |
| SIZE_MB | NUMBER |  |
| VOLUME_NUMBER | NUMBER |  |
| REDUNDANCY | VARCHAR2(6) |  |
| STRIPE_COLUMNS | NUMBER |  |
| STRIPE_WIDTH_K | NUMBER |  |
| STATE | VARCHAR2(8) |  |
| FILE_NUMBER | NUMBER |  |
| INCARNATION | NUMBER |  |
| DRL_FILE_NUMBER | NUMBER |  |
| RESIZE_UNIT_MB | NUMBER |  |
| USAGE | VARCHAR2(30) |  |
| VOLUME_DEVICE | VARCHAR2(256) |  |
| MOUNTPATH | VARCHAR2(1024) |  |
| PRIMARY_REGION | VARCHAR2(4) |  |
| MIRROR_REGION | VARCHAR2(4) |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information