---
id: 19c__DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP
name: DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP

This procedure sets a timestamp indicating when the audit records were last archived. The audit administrator provides the timestamp to be attached to the audit records.

## Syntax

```sql
DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP(
   audit_trail_type         IN PLS_INTEGER,
   last_archive_time        IN TIMESTAMP,
   rac_instance_number      IN PLS_INTEGER DEFAULT NULL,
   container                IN PLS_INTEGER DEFAULT CONTAINER_CURRENT,
   database_id              IN NUMBER DEFAULT NULL,
   container_guid           IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for which the timestamp needs to be set. Audit trail types are listed in Table 27-1 . |
| last_archive_time | TIMESTAMP | IN | The TIMESTAMP value based on which the audit records or files should be deleted. This indicates the last time when the audit records or files were archived. |
| rac_instance_number | PLS_INTEGER | IN | The instance number for the Oracle Real Application Clusters (Oracle RAC) instance. The default value is NULL . The rac_instance_number parameter is not accepted when AUDIT_TRAIL_TYPE has values: audit_trail_all audit_trail_aud_std audit_trail_db_std audit_trail_fga_std audit_trail_unified Set rac_instance_number to 1 for a single-instance database. |
| container | PLS_INTEGER | IN | Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this sets the value for last archive timestamp in all the pluggable databases, otherwise it sets the value in the connected PDB only. |
| database_id | NUMBER | IN | Database ID (DBID) of the audit records to cleanup |
| container_guid | VARCHAR2 | IN | Container GUID of the audit records to cleanup Note: This parameter has been deprecated but is currently retained for backward compatibility. |

## Usage Notes

The CLEAN_AUDIT_TRAIL Procedure uses this timestamp to decide on the audit records to be deleted. Syntax DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP( audit_trail_type IN PLS_INTEGER, last_archive_time IN TIMESTAMP, rac_instance_number IN PLS_INTEGER DEFAULT NULL, container IN PLS_INTEGER DEFAULT CONTAINER_CURRENT, database_id IN NUMBER DEFAULT NULL, container_guid IN VARCHAR2 DEFAULT NULL); Parameters Table 27-24 SET_LAST_ARCHIVE_TIMESTAMP Procedure Parameters Parameter Description audit_trail_type The audit trail type for which the timestamp needs to be set. Audit trail types are listed in Table 27-1 . last_archive_time The TIMESTAMP value based on which the audit records or files should be deleted. This indicates the last time when the audit records or files were archived. rac_instance_number The instance number for the Oracle Real Application Clusters (Oracle RAC) instance. The default value is NULL . The rac_instance_number parameter is not accepted when AUDIT_TRAIL_TYPE has values: audit_trail_all audit_trail_aud_std audit_trail_db_std audit_trail_fga_std audit_trail_unified Set rac_instance_number to 1 for a single-instance database. container Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this sets the value for last archive timestamp in all the pluggable databases, otherwise it sets the value in the connected PDB only. database_id Database ID (DBID) of the audit records to cleanup container_guid Container GUID of the audit records to cleanup Note: This parameter has been deprecated but is currently retained for backward compatibility. Usage Notes The following usage notes apply: The last_archive_time must be specified in Coordinated Universal Time (UTC) when the audit trail types are AUDIT_TRAIL_AUD_STD , AUDIT_TRAIL_FGA_STD , or AUDIT_TRAIL_UNIFIED . This is because the database audit trails store the timestamps in UTC. UTC is also known as Greenwich Mean Time (GMT). The last_archive_time must be specified as the local time zone time when the audit trail types are AUDIT_TRAIL_OS or AUDIT_TRAIL_XML . The time zone must be the time zone of the machine where the OS or XML audit files were created. This is because the operating system audit files are cleaned based on the audit file's Last Modification Timestamp property. The Last Modification Timestamp property value is stored in the local time zone of the machine. When using an Oracle Real Application Clusters (Oracle RAC) database, Oracle recommends that you use the Network Time Protocol (NTP) to synchronize individual Oracle RAC nodes. Examples The following example calls the SET_LAST_ARCHIVE_TIMESTAMP procedure to set the last archive timestamp for the operating system (OS) audit trail type on Oracle RAC instance 1. It uses the TO_TIMESTAMP function to convert a character string into a timestamp value. A subsequent call to the CLEAN_AUDIT_TRAIL Procedure , with use_last_arch_timestamp set to TRUE , will delete all those OS audit files from the current AUDIT_FILE_DEST directory that were modified before 10-Sep-2012 14:10:10.0. BEGIN DBMS_AUDIT_MGMT.SET_LAST_ARCHIVE_TIMESTAMP( audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS, last_archive_time => TO_TIMESTAMP('12-SEP-0714:10:10.0','DD-MON-RRHH24:MI:SS.FF'), rac_instance_number => 1); END;