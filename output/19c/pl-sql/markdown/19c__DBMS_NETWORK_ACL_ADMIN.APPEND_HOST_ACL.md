---
id: 19c__DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACL
name: DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACL

This procedure appends access control entries (ACE) of an access control list (ACL) to the ACL of a network host.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACL (
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
| acl | VARCHAR2) | IN | The ACL from which to append |

## Usage Notes

Syntax DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACL ( host IN VARCHAR2, lower_port IN PLS_INTEGER DEFAULT NULL, upper_port IN PLS_INTEGER DEFAULT NULL, acl IN VARCHAR2); Parameters Table 115-6 APPEND_HOST_ACL Function Parameters Parameter Description host The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. lower_port Lower bound of an optional TCP port range upper_port Upper bound of an optional TCP port range. If NULL , lower_port is assumed. acl The ACL from which to append Usage Notes Duplicate privileges in the matching ACE in the host ACL will be skipped. To remove the ACE, use the REMOVE_HOST_ACE Procedure . A host's ACL takes precedence over its domains' ACLs. For a given host, say www.us.example.com , the following domains are listed in decreasing precedence: www.us.example.com *.us.example.com *.example.com *.com * An IP address' ACL takes precedence over its subnets' ACLs. For a given IP address, say 192.168.0.100 , the following subnets are listed in decreasing precedence: 192.168.0.100 192.168.0.* 192.168.* 192.* * An ACE with a "resolve" privilege can be appended only to a host's ACL without a port range. When ACEs with "connect" privileges are appended to a host's ACLs with and without a port range, the one appended to the host with a port range takes precedence. When specifying a TCP port range of a host, it cannot overlap with other existing port ranges of the host.- If the ACL is shared with another host or wallet, a copy of the ACL will be made before the ACL is modified.