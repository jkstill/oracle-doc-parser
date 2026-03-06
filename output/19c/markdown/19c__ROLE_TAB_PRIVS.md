---
id: 19c__ROLE_TAB_PRIVS
name: ROLE_TAB_PRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
source_file: ROLE_TAB_PRIVS.html
---

# ROLE_TAB_PRIVS

ROLE_TAB_PRIVS describes table privileges granted to roles. Information is provided only about roles to which the user has access.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ROLE | VARCHAR2(128) | Name of the role |
| OWNER | VARCHAR2(128) | Owner of the object |
| TABLE_NAME | VARCHAR2(128) | Name of the object |
| COLUMN_NAME | VARCHAR2(128) | Name of the column, if applicable |
| PRIVILEGE | VARCHAR2(40) | Object privilege granted to the role |
| GRANTABLE | VARCHAR2(3) | YES if the role was granted with ADMIN OPTION ; otherwise NO |
| COMMON | VARCHAR2(3) | Indicates how the grant was made. Possible values: YES if the privilege was granted commonly ( CONTAINER=ALL was used) NO if the privilege was granted locally ( CONTAINER=ALL was not used) |
| INHERITED | VARCHAR2(3) | Indicates whether the role grant was inherited from another container ( YES ) or not ( NO ) |