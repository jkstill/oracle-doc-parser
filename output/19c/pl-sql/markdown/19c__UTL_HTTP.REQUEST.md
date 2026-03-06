---
id: 19c__UTL_HTTP.REQUEST
name: UTL_HTTP.REQUEST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.REQUEST

This function returns up to the first 2000 bytes of data retrieved from the given URL.

## Syntax

```sql
scheme://[user[:password]@]host[:port]/[...]
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| url |  |  | Uniform resource locator |
| proxy |  |  | (Optional) Specifies a proxy server to use when making the HTTP request. See SET_PROXY for the full format of the proxy setting. |
| wallet_path |  |  | (Optional) Specifies a client-side wallet. The client-side wallet contains the list of trusted certificate authorities required for HTTPS request. The format of wallet_path on a PC is, for example, file:c :\WINNT\Profiles\ username \WALLETS, and in Unix is, for example, file:/home/ username /wallets When the UTL_HTTP package is executed in the Oracle database server, the wallet is accessed from the database server. Therefore, the wallet path must be accessible from the database server. See SET_WALLET for a description on how to set up an Oracle wallet. Non-HTTPS requests do not require an Oracle wallet. |
| wallet_password |  |  | (Optional) Specifies the password required to open the wallet |
| https_host |  |  | A string representing the host name. If the string does not begin with a wildcard, the string will be used as the host name for server name indication (SNI). If the string begins with a wildcard, the string will be used to match against the common name (CN) of the remote server's certificate for an HTTPS request. If NULL, the host name in the given URL will be used for SNI. |

**Returns:** `UNKNOWN`

## Usage Notes

This function can be used directly in SQL queries. The URL may contain the username and password needed to authenticate the request to the server. The format is scheme://[user[:password]@]host[:port]/[...] You can define a username/password for the proxy to be specified in the proxy string. The format is [http://][user[:password]@]host[:port][/] See Also: Simple HTTP Fetches and Simple HTTP Fetches in a Single Call Subprograms See Also: Simple HTTP Fetches and Simple HTTP Fetches in a Single Call Subprograms Syntax UTL_HTTP.REQUEST ( url IN VARCHAR2, proxy IN VARCHAR2 DEFAULT NULL, wallet_path IN VARCHAR2 DEFAULT NULL, wallet_password IN VARCHAR2 DEFAULT NULL, https_host IN VARCHAR2 DEFAULT NULL) RETURN VARCHAR2; Pragmas pragma restrict_references (request, wnds, rnds, wnps, rnps); Parameters Table 264-45 REQUEST Function Parameters Parameter Description url Uniform resource locator proxy (Optional) Specifies a proxy server to use when making the HTTP request. See SET_PROXY for the full format of the proxy setting. wallet_path (Optional) Specifies a client-side wallet. The client-side wallet contains the list of trusted certificate authorities required for HTTPS request. The format of wallet_path on a PC is, for example, file:c :\WINNT\Profiles\ username \WALLETS, and in Unix is, for example, file:/home/ username /wallets When the UTL_HTTP package is executed in the Oracle database server, the wallet is accessed from the database server. Therefore, the wallet path must be accessible from the database server. See SET_WALLET for a description on how to set up an Oracle wallet. Non-HTTPS requests do not require an Oracle wallet. wallet_password (Optional) Specifies the password required to open the wallet https_host A string representing the host name. If the string does not begin with a wildcard, the string will be used as the host name for server name indication (SNI). If the string begins with a wildcard, the string will be used to match against the common name (CN) of the remote server's certificate for an HTTPS request. If NULL, the host name in the given URL will be used for SNI.