---
id: 19c__DBMS_CONNECTION_POOL.START_POOL
name: DBMS_CONNECTION_POOL.START_POOL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CONNECTION_POOL
tags: [dbms_connection_pool]
source_file: DBMS_CONNECTION_POOL.html
---

# DBMS_CONNECTION_POOL.START_POOL

This procedure starts the pool for operations. It is only after this call that the pool could be used by connection classes for creating sessions.

## Syntax

```sql
DBMS_CONNECTION_POOL.START_POOL (
   pool_name  IN  VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pool_name | VARCHAR2 | IN | Pool to be started. Currently only the default pool name is supported. |

## Usage Notes

Syntax DBMS_CONNECTION_POOL.START_POOL ( pool_name IN VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL'); Parameters Table 39-6 START_POOL Procedure Parameters Parameter Description pool_name Pool to be started. Currently only the default pool name is supported. Exceptions Table 39-7 START_POOL Procedure Exceptions Exception Description ORA-56500 Connection pool not found ORA-56501 Connection pool startup failed Usage Notes If the instance is restarted (shutdown followed by startup), the pool is automatically started.