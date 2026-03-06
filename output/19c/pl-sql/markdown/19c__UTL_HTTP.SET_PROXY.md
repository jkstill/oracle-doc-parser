---
id: 19c__UTL_HTTP.SET_PROXY
name: UTL_HTTP.SET_PROXY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_PROXY

This procedure sets the proxy to be used for requests of the HTTP or other protocols, excluding those for hosts that belong to the domain specified in no_proxy_domains .

## Syntax

```sql
UTL_HTTP.SET_PROXY (
   proxy             IN VARCHAR2,
   no_proxy_domains  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| proxy | VARCHAR2 | IN | The proxy (host and an optional port number) to be used by the UTL_HTTP package |
| no_proxy_domains | VARCHAR2) | IN | The list of hosts and domains for which no proxy should be used for all requests |

## Usage Notes

no_proxy_domains is a comma-, semi-colon-, or space-separated list of domains or hosts for which HTTP requests should be sent directly to the destination HTTP server instead of going through a proxy server. See Also: Session Settings and Session Settings Subprograms See Also: Session Settings and Session Settings Subprograms Syntax UTL_HTTP.SET_PROXY ( proxy IN VARCHAR2, no_proxy_domains IN VARCHAR2); Parameters Table 264-55 SET_PROXY Procedure Parameters Parameter Description proxy The proxy (host and an optional port number) to be used by the UTL_HTTP package no_proxy_domains The list of hosts and domains for which no proxy should be used for all requests Usage Notes The proxy may include an optional TCP/IP port number at which the proxy server listens. The syntax is [http://]host[:port][/] , for example, www-proxy.my-company.com:80 . If the port is not specified for the proxy, port 80 is assumed. Optionally, a port number can be specified for each domain or host. If the port number is specified, the no-proxy restriction is only applied to the request at the port of the particular domain or host, for example, corp.my-company.com, eng.my-company.com:80 . When no_proxy_domains is NULL and the proxy is set, all requests go through the proxy. When the proxy is not set, UTL_HTTP sends requests to the target Web servers directly. You can define a username/password for the proxy to be specified in the proxy string. The format is [http://][user[:password]@]host[:port][/] If proxy settings are set when the database server instance is started, the proxy settings in the environment variables http_proxy and no_proxy are assumed. Proxy settings set by this procedure override the initial settings.