---
id: 19c__V$ASM_AUDIT_CLEANUP_JOBS
name: V$ASM_AUDIT_CLEANUP_JOBS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [dynamic_performance]
source_file: V-ASM_AUDIT_CLEANUP_JOBS.html
---

# V$ASM_AUDIT_CLEANUP_JOBS

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_AUDIT_CLEANUP_JOBS displays information about the configured audit trail purge jobs.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| JOB_NAME | VARCHAR2(64) |  |
| JOB_STATUS | VARCHAR2(64) |  |
| AUDIT_TRAIL | VARCHAR2(64) |  |
| JOB_FREQUENCY | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

In a database instance, V$ASM_AUDIT_CLEANUP_JOBS displays no rows. See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information