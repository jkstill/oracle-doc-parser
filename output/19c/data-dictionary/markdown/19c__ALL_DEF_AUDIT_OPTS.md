---
id: 19c__ALL_DEF_AUDIT_OPTS
name: ALL_DEF_AUDIT_OPTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [all]
source_file: ALL_DEF_AUDIT_OPTS.html
---

# ALL_DEF_AUDIT_OPTS

ALL_DEF_AUDIT_OPTS contains default object-auditing options that will be applied when objects are created.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ALT | VARCHAR2(3) | Auditing ALTER WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| AUD | VARCHAR2(3) | Auditing AUDIT WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| COM | VARCHAR2(3) | Auditing COMMENT WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| DEL | VARCHAR2(3) | Auditing DELETE WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| GRA | VARCHAR2(3) | Auditing GRANT WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| IND | VARCHAR2(3) | Auditing INDEX WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| INS | VARCHAR2(3) | Auditing INSERT WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| LOC | VARCHAR2(3) | Auditing LOCK WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| REN | VARCHAR2(3) | Auditing RENAME WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| SEL | VARCHAR2(3) | Auditing SELECT WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| UPD | VARCHAR2(3) | Auditing UPDATE WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| EXE | VARCHAR2(3) | Auditing EXECUTE WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| FBK | VARCHAR2(3) | Auditing FLASHBACK WHENEVER SUCCESSFUL / UNSUCCESSFUL |
| REA | VARCHAR2(3) | Auditing READ WHENEVER SUCCESSFUL / UNSUCCESSFUL |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content The output for each column takes one of the following forms: -/- : no default auditing S/- : auditing whenever successful -/S : auditing whenever not successful Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated only in an Oracle Database where unified auditing is not enabled. When unified auditing is enabled in Oracle Database, the audit records are populated in the new audit trail and can be viewed from UNIFIED_AUDIT_TRAIL . See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing.