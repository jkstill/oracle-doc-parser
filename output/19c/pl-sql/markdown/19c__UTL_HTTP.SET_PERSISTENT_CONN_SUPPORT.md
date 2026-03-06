---
id: 19c__UTL_HTTP.SET_PERSISTENT_CONN_SUPPORT
name: UTL_HTTP.SET_PERSISTENT_CONN_SUPPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_PERSISTENT_CONN_SUPPORT

This overloaded procedure provides persistent connection support. Descriptions of the different functionality are given in the syntax declarations.

## Syntax

```sql
UTL_HTTP.SET_PERSISTENT_CONN_SUPPORT(
   enable      IN BOOLEAN DEFAULT FALSE,
   max_conns   IN PLS_INTEGER DEFAULT 0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enable | BOOLEAN | IN | TRUE to keep the network connection persistent. FALSE otherwise. |
| maximum_conns |  |  | Maximum number of connections |
| r |  |  | The HTTP request |

## Usage Notes

See Also: HTTP Requests and HTTP Requests Subprograms See Also: HTTP Requests and HTTP Requests Subprograms Syntax Sets whether future HTTP requests should support the HTTP 1.1 persistent connection or not, and the maximum numbers of persistent connections to be maintained in the current database user session. UTL_HTTP.SET_PERSISTENT_CONN_SUPPORT( enable IN BOOLEAN DEFAULT FALSE, max_conns IN PLS_INTEGER DEFAULT 0); Enables or disables support for the HTTP 1.1 persistent-connection in the request. UTL_HTTP.SET_PERSISTENT_CONN_SUPPORT( r IN OUT NOCOPY req, enable IN BOOLEAN DEFAULT FALSE); Parameters Table 264-54 SET_PERSISTENT_CONN_SUPPORT Procedure Parameters Parameter Description enable TRUE to keep the network connection persistent. FALSE otherwise. maximum_conns Maximum number of connections r The HTTP request Usage Notes If the persistent-connection support is enabled for an HTTP request, the package will keep the network connections to a Web server or the proxy server open in the package after the request is completed properly for a subsequent request to the same server to reuse for each HTTP 1.1 protocol specification. With the persistent connection support, subsequent HTTP requests may be completed faster because the network connection latency is avoided. If the persistent-connection support is disabled for a request, the package will always send the HTTP header "Connection: close" automatically in the HTTP request and close the network connection when the request is completed. This setting has no effect on HTTP requests that follows HTTP 1.0 protocol, for which the network connections will always be closed after the requests are completed. When a request is being made, the package attempts to reuse an existing persistent connection to the target Web server (or proxy server) if one is available. If none is available, a new network connection will be initiated. The persistent-connection support setting for a request affects only whether the network connection should be closed after a request completes. Use this procedure to change the persistent-connection support setting a request inherits from the session default setting. Users should note that while the use of persistent connections in UTL_HTTP may reduce the time it takes to fetch multiple Web pages from the same server, it consumes precious system resources (network connections) in the database server. Also, excessive use of persistent connections may reduce the scalability of the database server when too many network connections are kept open in the database server. Network connections should be kept open only if they will be used immediately by subsequent requests and should be closed immediately when they are no longer needed. Set the default persistent connection support as disabled in the session, and enable persistent connection in individual HTTP requests as shown in " Examples " .