---
id: 19c__UTL_HTTP.GET_COOKIE_COUNT
name: UTL_HTTP.GET_COOKIE_COUNT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_COOKIE_COUNT

This function returns the number of cookies maintained either in a request context or in the UTL_HTTP package's session state.

## Syntax

```sql
UTL_HTTP.GET_COOKIE_COUNT (
   request_context  IN  request_context_key DEFAULT NULL) 
 RETURN PLS_INTEGER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| request_context | request_context_key | IN | Request context to return the cookie count for. If NULL , the cookie count maintained in the UTL_HTTP package's session state will be returned instead. |

**Returns:** `PLS_INTEGER`

## Usage Notes

See Also: HTTP Cookies and HTTP Cookies Subprograms See Also: HTTP Cookies and HTTP Cookies Subprograms Syntax UTL_HTTP.GET_COOKIE_COUNT ( request_context IN request_context_key DEFAULT NULL) RETURN PLS_INTEGER; Parameters Table 264-28 GET_COOKIE_COUNT Function Parameters Parameter Description request_context Request context to return the cookie count for. If NULL , the cookie count maintained in the UTL_HTTP package's session state will be returned instead.