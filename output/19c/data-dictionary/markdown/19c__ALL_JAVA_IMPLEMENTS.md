---
id: 19c__ALL_JAVA_IMPLEMENTS
name: ALL_JAVA_IMPLEMENTS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JAVA_IMPLEMENTS.html
---

# ALL_JAVA_IMPLEMENTS

ALL_JAVA_IMPLEMENTS describes interfaces implemented by the stored Java classes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Java class |
| NAME | VARCHAR2(4000) | Name of the Java class |
| INTERFACE_INDEX | NUMBER | Index of the interfaces implemented by the Java class |
| INTERFACE_NAME | VARCHAR2(4000) | Name of the interface identified by the INTERFACE_INDEX column |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_JAVA_IMPLEMENTS describes interfaces implemented by all stored Java classes in the database. USER_JAVA_IMPLEMENTS describes interfaces implemented by the stored Java classes owned by the current user. This view does not display the OWNER column. See Also: " DBA_JAVA_IMPLEMENTS " " USER_JAVA_IMPLEMENTS " See Also: " DBA_JAVA_IMPLEMENTS " " USER_JAVA_IMPLEMENTS "