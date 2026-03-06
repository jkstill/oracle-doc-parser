---
id: 19c__AUDIT_SYS_OPERATIONS
name: AUDIT_SYS_OPERATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
source_file: AUDIT_SYS_OPERATIONS.html
---

# AUDIT_SYS_OPERATIONS

AUDIT_SYS_OPERATIONS enables or disables the auditing of directly issued user SQL statements with SYS authorization. These include SQL statements directly issued by users when connected with the SYSASM , SYSBACKUP , SYSDBA , SYSDG , SYSKM , or SYSOPER privileges, as well as SQL statements that have been executed with SYS authorization using the PL/SQL package DBMS_SYS_SQL .

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. The audit records are written to the operating system's audit trail. The audit records will be written in XML format if the AUDIT_TRAIL initialization parameter is set to xml or xml, extended On UNIX platforms, if the AUDIT_SYSLOG_LEVEL parameter has also been set, then it overrides the AUDIT_TRAIL parameter and SYS audit records are written to the system audit log using the SYSLOG utility. In a CDB, the scope of the settings for this initialization parameter is the CDB. Although the audit trail is provided per PDB in a CDB, this initialization parameter cannot be configured for individual PDBs. Note: In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing.