---
id: 19c__UTL_HTTP.GET_BODY_CHARSET
name: UTL_HTTP.GET_BODY_CHARSET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_BODY_CHARSET

This procedure retrieves the default character set of the body of all future HTTP requests.

## Syntax

```sql
UTL_HTTP.GET_BODY_CHARSET (
   charset  OUT NOCOPY VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| charset | NOCOPY | OUT | The default character set of the body of all future HTTP requests |

## Usage Notes

See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.GET_BODY_CHARSET ( charset OUT NOCOPY VARCHAR2); Parameters Table 264-27 GET_BODY_CHARSET Procedure Parameters Parameter Description charset The default character set of the body of all future HTTP requests