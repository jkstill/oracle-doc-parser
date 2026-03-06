---
id: 19c__ALL_LIBRARIES
name: ALL_LIBRARIES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_LIBRARIES.html
---

# ALL_LIBRARIES

ALL_LIBRARIES describes the libraries accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the library |
| LIBRARY_NAME | VARCHAR2(128) | Library name |
| FILE_SPEC | VARCHAR2(2000) | Operating system file specification associated with the library |
| DYNAMIC | VARCHAR2(1) | Indicates whether the library is dynamically loadable ( Y ) or not ( N ) |
| STATUS | VARCHAR2(7) | Status of the library: N/A VALID INVALID |
| AGENT | VARCHAR2(128) | Agent of the library |
| LEAF_FILENAME | VARCHAR2(2000) | Leaf filename of the library |
| ORIGIN_CON_ID | VARCHAR2(256) | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_LIBRARIES describes all libraries in the database. USER_LIBRARIES describes the libraries owned by the current user. This view does not display the OWNER column. See Also: " DBA_LIBRARIES " " USER_LIBRARIES " See Also: " DBA_LIBRARIES " " USER_LIBRARIES "