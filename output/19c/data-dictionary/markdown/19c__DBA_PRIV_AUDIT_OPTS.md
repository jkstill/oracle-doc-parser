---
id: 19c__DBA_PRIV_AUDIT_OPTS
name: DBA_PRIV_AUDIT_OPTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_PRIV_AUDIT_OPTS.html
---

# DBA_PRIV_AUDIT_OPTS

DBA_PRIV_AUDIT_OPTS describes current system privileges being audited across the system and by user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USER_NAME | VARCHAR2(128) | User name if by user auditing; ANY CLIENT if access by a proxy on behalf of a client is being audited; NULL for systemwide auditing |
| PROXY_NAME | VARCHAR2(128) | Name of the proxy user which is performing an operation for the client; NULL if the client is performing the operation directly |
| PRIVILEGE | VARCHAR2(40) | Name of the system privilege being audited |
| SUCCESS | VARCHAR2(10) | Mode for WHENEVER SUCCESSFUL system auditing |
| FAILURE | VARCHAR2(10) | Mode for WHENEVER NOT SUCCESSFUL system auditing |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing.