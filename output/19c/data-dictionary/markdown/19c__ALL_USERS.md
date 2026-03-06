---
id: 19c__ALL_USERS
name: ALL_USERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [all]
source_file: ALL_USERS.html
---

# ALL_USERS

ALL_USERS lists all users of the database visible to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(128) | Name of the user |
| USER_ID | NUMBER | ID number of the user |
| CREATED | DATE | User creation date |
| COMMON | VARCHAR2(3) | Indicates whether a given user is common. Possible values: YES if a user is common NO if a user is local (not common) |
| ORACLE_MAINTAINED | VARCHAR2(1) | Denotes whether the user was created, and is maintained, by Oracle-supplied scripts (such as catalog.sql or catproc.sql). A user for which this column has the value Y must not be changed in any way except by running an Oracle-supplied script. |
| INHERITED | VARCHAR2(3) | Indicates whether the user definition was inherited from another container ( YES ) or not ( NO ) |
| DEFAULT_COLLATION | VARCHAR2(100) | Default collation for the user’s schema |
| IMPLICIT | VARCHAR2(3) | Indicates whether this user is a common user created by an implicit application ( YES ) or not ( NO ) |
| ALL_SHARD | VARCHAR2(3) | In a sharded database, the value in this column indicates whether the user was created with shard DDL enabled. The possible values are: YES : The user was created with shard DDL enabled. The user exists on all shards and the shard catalog. NO : The user was created without shard DDL enabled. The user exists only in the database in which the user was created. In a non-sharded database, the value in this column is always NO . |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content This view does not describe the users (see the related views). Related Views DBA_USERS describes all users of the database, and contains more columns than ALL_USERS . USER_USERS describes the current user, and contains more columns than ALL_USERS . See Also: " DBA_USERS " " USER_USERS " Using Oracle Sharding for more information about sharded database management