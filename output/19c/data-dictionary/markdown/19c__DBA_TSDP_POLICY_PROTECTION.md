---
id: 19c__DBA_TSDP_POLICY_PROTECTION
name: DBA_TSDP_POLICY_PROTECTION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_TSDP_POLICY_PROTECTION.html
---

# DBA_TSDP_POLICY_PROTECTION

DBA_TSDP_POLICY_PROTECTION shows the list of columns that have been protected through Transparent Sensitive Data Protection.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SCHEMA_NAME | VARCHAR2(128) | The schema containing the sensitive data |
| TABLE_NAME | VARCHAR2(128) | The table containing the sensitive column |
| COLUMN_NAME | VARCHAR2(128) | The name of the sensitive column |
| TSDP_POLICY | VARCHAR2(128) | The TSDP policy name based on which the column protection was enabled |
| SECURITY_FEATURE | VARCHAR2(12) | The security feature enabled on the sensitive column |
| SECURITY_FEATURE_POLICY | VARCHAR2(128) | Name of the underlying Oracle security feature policy |
| SUBPOLICY# | NUMBER | The subpolicy of the Transparent Sensitive Data Protection policy based on which protection has been enabled |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection