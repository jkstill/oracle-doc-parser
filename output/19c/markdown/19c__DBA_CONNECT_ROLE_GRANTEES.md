---
id: 19c__DBA_CONNECT_ROLE_GRANTEES
name: DBA_CONNECT_ROLE_GRANTEES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_CONNECT_ROLE_GRANTEES.html
---

# DBA_CONNECT_ROLE_GRANTEES

DBA_CONNECT_ROLE_GRANTEES displays information about users who are granted the CONNECT privilege.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GRANTEE | VARCHAR2(128) | User or schema to which the CONNECT role is granted |
| PATH_OF_CONNECT_ROLE_GRANT | VARCHAR2(4000) | The path of role inheritance through which the grantee is granted the CONNECT role |
| ADMIN_OPT | VARCHAR2(3) | Whether or not the grantee was granted the ADMIN option for the CONNECT role |