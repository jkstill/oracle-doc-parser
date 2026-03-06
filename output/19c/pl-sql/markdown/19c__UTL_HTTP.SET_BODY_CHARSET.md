---
id: 19c__UTL_HTTP.SET_BODY_CHARSET
name: UTL_HTTP.SET_BODY_CHARSET
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_BODY_CHARSET

This procedure is overloaded. The description of different functionality is located alongside the syntax declarations.

## Syntax

```sql
UTL_HTTP.SET_BODY_CHARSET (
   charset  IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r |  |  | The HTTP response. |
| charset | VARCHAR2 | IN | The default character set of the response body. The character set can be in Oracle or Internet Assigned Numbers Authority (IANA) naming convention. If charset is NULL , the database character set is assumed. |

## Usage Notes

See Also: HTTP Responses and HTTP Responses Subprograms Session Settings and Session Settings Subprograms See Also: HTTP Responses and HTTP Responses Subprograms Session Settings and Session Settings Subprograms Syntax Sets the default character set of the body of all future HTTP requests when the media type is text and the character set is not specified in the Content-Type header. Following the HTTP protocol standard specification, if the media type of a request or a response is text , but the character set information is missing in the Content-Type header, the character set of the request or response body should default to ISO-8859-1 . A response created for a request inherits the default body character set of the request instead of the body character set of the current session. The default body character set is ISO-8859-1 in a database user session. The default body character set setting affects only future requests and has no effect on existing requests. After a request is created, the body character set can be changed by using the other SET_BODY_CHARSET procedure that operates on a request: UTL_HTTP.SET_BODY_CHARSET ( charset IN VARCHAR2 DEFAULT NULL); Sets the character set of the request body when the media type is text but the character set is not specified in the Content-Type header. According to the HTTP protocol standard specification, if the media type of a request or a response is "text" but the character set information is missing in the Content-Type header, the character set of the request or response body should default to " ISO-8859-1 ". Use this procedure to change the default body character set a request inherits from the session default setting: UTL_HTTP.SET_BODY_CHARSET( r IN OUT NOCOPY req, charset IN VARCHAR2 DEFAULT NULL); Sets the character set of the response body when the media type is "text" but the character set is not specified in the Content-Type header. For each the HTTP protocol standard specification, if the media type of a request or a response is "text" but the character set information is missing in the Content-Type header, the character set of the request or response body should default to "ISO-8859-1". Use this procedure to change the default body character set a response inherits from the request: UTL_HTTP.SET_BODY_CHARSET( r IN OUT NOCOPY resp, charset IN VARCHAR2 DEFAULT NULL); Parameters Table 264-49 SET_BODY_CHARSET Procedure Parameters Parameter Description r The HTTP response. charset The default character set of the response body. The character set can be in Oracle or Internet Assigned Numbers Authority (IANA) naming convention. If charset is NULL , the database character set is assumed.