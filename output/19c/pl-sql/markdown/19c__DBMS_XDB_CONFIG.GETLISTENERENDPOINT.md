---
id: 19c__DBMS_XDB_CONFIG.GETLISTENERENDPOINT
name: DBMS_XDB_CONFIG.GETLISTENERENDPOINT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.GETLISTENERENDPOINT

This procedure retrieves the parameters of a listener end point corresponding to the XML DB HTTP server. The parameters of both HTTP and HTTP2 end points can be retrieved by invoking this procedure.

## Syntax

```sql
DBMS_XDB_CONFIG.GETLISTENERENDPOINT (
   endpoint  IN   NUMBER, 
   host      OUT  VARCHAR2,    port      OUT  NUMBER, 
   protocol  OUT  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| endpoint | NUMBER | IN | End point to be retrieved. Its value can be XDB_ENDPOINT_HTTP or XDB_ENDPOINT_HTTP2 . |
| host | VARCHAR2 | OUT | Interface on which the listener end point listens |
| port | NUMBER | OUT | Port on which the listener end point listens |
| protocol | NUMBER) | OUT | Transport protocol accepted by the listener end point |

## Usage Notes

Syntax DBMS_XDB_CONFIG.GETLISTENERENDPOINT ( endpoint IN NUMBER, host OUT VARCHAR2, port OUT NUMBER, protocol OUT NUMBER); Parameters Table 196-18 GETLISTENERENDPOINT Procedure Parameters Parameter Description endpoint End point to be retrieved. Its value can be XDB_ENDPOINT_HTTP or XDB_ENDPOINT_HTTP2 . host Interface on which the listener end point listens port Port on which the listener end point listens protocol Transport protocol accepted by the listener end point