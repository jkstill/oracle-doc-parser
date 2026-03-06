---
id: 19c__DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_FROM_LOCAL
name: DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_FROM_LOCAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_FROM_LOCAL

This procedure migrates a locally managed tablespace to a dictionary-managed tablespace.

## Syntax

```sql
DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_FROM_LOCAL (
   tablespace_name         IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2) | IN | Name of tablespace |

## Usage Notes

Syntax DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_FROM_LOCAL ( tablespace_name IN VARCHAR2); Parameter Table 159-15 TABLESPACE_MIGRATE_FROM_LOCAL Procedure Parameter Parameter Description tablespace_name Name of tablespace Usage Notes The tablespace must be kept online and read/write during migration. Migration of temporary tablespaces and migration of SYSTEM tablespaces are not supported. Examples EXECUTE DBMS_SPACE_ADMIN.TABLESPACE_MIGRATE_FROM_LOCAL('USERS');