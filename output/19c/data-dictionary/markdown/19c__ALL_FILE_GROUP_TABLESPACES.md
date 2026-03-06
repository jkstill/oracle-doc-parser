---
id: 19c__ALL_FILE_GROUP_TABLESPACES
name: ALL_FILE_GROUP_TABLESPACES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: storage
tags: [all]
source_file: ALL_FILE_GROUP_TABLESPACES.html
---

# ALL_FILE_GROUP_TABLESPACES

ALL_FILE_GROUP_TABLESPACES shows information about the transportable tablespaces present (partially or completely) in the file groups accessible to the current user (when the file groups contain dump files).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_GROUP_OWNER | VARCHAR2(128) | Owner of the file group |
| FILE_GROUP_NAME | VARCHAR2(128) | Name of the file group |
| VERSION_NAME | VARCHAR2(128) | Version of the file group that contains the tablespace |
| VERSION | NUMBER | Internal version number |
| TABLESPACE_NAME | VARCHAR2(30) | Name of the tablespace |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_FILE_GROUP_TABLESPACES shows information about the transportable tablespaces present (partially or completely) in all file groups in the database (when the file groups contain dump files). USER_FILE_GROUP_TABLESPACES shows information about the transportable tablespaces present (partially or completely) in the file groups owned by the current user (when the file groups contain dump files). This view does not display the FILE_GROUP_OWNER column. See Also: " DBA_FILE_GROUP_TABLESPACES " " USER_FILE_GROUP_TABLESPACES " See Also: " DBA_FILE_GROUP_TABLESPACES " " USER_FILE_GROUP_TABLESPACES "