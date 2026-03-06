---
id: 19c__DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL
name: DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL

This procedure deletes audit trail records.

## Syntax

```sql
DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL(
   audit_trail_type         IN PLS_INTEGER,
   use_last_arch_timestamp  IN BOOLEAN DEFAULT TRUE,
   container                IN PLS_INTEGER DEFAULT CONTAINER_CURRENT,
   database_id              IN NUMBER DEFAULT NULL,
   container_guid           IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for which the cleanup operation needs to be performed. Audit trail types are listed in Table 27-1 . |
| use_last_arch_timestamp | BOOLEAN | IN | Specifies whether the last archived timestamp should be used for deciding on the records that should be deleted. A value of TRUE indicates that only audit records created before the last archive timestamp should be deleted. A value of FALSE indicates that all audit records should be deleted. The default value is TRUE . Oracle recommends using this value, as this helps guard against inadvertent deletion of records. |
| container | PLS_INTEGER | IN | Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this purges the audit trail in all the PDBs, otherwise it only purges from the connected PDB. |
| database_id | NUMBER | IN | Database ID (DBID) of the audit records to cleanup |
| container_guid | VARCHAR2 | IN | Container GUID of the audit records to cleanup Note: This parameter has been deprecated but is currently retained for backward compatibility. |

## Usage Notes

The CLEAN_AUDIT_TRAIL procedure is usually called after the SET_LAST_ARCHIVE_TIMESTAMP Procedure has been used to set the last archived timestamp for the audit records. Syntax DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL( audit_trail_type IN PLS_INTEGER, use_last_arch_timestamp IN BOOLEAN DEFAULT TRUE, container IN PLS_INTEGER DEFAULT CONTAINER_CURRENT, database_id IN NUMBER DEFAULT NULL, container_guid IN VARCHAR2 DEFAULT NULL); Parameters Table 27-9 CLEAN_AUDIT_TRAIL Procedure Parameters Parameter Description audit_trail_type The audit trail type for which the cleanup operation needs to be performed. Audit trail types are listed in Table 27-1 . use_last_arch_timestamp Specifies whether the last archived timestamp should be used for deciding on the records that should be deleted. A value of TRUE indicates that only audit records created before the last archive timestamp should be deleted. A value of FALSE indicates that all audit records should be deleted. The default value is TRUE . Oracle recommends using this value, as this helps guard against inadvertent deletion of records. container Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this purges the audit trail in all the PDBs, otherwise it only purges from the connected PDB. database_id Database ID (DBID) of the audit records to cleanup container_guid Container GUID of the audit records to cleanup Note: This parameter has been deprecated but is currently retained for backward compatibility. Usage Notes The following usage notes apply: When cleaning up operating system (OS) or XML audit files, only files in the current audit directory, specified by the AUDIT_FILE_DEST parameter, are cleaned up. For Windows platforms, no cleanup is performed when the audit_trail_type parameter is set to DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS. This is because operating system (OS) audit records on Windows are written to the Windows Event Viewer. For Unix platforms, no cleanup is performed for cases where the operating system (OS) audit records are written to the syslog. When the audit_trail_type parameter is set to DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS, it removes only the *.aud files under the directory specified by the AUDIT_FILE_DEST initialization parameter. See Also: "AUDIT_SYSLOG_LEVEL" in the Oracle Database Reference When the audit_trail_type parameter is set to DBMS_AUDIT_MGMT.AUDIT_TRAIL_XML, this procedure only removes XML audit files ( *.xml ) from the current audit directory. Oracle database maintains a book-keeping file (adx_ $ORACLE_SID .txt ) for the XML audit files. This file is not removed by the cleanup procedure. If the cleanup of the unified audit trail is performed when the use_last_arch_timestamp parameter is set to TRUE : If you set the database_id value for the cleanup operation, then this value is used with the last archive timestamp while CLEAN_AUDIT_TRAIL runs. However, for the unified audit records that are present during the cleanup of spillover operating system audit files, the database_id value is ignored. Cleanup for operating system audit files is based on the last archive timestamp only. If you want to have the database_id value used for the cleanup operation of unified audit trail records that are present in the spillover operating system audit files, then load the contents of these files into database tables by using the DBMS_AUDIT_MGMT.LOAD_UNIFIED_AUDIT_FILES procedure before you run DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL . If you do not set the database_id value for the cleanup operation, then CLEAN_AUDIT_TRAIL uses the database ID of the current database container. This ID is used along with the last archive timestamp value while cleaning up the unified audit records that are present in the database tables. However, for unified audit records that are present in the spillover operating system audit records, this database ID is not used and cleanup of these records is based on the last archive timestamp value only. If you want to include the database ID value in the cleanup of unified audit records that are present in the spillover operating system audit files, then load the contents of these files by using the DBMS_AUDIT_MGMT.LOAD_UNIFIED_AUDIT_FILES procedure before you run DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL . If the cleanup of the unified audit trail is performed when the use_last_arch_timestamp parameter is set to FALSE : If you set the database_id value for the cleanup operation, then this value is used while CLEAN_AUDIT_TRAIL cleans up the unified audit trail records that are present in database tables. However, the database_id value is not used for the cleanup of unified audit trail records that are present in spillover operating system files. If want the database_id value to be used in the CLEAN_AUDIT_TRAIL operation of unified audit records that are present in spillover operating system audit files, then load the contents of these files to the database tables by using the DBMS_AUDIT_MGMT.LOAD_UNIFIED_AUDIT_FILES procedure before you run DBMS_AUDIT_MGMT.CLEAN_AUDIT_TRAIL . If you do not set the database_id value when you invoke the CLEAN_AUDIT_TRAIL procedure, then Oracle Database purges all unified audit records irrespective of database_id values and irrespective of the location (that is, database tables or spillover operating system audit files) where the unified audit records reside. See Also: "AUDIT_SYSLOG_LEVEL" in the Oracle Database Reference