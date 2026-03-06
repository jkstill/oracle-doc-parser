---
id: 19c__DBA_TSDP_IMPORT_ERRORS
name: DBA_TSDP_IMPORT_ERRORS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_TSDP_IMPORT_ERRORS.html
---

# DBA_TSDP_IMPORT_ERRORS

DBA_TSDP_IMPORT_ERRORS shows information about the errors encountered during import of the Transparent Sensitive Data Protection discovery result.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ERROR_CODE | NUMBER | The ORA error code of the error encountered |
| SCHEMA_NAME | VARCHAR2(128) | The schema corresponding to the error |
| TABLE_NAME | VARCHAR2(128) | The table corresponding to the error |
| COLUMN_NAME | VARCHAR2(128) | The column corresponding to the error |
| SENSITIVE_TYPE | VARCHAR2(128) | The sensitive type corresponding to the error |

## Usage Notes

This error information corresponds to the last import of the discovery result done using the DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT API. See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT procedure See Also: Oracle Database Security Guide for more information about using Transparent Sensitive Data Protection Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_TSDP_MANAGE.IMPORT_DISCOVERY_RESULT procedure