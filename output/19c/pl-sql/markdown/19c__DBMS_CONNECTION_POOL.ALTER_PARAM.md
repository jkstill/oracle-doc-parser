---
id: 19c__DBMS_CONNECTION_POOL.ALTER_PARAM
name: DBMS_CONNECTION_POOL.ALTER_PARAM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_CONNECTION_POOL
tags: [dbms_connection_pool]
source_file: DBMS_CONNECTION_POOL.html
---

# DBMS_CONNECTION_POOL.ALTER_PARAM

This procedure alters a specific configuration parameter as a standalone unit and does not affect other parameters.

## Syntax

```sql
DBMS_CONNECTION_POOL.ALTER_PARAM (
   pool_name     IN  VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL',   
   param_name    IN  VARCHAR2,   
   param_value   IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| pool_name | VARCHAR2 | IN | Pool to be configured. Currently only the default pool name is supported. |
| param_name | VARCHAR2 | IN | Any parameter name from CONFIGURE_POOL |
| param_value | VARCHAR2) | IN | Parameter value for param_name . |

## Usage Notes

Syntax DBMS_CONNECTION_POOL.ALTER_PARAM ( pool_name IN VARCHAR2 DEFAULT 'SYS_DEFAULT_CONNECTION_POOL', param_name IN VARCHAR2, param_value IN VARCHAR2); Parameters Table 39-2 ALTER_PARAM Procedure Parameters Parameter Description pool_name Pool to be configured. Currently only the default pool name is supported. param_name Any parameter name from CONFIGURE_POOL param_value Parameter value for param_name . See Also: For the list and description of all the database resident connection pooling parameters that can be configured using this procedure, see the Oracle Database Administrator's Guide . See Also: For the list and description of all the database resident connection pooling parameters that can be configured using this procedure, see the Oracle Database Administrator's Guide . Exceptions Table 39-3 ALTER_PARAM Procedure Exceptions Exception Description ORA-56500 Connection pool not found ORA-56504 Invalid connection pool configuration parameter name ORA-56505 Invalid connection pool configuration parameter value ORA-56507 Connection pool alter configuration failed Examples DBMS_CONNECTION_POOL.ALTER_PARAM( 'SYS_DEFAULT_CONNECTION_POOL', 'MAX_LIFETIME_SESSION', '120');