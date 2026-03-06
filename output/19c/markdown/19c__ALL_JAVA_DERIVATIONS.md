---
id: 19c__ALL_JAVA_DERIVATIONS
name: ALL_JAVA_DERIVATIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JAVA_DERIVATIONS.html
---

# ALL_JAVA_DERIVATIONS

ALL_JAVA_DERIVATIONS displays mapping information about Java source objects and their derived Java class objects and Java resource objects for the Java classes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Java source object |
| SOURCE_NAME | VARCHAR2(4000) | Name of the Java source object |
| CLASS_INDEX | NUMBER | Index of the derived Java class object |
| CLASS_NAME | VARCHAR2(4000) | Name of the derived Java class object |

## Usage Notes

Related Views DBA_JAVA_DERIVATIONS displays mapping information about Java source objects and their derived Java class objects and Java resource objects for all Java classes in the database. USER_JAVA_DERIVATIONS displays mapping information about Java source objects and their derived Java class objects and Java resource objects for the Java classes owned by the current user. This view does not display the OWNER column. See Also: " DBA_JAVA_DERIVATIONS " " USER_JAVA_DERIVATIONS " See Also: " DBA_JAVA_DERIVATIONS " " USER_JAVA_DERIVATIONS "