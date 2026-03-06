---
id: 19c__UTL_HTTP.CREATE_REQUEST_CONTEXT
name: UTL_HTTP.CREATE_REQUEST_CONTEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.CREATE_REQUEST_CONTEXT

This function creates a request context. A request context is a context that holds a wallet and a cookie for private use in making a HTTP request. This allows the HTTP request to use a wallet and a cookie table that will not be shared with other applications making HTTP requests in the same database session.

## Syntax

```sql
UTL_HTTP.CREATE_REQUEST_CONTEXT (
 wallet_path          IN VARCHAR2 DEFAULT NULL,
 wallet_password      IN VARCHAR2 DEFAULT NULL,
 enable_cookies       IN BOOLEAN  DEFAULT TRUE,
 max_cookies          IN PLS_INTEGER DEFAULT 300,
 max_cookies_per_site IN PLS_INTEGER DEFAULT 20)
RETURN request_context_key;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| wallet_path | VARCHAR2 | IN | Directory path that contains the Oracle wallet. The format is file: directory-path |
| wallet_password | VARCHAR2 | IN | The password needed to open the wallet. If the wallet is auto-login enabled, the password may be omitted and should be set to NULL . See the Oracle Database Enterprise User Security Administrator's Guide for detailed information about wallets. |
| enable_cookies | BOOLEAN | IN | Sets whether HTTP requests using this request context should support HTTP cookies or not: TRUE to enable the support, FALSE to disable it. |
| max_cookies | PLS_INTEGER | IN | Sets the maximum total number of cookies that will be maintained in this request context |
| max_cookies_per_site | PLS_INTEGER | IN | Sets the maximum number of cookies per each Web site that will be maintained in this request context |

**Returns:** `request_context_key`

## Usage Notes

See Also: Request Context and HTTP Request Contexts Subprograms See Also: Request Context and HTTP Request Contexts Subprograms Syntax UTL_HTTP.CREATE_REQUEST_CONTEXT ( wallet_path IN VARCHAR2 DEFAULT NULL, wallet_password IN VARCHAR2 DEFAULT NULL, enable_cookies IN BOOLEAN DEFAULT TRUE, max_cookies IN PLS_INTEGER DEFAULT 300, max_cookies_per_site IN PLS_INTEGER DEFAULT 20) RETURN request_context_key; Parameters Table 264-22 CREATE_REQUEST_CONTEXT Function Parameters Parameter Description wallet_path Directory path that contains the Oracle wallet. The format is file: directory-path wallet_password The password needed to open the wallet. If the wallet is auto-login enabled, the password may be omitted and should be set to NULL . See the Oracle Database Enterprise User Security Administrator's Guide for detailed information about wallets. enable_cookies Sets whether HTTP requests using this request context should support HTTP cookies or not: TRUE to enable the support, FALSE to disable it. max_cookies Sets the maximum total number of cookies that will be maintained in this request context max_cookies_per_site Sets the maximum number of cookies per each Web site that will be maintained in this request context Return Values The request context created.