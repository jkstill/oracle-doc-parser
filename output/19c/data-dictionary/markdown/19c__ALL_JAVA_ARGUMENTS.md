---
id: 19c__ALL_JAVA_ARGUMENTS
name: ALL_JAVA_ARGUMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JAVA_ARGUMENTS.html
---

# ALL_JAVA_ARGUMENTS

ALL_JAVA_ARGUMENTS displays argument information about the stored Java classes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Java class |
| NAME | VARCHAR2(4000) | Name of the Java class |
| METHOD_INDEX | NUMBER | Index of the hosting method of the argument |
| METHOD_NAME | VARCHAR2(4000) | Name of the hosting method of the argument |
| ARGUMENT_POSITION | NUMBER | Position of the argument, starting from 0 |
| ARRAY_DEPTH | NUMBER | Array depth of the type of the argument |
| BASE_TYPE | VARCHAR2(7) | Base type of the type of the argument: int long float double boolean byte char short class |
| ARGUMENT_CLASS | VARCHAR2(4000) | Actual class name of the argument if the base type is class |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_JAVA_ARGUMENTS displays argument information about all stored Java classes in the database. USER_JAVA_ARGUMENTS displays argument information about the stored Java classes owned by the current user. This view does not display the OWNER column. See Also: " DBA_JAVA_ARGUMENTS " " USER_JAVA_ARGUMENTS " See Also: " DBA_JAVA_ARGUMENTS " " USER_JAVA_ARGUMENTS "