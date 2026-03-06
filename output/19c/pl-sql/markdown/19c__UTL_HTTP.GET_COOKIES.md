---
id: 19c__UTL_HTTP.GET_COOKIES
name: UTL_HTTP.GET_COOKIES
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_COOKIES

This function returns all the cookies maintained either in a request context or in the UTL_HTTP package's session state.

## Syntax

```sql
UTL_HTTP.GET_COOKIES (
   cookies          IN  OUT NOCOPY cookie_table,
   request_context  IN             request_context_key DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cookies | NOCOPY | IN  OUT | The cookies returned |
| request_context | request_context_key | IN | Request context to return the cookies for. If NULL , the cookies maintained in the UTL_HTTP package's session state will be returned instead. |

**Returns:** `UNKNOWN`

## Usage Notes

See Also: HTTP Cookies and HTTP Cookies Subprograms See Also: HTTP Cookies and HTTP Cookies Subprograms Syntax UTL_HTTP.GET_COOKIES ( cookies IN OUT NOCOPY cookie_table, request_context IN request_context_key DEFAULT NULL); Parameters Table 264-30 GET_COOKIES Function Parameters Parameter Description cookies The cookies returned request_context Request context to return the cookies for. If NULL , the cookies maintained in the UTL_HTTP package's session state will be returned instead.