---
id: 19c__DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL
name: DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL

This procedure assigns an access control list (ACL) to a host computer, domain, or IP subnet, and if specified, the TCP port range.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL (
   acl         IN VARCHAR2,
   host        IN VARCHAR2,
   lower_port  IN PLS_INTEGER DEFAULT NULL,
   upper_port  IN PLS_INTEGER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2 | IN | Name of the ACL. Relative path will be relative to " /sys/acls ". |
| host | VARCHAR2 | IN | Host to which the ACL is to be assigned. The host can be the name or the IP address of the host. A wildcard can be used to specify a domain or a IP subnet. The host or domain name is case-insensitive. |
| lower_port | PLS_INTEGER | IN | Lower bound of a TCP port range if not NULL |
| upper_port | PLS_INTEGER | IN | Upper bound of a TCP port range. If NULL , lower_port is assumed. |

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND_HOST_ACE Procedure and the APPEND_WALLET_ACE Procedure . Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND_HOST_ACE Procedure and the APPEND_WALLET_ACE Procedure . Syntax DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL ( acl IN VARCHAR2, host IN VARCHAR2, lower_port IN PLS_INTEGER DEFAULT NULL, upper_port IN PLS_INTEGER DEFAULT NULL); Parameters Table 115-9 ASSIGN_ACL Function Parameters Parameter Description acl Name of the ACL. Relative path will be relative to " /sys/acls ". host Host to which the ACL is to be assigned. The host can be the name or the IP address of the host. A wildcard can be used to specify a domain or a IP subnet. The host or domain name is case-insensitive. lower_port Lower bound of a TCP port range if not NULL upper_port Upper bound of a TCP port range. If NULL , lower_port is assumed. Usage Notes Only one ACL can be assigned to any host computer, domain, or IP subnet, and if specified, the TCP port range. When you assign a new access control list to a network target, Oracle Database unassigns the previous access control list that was assigned to the same target. However, Oracle Database does not drop the access control list. You can drop the access control list by using the DROP_ACL Procedure . To remove an access control list assignment, use the UNASSIGN_ACL Procedure . The ACL assigned to a domain takes a lower precedence than the other ACLs assigned sub-domains, which take a lower precedence than the ACLs assigned to the individual hosts. So for a given host, for example, "www.us.example.com", the following domains are listed in decreasing precedences: - www.us.example.com - *.us.example.com - *.example.com - *.com - * In the same way, the ACL assigned to an subnet takes a lower precedence than the other ACLs assigned smaller subnets, which take a lower precedence than the ACLs assigned to the individual IP addresses. So for a given IP address, for example, "192.168.0.100", the following subnets are listed in decreasing precedences: - 192.168.0.100 - 192.168.0.* - 192.168.* - 192.* - * The port range is applicable only to the "connect" privilege assignments in the ACL. The "resolve" privilege assignments in an ACL have effects only when the ACL is assigned to a host without a port range. For the "connect" privilege assignments, an ACL assigned to the host without a port range takes a lower precedence than other ACLs assigned to the same host with a port range. When specifying a TCP port range, both lower_port and upper_port must not be NULL and upper_port must be greater than or equal to lower_port . The port range must not overlap with any other port ranges for the same host assigned already. To remove the assignment, use UNASSIGN_ACL Procedure .