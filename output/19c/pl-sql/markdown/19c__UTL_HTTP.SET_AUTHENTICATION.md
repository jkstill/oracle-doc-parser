---
id: 19c__UTL_HTTP.SET_AUTHENTICATION
name: UTL_HTTP.SET_AUTHENTICATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_AUTHENTICATION

This procedure sets HTTP authentication information in the HTTP request header. The Web server needs this information to authorize the request.

## Syntax

```sql
UTL_HTTP.SET_AUTHENTICATION(
   r         IN OUT NOCOPY req,
   username  IN VARCHAR2,
   password  IN VARCHAR2,
   scheme    IN VARCHAR2 DEFAULT 'Basic',
   for_proxy IN BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | HTTP request |
| username | VARCHAR2 | IN | Username for the HTTP authentication |
| password | VARCHAR2 | IN | Password for the HTTP authentication |
| scheme | VARCHAR2 | IN | HTTP authentication scheme. Either Basic for the HTTP basic or AWS for Amazon S3 authentication scheme. Default is basic. |
| for_proxy | BOOLEAN | IN | Identifies if the HTTP authentication information is for access to the HTTP proxy server instead of the Web server. Default is FALSE . |

## Usage Notes

See Also: HTTP Requests and HTTP Requests Subprograms See Also: HTTP Requests and HTTP Requests Subprograms Syntax UTL_HTTP.SET_AUTHENTICATION( r IN OUT NOCOPY req, username IN VARCHAR2, password IN VARCHAR2, scheme IN VARCHAR2 DEFAULT 'Basic', for_proxy IN BOOLEAN DEFAULT FALSE); Parameters Table 264-47 SET_AUTHENTICATION Procedure Parameters Parameter Description r HTTP request username Username for the HTTP authentication password Password for the HTTP authentication scheme HTTP authentication scheme. Either Basic for the HTTP basic or AWS for Amazon S3 authentication scheme. Default is basic. for_proxy Identifies if the HTTP authentication information is for access to the HTTP proxy server instead of the Web server. Default is FALSE . Usage Notes The supported authentication schemes are HTTP basic and Amazon S3 authentication.