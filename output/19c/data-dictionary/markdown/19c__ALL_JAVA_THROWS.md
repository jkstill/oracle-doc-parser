---
id: 19c__ALL_JAVA_THROWS
name: ALL_JAVA_THROWS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JAVA_THROWS.html
---

# ALL_JAVA_THROWS

ALL_JAVA_THROWS displays information about exceptions thrown from methods of the Java classes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Java class |
| NAME | VARCHAR2(4000) | Name of the Java class |
| METHOD_INDEX | NUMBER | Index of the throwing method of the exception |
| METHOD_NAME | VARCHAR2(4000) | Name of the throwing method of the exception |
| EXCEPTION_INDEX | NUMBER | Index of the exception |
| EXCEPTION_CLASS | VARCHAR2(4000) | Class of the exception |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_JAVA_THROWS displays information about exceptions thrown from methods of all Java classes in the database. USER_JAVA_THROWS displays information about exceptions thrown from methods of the Java classes owned by the current user. This view does not display the OWNER column. See Also: " DBA_JAVA_THROWS " " USER_JAVA_THROWS " See Also: " DBA_JAVA_THROWS " " USER_JAVA_THROWS "