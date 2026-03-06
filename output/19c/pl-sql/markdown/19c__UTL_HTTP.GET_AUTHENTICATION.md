---
id: 19c__UTL_HTTP.GET_AUTHENTICATION
name: UTL_HTTP.GET_AUTHENTICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_AUTHENTICATION

This procedure retrieves the HTTP authentication information needed for the request to be accepted by the Web server as indicated in the HTTP response header.

## Syntax

```sql
UTL_HTTP.GET_AUTHENTICATION(
   r          IN OUT NOCOPY resp,
   scheme     OUT VARCHAR2,
   realm      OUT VARCHAR2,
   for_proxy  IN BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP response |
| scheme | VARCHAR2 | OUT | The scheme for the required HTTP authentication |
| realm | VARCHAR2 | OUT | The realm for the required HTTP authentication |
| for_proxy | BOOLEAN | IN | Returns the HTTP authentication information required for the access to the HTTP proxy server instead of the Web server? Default is FALSE |

## Usage Notes

See Also: HTTP Responses and HTTP Responses Subprograms See Also: HTTP Responses and HTTP Responses Subprograms Syntax UTL_HTTP.GET_AUTHENTICATION( r IN OUT NOCOPY resp, scheme OUT VARCHAR2, realm OUT VARCHAR2, for_proxy IN BOOLEAN DEFAULT FALSE); Parameters Table 264-26 GET_AUTHENTICATION Procedure Parameters Parameter Description r The HTTP response scheme The scheme for the required HTTP authentication realm The realm for the required HTTP authentication for_proxy Returns the HTTP authentication information required for the access to the HTTP proxy server instead of the Web server? Default is FALSE Usage Notes When a Web client is unaware that a document is protected, at least two HTTP requests are required for the document to be retrieved. In the first HTTP request, the Web client makes the request without supplying required authentication information; so the request is denied. The Web client can determine the authentication information required for the request to be authorized by calling GET_AUTHENTICATION . The Web client makes the second request and supplies the required authentication information with SET_AUTHORIZATION . If the authentication information can be verified by the Web server, the request will succeed and the requested document is returned. Before making the request, if the Web client knows that authentication information is required, it can supply the required authentication information in the first request, thus saving an extra request.