---
id: 19c__DBA_XS_ENABLED_AUDIT_POLICIES
name: DBA_XS_ENABLED_AUDIT_POLICIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [dba]
source_file: DBA_XS_ENABLED_AUDIT_POLICIES.html
---

# DBA_XS_ENABLED_AUDIT_POLICIES

DBA_XS_ENABLED_AUDIT_POLICIES describes all the audit policies specific to Oracle Database Real Application Security that are enabled to users.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| POLICY_NAME | VARCHAR2(128) | Name of the audit policy |
| ENABLED_OPTION | VARCHAR2(15) | Enabled option of the audit policy. Possible values: BY USER : For policies that are enabled on users EXCEPT USERS : For policies that are enabled on users BY GRANTED ROLE : For policies that are enabled on roles INVALID : For policies that are enabled on roles |
| ENTITY_NAME | VARCHAR2(128) | Database entity (user name or role name) on which the audit policy is enabled |
| ENTITY_TYPE | VARCHAR2(7) | Database entity type. Possible values: USER : Indicates that the policy is enabled on a user or users. ROLE : Indicates that the policy is enabled on a role or roles. |
| SUCCESS | VARCHAR2(3) | Indicates whether the audit policy is enabled for auditing successful events ( YES ) or not ( NO ) |
| FAILURE | VARCHAR2(3) | Indicates whether the audit policy is enabled for auditing unsuccessful events ( YES ) or not ( NO ) |

## Usage Notes

Note: This view was known as DBA_XS_ENB_AUDIT_POLICIES in Oracle Database 12 c Release 1. It was renamed to DBA_XS_ENABLED_AUDIT_POLICIES in Oracle Database 12 c Release 2 (12.2.0.1). Note: This view was known as DBA_XS_ENB_AUDIT_POLICIES in Oracle Database 12 c Release 1. It was renamed to DBA_XS_ENABLED_AUDIT_POLICIES in Oracle Database 12 c Release 2 (12.2.0.1). See Also: Oracle Database Security Guide for more information about auditing See Also: Oracle Database Security Guide for more information about auditing