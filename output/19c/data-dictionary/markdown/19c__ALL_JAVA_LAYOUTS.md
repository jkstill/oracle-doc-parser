---
id: 19c__ALL_JAVA_LAYOUTS
name: ALL_JAVA_LAYOUTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JAVA_LAYOUTS.html
---

# ALL_JAVA_LAYOUTS

ALL_JAVA_LAYOUTS displays class layout information about the stored Java classes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Java class |
| NAME | VARCHAR2(4000) | Name of the Java class |
| INTERFACES | NUMBER | Number of interfaces that this Java class implements |
| INNER_CLASSES | NUMBER | Number of inner classes that this Java class contains |
| FIELDS | NUMBER | Number of locally declared fields that this Java class contains |
| STATIC_FIELDS | NUMBER | Number of locally declared static fields that this Java class contains |
| METHODS | NUMBER | Number of locally declared methods that this Java class contains |
| STATIC_METHODS | NUMBER | Number of locally declared static methods that this Java class contains |
| NATIVE_METHODS | NUMBER | Number of locally declared native methods that this Java class contains |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_JAVA_LAYOUTS displays class layout information about all stored Java classes in the database. USER_JAVA_LAYOUTS displays class layout information about the stored Java classes owned by the current user. This view does not display the OWNER column. See Also: " DBA_JAVA_LAYOUTS " " USER_JAVA_LAYOUTS " See Also: " DBA_JAVA_LAYOUTS " " USER_JAVA_LAYOUTS "