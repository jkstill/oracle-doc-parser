---
id: 19c__ALL_ERRORS_AE
name: ALL_ERRORS_AE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_ERRORS_AE.html
---

# ALL_ERRORS_AE

ALL_ERRORS_AE describes the current errors on the stored objects (across all editions) accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the object |
| NAME | VARCHAR2(128) | Name of the object |
| TYPE | VARCHAR2(12) | Type of the object: TYPE TYPE BODY VIEW PROCEDURE FUNCTION PACKAGE PACKAGE BODY TRIGGER JAVA SOURCE JAVA CLASS |
| SEQUENCE | NUMBER | Sequence number (for ordering purposes) |
| LINE | NUMBER | Line number at which this error occurred |
| POSITION | NUMBER | Position in the line at which this error occurred |
| TEXT | VARCHAR2(4000) | Text of the error |
| ATTRIBUTE | VARCHAR2(9) | Indicates whether the error is an error ( ERROR ) or a warning ( WARNING ) |
| MESSAGE_NUMBER | NUMBER | Numeric error number (without any prefix) |
| EDITION_NAME | VARCHAR2(128) | Name of the edition in which the object is actual |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_ERRORS_AE describes the current errors on all stored objects (across all editions) in the database. USER_ERRORS_AE describes the current errors on the stored objects (across all editions) owned by the current user. This view does not display the OWNER column. See Also: " DBA_ERRORS_AE " " USER_ERRORS_AE " See Also: " DBA_ERRORS_AE " " USER_ERRORS_AE "