---
id: 19c__ALL_SOURCE
name: ALL_SOURCE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SOURCE.html
---

# ALL_SOURCE

ALL_SOURCE describes the text source of the stored objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| NAME | VARCHAR2(128) | Name of the object |
| TYPE | VARCHAR2(12) | Type of object: FUNCTION , JAVA SOURCE , PACKAGE , PACKAGE BODY , PROCEDURE , TRIGGER , TYPE , TYPE BODY |
| LINE | NUMBER | Line number of this line of source |
| TEXT | VARCHAR2(4000) | Text source of the stored object |
| ORIGIN_CON_ID | VARCHAR2(256) | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_SOURCE describes the text source of all stored objects in the database. USER_SOURCE describes the text source of the stored objects owned by the current user. This view does not display the OWNER column. See Also: " DBA_SOURCE " " USER_SOURCE " See Also: " DBA_SOURCE " " USER_SOURCE "