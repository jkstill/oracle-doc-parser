---
id: 19c__DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE
name: DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE

This procedure appends an access control entry (ACE) to the access control list (ACL) of a network host. The ACL controls access to the given host from the database and the ACE specifies the privileges granted to or denied from the specified principal.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE (
   host         IN VARCHAR2,
   lower_port   IN PLS_INTEGER DEFAULT NULL,
   upper_port   IN PLS_INTEGER DEFAULT NULL,
   ace          IN XS$ACE_TYPE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host | VARCHAR2 | IN | The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| lower_port | PLS_INTEGER | IN | Lower bound of an optional TCP port range |
| upper_port | PLS_INTEGER | IN | Upper bound of an optional TCP port range. If NULL , lower_port is assumed. |
| ace | XS$ACE_TYPE) | IN | The ACE |

## Usage Notes

Syntax DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE ( host IN VARCHAR2, lower_port IN PLS_INTEGER DEFAULT NULL, upper_port IN PLS_INTEGER DEFAULT NULL, ace IN XS$ACE_TYPE); Parameters Table 115-5 APPEND_HOST_ACE Function Parameters Parameter Description host The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. lower_port Lower bound of an optional TCP port range upper_port Upper bound of an optional TCP port range. If NULL , lower_port is assumed. ace The ACE Usage Notes Duplicate privileges in the matching ACE in the host ACL will be skipped. To remove the ACE, use the REMOVE_HOST_ACE Procedure . A host's ACL takes precedence over its domains' ACLs. For a given host, say www.us.example.com , the following domains are listed in decreasing precedence: www.us.example.com *.us.example.com *.example.com *.com * An IP address' ACL takes precedence over its subnets' ACLs. For a given IP address, say 192.168.0.100 , the following subnets are listed in decreasing precedence: 192.168.0.100 192.168.0.* 192.168.* 192.* * An ACE with a "resolve" privilege can be appended only to a host's ACL without a port range. When ACEs with "connect" privileges are appended to a host's ACLs with and without a port range, the one appended to the host with a port range takes precedence. When specifying a TCP port range of a host, it cannot overlap with other existing port ranges of the host. If the ACL is shared with another host or wallet, a copy of the ACL will be made before the ACL is modified. See Also: Oracle Database Real Application Security Administrator's and Developer's Guide for more information about the XS$ACE_TYPE object type See Also: Oracle Database Real Application Security Administrator's and Developer's Guide for more information about the XS$ACE_TYPE object type