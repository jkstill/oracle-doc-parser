---
id: 19c__PROXY_USERS
name: PROXY_USERS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
source_file: PROXY_USERS.html
---

# PROXY_USERS

PROXY_USERS describes the list of proxy users and the clients on whose behalf they can act.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| PROXY | VARCHAR2(128) | Name of a proxy user |
| CLIENT | VARCHAR2(128) | Name of the client user who the proxy user can act as |
| AUTHENTICATION | VARCHAR2(3) | Indicates whether the proxy is required to supply the client's authentication credentials ( YES ) or not ( NO ) |
| FLAGS | VARCHAR2(35) | Flags associated with the proxy/client pair: PROXY MAY ACTIVATE ALL CLIENT ROLES NO CLIENT ROLES MAY BE ACTIVATED PROXY MAY ACTIVATE ROLE PROXY MAY ACTIVATE ALL CLIENT ROLES PROXY MAY NOT ACTIVATE ROLE |

## Usage Notes

Previous Next JavaScript must be enabled to correctly display this content