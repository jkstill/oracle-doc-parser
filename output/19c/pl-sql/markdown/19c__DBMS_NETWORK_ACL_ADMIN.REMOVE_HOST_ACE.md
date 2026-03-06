---
id: 19c__DBMS_NETWORK_ACL_ADMIN.REMOVE_HOST_ACE
name: DBMS_NETWORK_ACL_ADMIN.REMOVE_HOST_ACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.REMOVE_HOST_ACE

This procedure removes privileges from access control entries (ACE) in the access control list (ACL) of a network host matching the given ACE.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.REMOVE_HOST_ACE (
   host               IN VARCHAR2,
   lower_port         IN PLS_INTEGER DEFAULT NULL,
   upper_port         IN PLS_INTEGER DEFAULT NULL,
   ace                IN XS$ACE_TYPE,
   remove_empty_acl   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host | VARCHAR2 | IN | The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| lower_port | PLS_INTEGER | IN | Lower bound of an optional TCP port range |
| upper_port | PLS_INTEGER | IN | Upper bound of an optional TCP port range. If NULL , lower_port is assumed. |
| ace | XS$ACE_TYPE | IN | The ACE |
| remove_empty_acl | BOOLEAN | IN | Whether to remove the ACL when it becomes empty when the ACE is removed |

## Usage Notes

Syntax DBMS_NETWORK_ACL_ADMIN.REMOVE_HOST_ACE ( host IN VARCHAR2, lower_port IN PLS_INTEGER DEFAULT NULL, upper_port IN PLS_INTEGER DEFAULT NULL, ace IN XS$ACE_TYPE, remove_empty_acl IN BOOLEAN DEFAULT FALSE); Parameters Table 115-16 REMOVE_HOST_ACE Function Parameters Parameter Description host The host, which can be the name or the IP address of the host. You can use a wildcard to specify a domain or a IP subnet. The host or domain name is case-insensitive. lower_port Lower bound of an optional TCP port range upper_port Upper bound of an optional TCP port range. If NULL , lower_port is assumed. ace The ACE remove_empty_acl Whether to remove the ACL when it becomes empty when the ACE is removed Usage Notes If the ACL is shared with another host or wallet, a copy of the ACL is made before the ACL is modified.