---
id: 19c__UTL_HTTP.READ_TEXT
name: UTL_HTTP.READ_TEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.READ_TEXT

This procedure reads the HTTP response body in text form and returns the output in the caller-supplied buffer.

## Syntax

```sql
UTL_HTTP.READ_TEXT(
   r     IN OUT NOCOPY resp,
   data  OUT NOCOPY VARCHAR2 CHARACTER SET ANY_CS,
   len   IN PLS_INTEGER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP response |
| data | NOCOPY | OUT | The HTTP response body in text form |
| len | PLS_INTEGER | IN | The maximum number of characters of data to read. If len is NULL, this procedure will read as much input as possible to fill the buffer allocated in data . The actual amount of data returned may be less than that specified if little data is available before the end of the HTTP response body is reached or the transfer_timeout amount of time has elapsed. The default is NULL. |

## Usage Notes

The end_of_body exception is raised if the end of the HTTP response body is reached. Text data is automatically converted from the response body character set to the database character set. See Also: HTTP Responses and HTTP Responses Subprograms See Also: HTTP Responses and HTTP Responses Subprograms Syntax UTL_HTTP.READ_TEXT( r IN OUT NOCOPY resp, data OUT NOCOPY VARCHAR2 CHARACTER SET ANY_CS, len IN PLS_INTEGER DEFAULT NULL); Parameters Table 264-44 READ_TEXT Procedure Parameters Parameter Description r The HTTP response data The HTTP response body in text form len The maximum number of characters of data to read. If len is NULL, this procedure will read as much input as possible to fill the buffer allocated in data . The actual amount of data returned may be less than that specified if little data is available before the end of the HTTP response body is reached or the transfer_timeout amount of time has elapsed. The default is NULL. Usage Notes The UTL_HTTP package supports HTTP 1.1 chunked transfer-encoding. When the response body is returned in chunked transfer-encoding format as indicated in the response header, the package automatically decodes the chunks and returns the response body in de-chunked format. If transfer timeout is set in the request of this response, read_text waits for each data packet to be ready to read until timeout occurs. If it occurs, this procedure stops reading and returns all the data read successfully. If no data is read successfully, the transfer_timeout exception is raised. The exception can be handled and the read operation can be retried later. If a partial multibyte character is found at the end of the response body, read_text stops reading and returns all the complete multibyte characters read successfully. If no complete character is read successfully, the partial_multibyte_char exception is raised. The exception can be handled and the bytes of that partial multibyte character can be read as binary by the read_raw procedure. If a partial multibyte character is seen in the middle of the response body because the remaining bytes of the character have not arrived and read timeout occurs, the transfer_timeout exception is raised instead. The exception can be handled and the read operation can be retried later. When the Content-Type response header specifies the character set of the response body and the character set is unknown or unsupported by Oracle, the " ORA-01482: unsupported character set " exception is raised if you try to read the response body as text. You can either read the response body as binary using the READ_RAW procedure, or set the character set of the response body explicitly using the SET_BODY_CHARSET procedure and read the response body as text again.