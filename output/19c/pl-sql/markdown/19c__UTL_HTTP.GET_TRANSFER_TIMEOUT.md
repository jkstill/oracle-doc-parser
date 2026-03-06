---
id: 19c__UTL_HTTP.GET_TRANSFER_TIMEOUT
name: UTL_HTTP.GET_TRANSFER_TIMEOUT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_TRANSFER_TIMEOUT

This procedure retrieves the default timeout value for all future HTTP requests.

## Syntax

```sql
UTL_HTTP.GET_TRANSFER_TIMEOUT (
   timeout  OUT PLS_INTEGER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| timeout | PLS_INTEGER) | OUT | The network transfer timeout value in seconds |

## Usage Notes

See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.GET_TRANSFER_TIMEOUT ( timeout OUT PLS_INTEGER); Parameters Table 264-41 GET_TRANSFER_TIMEOUT Procedure Parameters Parameter Description timeout The network transfer timeout value in seconds