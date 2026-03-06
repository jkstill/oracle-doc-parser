---
id: 19c__UTL_HTTP.ADD_COOKIES
name: UTL_HTTP.ADD_COOKIES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.ADD_COOKIES

This procedure adds the cookies either to a request context or to the UTL_HTTP package's session state.

## Syntax

```sql
UTL_HTTP.ADD_COOKIES (
   cookies          IN  cookie_table,
   request_context  IN  request_context_key DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| cookies | cookie_table | IN | The cookies to be added |
| request_context | request_context_key | IN | Request context to add the cookies. If NULL , the cookies will be added to the UTL_HTTP package's session state instead. |

## Usage Notes

See Also: HTTP Cookies and HTTP Cookies Subprograms See Also: HTTP Cookies and HTTP Cookies Subprograms Syntax UTL_HTTP.ADD_COOKIES ( cookies IN cookie_table, request_context IN request_context_key DEFAULT NULL); Parameters Table 264-17 ADD_COOKIES Procedure Parameters Parameter Description cookies The cookies to be added request_context Request context to add the cookies. If NULL , the cookies will be added to the UTL_HTTP package's session state instead. Usage Notes The cookies that the package currently maintains are not cleared before new cookies are added.