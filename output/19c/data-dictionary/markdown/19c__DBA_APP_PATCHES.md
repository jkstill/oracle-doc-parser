---
id: 19c__DBA_APP_PATCHES
name: DBA_APP_PATCHES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_APP_PATCHES.html
---

# DBA_APP_PATCHES

DBA_APP_PATCHES describes all the application patches in the Application Container.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| APP_NAME | VARCHAR2(128) | Name of the application |
| PATCH_NUMBER | NUMBER | Patch number |
| PATCH_MIN_VERSION | VARCHAR2(30) | Minimum application version for the patch |
| PATCH_STATUS | VARCHAR2(10) | Status of the patch |
| PATCH_COMMENT | VARCHAR2(4000) | Comment associated with the patch |
| PATCH_CHECKSUM | NUMBER | Checksum for the patch |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content