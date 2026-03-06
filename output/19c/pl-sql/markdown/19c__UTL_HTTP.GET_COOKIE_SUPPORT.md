---
id: 19c__UTL_HTTP.GET_COOKIE_SUPPORT
name: UTL_HTTP.GET_COOKIE_SUPPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_COOKIE_SUPPORT

This procedure retrieves the current cookie support settings.

## Syntax

```sql
UTL_HTTP.GET_COOKIE_SUPPORT (
   enable                OUT BOOLEAN,
   max_cookies           OUT PLS_INTEGER,
   max_cookies_per_site  OUT PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enable | BOOLEAN | OUT | Indicates whether future HTTP requests should support HTTP cookies ( TRUE ) or not ( FALSE ) |
| max_cookies | PLS_INTEGER | OUT | Indicates the maximum total number of cookies maintained in the current session |
| max_cookies_per_site | PLS_INTEGER) | OUT | Indicates the maximum number of cookies maintained in the current session for each Web site |

## Usage Notes

See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.GET_COOKIE_SUPPORT ( enable OUT BOOLEAN, max_cookies OUT PLS_INTEGER, max_cookies_per_site OUT PLS_INTEGER); Parameters Table 264-29 GET_COOKIE_SUPPORT Procedure Parameters Parameter Description enable Indicates whether future HTTP requests should support HTTP cookies ( TRUE ) or not ( FALSE ) max_cookies Indicates the maximum total number of cookies maintained in the current session max_cookies_per_site Indicates the maximum number of cookies maintained in the current session for each Web site