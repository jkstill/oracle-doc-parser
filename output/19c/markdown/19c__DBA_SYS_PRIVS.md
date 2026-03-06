---
id: 19c__DBA_SYS_PRIVS
name: DBA_SYS_PRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_SYS_PRIVS.html
---

# DBA_SYS_PRIVS

DBA_SYS_PRIVS describes system privileges granted to users and roles.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GRANTEE | VARCHAR2(128) | Grantee name, user, or role receiving the grant |
| PRIVILEGE | VARCHAR2(40) | System privilege |
| ADMIN_OPTION | VARCHAR2(3) | Indicates whether the grant was with the ADMIN option ( YES ) or not ( NO ) |
| COMMON | VARCHAR2(3) | Indicates how the grant was made. Possible values: YES if the privilege was granted commonly ( CONTAINER=ALL was used) NO if the privilege was granted locally ( CONTAINER=ALL was not used) |
| INHERITED | VARCHAR2(3) | Indicates whether the grant was inherited from another container ( YES ) or not ( NO ) |

## Usage Notes

See Also: " USER_SYS_PRIVS " See Also: " USER_SYS_PRIVS "