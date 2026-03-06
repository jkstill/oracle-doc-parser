---
id: 19c__UTL_HTTP.SET_RESPONSE_ERROR_CHECK
name: UTL_HTTP.SET_RESPONSE_ERROR_CHECK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_RESPONSE_ERROR_CHECK

This procedure sets whether or not GET_RESPONSE raises an exception when the Web server returns a status code that indicates an error—a status code in the 4xx or 5xx ranges.

## Syntax

```sql
UTL_HTTP.SET_RESPONSE_ERROR_CHECK (
   enable  IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enable | BOOLEAN | IN | TRUE to check for response errors; otherwise FALSE |

## Usage Notes

For example, when the requested URL is not found in the destination Web server, a 404 (document not found) response status code is returned. See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.SET_RESPONSE_ERROR_CHECK ( enable IN BOOLEAN DEFAULT FALSE); Parameters Table 264-56 SET_RESPONSE_ERROR_CHECK Procedure Parameters Parameter Description enable TRUE to check for response errors; otherwise FALSE Usage Notes If the status code indicates an error—a 4xx or 5xx code—and this procedure is enabled, GET_RESPONSE will raise the HTTP_CLIENT_ERROR or HTTP_SERVER_ERROR exception. If SET_RESPONSE_ERROR_CHECK is set to FALSE , GET_RESPONSE will not raise an exception when the status code indicates an error. Response error check is turned off by default. The GET_RESPONSE function can raise other exceptions when SET_RESPONSE_ERROR_CHECK is set to FALSE .