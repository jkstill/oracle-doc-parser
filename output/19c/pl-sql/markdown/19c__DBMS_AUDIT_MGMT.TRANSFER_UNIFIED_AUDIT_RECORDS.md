---
id: 19c__DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS
name: DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS

This procedure transfers unified audit records that were in a pre-upgraded Oracle database to an internal relational table that is designed to improve read performance.

## Syntax

```sql
DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS (
   container_guid       IN VARCHAR2   DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| container_guid | VARCHAR2 | IN | The GUID of the container of the associated CLI back-end table. This back-end table contains the audit records from the pre-upgraded Oracle database. If you omit this setting, then the GUID of the current container is used. |

## Usage Notes

Syntax In the pre-upgraded Oracle database, these records resided in the common logging infrastructure (CLI) SGA back-end tables. DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS ( container_guid IN VARCHAR2 DEFAULT NULL); Parameters Table 27-27 TRANSFER_UNIFIED_AUDIT_RECORDS Procedure Parameters Parameter Description container_guid The GUID of the container of the associated CLI back-end table. This back-end table contains the audit records from the pre-upgraded Oracle database. If you omit this setting, then the GUID of the current container is used. Usage Notes It is not mandatory to run DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS after an upgrade, but for better read performance of the unified audit trail, Oracle highly recommends that you run this procedure. The DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS is designed to be a one-time operation, to be performed after you upgrade from Oracle Database 12 c release 12.1. There is one CLI back-end table per GUID of the container. You can find the GUIDs for containers by querying the PDB_GUID column of the DBA_PDB_HISTORY data dictionary view. Execute the DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS procedure by passing each of these GUIDs one by one to ensure that you move the unified audit records from these CLI back-end tables to the AUDSYS.AUD$UNIFIED table. In a multitenant environment, you must run the DBMS_AUDIT_MGMT.TRANSFER_UNIFIED_AUDIT_RECORDS procedure only in the container to which the transfer operation applies, whether it is the root or an individual PDB. You cannot run this procedure in the root, for example, to transfer audit records in a PDB. If you have a high rate of audit record generation and your database supports partitioning, then you may want to use the DBMS_AUDIT_MGMT.ALTER_PARTITION_INTERVAL procedure to alter the partition interval setting for the internal relational table. See ALTER_PARTITION_INTERVAL Procedure for more information.