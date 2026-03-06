---
id: 19c__UTL_HTTP.GET_FOLLOW_REDIRECT
name: UTL_HTTP.GET_FOLLOW_REDIRECT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_FOLLOW_REDIRECT

This procedure retrieves the follow-redirect setting in the current session

## Syntax

```sql
UTL_HTTP.GET_FOLLOW_REDIRECT (
   max_redirects  OUT PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| max_redirects | PLS_INTEGER) | OUT | The maximum number of redirections for all future HTTP requests |

## Usage Notes

See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.GET_FOLLOW_REDIRECT ( max_redirects OUT PLS_INTEGER); Parameters Table 264-32 GET_FOLLOW_REDIRECT Procedure Parameters Parameter Description max_redirects The maximum number of redirections for all future HTTP requests