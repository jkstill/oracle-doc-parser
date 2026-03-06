---
id: 19c__AUDIT_UNIFIED_POLICIES
name: AUDIT_UNIFIED_POLICIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
source_file: AUDIT_UNIFIED_POLICIES.html
---

# AUDIT_UNIFIED_POLICIES

AUDIT_UNIFIED_POLICIES describes all audit policies created in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| POLICY_NAME | VARCHAR2(128) | Name of the audit policy |
| AUDIT_CONDITION | VARCHAR2(4000) | Condition associated with the audit policy |
| CONDITION_EVAL_OPT | VARCHAR2(9) | Evaluation option associated with the audit policy's condition. The possible values are STATEMENT , SESSION , INSTANCE , and NONE . |
| AUDIT_OPTION | VARCHAR2(128) | Auditing option defined in the audit policy |
| AUDIT_OPTION_TYPE | VARCHAR2(18) | Type of the auditing option. Possible values: SYSTEM PRIVILEGE STANDARD ACTION SYSTEM ACTION XS ACTION OLS_ACTION DATAPUMP ACTION DIRECT LOAD ACTION DV ACTION INVALID OBJECT ACTION ROLE PRIVILEGE |
| OBJECT_SCHEMA | VARCHAR2(128) | Owner of the object, for an object-specific auditing option |
| OBJECT_NAME | VARCHAR2(128) | Name of the object, for an object-specific auditing option |
| OBJECT_TYPE | VARCHAR2(23) | Type of the object, for an object-specific auditing option |
| COMMON | VARCHAR2(3) | Indicates whether the audit policy is a common audit policy or local audit policy. The value is NULL for a non-CDB. For local audit policies, the value of the COMMON column is always NO . For a CDB common policy: If you query AUDIT_UNIFIED_POLICIES from the CDB root container, the value of the COMMON column will be YES and the value of the INHERITED column will be NO . If you query AUDIT_UNIFIED_POLICIES from any other container besides the CDB root container, the value of the COMMON column and the INHERITED column will be YES . For an application container common policy: If you query AUDIT_UNIFIED_POLICIES from the application root container, the value of the COMMON column will be YES and the value of the INHERITED column will be NO . If you query AUDIT_UNIFIED_POLICIES from any other container besides the application root container, the value of the COMMON column and the INHERITED column will be YES . |
| INHERITED | VARCHAR2(3) | Indicates whether the audit policy was inherited from another container ( YES ) or not ( NO ). This value is NULL for non-CDBs. |
| AUDIT_ONLY_TOPLEVEL Foot 1 | VARCHAR2(3) | Indicates whether the audit policy is defined to audit only top level SQL statements ( YES ) or both top level SQL statements and recursive SQL statements ( NO ) |
| ORACLE_SUPPLIED Foot 2 | VARCHAR2(3) | Indicates whether the audit policy is an Oracle-supplied policy ( YES ) or not ( NO ) Oracle-supplied policies are also called predefined policies. |

## Usage Notes

Note: This view is populated only in an Oracle Database where unified auditing is enabled. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is enabled. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing.