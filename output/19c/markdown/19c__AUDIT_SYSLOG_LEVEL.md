---
id: 19c__AUDIT_SYSLOG_LEVEL
name: AUDIT_SYSLOG_LEVEL
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: logging
source_file: AUDIT_SYSLOG_LEVEL.html
---

# AUDIT_SYSLOG_LEVEL

AUDIT_SYSLOG_LEVEL allows SYS and standard OS audit records to be written to the system audit log using the SYSLOG utility.

## Usage Notes

Note: In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. If you use this parameter, it is best to assign a file corresponding to every combination of facility and priority (especially KERN.EMERG ) in syslog.conf . Sometimes these are assigned to print to the console in the default syslog.conf file. This can become annoying and will be useless as audit logs. Also, if you use this parameter, it is best to set the maximum length of syslog messages in the system to 512 bytes. Note: Audit records written to the system audit log could get truncated to 512 bytes, and different parts of the same audit record may not be joined to get the original complete audit record. See Also: Oracle Database Security Guide for information about configuring syslog auditing If AUDIT_SYSLOG_LEVEL is set and SYS auditing is enabled ( AUDIT_SYS_OPERATIONS = TRUE ), then SYS audit records are written to the system audit log. If AUDIT_SYSLOG_LEVEL is set and standard audit records are being sent to the operating system ( AUDIT_TRAIL = os ), then standard audit records are written to the system audit log. In a CDB, the scope of the settings for this initialization parameter is the CDB. Although the audit trail is provided per PDB in a CDB, this initialization parameter cannot be configured for individual PDBs. Note: In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. Note: Audit records written to the system audit log could get truncated to 512 bytes, and different parts of the same audit record may not be joined to get the original complete audit record. See Also: Oracle Database Security Guide for information about configuring syslog auditing