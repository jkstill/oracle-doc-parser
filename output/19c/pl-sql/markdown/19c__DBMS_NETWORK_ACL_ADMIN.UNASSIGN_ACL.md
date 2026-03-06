---
id: 19c__DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL
name: DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL

This deprecated procedure unassigns the access control list (ACL) currently assigned to a network host.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL (
   acl         IN VARCHAR2 DEFAULT NULL,
   host        IN VARCHAR2 DEFAULT NULL,
   lower_port  IN PLS_INTEGER DEFAULT NULL,
   upper_port  IN PLS_INTEGER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2 | IN | Name of the ACL. Relative path will be relative to "/sys/acls". If ACL is NULL , any ACL assigned to the host is unassigned. |
| host | VARCHAR2 | IN | Host from which the ACL is to be removed. The host can be the name or the IP address of the host. A wildcard can be used to specify a domain or a IP subnet. The host or domain name is case-insensitive. If host is NULL , the ACL will be unassigned from any host. If both host and acl are NULL , all ACLs assigned to any hosts are unassigned. |
| lower_port | PLS_INTEGER | IN | Lower bound of a TCP port range if not NULL |
| upper_port | PLS_INTEGER | IN | Upper bound of a TCP port range. If NULL , lower_port is assumed. |

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the REMOVE_HOST_ACE Procedure and the REMOVE_WALLET_ACE Procedure . Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the REMOVE_HOST_ACE Procedure and the REMOVE_WALLET_ACE Procedure . Syntax DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL ( acl IN VARCHAR2 DEFAULT NULL, host IN VARCHAR2 DEFAULT NULL, lower_port IN PLS_INTEGER DEFAULT NULL, upper_port IN PLS_INTEGER DEFAULT NULL); Parameters Table 115-20 UNASSIGN_ACL Function Parameters Parameter Description acl Name of the ACL. Relative path will be relative to "/sys/acls". If ACL is NULL , any ACL assigned to the host is unassigned. host Host from which the ACL is to be removed. The host can be the name or the IP address of the host. A wildcard can be used to specify a domain or a IP subnet. The host or domain name is case-insensitive. If host is NULL , the ACL will be unassigned from any host. If both host and acl are NULL , all ACLs assigned to any hosts are unassigned. lower_port Lower bound of a TCP port range if not NULL upper_port Upper bound of a TCP port range. If NULL , lower_port is assumed. Examples BEGIN DBMS_NETWORK_ACL_ADMIN.UNASSIGN_ACL( host => '*.us.example.com', lower_port => 80); END;