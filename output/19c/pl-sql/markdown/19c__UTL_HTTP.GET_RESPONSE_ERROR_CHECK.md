---
id: 19c__UTL_HTTP.GET_RESPONSE_ERROR_CHECK
name: UTL_HTTP.GET_RESPONSE_ERROR_CHECK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_RESPONSE_ERROR_CHECK

This procedure checks if the response error check is set or not.

## Syntax

```sql
UTL_HTTP.GET_RESPONSE_ERROR_CHECK (
   enable  OUT BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| enable | BOOLEAN) | OUT | TRUE if the response error check is set; otherwise FALSE |

## Usage Notes

See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.GET_RESPONSE_ERROR_CHECK ( enable OUT BOOLEAN); Parameters Table 264-40 GET_RESPONSE_ERROR_CHECK Procedure Parameters Parameter Description enable TRUE if the response error check is set; otherwise FALSE