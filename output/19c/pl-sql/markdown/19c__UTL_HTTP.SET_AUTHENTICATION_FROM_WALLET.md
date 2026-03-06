---
id: 19c__UTL_HTTP.SET_AUTHENTICATION_FROM_WALLET
name: UTL_HTTP.SET_AUTHENTICATION_FROM_WALLET
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.SET_AUTHENTICATION_FROM_WALLET

This procedure sets the HTTP authentication information in the HTTP request header needed for the request to be authorized by the Web server using the username and password credential stored in the Oracle wallet.

## Syntax

```sql
UTL_HTTP.SET_AUTHENTICATION_FROM_WALLET(
   r         IN OUT NOCOPY req,
   alias     IN VARCHAR2,
   scheme    IN VARCHAR2 DEFAULT 'Basic',
   for_proxy IN BOOLEAN  DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| r | NOCOPY | IN OUT | The HTTP request |
| alias | VARCHAR2 | IN | Alias to identify and retrieve the username and password credential stored in the Oracle wallet |
| scheme | VARCHAR2 | IN | HTTP authentication scheme. Either Basic for the HTTP basic or AWS for Amazon S3 authentication scheme. Default is basic. |
| for_proxy | BOOLEAN | IN | Identifies if the HTTP authentication information is for access to the HTTP proxy server instead of the Web server. Default is FALSE . |

## Usage Notes

See Also: External Password Store on , and HTTP Requests Subprograms See Also: External Password Store on , and HTTP Requests Subprograms Syntax UTL_HTTP.SET_AUTHENTICATION_FROM_WALLET( r IN OUT NOCOPY req, alias IN VARCHAR2, scheme IN VARCHAR2 DEFAULT 'Basic', for_proxy IN BOOLEAN DEFAULT FALSE); Parameters Table 264-48 SET_AUTHENTICATION_FROM_WALLET Procedure Parameters Parameter Description r The HTTP request alias Alias to identify and retrieve the username and password credential stored in the Oracle wallet scheme HTTP authentication scheme. Either Basic for the HTTP basic or AWS for Amazon S3 authentication scheme. Default is basic. for_proxy Identifies if the HTTP authentication information is for access to the HTTP proxy server instead of the Web server. Default is FALSE . Usage Notes To use the password credentials in a wallet, the UTL_HTTP user must have the use-passwords privilege on the wallet. The supported authentication schemes are HTTP basic and Amazon S3 authentication schemes.