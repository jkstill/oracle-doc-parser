---
id: 19c__UTL_HTTP.GET_PERSISTENT_CONN_SUPPORT
name: UTL_HTTP.GET_PERSISTENT_CONN_SUPPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_PERSISTENT_CONN_SUPPORT

This procedure checks if the persistent connection support is enabled, and gets the maximum number of persistent connections in the current session.

## Syntax

```sql
UTL_HTTP.GET_PERSISTENT_CONN_SUPPORT (
   enable     OUT BOOLEAN,
   max_conns  OUT PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enable | BOOLEAN | OUT | TRUE if persistent connection support is enabled; otherwise FALSE |
| max_conns | PLS_INTEGER) | OUT | the maximum number of persistent connections maintained in the current session |

## Usage Notes

See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.GET_PERSISTENT_CONN_SUPPORT ( enable OUT BOOLEAN, max_conns OUT PLS_INTEGER); Parameters Table 264-36 GET_PERSISTENT_CONN_SUPPORT Procedure Parameters Parameter Description enable TRUE if persistent connection support is enabled; otherwise FALSE max_conns the maximum number of persistent connections maintained in the current session