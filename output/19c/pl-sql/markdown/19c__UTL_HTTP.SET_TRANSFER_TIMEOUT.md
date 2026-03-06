---
id: 19c__UTL_HTTP.SET_TRANSFER_TIMEOUT
name: UTL_HTTP.SET_TRANSFER_TIMEOUT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_TRANSFER_TIMEOUT

This procedure sets the default time out value for all future HTTP requests that the UTL_HTTP package should attempt while reading the HTTP response from the Web server or proxy server.

## Syntax

```sql
UTL_HTTP.SET_TRANSFER_TIMEOUT (
   timeout  IN PLS_INTEGER DEFAULT 60);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| timeout | PLS_INTEGER | IN | The network transfer timeout value in seconds. |

## Usage Notes

This time out value may be used to avoid the PL/SQL programs from being blocked by busy Web servers or heavy network traffic while retrieving Web pages from the Web servers. See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.SET_TRANSFER_TIMEOUT ( timeout IN PLS_INTEGER DEFAULT 60); Parameters Table 264-57 SET_TRANSFER_TIMEOUT Procedure Parameters Parameter Description timeout The network transfer timeout value in seconds. Usage Notes The default value of the time out is 60 seconds.