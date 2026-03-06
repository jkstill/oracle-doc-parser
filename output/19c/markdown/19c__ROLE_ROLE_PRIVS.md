---
id: 19c__ROLE_ROLE_PRIVS
name: ROLE_ROLE_PRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
source_file: ROLE_ROLE_PRIVS.html
---

# ROLE_ROLE_PRIVS

ROLE_ROLE_PRIVS describes the roles granted to other roles.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ROLE | VARCHAR2(128) | Name of the role |
| GRANTED_ROLE | VARCHAR2(128) | Role that was granted |
| ADMIN_OPTION | VARCHAR2(3) | Signifies that the role was granted with ADMIN option |
| COMMON | VARCHAR2(3) | Indicates how the grant was made. Possible values: YES if the role was granted commonly ( CONTAINER=ALL was used) NO if the role was granted locally ( CONTAINER=ALL was not used) |
| INHERITED | VARCHAR2(3) | Indicates whether the role grant was inherited from another container ( YES ) or not ( NO ) |

## Usage Notes

Information is provided only about roles to which the user has access.