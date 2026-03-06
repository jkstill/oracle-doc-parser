---
id: 19c__V$SESSION_CONNECT_INFO
name: V$SESSION_CONNECT_INFO
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: performance
tags: [dynamic_performance]
source_file: V-SESSION_CONNECT_INFO.html
---

# V$SESSION_CONNECT_INFO

V$SESSION_CONNECT_INFO displays information about network connections for all currently logged in sessions.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| SID | NUMBER |  |
| SERIAL# | NUMBER |  |
| AUTHENTICATION_TYPE | VARCHAR2(26) |  |
| OSUSER | VARCHAR2(128) |  |
| NETWORK_SERVICE_BANNER | VARCHAR2(4000) |  |
| CLIENT_CHARSET | VARCHAR2(40) |  |
| CLIENT_CONNECTION | VARCHAR2(13) |  |
| CLIENT_OCI_LIBRARY | VARCHAR2(27) |  |
| CLIENT_VERSION | VARCHAR2(40) |  |
| CLIENT_DRIVER | VARCHAR2(30) |  |
| CLIENT_LOBATTR | VARCHAR2(23) |  |
| CLIENT_REGID | NUMBER |  |
| CON_ID | NUMBER |  |

## Usage Notes

See Also: " V$SESSION " See Also: " V$SESSION "