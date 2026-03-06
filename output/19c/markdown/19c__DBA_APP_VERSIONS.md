---
id: 19c__DBA_APP_VERSIONS
name: DBA_APP_VERSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_APP_VERSIONS.html
---

# DBA_APP_VERSIONS

DBA_APP_VERSIONS displays information about all application versions installed in an application container.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APP_NAME | VARCHAR2(128) | Name of the application |
| APP_VERSION | VARCHAR2(30) | Version of the application |
| APP_VERSION_COMMENT | VARCHAR2(4000) | Comment associated with the application version |
| APP_VERSION_CHECKSUM | NUMBER | Checksum for the application version |
| APP_ROOT_CLONE_NAME Foot 1 | VARCHAR2(64) | Name of the application root clone that corresponds to the application |

## Usage Notes

See Also: Oracle Multitenant Administrator's Guide for more information about application containers See Also: Oracle Multitenant Administrator's Guide for more information about application containers