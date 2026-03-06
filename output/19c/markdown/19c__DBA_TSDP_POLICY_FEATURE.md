---
id: 19c__DBA_TSDP_POLICY_FEATURE
name: DBA_TSDP_POLICY_FEATURE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_TSDP_POLICY_FEATURE.html
---

# DBA_TSDP_POLICY_FEATURE

DBA_TSDP_POLICY_FEATURE shows the Transparent Sensitive Data Protection policy security feature mapping for all the TSDP policies in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| POLICY_NAME | VARCHAR2(128) | The name of the Transparent Sensitive Data Protection policy |
| SECURITY_FEATURE | VARCHAR2(12) | The Oracle security feature with which the Transparent Sensitive Data Protection policy is associated |

## Usage Notes

At this time, only Oracle Data Redaction is supported. See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection