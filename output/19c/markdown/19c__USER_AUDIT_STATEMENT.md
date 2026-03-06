---
id: 19c__USER_AUDIT_STATEMENT
name: USER_AUDIT_STATEMENT
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_AUDIT_STATEMENT.html
---

# USER_AUDIT_STATEMENT

USER_AUDIT_STATEMENT displays audit trail entries for the GRANT , REVOKE , AUDIT , NOAUDIT , and ALTER SYSTEM statements issued by the current user.

## Usage Notes

Its columns are the same as those in " DBA_AUDIT_STATEMENT " . Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing.