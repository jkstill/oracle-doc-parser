---
id: 19c__ALL_UNIFIED_AUDIT_ACTIONS
name: ALL_UNIFIED_AUDIT_ACTIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [all]
source_file: ALL_UNIFIED_AUDIT_ACTIONS.html
---

# ALL_UNIFIED_AUDIT_ACTIONS

ALL_UNIFIED_AUDIT_ACTIONS describes unified audit trail actions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| TYPE | NUMBER | Numeric component type for system wide actions |
| COMPONENT | VARCHAR2(64) | Name of component for system wide actions |
| ACTION | NUMBER | Numeric auditable action code for system wide actions Note: The action code values have changed from Oracle Database release 12.2 to the current release. If your applications have queries that include the ACTION column, and if these queries were written in release 12.2, then be aware that the output may be different if you are running these queries in the current release. |
| NAME | VARCHAR2(64) | Name of auditable action |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The actions described in this view are valid for audit trail records from the UNIFIED_AUDIT_TRAIL view. Such records are generated only when unified auditing is enabled. See Also: Oracle Database Security Guide for more information about unified auditing. Oracle Database Upgrade Guide for more information about migrating to unified auditing. See Also: Oracle Database Security Guide for more information about unified auditing. Oracle Database Upgrade Guide for more information about migrating to unified auditing. See Also: " UNIFIED_AUDIT_TRAIL " See Also: " UNIFIED_AUDIT_TRAIL "