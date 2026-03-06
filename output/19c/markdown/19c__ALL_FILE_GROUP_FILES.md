---
id: 19c__ALL_FILE_GROUP_FILES
name: ALL_FILE_GROUP_FILES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_FILE_GROUP_FILES.html
---

# ALL_FILE_GROUP_FILES

ALL_FILE_GROUP_FILES shows the file set for each versioned file group accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| FILE_GROUP_OWNER | VARCHAR2(128) | Owner of the file group |
| FILE_GROUP_NAME | VARCHAR2(128) | Name of the file group |
| VERSION_NAME | VARCHAR2(128) | Name of the version to which the file belongs |
| VERSION | NUMBER | Internal version number of the file group version to which the file belongs |
| FILE_NAME | VARCHAR2(512) | Name of the file |
| FILE_DIRECTORY | VARCHAR2(128) | Directory object for the directory where the file is stored |
| FILE_TYPE | VARCHAR2(32) | User-specified file type |
| FILE_SIZE | NUMBER | Size of the file |
| FILE_BLOCK_SIZE | NUMBER | Block size for the file |
| COMMENTS | VARCHAR2(4000) | Comments about the file group |

## Usage Notes

Related Views DBA_FILE_GROUP_FILES shows the file set for each versioned group in the database. USER_FILE_GROUP_FILES shows the file set for each versioned group owned by the current user. This view does not display the FILE_GROUP_OWNER column. See Also: " DBA_FILE_GROUP_FILES " " USER_FILE_GROUP_FILES " See Also: " DBA_FILE_GROUP_FILES " " USER_FILE_GROUP_FILES "