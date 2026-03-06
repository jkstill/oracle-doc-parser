---
id: 19c__ALL_DIRECTORIES
name: ALL_DIRECTORIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_DIRECTORIES.html
---

# ALL_DIRECTORIES

ALL_DIRECTORIES describes all directories accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the directory (always SYS ) |
| DIRECTORY_NAME | VARCHAR2(128) | Name of the directory |
| DIRECTORY_PATH | VARCHAR2(4000) | Operating system pathname for the directory |
| ORIGIN_CON_ID | VARCHAR2(256) | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View DBA_DIRECTORIES describes all directories in the database. See Also: " DBA_DIRECTORIES " See Also: " DBA_DIRECTORIES "