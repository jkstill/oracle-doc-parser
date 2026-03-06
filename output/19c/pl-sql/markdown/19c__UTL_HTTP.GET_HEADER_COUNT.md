---
id: 19c__UTL_HTTP.GET_HEADER_COUNT
name: UTL_HTTP.GET_HEADER_COUNT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_HEADER_COUNT

This function returns the number of HTTP response headers returned in the response.

## Syntax

```sql
UTL_HTTP.GET_HEADER_COUNT (
   r  IN OUT NOCOPY resp) 
RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP response |

**Returns:** `PLS_INTEGER`

## Usage Notes

See Also: HTTP Responses and HTTP Responses Subprograms See Also: HTTP Responses and HTTP Responses Subprograms Syntax UTL_HTTP.GET_HEADER_COUNT ( r IN OUT NOCOPY resp) RETURN PLS_INTEGER; Parameters Table 264-35 GET_HEADER_COUNT Function Parameters Parameter Description r The HTTP response Usage Notes If the response body returned by the remote Web server is encoded in chunked transfer encoding format, the trailer headers that are returned at the end of the response body will be added to the response, and the response header count will be updated. You can retrieve the additional headers after the end of the response body is reached and before you end the response.