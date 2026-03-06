---
id: 19c__AUDIT_ACTIONS
name: AUDIT_ACTIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
source_file: AUDIT_ACTIONS.html
---

# AUDIT_ACTIONS

AUDIT_ACTIONS describes audit trail action type codes. This table can be used to map action type numbers to action type names.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ACTION | NUMBER | Numeric audit trail action type code. |
| NAME | VARCHAR2(28) | Name of the type of audit trail action |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: The mapping explained in this view is valid for audit trail records from the following views only, and such audit records are generated only when unified auditing is not enabled: DBA_AUDIT_TRAIL DBA_COMMON_AUDIT_TRAIL DBA_FGA_AUDIT_TRAIL USER_AUDIT_TRAIL V$XML_AUDIT_TRAIL See Also: Oracle Database Security Guide for more information about unified auditing. Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: The mapping explained in this view is valid for audit trail records from the following views only, and such audit records are generated only when unified auditing is not enabled: DBA_AUDIT_TRAIL DBA_COMMON_AUDIT_TRAIL DBA_FGA_AUDIT_TRAIL USER_AUDIT_TRAIL V$XML_AUDIT_TRAIL See Also: Oracle Database Security Guide for more information about unified auditing. Oracle Database Upgrade Guide for more information about migrating to unified auditing.