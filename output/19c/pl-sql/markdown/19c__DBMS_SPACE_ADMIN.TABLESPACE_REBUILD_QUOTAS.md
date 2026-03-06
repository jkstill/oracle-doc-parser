---
id: 19c__DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_QUOTAS
name: DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_QUOTAS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPACE_ADMIN
tags: [dbms_space_admin]
source_file: DBMS_SPACE_ADMIN.html
---

# DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_QUOTAS

This procedure rebuilds quotas for the given tablespace.

## Syntax

```sql
DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_QUOTAS (
   tablespace_name         IN    VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| tablespace_name | VARCHAR2) | IN | Name of tablespace |

## Usage Notes

Syntax DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_QUOTAS ( tablespace_name IN VARCHAR2); Parameters Table 159-18 TABLESPACE_REBUILD_QUOTAS Procedure Parameters Parameter Description tablespace_name Name of tablespace Examples EXECUTE DBMS_SPACE_ADMIN.TABLESPACE_REBUILD_QUOTAS('USERS');