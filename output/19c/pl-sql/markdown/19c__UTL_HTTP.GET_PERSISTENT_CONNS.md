---
id: 19c__UTL_HTTP.GET_PERSISTENT_CONNS
name: UTL_HTTP.GET_PERSISTENT_CONNS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_PERSISTENT_CONNS

This procedure returns all the network connections currently kept persistent by the UTL_HTTP package to the Web servers.

## Syntax

```sql
UTL_HTTP.get_persistent_conns (
   connections  IN OUT NOCOPY connection_table);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| connections | NOCOPY | IN OUT | The network connections kept persistent |

## Usage Notes

See Also: HTTP Persistent Connections and HTTP Persistent Connections Subprograms See Also: HTTP Persistent Connections and HTTP Persistent Connections Subprograms Syntax UTL_HTTP.get_persistent_conns ( connections IN OUT NOCOPY connection_table); Parameters Table 264-37 GET_PERSISTENT_CONNS Procedure Parameters Parameter Description connections The network connections kept persistent Usage Notes Connections to the same Web server at different TCP/IP ports are counted individually. The host names of the Web servers are identified as specified in the URL of the original HTTP requests. Therefore, fully qualified host names with domain names will be counted differently from the host names without domain names.