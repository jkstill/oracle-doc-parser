---
id: 19c__V$ASM_AUDIT_LAST_ARCH_TS
name: V$ASM_AUDIT_LAST_ARCH_TS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [dynamic_performance]
source_file: V-ASM_AUDIT_LAST_ARCH_TS.html
---

# V$ASM_AUDIT_LAST_ARCH_TS

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_AUDIT_LAST_ARCH_TS displays information about the last archive timestamps set for audit trail cleanup or purges.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AUDIT_TRAIL | VARCHAR2(64) |  |
| LAST_ARCHIVE_TS | TIMESTAMP(6) WITH TIME ZONE |  |
| CON_ID | NUMBER |  |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content In a database instance, V$ASM_AUDIT_LAST_ARCH_TS displays no rows. See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information