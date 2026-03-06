---
id: 19c__ALL_JAVA_RESOLVERS
name: ALL_JAVA_RESOLVERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [all]
source_file: ALL_JAVA_RESOLVERS.html
---

# ALL_JAVA_RESOLVERS

ALL_JAVA_RESOLVERS displays information about resolvers of the Java classes accessible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| OWNER | VARCHAR2(128) | Owner of the Java class object |
| NAME | VARCHAR2(4000) | Name of the Java class object |
| TERM_INDEX | NUMBER | Index of the resolver term in this row |
| PATTERN | VARCHAR2(4000) | Resolver pattern of the resolver term identified by the TERM_INDEX column |
| SCHEMA | VARCHAR2(64) | Resolver schema of the resolver term identified by the TERM_INDEX column |

## Usage Notes

Related Views DBA_JAVA_RESOLVERS displays information about resolvers of all Java classes in the database. USER_JAVA_RESOLVERS displays information about resolvers of the Java classes owned by the current user. This view does not display the OWNER column. See Also: " DBA_JAVA_RESOLVERS " " USER_JAVA_RESOLVERS " See Also: " DBA_JAVA_RESOLVERS " " USER_JAVA_RESOLVERS "