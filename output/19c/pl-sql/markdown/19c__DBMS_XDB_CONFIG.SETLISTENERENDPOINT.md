---
id: 19c__DBMS_XDB_CONFIG.SETLISTENERENDPOINT
name: DBMS_XDB_CONFIG.SETLISTENERENDPOINT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XDB_CONFIG
tags: [dbms_xdb_config]
source_file: DBMS_XDB_CONFIG.html
---

# DBMS_XDB_CONFIG.SETLISTENERENDPOINT

This procedure sets the parameters of a listener end point corresponding to the XML DB HTTP server.

## Syntax

```sql
DBMS_XDB_CONFIG.SETLISTENERENDPOINT (
   endpoint  IN  NUMBER, 
   host      IN  VARCHAR2,    port      IN  NUMBER, 
   protocol  IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| endpoint | NUMBER | IN | End point to be set. Its value can be XDB_ENDPOINT_HTTP or XDB_ENDPOINT_HTTP2 . |
| host | VARCHAR2 | IN | Interface on which the listener end point is to listen. Its value can be ' LOCALHOST ,' NULL , or a hostname. If its value is ' LOCALHOST ' the listener end point is permitted to only listen on the localhost interface. If its value is NULL or hostname, the listener end point is permitted to listen on both localhost and non-localhost interfaces. |
| port | NUMBER | IN | Port on which the listener end point is to listen |
| protocol | NUMBER) | IN | Transport protocol that the listener end point is to accept. Its value can be XDB_PROTOCOL_TCP or XDB_PROTOCOL_TCPS |

## Usage Notes

Both HTTP and HTTP2 end points can be set by invoking this procedure. Syntax DBMS_XDB_CONFIG.SETLISTENERENDPOINT ( endpoint IN NUMBER, host IN VARCHAR2, port IN NUMBER, protocol IN NUMBER); Parameters Table 196-24 SETLISTENERENDPOINT Procedure Parameters Parameter Description endpoint End point to be set. Its value can be XDB_ENDPOINT_HTTP or XDB_ENDPOINT_HTTP2 . host Interface on which the listener end point is to listen. Its value can be ' LOCALHOST ,' NULL , or a hostname. If its value is ' LOCALHOST ' the listener end point is permitted to only listen on the localhost interface. If its value is NULL or hostname, the listener end point is permitted to listen on both localhost and non-localhost interfaces. port Port on which the listener end point is to listen protocol Transport protocol that the listener end point is to accept. Its value can be XDB_PROTOCOL_TCP or XDB_PROTOCOL_TCPS