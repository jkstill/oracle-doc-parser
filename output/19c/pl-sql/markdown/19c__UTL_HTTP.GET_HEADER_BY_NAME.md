---
id: 19c__UTL_HTTP.GET_HEADER_BY_NAME
name: UTL_HTTP.GET_HEADER_BY_NAME
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_HEADER_BY_NAME

This procedure returns the HTTP response header value returned in the response given the name of the header.

## Syntax

```sql
UTL_HTTP.GET_HEADER_BY_NAME(
   r      IN OUT NOCOPY resp,
   name   IN VARCHAR2,
   value  OUT NOCOPY VARCHAR2,
   n      IN PLS_INTEGER DEFAULT 1);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP response |
| name | VARCHAR2 | IN | The name of the HTTP response header for which the value is to return |
| value | NOCOPY | OUT | The value of the HTTP response header |
| n | PLS_INTEGER | IN | The n th occurrence of an HTTP response header by the specified name to return. The default is 1. |

## Usage Notes

See Also: HTTP Responses and HTTP Responses Subprograms See Also: HTTP Responses and HTTP Responses Subprograms Syntax UTL_HTTP.GET_HEADER_BY_NAME( r IN OUT NOCOPY resp, name IN VARCHAR2, value OUT NOCOPY VARCHAR2, n IN PLS_INTEGER DEFAULT 1); Parameters Table 264-34 GET_HEADER_BY_NAME Procedure Parameters Parameter Description r The HTTP response name The name of the HTTP response header for which the value is to return value The value of the HTTP response header n The n th occurrence of an HTTP response header by the specified name to return. The default is 1. Usage Notes If the response body returned by the remote Web server is encoded in chunked transfer encoding format, the trailer headers that are returned at the end of the response body will be added to the response, and the response header count will be updated. You can retrieve the additional headers after the end of the response body is reached and before you end the response.