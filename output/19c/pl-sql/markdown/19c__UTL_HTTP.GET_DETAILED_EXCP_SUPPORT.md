---
id: 19c__UTL_HTTP.GET_DETAILED_EXCP_SUPPORT
name: UTL_HTTP.GET_DETAILED_EXCP_SUPPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_DETAILED_EXCP_SUPPORT

This procedure checks if the UTL_HTTP package will raise a detailed exception or not.

## Syntax

```sql
UTL_HTTP.GET_DETAILED_EXCP_SUPPORT (
   enable  OUT BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enable | BOOLEAN) | OUT | TRUE if UTL_HTTP raises a detailed exception; otherwise FALSE |

## Usage Notes

See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.GET_DETAILED_EXCP_SUPPORT ( enable OUT BOOLEAN); Parameters Table 264-31 GET_DETAILED_EXCP_SUPPORT Procedure Parameters Parameter Description enable TRUE if UTL_HTTP raises a detailed exception; otherwise FALSE