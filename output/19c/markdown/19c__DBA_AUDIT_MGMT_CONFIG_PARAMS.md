---
id: 19c__DBA_AUDIT_MGMT_CONFIG_PARAMS
name: DBA_AUDIT_MGMT_CONFIG_PARAMS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: configuration
tags: [dba]
source_file: DBA_AUDIT_MGMT_CONFIG_PARAMS.html
---

# DBA_AUDIT_MGMT_CONFIG_PARAMS

DBA_AUDIT_MGMT_CONFIG_PARAMS displays information about the currently configured audit trail properties that are used by the DBMS_AUDIT_MGMT PL/SQL package.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PARAMETER_NAME | VARCHAR2(1024) | Name of the property |
| PARAMETER_VALUE | VARCHAR2(4000) | Value of the property |
| AUDIT_TRAIL | VARCHAR2(28) | Audit trails for which the property is configured: STANDARD AUDIT TRAIL FGA AUDIT TRAIL STANDARD AND FGA AUDIT TRAIL OS AUDIT TRAIL XML AUDIT TRAIL OS AND XML AUDIT TRAIL ALL AUDIT TRAILS UNIFIED AUDIT TRAIL |

## Usage Notes

Note: This view is populated in any Oracle Database where auditing is enabled, regardless of whether pre-Oracle Database 12 c auditing or unified auditing is enabled for the database. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated in any Oracle Database where auditing is enabled, regardless of whether pre-Oracle Database 12 c auditing or unified auditing is enabled for the database. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: In a read-only database, including an Oracle Active Data Guard physical standby database, this view is not populated when the DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL PL/SQL procedure is invoked. If the procedure was used when the database was in read-only mode, use DBMS_AUDIT_MGMT.GET_AUDIT_TRAIL to check the value of the property. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the parameters specified with the DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_PROPERTY procedure Note: In a read-only database, including an Oracle Active Data Guard physical standby database, this view is not populated when the DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL PL/SQL procedure is invoked. If the procedure was used when the database was in read-only mode, use DBMS_AUDIT_MGMT.GET_AUDIT_TRAIL to check the value of the property. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about the parameters specified with the DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_PROPERTY procedure