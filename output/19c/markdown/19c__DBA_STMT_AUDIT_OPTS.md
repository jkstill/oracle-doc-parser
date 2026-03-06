---
id: 19c__DBA_STMT_AUDIT_OPTS
name: DBA_STMT_AUDIT_OPTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [dba]
source_file: DBA_STMT_AUDIT_OPTS.html
---

# DBA_STMT_AUDIT_OPTS

DBA_STMT_AUDIT_OPTS describes current system auditing options across the system and by user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USER_NAME | VARCHAR2(128) | User name if by user auditing; ANY CLIENT if access by a proxy on behalf of a client is being audited; NULL for system-wide auditing |
| PROXY_NAME | VARCHAR2(128) | Name of the proxy user which is performing an operation for the client; NULL if the client is performing the operation directly |
| AUDIT_OPTION | VARCHAR2(40) | Name of the system auditing option |
| SUCCESS | VARCHAR2(10) | Mode for WHENEVER SUCCESSFUL system auditing |
| FAILURE | VARCHAR2(10) | Mode for WHENEVER NOT SUCCESSFUL system auditing |

## Usage Notes

Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing.