---
id: 19c__UTL_HTTP.SET_HEADER
name: UTL_HTTP.SET_HEADER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_HEADER

This procedure sets an HTTP request header. The request header is sent to the Web server as soon as it is set.

## Syntax

```sql
UTL_HTTP.SET_HEADER (
   r      IN OUT NOCOPY req,
   name   IN VARCHAR2,
   value  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP request |
| name | VARCHAR2 | IN | The name of the HTTP request header |
| value | VARCHAR2) | IN | The value of the HTTP request header |

## Usage Notes

See Also: HTTP Requests and HTTP Requests Subprograms See Also: HTTP Requests and HTTP Requests Subprograms Syntax UTL_HTTP.SET_HEADER ( r IN OUT NOCOPY req, name IN VARCHAR2, value IN VARCHAR2); Parameters Table 264-53 SET_HEADER Procedure Parameters Parameter Description r The HTTP request name The name of the HTTP request header value The value of the HTTP request header Usage Notes Multiple HTTP headers with the same name are allowed in the HTTP protocol standard. Therefore, setting a header does not replace a prior header with the same name. If the request is made using HTTP 1.1, UTL_HTTP sets the Host header automatically for you. When you set the Content-Type header with this procedure, UTL_HTTP looks for the character set information in the header value. If the character set information is present, it is set as the character set of the request body. It can be overridden later by using the SET_BODY_CHARSET procedure. When you set the Transfer-Encoding header with the value chunked, UTL_HTTP automatically encodes the request body written by the WRITE_TEXT, WRITE_LINE and WRITE_RAW procedures. Note that some HTTP-1.1-based Web servers or CGI programs do not support or accept the request body encoding in the HTTP 1.1 chunked transfer-encoding format.