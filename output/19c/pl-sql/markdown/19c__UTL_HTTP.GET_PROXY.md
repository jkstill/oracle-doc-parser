---
id: 19c__UTL_HTTP.GET_PROXY
name: UTL_HTTP.GET_PROXY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.GET_PROXY

This procedure retrieves the current proxy settings.

## Syntax

```sql
UTL_HTTP.GET_PROXY (
   proxy             OUT NOCOPY VARCHAR2, 
   no_proxy_domains  OUT NOCOPY VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| proxy | NOCOPY | OUT | The proxy (host and an optional port number) currently used by the UTL_HTTP package |
| no_proxy_domains | NOCOPY | OUT | The list of hosts and domains for which no proxy is used for all requests |

## Usage Notes

See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.GET_PROXY ( proxy OUT NOCOPY VARCHAR2, no_proxy_domains OUT NOCOPY VARCHAR2); Parameters Table 264-38 GET_PROXY Procedure Parameters Parameter Description proxy The proxy (host and an optional port number) currently used by the UTL_HTTP package no_proxy_domains The list of hosts and domains for which no proxy is used for all requests