---
id: 19c__DBA_APPLICATIONS
name: DBA_APPLICATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_APPLICATIONS.html
---

# DBA_APPLICATIONS

DBA_APPLICATIONS provides information about the applications in the current application container.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APP_NAME | VARCHAR2(128) | Name of the application |
| APP_ID | NUMBER | ID of the application |
| APP_VERSION | VARCHAR2(30) | Version of the application |
| APP_STATUS | VARCHAR2(12) | Status of the application |
| APP_IMPLICIT | VARCHAR2(1) | Indicates whether the application is implicit ( Y ) or not ( N ) |
| APP_CAPTURE_SERVICE | VARCHAR2(64) | Service name used for the capture |
| APP_CAPTURE_MODULE | VARCHAR2(64) | Module name used for the capture |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content