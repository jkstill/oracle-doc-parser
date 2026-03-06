---
id: 19c__DBA_TSDP_POLICY_PARAMETER
name: DBA_TSDP_POLICY_PARAMETER
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_TSDP_POLICY_PARAMETER.html
---

# DBA_TSDP_POLICY_PARAMETER

DBA_TSDP_POLICY_PARAMETER shows the parameter-value pairs for the condition of the Transparent Sensitive Data Protection policy.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| POLICY_NAME | VARCHAR2(128) | The name of the Transparent Sensitive Data Protection policy |
| SUB_POLICY | NUMBER | The sub policy of the Transparent Sensitive Data Protection policy |
| PARAMETER | VARCHAR2(128) | The parameter for the Transparent Sensitive Data Protection sub policy |
| VALUE | VARCHAR2(4000) | The value of the parameter |
| DEFAULT_OPTION | VARCHAR2(5) | Indicates whether this is the default option for the policy: TRUE : This is the default option for the policy FALSE : This is not the default option for the policy |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection