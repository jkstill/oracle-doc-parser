---
id: 19c__DBMS_CONNECTION_POOL.STOP_POOL
name: DBMS_CONNECTION_POOL.STOP_POOL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CONNECTION_POOL
tags: [dbms_connection_pool]
source_file: DBMS_CONNECTION_POOL.html
---

# DBMS_CONNECTION_POOL.STOP_POOL

This procedure stops the pool and makes it unavailable for the registered connection classes.

## Syntax

```sql
DBMS_CONNECTION_POOL.STOP_POOL (
   pool_name   IN   VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pool_name | VARCHAR2 | IN | Pool to be stopped. Currently only the default pool name is supported. |

## Usage Notes

Syntax DBMS_CONNECTION_POOL.STOP_POOL ( pool_name IN VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL'); Parameters Table 39-8 STOP_POOL Procedure Parameters Parameter Description pool_name Pool to be stopped. Currently only the default pool name is supported. Exceptions Table 39-9 STOP_POOL Procedure Exceptions Exception Description ORA-56500 Connection pool not found ORA-56506 Connection pool shutdown failed Usage Notes This stops the pool and takes it offline. This does not destroy the persistent data (such as, the pool name and configuration parameters) associated with the pool.