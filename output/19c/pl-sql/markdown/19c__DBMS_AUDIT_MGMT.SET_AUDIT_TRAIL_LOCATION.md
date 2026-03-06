---
id: 19c__DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION
name: DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION

This procedure moves the audit trail tables from their current tablespace to a user-specified tablespace.

## Syntax

```sql
DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION(
   audit_trail_type            IN PLS_INTEGER,
   audit_trail_location_value  IN VARCHAR2) ;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for which the audit trail location needs to be set. Audit trail types are listed in Table 27-1 |
| audit_trail_location_value | VARCHAR2) | IN | Target location or tablespace for the audit trail records |

## Usage Notes

The SET_AUDIT_TRAIL_LOCATION procedure is not relevant for the AUDIT_TRAIL_OS , AUDIT_TRAIL_XML , and AUDIT_TRAIL_FILES audit trail types. The AUDIT_FILE_DEST initialization parameter is the only way you can specify the destination directory for these audit trail types. See Also: Table 27-1 for a list of all audit trail types AUDIT_FILE_DEST in the Oracle Database Reference See Also: Table 27-1 for a list of all audit trail types AUDIT_FILE_DEST in the Oracle Database Reference Syntax DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION( audit_trail_type IN PLS_INTEGER, audit_trail_location_value IN VARCHAR2) ; Parameters Table 27-22 SET_AUDIT_TRAIL_LOCATION Procedure Parameters Parameter Description audit_trail_type The audit trail type for which the audit trail location needs to be set. Audit trail types are listed in Table 27-1 audit_trail_location_value Target location or tablespace for the audit trail records Usage Notes The following usage notes apply: By default, audit trail records are written to the SYSAUX tablespace. You can change the tablespace location to a user tablespace using this procedure. However the designated tablespace must be an automatic storage space management (ASSM) tablespace. This procedure is valid for the following audit_trail_type values: AUDIT_TRAIL_AUD_STD AUDIT_TRAIL_FGA_STD AUDIT_TRAIL_DB_STD AUDIT_TRAIL_UNIFIED For the audit_trail_type values AUDIT_TRAIL_AUD_STD , AUDIT_TRAIL_FGA_STD , and AUDIT_TRAIL_DB_STD , you should ensure that the target tablespace, into which the audit trail tables are being moved, has sufficient space to accommodate the audit trail tables. You should also optimize the target tablespace for frequent write operations. This procedure involves data movement across tablespaces. For the audit_trail_type values AUDIT_TRAIL_AUD_STD , AUDIT_TRAIL_FGA_STD , and AUDIT_TRAIL_DB_STD , this can be a resource intensive operation especially if your database audit trail tables are already populated. Oracle recommends that you invoke the procedure during non-peak hours. You optionally can specify an encrypted tablespace for the audit trail location. When AUDIT_TRAIL_TYPE is AUDIT_TRAIL_UNIFIED , this procedure sets the tablespace for newer audit records in the unified audit trail but does not move the older audit records. Thus, it is not resource intensive for the unified audit trail. The UNIFIED_AUDIT_TRAIL data dictionary view is built on top of an internal relational table. This table is an interval partitioned table (irrespective of database editions) with a default interval of 1 month. This setting means that when you execute the DBMS_AUDIT_MGMT.SET_AUDIT_TRAIL_LOCATION procedure, only newly created partitions of the internal table are created in the new tablespace that is set as part of this procedure. Existing partitions of this table remain in the earlier tablespace ( SYSAUX is the default tablespace for this internal table). If you want to change this table’s partition interval, then use the DBMS_AUDIT_MGMT.ALTER_PARTITION_INTERVAL procedure.