---
id: 19c__DBA_TAB_PRIVS
name: DBA_TAB_PRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_TAB_PRIVS.html
---

# DBA_TAB_PRIVS

DBA_TAB_PRIVS describes all object grants in the database.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GRANTEE | VARCHAR2(128) | Name of the user or role to whom access was granted |
| OWNER | VARCHAR2(128) | Owner of the object |
| TABLE_NAME | VARCHAR2(128) | Name of the object. The object can be any object, including tables, packages, indexes, sequences, and so on. |
| GRANTOR | VARCHAR2(128) | Name of the user who performed the grant |
| PRIVILEGE | VARCHAR2(40) | Privilege on the object |
| GRANTABLE | VARCHAR2(3) | Indicates whether the privilege was granted with the GRANT OPTION ( YES ) or not ( NO ) |
| HIERARCHY | VARCHAR2(3) | Indicates whether the privilege was granted with the HIERARCHY OPTION ( YES ) or not ( NO ) |
| COMMON | VARCHAR2(3) | Indicates how the grant was made. Possible values: YES if the privilege was granted commonly ( CONTAINER=ALL was used) NO if the privilege was granted locally ( CONTAINER=ALL was not used) |
| TYPE | VARCHAR2(24) | Type of the object |
| INHERITED | VARCHAR2(3) | Indicates whether the grant was inherited from another container ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content Related View USER_TAB_PRIVS describes the object grants for which the current user is the object owner, grantor, or grantee. See Also: " USER_TAB_PRIVS " See Also: " USER_TAB_PRIVS "