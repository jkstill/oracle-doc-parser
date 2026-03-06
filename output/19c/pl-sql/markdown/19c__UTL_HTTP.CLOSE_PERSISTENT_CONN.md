---
id: 19c__UTL_HTTP.CLOSE_PERSISTENT_CONN
name: UTL_HTTP.CLOSE_PERSISTENT_CONN
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.CLOSE_PERSISTENT_CONN

This procedure closes an HTTP persistent connection maintained by the UTL_HTTP package in the current database session.

## Syntax

```sql
UTL_HTTP.CLOSE_PERSISTENT_CONN (
   conn  IN connection);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| conn | connection) | IN | The HTTP persistent connection to close |

## Usage Notes

See Also: HTTP Persistent Connections and HTTP Persistent Connections Subprograms See Also: HTTP Persistent Connections and HTTP Persistent Connections Subprograms Syntax UTL_HTTP.CLOSE_PERSISTENT_CONN ( conn IN connection); Parameters Table 264-20 CLOSE_PERSISTENT_CONN Procedure Parameters Parameter Description conn The HTTP persistent connection to close