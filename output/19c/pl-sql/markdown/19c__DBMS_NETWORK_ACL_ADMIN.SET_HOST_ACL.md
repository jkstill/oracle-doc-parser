---
id: 19c__DBMS_NETWORK_ACL_ADMIN.SET_HOST_ACL
name: DBMS_NETWORK_ACL_ADMIN.SET_HOST_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.SET_HOST_ACL

This procedure sets the access control list (ACL) of a network host which controls access to the host from the database.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.SET_HOST_ACL (
   host         IN VARCHAR2,
   lower_port   IN PLS_INTEGER DEFAULT NULL,
   upper_port   IN PLS_INTEGER DEFAULT NULL,
   acl          IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host | VARCHAR2 | IN | The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| lower_port | PLS_INTEGER | IN | Lower bound of an optional TCP port range |
| upper_port | PLS_INTEGER | IN | Upper bound of an optional TCP port range. If NULL , lower_port is assumed. |
| acl | VARCHAR2) | IN | The ACL. NULL to unset the host's ACL. |

## Usage Notes

Syntax DBMS_NETWORK_ACL_ADMIN.SET_HOST_ACL ( host IN VARCHAR2, lower_port IN PLS_INTEGER DEFAULT NULL, upper_port IN PLS_INTEGER DEFAULT NULL, acl IN VARCHAR2); Parameters Table 115-18 SET_HOST_ACL Function Parameters Parameter Description host The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. lower_port Lower bound of an optional TCP port range upper_port Upper bound of an optional TCP port range. If NULL , lower_port is assumed. acl The ACL. NULL to unset the host's ACL. Usage Notes A host's ACL is created and set on-demand when an access control entry (ACE) is appended to the host's ACL. Users are discouraged from setting a host's ACL manually.