---
id: 19c__UTL_HTTP.BEGIN_REQUEST
name: UTL_HTTP.BEGIN_REQUEST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: UTL_HTTP
tags: [utl_http]
source_file: UTL_HTTP.html
---

# UTL_HTTP.BEGIN_REQUEST

This function begins a new HTTP request. UTL_HTTP establishes the network connection to the target Web server or the proxy server and sends the HTTP request line. The PL/SQL program continues the request by calling some other interface to complete the request.

## Syntax

```sql
scheme://[user[:password]@]host[:port]/[...]
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| url |  |  | The URL of the HTTP request |
| method |  |  | The method performed on the resource identified by the URL |
| http_version |  |  | The HTTP protocol version that sends the request. The format of the protocol version is HTTP/major-version.minor-version , where major-version and minor-version are positive numbers. If this parameter is set to NULL , UTL_HTTP uses the latest HTTP protocol version that it supports to send the request. The latest version that the package supports is 1.1 and it can be upgraded to a later version. The default is NULL . |
| request_context |  |  | Request context that holds the private wallet and the cookie table to use in this HTTP request. If this parameter is NULL , the wallet and cookie table shared in the current database session will be used instead. |
| https_host |  |  | A string representing the host name. If the string does not begin with a wildcard, the string will be used as the host name for server name indication (SNI). If the string begins with a wildcard, the string will be used to match against the common name (CN) of the remote server's certificate for an HTTPS request. If NULL, the host name in the given URL will be used for SNI. |

**Returns:** `UNKNOWN`

## Usage Notes

The URL may contain the username and password needed to authenticate the request to the server. The format is: scheme://[user[:password]@]host[:port]/[...] See Also: HTTP Requests and HTTP Requests Subprograms See Also: HTTP Requests and HTTP Requests Subprograms Syntax UTL_HTTP.BEGIN_REQUEST ( url IN VARCHAR2, method IN VARCHAR2 DEFAULT 'GET', http_version IN VARCHAR2 DEFAULT NULL, request_context IN request_context_key DEFAULT NULL, https_host IN VARCHAR2 DEFAULT NULL) RETURN req; Parameters Table 264-18 BEGIN_REQUEST Function Parameters Parameter Description url The URL of the HTTP request method The method performed on the resource identified by the URL http_version The HTTP protocol version that sends the request. The format of the protocol version is HTTP/major-version.minor-version , where major-version and minor-version are positive numbers. If this parameter is set to NULL , UTL_HTTP uses the latest HTTP protocol version that it supports to send the request. The latest version that the package supports is 1.1 and it can be upgraded to a later version. The default is NULL . request_context Request context that holds the private wallet and the cookie table to use in this HTTP request. If this parameter is NULL , the wallet and cookie table shared in the current database session will be used instead. https_host A string representing the host name. If the string does not begin with a wildcard, the string will be used as the host name for server name indication (SNI). If the string begins with a wildcard, the string will be used to match against the common name (CN) of the remote server's certificate for an HTTPS request. If NULL, the host name in the given URL will be used for SNI. Usage Notes The URL passed as an argument to this function is not examined for illegal characters, such as spaces, according to URL specification RFC 2396. You should escape those characters with the UTL_URL package to return illegal and reserved characters. URLs should consist of US-ASCII characters only. See UTL_URL for a list of legal characters in URLs. Note that URLs should consist of US-ASCII characters only. The use of non-US-ASCII characters in a URL is generally unsafe. BEGIN_REQUEST can send a URL whose length is up to 32767 bytes. However, different Web servers impose different limits on the length of the URL they can accept. This limit is often about 4000 bytes. If this limit is exceeded, the outcome will depend on the Web server. For example, a Web server might simply drop the HTTP connection without returning a response of any kind. If this happens, a subsequent invocation of the GET_RESPONSE Function will raise the PROTOCOL_ERROR exception. A URL will be long when its QUERY_STRING (that is, the information that follows the question mark (?)) is long. In general, it is better to send this parameterization in the body of the request using the POST method. req := UTL_HTTP.BEGIN_REQUEST (url=>the_url, method=>'POST'); UTL_HTTP.SET_HEADER (r => req, name => 'Content-Type', value => 'application/x-www-form-urlencoded'); UTL_HTTP.SET_HEADER (r => req, name => 'Content-Length', value =>' <length of data posted in bytes>'); UTL_HTTP.WRITE_TEXT (r => req, data => 'p1 = value1&p2=value2...'); resp := UTL_HTTP.GET_RESPONSE (r => req); ... The programmer must determine whether a particular Web server may, or may not, accept data provided in this way. An Oracle wallet must be set before accessing Web servers over HTTPS. See the SET_WALLET Procedure procedure on how to set up an Oracle wallet. To use SSL client authentication, the client certificate should be stored in the wallet and the caller must have the use-client-certificates privilege on the wallet. See "Managing Fine-grained Access to External Network Services" in the Oracle Database Security Guide to grant the privilege. To connect to the remote Web server directly, or indirectly through a HTTP proxy, the UTL_HTTP must have the connect ACL privilege to the remote Web server host or the proxy host respectively.