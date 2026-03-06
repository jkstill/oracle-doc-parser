---
id: 19c__UTL_HTTP.READ_RAW
name: UTL_HTTP.READ_RAW
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.READ_RAW

This procedure reads the HTTP response body in binary form and returns the output in the caller-supplied buffer.

## Syntax

```sql
UTL_HTTP.READ_RAW(
   r     IN OUT NOCOPY resp,
   data  OUT NOCOPY RAW,
   len   IN PLS_INTEGER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP response |
| data | NOCOPY | OUT | The HTTP response body in binary form |
| len | PLS_INTEGER | IN | The number of bytes of data to read. If len is NULL , this procedure will read as much input as possible to fill the buffer allocated in data . The actual amount of data returned may be less than that specified if not much data is available before the end of the HTTP response body is reached or the transfer_timeout amount of time has elapsed. The default is NULL |

## Usage Notes

The end_of_body exception is raised if the end of the HTTP response body is reached. See Also: HTTP Responses and HTTP Responses Subprograms See Also: HTTP Responses and HTTP Responses Subprograms Syntax UTL_HTTP.READ_RAW( r IN OUT NOCOPY resp, data OUT NOCOPY RAW, len IN PLS_INTEGER DEFAULT NULL); Parameters Table 264-43 READ_RAW Procedure Parameters Parameter Description r The HTTP response data The HTTP response body in binary form len The number of bytes of data to read. If len is NULL , this procedure will read as much input as possible to fill the buffer allocated in data . The actual amount of data returned may be less than that specified if not much data is available before the end of the HTTP response body is reached or the transfer_timeout amount of time has elapsed. The default is NULL Usage Notes The UTL_HTTP package supports HTTP 1.1 chunked transfer-encoding. When the response body is returned in chunked transfer-encoding format as indicated in the response header, the package automatically decodes the chunks and returns the response body in de-chunked format. If transfer timeout is set in the request of this response, read_raw waits for each data packet to be ready to read until timeout occurs. If it occurs, read_raw stops reading and returns all the data read successfully. If no data is read successfully, the transfer_timeout exception is raised. The exception can be handled and the read operation can be retried later.