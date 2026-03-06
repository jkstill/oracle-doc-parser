---
id: 19c__AUDIT_FILE_DEST
name: AUDIT_FILE_DEST
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: auditing
source_file: AUDIT_FILE_DEST.html
---

# AUDIT_FILE_DEST

AUDIT_FILE_DEST specifies the operating system directory into which the audit trail is written when the AUDIT_TRAIL initialization parameter is set to os , xml , or xml,extended .

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Note: In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. The audit records will be written in XML format if the AUDIT_TRAIL initialization parameter is set to xml or xml, extended . It is also the location to which mandatory auditing information is written and, if so specified by the AUDIT_SYS_OPERATIONS initialization parameter, audit records for user SYS . In a multitenant container database (CDB), the scope of the settings for this initialization parameter is the CDB. Although the audit trail is provided per pluggable database (PDB) in a CDB, this initialization parameter cannot be configured for individual PDBs. See Also: Oracle Multitenant Administrator's Guide for conceptual information about CDBs and PDBs Oracle Multitenant Administrator's Guide for information about managing CDBs and PDBs " V$CONTAINERS " " V$PDBS " Note: In an Oracle database that has migrated to unified auditing, the setting of this parameter has no effect. See Oracle Database Security Guide for more information about unified auditing. See Oracle Database Upgrade Guide for more information about migrating to unified auditing. See Also: Oracle Multitenant Administrator's Guide for conceptual information about CDBs and PDBs Oracle Multitenant Administrator's Guide for information about managing CDBs and PDBs " V$CONTAINERS " " V$PDBS "