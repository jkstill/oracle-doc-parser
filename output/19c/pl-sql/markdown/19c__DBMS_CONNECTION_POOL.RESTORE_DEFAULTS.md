---
id: 19c__DBMS_CONNECTION_POOL.RESTORE_DEFAULTS
name: DBMS_CONNECTION_POOL.RESTORE_DEFAULTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CONNECTION_POOL
tags: [dbms_connection_pool]
source_file: DBMS_CONNECTION_POOL.html
---

# DBMS_CONNECTION_POOL.RESTORE_DEFAULTS

This procedure restores the pool to default settings.

## Syntax

```sql
DBMS_CONNECTION_POOL.RESTORE_DEFAULTS (
   pool_name   IN  VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pool_name | VARCHAR2 | IN | Pool to be restored. Currently only the default pool name is supported. |

## Usage Notes

Syntax DBMS_CONNECTION_POOL.RESTORE_DEFAULTS ( pool_name IN VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL'); Parameters Table 39-10 RESTORE_DEFAULTS Procedure Parameters Parameter Description pool_name Pool to be restored. Currently only the default pool name is supported. Exceptions Table 39-11 RESTORE_DEFAULTS Procedure Exceptions Exception Description ORA-56500 Connection pool not found ORA-56507 Connection pool alter configuration failed Usage Notes If the instance is restarted (shutdown followed by startup), the pool is automatically started.