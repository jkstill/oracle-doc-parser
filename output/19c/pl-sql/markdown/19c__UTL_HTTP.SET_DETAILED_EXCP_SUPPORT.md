---
id: 19c__UTL_HTTP.SET_DETAILED_EXCP_SUPPORT
name: UTL_HTTP.SET_DETAILED_EXCP_SUPPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_DETAILED_EXCP_SUPPORT

This procedure sets the UTL_HTTP package to raise a detailed exception.

## Syntax

```sql
UTL_HTTP.SET_DETAILED_EXCP_SUPPORT (
   enable  IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enable | BOOLEAN | IN | Asks UTL_HTTP to raise a detailed exception directly if set to TRUE ; otherwise FALSE |

## Usage Notes

By default, UTL_HTTP raises the request_failed exception when an HTTP request fails. Use GET_DETAILED_SQLCODE and GET_DETAILED_SQLEERM for more detailed information about the error. See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.SET_DETAILED_EXCP_SUPPORT ( enable IN BOOLEAN DEFAULT FALSE); Parameters Table 264-51 SET_DETAILED_EXCP_SUPPORT Procedure Parameters Parameter Description enable Asks UTL_HTTP to raise a detailed exception directly if set to TRUE ; otherwise FALSE