---
id: 19c__DBA_USERS_WITH_DEFPWD
name: DBA_USERS_WITH_DEFPWD
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_USERS_WITH_DEFPWD.html
---

# DBA_USERS_WITH_DEFPWD

DBA_USERS_WITH_DEFPWD displays all users in the database that are still using their default passwords.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| USERNAME | VARCHAR2(128) | Name of the user |
| PRODUCT | VARCHAR2(4000) | Name of the product the user belongs to |

## Usage Notes

Note: In a CDB, when DBA_USERS_WITH_DEFPWD is queried from a PDB, information about local users who are using their default passwords is displayed. To display information about common users, query DBA_USERS_WITH_DEFPWD from the root. See Also: Oracle Multitenant Administrator's Guide for an introduction to local and common users in a CDB Note: In a CDB, when DBA_USERS_WITH_DEFPWD is queried from a PDB, information about local users who are using their default passwords is displayed. To display information about common users, query DBA_USERS_WITH_DEFPWD from the root. See Also: Oracle Multitenant Administrator's Guide for an introduction to local and common users in a CDB