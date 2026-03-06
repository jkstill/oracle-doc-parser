---
id: 19c__DBA_AUDIT_MGMT_LAST_ARCH_TS
name: DBA_AUDIT_MGMT_LAST_ARCH_TS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
tags: [dba]
source_file: DBA_AUDIT_MGMT_LAST_ARCH_TS.html
---

# DBA_AUDIT_MGMT_LAST_ARCH_TS

DBA_AUDIT_MGMT_LAST_ARCH_TS displays information about the last archive timestamps set for audit trail cleanup or purges.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| AUDIT_TRAIL | VARCHAR2(20) | Audit trail for which the last archive timestamp applies: STANDARD AUDIT TRAIL FGA AUDIT TRAIL OS AUDIT TRAIL XML AUDIT TRAIL UNIFIED AUDIT TRAIL |
| RAC_INSTANCE | NUMBER | Oracle RAC instance number for which the last archive timestamp applies; 0 implies not applicable |
| LAST_ARCHIVE_TS | TIMESTAMP(6) WITH TIME ZONE | Timestamp of the last audit record or audit file that has been archived |
| DATABASE_ID | NUMBER | Database ID of the audit records to clean up |
| CONTAINER_GUID | VARCHAR2(33) | GUID of the container of the audit records to clean up |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: This view is populated in any Oracle Database where auditing is enabled, regardless of whether pre-Oracle Database 12 c auditing or unified auditing is enabled for the database. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: This view is populated in any Oracle Database where auditing is enabled, regardless of whether pre-Oracle Database 12 c auditing or unified auditing is enabled for the database. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: In a read-only database, including an Oracle Active Data Guard physical standby database, this view is not populated when DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP is invoked. In such a case, use DBMS_AUDIT_MGMT.GET_LAST_ARCHIVE_TIMESTAMP to check for the timestamp, if it was configured for the database instance. See Also: Oracle Database PL/SQL Packages and Types Reference for more information about DBMS_AUDIT_MGMT subprograms Note: In a read-only database, including an Oracle Active Data Guard physical standby database, this view is not populated when DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP is invoked. In such a case, use DBMS_AUDIT_MGMT.GET_LAST_ARCHIVE_TIMESTAMP to check for the timestamp, if it was configured for the database instance.