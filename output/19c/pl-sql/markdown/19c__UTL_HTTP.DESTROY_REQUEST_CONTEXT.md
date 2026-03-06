---
id: 19c__UTL_HTTP.DESTROY_REQUEST_CONTEXT
name: UTL_HTTP.DESTROY_REQUEST_CONTEXT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.DESTROY_REQUEST_CONTEXT

This procedure destroys a request context in UTL_HTTP . A request context cannot be destroyed when it is in use by a HTTP request or response.

## Syntax

```sql
UTL_HTTP.DESTROY_REQUEST_CONTEXT (
   request_context    request_context_key);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| request_context | request_context_key) | IN | Request context to destroy |

## Usage Notes

See Also: Request Context and HTTP Request Contexts Subprograms See Also: Request Context and HTTP Request Contexts Subprograms Syntax UTL_HTTP.DESTROY_REQUEST_CONTEXT ( request_context request_context_key); Parameters Table 264-23 DESTROY_REQUEST_CONTEXT Procedure Parameters Parameter Description request_context Request context to destroy Examples DECLARE request_context UTL_HTTP.REQUEST_CONTEXT_KEY; BEGIN request_context := UTL_HTTP.CREATE_REQUEST_CONTEXT(…); … UTL_HTTP.DESTROY_REQUEST_CONTEXT(request_context); END;