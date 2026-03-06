---
id: 19c__UTL_HTTP.SET_FOLLOW_REDIRECT
name: UTL_HTTP.SET_FOLLOW_REDIRECT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_FOLLOW_REDIRECT

This procedure sets the maximum number of times UTL_HTTP follows the HTTP redirect instruction in the HTTP response to this request, or future requests, in the GET_RESPONSE function.

## Syntax

```sql
UTL_HTTP.SET_FOLLOW_REDIRECT (
   max_redirects  IN PLS_INTEGER DEFAULT 3);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r |  |  | The HTTP request |
| max_redirects | PLS_INTEGER | IN | The maximum number of redirects. Set to zero to disable redirects. |

## Usage Notes

See Also: HTTP Requests and HTTP Requests Subprograms Session Settings and Session Settings Subprograms See Also: HTTP Requests and HTTP Requests Subprograms Session Settings and Session Settings Subprograms Syntax Use this procedure to set the maximum number of redirections: UTL_HTTP.SET_FOLLOW_REDIRECT ( max_redirects IN PLS_INTEGER DEFAULT 3); Use this procedure to change the maximum number of redirections a request inherits from the session default setting: UTL_HTTP.SET_FOLLOW_REDIRECT( r IN OUT NOCOPY req, max_redirects IN PLS_INTEGER DEFAULT 3); Parameters Table 264-52 SET_FOLLOW_REDIRECT Procedure Parameters Parameter Description r The HTTP request max_redirects The maximum number of redirects. Set to zero to disable redirects. Usage Notes If max_redirects is set to a positive number, the GET_RESPONSE Function will automatically follow the redirected URL for the HTTP response status code 301, 302, and 307 for the HTTP HEAD and GET methods, and 303 for all HTTP methods, and retry the HTTP request (the request method will be changed to HTTP GET for the status code 303) at the new location. It follows the redirection until the final, non-redirect location is reached, or an error occurs, or the maximum number of redirections has been reached (to prevent an infinite loop). The URL and method fields in the REQ record will be updated to the last redirected URL and the method used to access the URL. Set the maximum number of redirects to zero to disable automatic redirection. While it is set not to follow redirect automatically in the current session, it is possible to specify individual HTTP requests to follow redirect instructions the function FOLLOW_REDIRECT and vice versa. The default maximum number of redirections in a database user session is 3. The default value affects only future requests and has no effect on existing requests. The SET_FOLLOW_REDIRECT procedure must be called before GET_RESPONSE for any redirection to take effect.