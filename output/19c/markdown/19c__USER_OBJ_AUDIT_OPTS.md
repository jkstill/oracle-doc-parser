---
id: 19c__USER_OBJ_AUDIT_OPTS
name: USER_OBJ_AUDIT_OPTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_OBJ_AUDIT_OPTS.html
---

# USER_OBJ_AUDIT_OPTS

USER_OBJ_AUDIT_OPTS describes auditing options on all objects owned by the current user. Its columns (except for OWNER ) are the same as those in DBA_OBJ_AUDIT_OPTS .

## Usage Notes

Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. See Also: " DBA_OBJ_AUDIT_OPTS " Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. See Also: " DBA_OBJ_AUDIT_OPTS "