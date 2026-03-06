---
id: 19c__UTL_HTTP.SET_COOKIE_SUPPORT
name: UTL_HTTP.SET_COOKIE_SUPPORT
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_COOKIE_SUPPORT

This overloaded procedure handles cookie support. The description of different functionality is located alongside the syntax declarations.

## Syntax

```sql
UTL_HTTP.SET_COOKIE_SUPPORT(
   r       IN OUT NOCOPY REQ,
   enable  IN BOOLEAN DEFAULT TRUE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP request |
| enable | BOOLEAN | IN | Set enable to TRUE to enable HTTP cookie support; FALSE to disable |
| max_cookies |  |  | Sets the maximum total number of cookies maintained in the current session |
| max_cookies_per_site |  |  | Sets the maximum number of cookies maintained in the current session for each Web site |

## Usage Notes

See Also: HTTP Requests and HTTP Requests Subprograms Session Settings and Session Settings Subprograms See Also: HTTP Requests and HTTP Requests Subprograms Session Settings and Session Settings Subprograms Syntax Enables or disables support for the HTTP cookies in the request. Use this procedure to change the cookie support setting a request inherits from the session default setting: UTL_HTTP.SET_COOKIE_SUPPORT( r IN OUT NOCOPY REQ, enable IN BOOLEAN DEFAULT TRUE); Sets whether or not future HTTP requests will support HTTP cookies, and the maximum number of cookies maintained in the current database user session: UTL_HTTP.SET_COOKIE_SUPPORT ( enable IN BOOLEAN, max_cookies IN PLS_INTEGER DEFAULT 300, max_cookies_per_site IN PLS_INTEGER DEFAULT 20); Parameters Table 264-50 SET_COOKIE_SUPPORT Procedure Parameters Parameter Description r The HTTP request enable Set enable to TRUE to enable HTTP cookie support; FALSE to disable max_cookies Sets the maximum total number of cookies maintained in the current session max_cookies_per_site Sets the maximum number of cookies maintained in the current session for each Web site Usage Notes If cookie support is enabled for an HTTP request, all cookies saved in the current session and applicable to the request are returned to the Web server in the request in accordance with HTTP cookie specification standards. Cookies set in the response to the request are saved in the current session for return to the Web server in the subsequent requests if cookie support is enabled for those requests. If the cookie support is disabled for an HTTP request, no cookies are returned to the Web server in the request and the cookies set in the response to the request are not saved in the current session, although the Set-Cookie HTTP headers can still be retrieved from the response. Cookie support is enabled by default for all HTTP requests in a database user session. The default setting of the cookie support (enabled versus disabled) affects only the future requests and has no effect on the existing ones. After your request is created, the cookie support setting may be changed by using the other SET_COOKIE_SUPPORT procedure that operates on a request. The default maximum number of cookies saved in the current session is 20 for each site and 300 total. If you lower the maximum total number of cookies or the maximum number of cookies for each Web site, the oldest cookies will be purged first to reduce the number of cookies to the lowered maximum. HTTP cookies saved in the current session last for the duration of the database session only; there is no persistent storage for the cookies. Cookies saved in the current session are not cleared if you disable cookie support. See " Examples " for how to use GET_COOKIES and ADD_COOKIES to retrieve, save, and restore cookies.