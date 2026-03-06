---
id: 19c__ALL_SOURCE_AE
name: ALL_SOURCE_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_SOURCE_AE.html
---

# ALL_SOURCE_AE

ALL_SOURCE_AE describes the text source of the stored objects (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| NAME | VARCHAR2(128) | Name of the object |
| TYPE | VARCHAR2(12) | Type of the object: TYPE TYPE BODY PROCEDURE FUNCTION PACKAGE PACKAGE BODY LIBRARY JAVA SOURCE |
| LINE | NUMBER | Line number of this line of source |
| TEXT | VARCHAR2(4000) | Source text |
| EDITION_NAME | VARCHAR2(128) | Name of the Edition |
| ORIGIN_CON_ID | NUMBER | The ID of the container where the data originates. Possible values include: 0 : This value is used for rows in non-CDBs. This value is not used for CDBs. n : This value is used for rows containing data that originate in the container with container ID n ( n = 1 if the row originates in root) |

## Usage Notes

Related Views DBA_SOURCE_AE describes the text source of all stored objects (across all editions) in the database. USER_SOURCE_AE describes the text source of the stored objects (across all editions) owned by the current user. This view does not display the OWNER column. See Also: " DBA_SOURCE_AE " " USER_SOURCE_AE " See Also: " DBA_SOURCE_AE " " USER_SOURCE_AE "