---
id: 19c__ALL_AUDIT_POLICY_COLUMNS
name: ALL_AUDIT_POLICY_COLUMNS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: tables
tags: [all]
source_file: ALL_AUDIT_POLICY_COLUMNS.html
---

# ALL_AUDIT_POLICY_COLUMNS

ALL_AUDIT_POLICY_COLUMNS describes the fine-grained auditing policy columns on the tables and views accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OBJECT_SCHEMA | VARCHAR2(128) | Owner of the table or view |
| OBJECT_NAME | VARCHAR2(128) | Name of the table or view |
| POLICY_NAME | VARCHAR2(128) | Name of the policy |
| POLICY_COLUMN | VARCHAR2(128) | Relevant column of the policy |

## Usage Notes

Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Related Views DBA_AUDIT_POLICY_COLUMNS describes all fine-grained auditing policy columns in the database. USER_AUDIT_POLICY_COLUMNS describes the fine-grained auditing policy columns on the tables and views owned by the current user. See Also: " DBA_AUDIT_POLICY_COLUMNS " " USER_AUDIT_POLICY_COLUMNS "