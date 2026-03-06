---
id: 19c__UTL_HTTP.END_REQUEST
name: UTL_HTTP.END_REQUEST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.END_REQUEST

This procedure ends the HTTP request. To terminate the HTTP request without completing the request and waiting for the response, the program can call this procedure. Otherwise, the program should go through the normal sequence of beginning a request, getting the response, and closing the response. The network connection will always be closed and will not be reused.

## Syntax

```sql
UTL_HTTP.END_REQUEST (
   r  IN OUT NOCOPY req);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP request |

## Usage Notes

See Also: HTTP Requests and HTTP Requests Subprograms See Also: HTTP Requests and HTTP Requests Subprograms Syntax UTL_HTTP.END_REQUEST ( r IN OUT NOCOPY req); Parameters Table 264-24 END_REQUEST Procedure Parameters Parameter Description r The HTTP request