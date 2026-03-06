---
id: 19c__UTL_HTTP.CLOSE_PERSISTENT_CONNS
name: UTL_HTTP.CLOSE_PERSISTENT_CONNS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.CLOSE_PERSISTENT_CONNS

This procedure closes a group of HTTP persistent connections maintained by the UTL_HTTP package in the current database session. This procedure uses a pattern-match approach to decide which persistent connections to close.

## Syntax

```sql
UTL_HTTP.CLOSE_PERSISTENT_CONNS(host => 'foobar');
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host |  |  | The host for which persistent connections are to be closed |
| port |  |  | The port number for which persistent connections are to be closed |
| proxy_host |  |  | The proxy host for which persistent connections are to be closed |
| proxy_port |  |  | The proxy port for which persistent connections are to be closed |
| ssl |  |  | Close persistent SSL connection |

## Usage Notes

To close a group of HTTP persistent connection that share a common property (for example, all connections to a particular host, or all SSL connections), set the particular parameters and leave the rest of the parameters NULL . If a particular parameter is set to NULL when this procedure is called, that parameter will not be used to decide which connections to close. For example, the following call to the procedure closes all persistent connections to foobar : UTL_HTTP.CLOSE_PERSISTENT_CONNS(host => 'foobar'); And the following call to the procedure closes all persistent connections through the foobar at TCP/IP port 80: UTL_HTTP.CLOSE_PERSISTENT_CONNS(proxy_host => 'foobar', proxy_port => 80); And the following call to the procedure closes all persistent connections: UTL_HTTP.CLOSE_PERSISTENT_CONNS; See Also: HTTP Persistent Connections and HTTP Persistent Connections Subprograms See Also: HTTP Persistent Connections and HTTP Persistent Connections Subprograms Syntax UTL_HTTP.CLOSE_PERSISTENT_CONNS ( host IN VARCHAR2 DEFAULT NULL, port IN PLS_INTEGER DEFAULT NULL, proxy_host IN VARCHAR2 DEFAULT NULL, proxy_port IN PLS_INTEGER DEFAULT NULL, ssl IN BOOLEAN DEFAULT NULL); Parameters Table 264-21 CLOSE_PERSISTENT_CONNS Procedure Parameters Parameter Description host The host for which persistent connections are to be closed port The port number for which persistent connections are to be closed proxy_host The proxy host for which persistent connections are to be closed proxy_port The proxy port for which persistent connections are to be closed ssl Close persistent SSL connection Usage Notes Connections to the same Web server at different TCP/IP ports are counted individually. The host names of the Web servers are identified as specified in the URL of the original HTTP requests. Therefore, fully qualified host names with domain names will be counted differently from the host names without domain names. Note that the use of a NULL value in a parameter when this procedure is called means that the caller does not care about its value when the package decides which persistent connection to close. If you want a NULL value in a parameter to match only a NULL value of the parameter of a persistent connection (which is when you want to close a specific persistent connection), you should use the CLOSE_PERSISTENT_CONN procedure that closes a specific persistent connection.