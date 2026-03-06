---
id: 19c__UTL_HTTP.CLEAR_COOKIES
name: UTL_HTTP.CLEAR_COOKIES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.CLEAR_COOKIES

This procedure clears all the cookies maintained either in a request context or in the UTL_HTTP package's session state.

## Syntax

```sql
UTL_HTTP.CLEAR_COOKIES (
   request_context  IN  request_context_key DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| request_context | request_context_key | IN | Request context to clear the cookies. If NULL , the cookies maintained in the UTL_HTTP package's session state will be cleared instead. |

## Usage Notes

See Also: HTTP Cookies and HTTP Cookies Subprograms See Also: HTTP Cookies and HTTP Cookies Subprograms Syntax UTL_HTTP.CLEAR_COOKIES ( request_context IN request_context_key DEFAULT NULL); Parameters Table 264-19 CLEAR_COOKIES Procedure Parameters Parameter Description request_context Request context to clear the cookies. If NULL , the cookies maintained in the UTL_HTTP package's session state will be cleared instead.