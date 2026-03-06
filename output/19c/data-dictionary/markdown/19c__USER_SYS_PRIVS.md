---
id: 19c__USER_SYS_PRIVS
name: USER_SYS_PRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [user]
source_file: USER_SYS_PRIVS.html
---

# USER_SYS_PRIVS

USER_SYS_PRIVS describes system privileges granted to the current user.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(128) | Name of the user, or PUBLIC |
| PRIVILEGE | VARCHAR2(40) | System privilege |
| ADMIN_OPTION | VARCHAR2(3) | Indicates whether the grant was with the ADMIN option ( YES ) or not ( NO ) |
| COMMON | VARCHAR2(3) | Indicates how the grant was made. Possible values: YES if the privilege was granted commonly ( CONTAINER=ALL was used) NO if the privilege was granted locally ( CONTAINER=ALL was not used) |
| INHERITED | VARCHAR2(3) | Indicates whether the grant was inherited from another container ( YES ) or not ( NO ) |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content See Also: " DBA_SYS_PRIVS " See Also: " DBA_SYS_PRIVS "