---
id: 19c__ALL_JAVA_NCOMPS
name: ALL_JAVA_NCOMPS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JAVA_NCOMPS.html
---

# ALL_JAVA_NCOMPS

ALL_JAVA_NCOMPS displays ncomp -related information about the Java classes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Java class object |
| NAME | VARCHAR2(4000) | Name of the Java class object |
| SOURCE | VARCHAR2(4000) | ncomp source shown in this row |
| INITIALIZER | VARCHAR2(4000) | ncomp initializer shown in this row |
| LIBRARYFILE | VARCHAR2(4000) | ncomp library file shown in this row |
| LIBRARY | VARCHAR2(4000) | ncomp library shown in this row |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_JAVA_NCOMPS displays ncomp -related information about all Java classes in the database. USER_JAVA_NCOMPS displays ncomp -related information about the Java classes owned by the current user. This view does not display the OWNER column. See Also: " DBA_JAVA_NCOMPS " " USER_JAVA_NCOMPS " See Also: " DBA_JAVA_NCOMPS " " USER_JAVA_NCOMPS "