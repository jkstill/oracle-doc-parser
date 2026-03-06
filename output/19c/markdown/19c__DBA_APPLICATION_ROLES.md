---
id: 19c__DBA_APPLICATION_ROLES
name: DBA_APPLICATION_ROLES
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_APPLICATION_ROLES.html
---

# DBA_APPLICATION_ROLES

DBA_APPLICATION_ROLES describes all the roles that have authentication policy functions defined.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| ROLE | VARCHAR2(128) | Name of the application role |
| SCHEMA | VARCHAR2(128) | Schema of the authorized package |
| PACKAGE | VARCHAR2(128) | Name of the authorized package |