---
id: 19c__UTL_HTTP.GET_PERSISTENT_CONN_COUNT
name: UTL_HTTP.GET_PERSISTENT_CONN_COUNT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_PERSISTENT_CONN_COUNT

This function returns the number of network connections currently kept persistent by the UTL_HTTP package to the Web servers.

## Syntax

```sql
UTL_HTTP.GET_PERSISTENT_CONN_COUNT 
RETURN PLS_INTEGER;
```

**Returns:** `PLS_INTEGER`

## Usage Notes

See Also: HTTP Persistent Connections and HTTP Persistent Connections Subprograms See Also: HTTP Persistent Connections and HTTP Persistent Connections Subprograms Syntax UTL_HTTP.GET_PERSISTENT_CONN_COUNT RETURN PLS_INTEGER; Usage Notes Connections to the same Web server at different TCP/IP ports are counted individually. The host names of the Web servers are identified as specified in the URL of the original HTTP requests. Therefore, fully qualified host names with domain names will be counted differently from the host names without domain names.