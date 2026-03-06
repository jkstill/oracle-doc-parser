---
id: 19c__DBMS_NETWORK_ACL_UTILITY.DOMAINS
name: DBMS_NETWORK_ACL_UTILITY.DOMAINS
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_UTILITY
tags: [dbms_network_acl_utility]
source_file: DBMS_NETWORK_ACL_UTILITY.html
---

# DBMS_NETWORK_ACL_UTILITY.DOMAINS

For a given host, this function returns the domains whose ACL assigned determines if a user has the privilege to access the given host or not. When the IP address of the host is given, return the subnets instead.

## Syntax

```sql
DBMS_NETWORK_ACL_UTILITY.DOMAINS (
    host  IN VARCHAR2) 
  RETURN DOMAIN_TABLE PIPELINED;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host | VARCHAR2) | IN | Network host |

**Returns:** `DOMAIN_TABLE`

## Usage Notes

Syntax DBMS_NETWORK_ACL_UTILITY.DOMAINS ( host IN VARCHAR2) RETURN DOMAIN_TABLE PIPELINED; Parameters Table 116-4 DOMAINS Function Parameters Parameter Description host Network host Return Values The domains or subnets for the given host. Usage Notes Note that this function cannot handle IPv6 addresses. Nor can it generate subnets of arbitrary number of prefix bits for an IPv4 address. Examples select * from table(dbms_network_acl_utility.domains('www.hr.example.com')); DOMAINS -------------------------- www.hr.example.com *.hr.example.com *.example.com *.com *