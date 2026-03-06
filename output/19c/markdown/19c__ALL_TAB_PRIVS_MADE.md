---
id: 19c__ALL_TAB_PRIVS_MADE
name: ALL_TAB_PRIVS_MADE
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [all]
source_file: ALL_TAB_PRIVS_MADE.html
---

# ALL_TAB_PRIVS_MADE

ALL_TAB_PRIVS_MADE describes the object grants for which the current user is the object owner or grantor.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GRANTEE | VARCHAR2(128) | Name of the user or role to whom access was granted |
| OWNER | VARCHAR2(128) | Owner of the object |
| TABLE_NAME | VARCHAR2(128) | Name of the object |
| GRANTOR | VARCHAR2(128) | Name of the user who performed the grant |
| PRIVILEGE | VARCHAR2(40) | Privilege on the object |
| GRANTABLE | VARCHAR2(3) | Indicates whether the privilege was granted with the GRANT OPTION ( YES ) or not ( NO ) |
| HIERARCHY | VARCHAR2(3) | Indicates whether the privilege was granted with the HIERARCHY OPTION ( YES ) or not ( NO ) |
| COMMON | VARCHAR2(3) | Indicates how the grant was made. Possible values: YES if the privilege was granted commonly ( CONTAINER=ALL was used) NO if the privilege was granted locally ( CONTAINER=ALL was not used) |
| TYPE | VARCHAR2(24) | Type of the object |
| INHERITED | VARCHAR2(3) | Indicates whether the privilege grant was inherited from another container ( YES ) or not ( NO ) |

## Usage Notes

Related View USER_TAB_PRIVS_MADE describes the object grants for which the current user is the object owner. This view does not display the OWNER column. See Also: " USER_TAB_PRIVS_MADE " See Also: " USER_TAB_PRIVS_MADE "