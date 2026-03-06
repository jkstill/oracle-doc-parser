---
id: 19c__UTL_HTTP.GET_RESPONSE
name: UTL_HTTP.GET_RESPONSE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_RESPONSE

This function reads the HTTP response.

## Syntax

```sql
UTL_HTTP.GET_RESPONSE (
   r                       IN OUT NOCOPY req,
   return_info_response    IN BOOLEAN DEFAULT FALSE) 
RETURN resp;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP response |
| return_info_response | BOOLEAN | IN | Return 100 informational response or not. TRUE means get_response should return 100 informational response when it is received from the HTTP server. The request will not be ended if a 100 response is returned. FALSE means the API should ignore any 100 informational response received from the HTTP server and should return the following non-100 response instead. The default is FALSE . |

**Returns:** `resp`

## Usage Notes

When the function returns, the status line and the HTTP response headers have been read and processed. The status code, reason phrase, and the HTTP protocol version are stored in the response record. This function completes the HTTP headers section. See Also: HTTP Responses and HTTP Responses Subprograms See Also: HTTP Responses and HTTP Responses Subprograms Syntax UTL_HTTP.GET_RESPONSE ( r IN OUT NOCOPY req, return_info_response IN BOOLEAN DEFAULT FALSE) RETURN resp; Parameters Table 264-39 GET_RESPONSE Function Parameters Parameter Description r The HTTP response return_info_response Return 100 informational response or not. TRUE means get_response should return 100 informational response when it is received from the HTTP server. The request will not be ended if a 100 response is returned. FALSE means the API should ignore any 100 informational response received from the HTTP server and should return the following non-100 response instead. The default is FALSE . Exceptions When detailed-exception is disabled: ORA-29273 REQUEST_FAILED - the request fails to execute. Use the GET_DETAILED_EXCP_SUPPORT Procedure and the GET_DETAILED_SQLERRM Function to get the detailed error message. When detailed-exception is enabled: ORA-29261 BAD_ARGUMENT - some arguments passed are not valid When response error check is enabled: ORA-29268 HTTP_CLIENT_ERROR - the response code is in 400 range ORA-29269 HTTP_SERVER_ERROR - the response code is in 500 range