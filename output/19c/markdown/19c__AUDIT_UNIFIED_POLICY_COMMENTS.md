---
id: 19c__AUDIT_UNIFIED_POLICY_COMMENTS
name: AUDIT_UNIFIED_POLICY_COMMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
source_file: AUDIT_UNIFIED_POLICY_COMMENTS.html
---

# AUDIT_UNIFIED_POLICY_COMMENTS

AUDIT_UNIFIED_POLICY_COMMENTS shows the description of each unified audit policy, if a description was entered for the unified audit policy using the COMMENT SQL statement.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| POLICY_NAME | VARCHAR2(128) | Name of the unified audit policy |
| COMMENTS | VARCHAR2(4000) | Description of the unified audit policy, if one was entered using the COMMENT SQL statement |

## Usage Notes

Note: This view is populated only in an Oracle Database where unified auditing is enabled. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is enabled. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing.