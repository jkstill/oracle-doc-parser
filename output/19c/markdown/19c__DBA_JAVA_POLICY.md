---
id: 19c__DBA_JAVA_POLICY
name: DBA_JAVA_POLICY
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: general
tags: [dba]
source_file: DBA_JAVA_POLICY.html
---

# DBA_JAVA_POLICY

DBA_JAVA_POLICY describes Java security permissions for all users in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| KIND | VARCHAR2(8) | Indicates whether the permission is a positive ( GRANT ) or a limitation ( RESTRICT ) |
| GRANTEE | VARCHAR2(128) | Name of the user, schema, or role to which the permission object is assigned |
| TYPE_SCHEMA | VARCHAR2(128) | Schema in which the permission object is loaded |
| TYPE_NAME | VARCHAR2(4000) | Permission class type, which is designated by a string containing the full class name, such as, java.io.FilePermission |
| NAME | VARCHAR2(4000) | Target attribute (name) of the permission object. This name is used when defining the permission. |
| ACTION | VARCHAR2(4000) | Action attribute for this permission. Many permissions expect a null value if no action is appropriate for the permission. |
| ENABLED | VARCHAR2(8) | Indicates whether the permission is enabled ( ENABLED ) or disabled ( DISABLED ) |
| SEQ | NUMBER | Sequence number used to identify this row. This number should be supplied when disabling, enabling, or deleting the permission. |

## Usage Notes

Related View USER_JAVA_POLICY describes Java security permissions for the current user. See Also: " USER_JAVA_POLICY " See Also: " USER_JAVA_POLICY "