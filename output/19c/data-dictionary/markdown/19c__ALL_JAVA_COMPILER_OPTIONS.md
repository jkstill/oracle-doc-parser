---
id: 19c__ALL_JAVA_COMPILER_OPTIONS
name: ALL_JAVA_COMPILER_OPTIONS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JAVA_COMPILER_OPTIONS.html
---

# ALL_JAVA_COMPILER_OPTIONS

ALL_JAVA_COMPILER_OPTIONS displays information about the native compiler options accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the native compiler option |
| OPTION_NAME | VARCHAR2(64) | Name of the native compiler option |
| VALUE | VARCHAR2(4000) | Value of the native compiler option |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related Views DBA_JAVA_COMPILER_OPTIONS displays information about all native compiler options in the database. USER_JAVA_COMPILER_OPTIONS displays information about the native compiler options owned by the current user. This view does not display the OWNER column. See Also: " DBA_JAVA_COMPILER_OPTIONS " " USER_JAVA_COMPILER_OPTIONS " See Also: " DBA_JAVA_COMPILER_OPTIONS " " USER_JAVA_COMPILER_OPTIONS "