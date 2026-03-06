---
id: 19c__ALL_ERRORS
name: ALL_ERRORS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ERRORS.html
---

# ALL_ERRORS

ALL_ERRORS describes the current errors on the stored objects accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| NAME | VARCHAR2(128) | Name of the object |
| TYPE | VARCHAR2(12) | Type of the object: VIEW PROCEDURE FUNCTION PACKAGE PACKAGE BODY TRIGGER TYPE TYPE BODY LIBRARY JAVA SOURCE JAVA CLASS DIMENSION |
| SEQUENCE | NUMBER | Sequence number (for ordering purposes) |
| LINE | NUMBER | Line number at which the error occurred |
| POSITION | NUMBER | Position in the line at which the error occurred |
| TEXT | VARCHAR2(4000) | Text of the error |
| ATTRIBUTE | VARCHAR2(9) | Indicates whether the error is an error ( ERROR ) or a warning ( WARNING ) |
| MESSAGE_NUMBER | NUMBER | Numeric error number (without any prefix) |

## Usage Notes

Related Views DBA_ERRORS describes the current errors on all stored objects in the database. USER_ERRORS describes the current errors on the stored objects owned by the current user. This view does not display the OWNER column. See Also: " DBA_ERRORS " " USER_ERRORS " See Also: " DBA_ERRORS " " USER_ERRORS "