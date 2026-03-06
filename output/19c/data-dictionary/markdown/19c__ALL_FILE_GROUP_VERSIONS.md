---
id: 19c__ALL_FILE_GROUP_VERSIONS
name: ALL_FILE_GROUP_VERSIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_FILE_GROUP_VERSIONS.html
---

# ALL_FILE_GROUP_VERSIONS

ALL_FILE_GROUP_VERSIONS shows top-level version information for the file groups accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_GROUP_OWNER | VARCHAR2(128) | Owner of the file group |
| FILE_GROUP_NAME | VARCHAR2(128) | Name of the file group |
| VERSION_NAME | VARCHAR2(128) | User-specified name for the version |
| VERSION | NUMBER | Internal version number |
| CREATOR | VARCHAR2(128) | User who created the version |
| CREATED | TIMESTAMP(6) WITH TIME ZONE | Time at which the version was created |
| COMMENTS | VARCHAR2(4000) | Comments about the file group |
| DEFAULT_DIRECTORY | VARCHAR2(128) | Default directory object for this version, if specified |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_FILE_GROUP_VERSIONS shows top-level version information for all file groups in the database. USER_FILE_GROUP_VERSIONS shows top-level version information for all file groups owned by the current user. This view does not display the FILE_GROUP_OWNER column. See Also: " DBA_FILE_GROUP_VERSIONS " " USER_FILE_GROUP_VERSIONS " See Also: " DBA_FILE_GROUP_VERSIONS " " USER_FILE_GROUP_VERSIONS "