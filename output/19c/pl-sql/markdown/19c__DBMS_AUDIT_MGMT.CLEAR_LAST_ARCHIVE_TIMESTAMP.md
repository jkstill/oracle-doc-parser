---
id: 19c__DBMS_AUDIT_MGMT.CLEAR_LAST_ARCHIVE_TIMESTAMP
name: DBMS_AUDIT_MGMT.CLEAR_LAST_ARCHIVE_TIMESTAMP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUDIT_MGMT
tags: [dbms_audit_mgmt]
source_file: DBMS_AUDIT_MGMT.html
---

# DBMS_AUDIT_MGMT.CLEAR_LAST_ARCHIVE_TIMESTAMP

This procedure clears the timestamp set by the SET_LAST_ARCHIVE_TIMESTAMP Procedure.

## Syntax

```sql
DBMS_AUDIT_MGMT.CLEAR_LAST_ARCHIVE_TIMESTAMP(
   audit_trail_type         IN PLS_INTEGER,
   rac_instance_number      IN PLS_INTEGER DEFAULT NULL,
   container                IN PLS_INTEGER DEFAULT CONTAINER_CURRENT,
   database_id              IN NUMBER DEFAULT NULL,
   container_guid           IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| audit_trail_type | PLS_INTEGER | IN | The audit trail type for which the timestamp needs to be cleared. Audit trail types are listed in Table 27-1 . |
| rac_instance_number | PLS_INTEGER | IN | The instance number for the Oracle Real Application Clusters (Oracle RAC) instance. The default value is NULL . The rac_instance_number is not relevant for single instance databases. You can find the instance number by issuing the SHOW PARAMETER INSTANCE_NUMBER command in SQL*Plus. |
| container | PLS_INTEGER | IN | Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this clears the last archive timestamp from all the PDBs, otherwise it clears from only the connected PDB. |
| database_id | NUMBER | IN | Database ID (DBID) of the audit records to cleanup |
| container_guid | VARCHAR2 | IN | Container GUID of the audit records to cleanup Note: This parameter has been deprecated but is currently retained for backward compatibility. |

## Usage Notes

Syntax DBMS_AUDIT_MGMT.CLEAR_LAST_ARCHIVE_TIMESTAMP( audit_trail_type IN PLS_INTEGER, rac_instance_number IN PLS_INTEGER DEFAULT NULL, container IN PLS_INTEGER DEFAULT CONTAINER_CURRENT, database_id IN NUMBER DEFAULT NULL, container_guid IN VARCHAR2 DEFAULT NULL); Parameters Table 27-11 CLEAR_LAST_ARCHIVE_TIMESTAMP Procedure Parameters Parameter Description audit_trail_type The audit trail type for which the timestamp needs to be cleared. Audit trail types are listed in Table 27-1 . rac_instance_number The instance number for the Oracle Real Application Clusters (Oracle RAC) instance. The default value is NULL . The rac_instance_number is not relevant for single instance databases. You can find the instance number by issuing the SHOW PARAMETER INSTANCE_NUMBER command in SQL*Plus. container Values: CONTAINER_CURRENT for the connected pluggable database (PDB) or CONTAINER_ALL for all pluggable databases (PDBs). When CONTAINER is set to CONTAINER_ALL , this clears the last archive timestamp from all the PDBs, otherwise it clears from only the connected PDB. database_id Database ID (DBID) of the audit records to cleanup container_guid Container GUID of the audit records to cleanup Note: This parameter has been deprecated but is currently retained for backward compatibility. Usage Notes The following usage notes apply: The timestamp for only one audit_trail_type can be cleared at a time. The following are invalid audit_trail_type values for this procedure and cannot be used: AUDIT_TRAIL_ALL AUDIT_TRAIL_DB_STD AUDIT_TRAIL_FILES Examples The following example calls the CLEAR_LAST_ARCHIVE_TIMESTAMP procedure to clear the timestamp value for the operating system (OS) audit trail type. BEGIN DBMS_AUDIT_MGMT.CLEAR_LAST_ARCHIVE_TIMESTAMP( audit_trail_type => DBMS_AUDIT_MGMT.AUDIT_TRAIL_OS, rac_instance_number => 1); END;