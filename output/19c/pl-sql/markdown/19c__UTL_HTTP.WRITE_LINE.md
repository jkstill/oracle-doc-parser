---
id: 19c__UTL_HTTP.WRITE_LINE
name: UTL_HTTP.WRITE_LINE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.WRITE_LINE

This procedure writes a text line in the HTTP request body and ends the line with new-line characters (CRLF as defined in UTL_TCP ).

## Syntax

```sql
UTL_HTTP.WRITE_LINE(
   r     IN OUT NOCOPY req,
   data  IN VARCHAR2 CHARACTER SET ANY_CS);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP request |
| data | VARCHAR2 | IN | The text line to send in the HTTP request body |

## Usage Notes

As soon as some data is sent as the HTTP request body, the HTTP request headers section is completed. Text data is automatically converted from the database character set to the request body character set. See Also: HTTP Requests and HTTP Requests Subprograms See Also: HTTP Requests and HTTP Requests Subprograms Syntax UTL_HTTP.WRITE_LINE( r IN OUT NOCOPY req, data IN VARCHAR2 CHARACTER SET ANY_CS); Parameters Table 264-59 WRITE_LINE Procedure Parameters Parameter Description r The HTTP request data The text line to send in the HTTP request body Usage Notes An HTTP client must always let the remote Web server know the length of the request body it is sending. If the amount of data is known beforehand, you can set the Content-Length header in the request, where the length of the content is measured in bytes instead of characters. If the length of the request body is not known beforehand, you can send the request body using the HTTP 1.1 chunked transfer-encoding format. The request body is sent in chunks, where the length of each chunk is sent before the chunk is sent. The UTL_HTTP package performs chunked transfer-encoding on the request body transparently when the Transfer-Encoding: chunked header is set. Note that some HTTP-1.1-based Web servers or CGI programs do not support or accept the request body encoding in the HTTP 1.1 chunked transfer-encoding format. See the SET_HEADER procedure for details. If you send the Content-Length header, you should note that the length specified in the header should be the byte-length of the textual request body after it is converted from the database character set to the request body character set. When either one of the two character sets is a multibyte character set, the precise byte-length of the request body in the request body character set cannot be known beforehand. In this case, you can perform the character set conversion explicitly, determine the byte-length of the results, send the Content-Length header, and the results using the WRITE_RAW procedure to avoid the automatic character set conversion. Or, if the remove Web server or CGI programs allow, you can send the request body using the HTTP 1.1 chunked transfer-encoding format, where UTL_HTTP handles the length of the chunks transparently.