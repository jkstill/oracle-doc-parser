---
id: 19c__AUDIT_UNIFIED_CONTEXTS
name: AUDIT_UNIFIED_CONTEXTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
source_file: AUDIT_UNIFIED_CONTEXTS.html
---

# AUDIT_UNIFIED_CONTEXTS

AUDIT_UNIFIED_CONTEXTS describes the application context's attributes, which are configured to be captured in the audit trail.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| NAMESPACE | VARCHAR2(128) | Application context namespace |
| ATTRIBUTE | VARCHAR2(128) | Application context attribute |
| USER_NAME | VARCHAR2(128) | Username of database user for whom the application context's attribute is confiured to be captured in the audit trail |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view is populated only in an Oracle Database where unified auditing is enabled. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is enabled. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing.