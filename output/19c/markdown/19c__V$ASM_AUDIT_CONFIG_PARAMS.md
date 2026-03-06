---
id: 19c__V$ASM_AUDIT_CONFIG_PARAMS
name: V$ASM_AUDIT_CONFIG_PARAMS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dynamic_performance]
source_file: V-ASM_AUDIT_CONFIG_PARAMS.html
---

# V$ASM_AUDIT_CONFIG_PARAMS

In an Oracle Automatic Storage Management (Oracle ASM) instance, V$ASM_AUDIT_CONFIG_PARAMS displays information about the currently configured audit trail properties that are used by the DBMS_AUDIT_MGMT package.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PARAMETER_NAME | VARCHAR2(64) |  |
| PARAMETER_VALUE | VARCHAR2(64) |  |
| AUDIT_TRAIL | VARCHAR2(64) |  |
| PARAMETER_UNIT Foot 1 | VARCHAR2(64) |  |
| CON_ID | NUMBER |  |

## Usage Notes

In a database instance, V$ASM_AUDIT_CONFIG_PARAMS displays no rows. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_AUDIT_MGMT package Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_AUDIT_MGMT package Oracle Automatic Storage Management Administrator's Guide for additional information about using views to display Oracle ASM information