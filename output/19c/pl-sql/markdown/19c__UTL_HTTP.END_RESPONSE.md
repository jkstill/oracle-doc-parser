---
id: 19c__UTL_HTTP.END_RESPONSE
name: UTL_HTTP.END_RESPONSE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.END_RESPONSE

This procedure ends the HTTP response. It completes the HTTP request and response. Unless HTTP 1.1 persistent connection is used in this request, the network connection is also closed.

## Syntax

```sql
UTL_HTTP.END_RESPONSE (
   r  IN OUT NOCOPY resp);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP response |

## Usage Notes

See Also: HTTP Responses and HTTP Responses Subprograms See Also: HTTP Responses and HTTP Responses Subprograms Syntax UTL_HTTP.END_RESPONSE ( r IN OUT NOCOPY resp); Parameters Table 264-25 END_RESPONSE Procedure Parameters Parameter Description r The HTTP response