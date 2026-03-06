---
id: 19c__DBMS_NETWORK_ACL_UTILITY.DOMAIN_LEVEL
name: DBMS_NETWORK_ACL_UTILITY.DOMAIN_LEVEL
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_UTILITY
tags: [dbms_network_acl_utility]
source_file: DBMS_NETWORK_ACL_UTILITY.html
---

# DBMS_NETWORK_ACL_UTILITY.DOMAIN_LEVEL

This function returns the domain level of the given host name, domain, or subnet.

## Syntax

```sql
DBMS_NETWORK_ACL_UTILITY.DOMAIN_LEVEL (
    host  IN VARCHAR2) 
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host | VARCHAR2) | IN | Network host, domain, or subnet |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_NETWORK_ACL_UTILITY.DOMAIN_LEVEL ( host IN VARCHAR2) RETURN NUMBER; Parameters Table 116-3 DOMAIN_LEVEL Function Parameters Parameter Description host Network host, domain, or subnet Return Values The domain level of the given host, domain, or subnet. Usage Notes Note that this function cannot handle IPv6 addresses and subnets, and subnets in CIDR notation. Examples SELECT host, acl, domain_level FROM (select host, acl, DBMS_NETWORK_ACL_UTILITY.DOMAIN_LEVEL(host) domain_level FROM dba_network_acls) order by domain_level desc; HOST ACL DOMAIN_LEVEL ---------------------- ---------------------------- ------------ www.hr.example.com /sys/acls/hr-www.xml 4 *.hr.example.com /sys/acls/hr-domain.xml 3 *.example.com /sys/acls/corp-domain.xml 2