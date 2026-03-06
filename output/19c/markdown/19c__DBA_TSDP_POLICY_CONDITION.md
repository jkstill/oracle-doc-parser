---
id: 19c__DBA_TSDP_POLICY_CONDITION
name: DBA_TSDP_POLICY_CONDITION
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_TSDP_POLICY_CONDITION.html
---

# DBA_TSDP_POLICY_CONDITION

DBA_TSDP_POLICY_CONDITION describes the Transparent Sensitive Data Protection policy and condition mapping. It also lists the property-value pairs for the condition.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| POLICY_NAME | VARCHAR2(128) | The name of the Transparent Sensitive Data Protection policy |
| SUB_POLICY | NUMBER | The sub policy of the Transparent Sensitive Data Protection policy |
| PROPERTY | VARCHAR2(11) | The condition property. Possible values: DATATYPE LENGTH SCHEMA_NAME TABLE_NAME |
| VALUE | VARCHAR2(128) | The value of the condition property |

## Usage Notes

See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection