---
id: 19c__UTL_HTTP.GET_HEADER
name: UTL_HTTP.GET_HEADER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_HEADER

This procedure returns the n th HTTP response header name and value returned in the response.

## Syntax

```sql
UTL_HTTP.GET_HEADER (
   r      IN OUT NOCOPY resp,
   n      IN PLS_INTEGER,
   name   OUT NOCOPY VARCHAR2,
   value  OUT NOCOPY VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP response |
| n | PLS_INTEGER | IN | The n th header to return |
| name | NOCOPY | OUT | The name of the HTTP response header |
| value | NOCOPY | OUT | The value of the HTTP response header |

## Usage Notes

See Also: HTTP Responses and HTTP Responses Subprograms See Also: HTTP Responses and HTTP Responses Subprograms Syntax UTL_HTTP.GET_HEADER ( r IN OUT NOCOPY resp, n IN PLS_INTEGER, name OUT NOCOPY VARCHAR2, value OUT NOCOPY VARCHAR2); Parameters Table 264-33 GET_HEADER Procedure Parameters Parameter Description r The HTTP response n The n th header to return name The name of the HTTP response header value The value of the HTTP response header Usage Notes If the response body returned by the remote Web server is encoded in chunked transfer encoding format, the trailer headers that are returned at the end of the response body will be added to the response, and the response header count will be updated. You can retrieve the additional headers after the end of the response body is reached and before you end the response.