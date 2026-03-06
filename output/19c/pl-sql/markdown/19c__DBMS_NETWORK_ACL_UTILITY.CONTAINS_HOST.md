---
id: 19c__DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST
name: DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_UTILITY
tags: [dbms_network_acl_utility]
source_file: DBMS_NETWORK_ACL_UTILITY.html
---

# DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST

This function determines if the given host is equal to or contained in the given host, domain, or subnet. It handles different representation of the same IP address or subnet. For example, an IPv4-mapped IPv6 address is considered equal to the IPv4-native address it represents. It does not perform domain name resolution when evaluating the host or domain.

## Syntax

```sql
DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST (
   host      IN    VARCHAR2,
   domain    IN    VARCHAR2)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host | VARCHAR2 | IN | Network host |
| domain | VARCHAR2) | IN | Network host, domain, or subnet |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST ( host IN VARCHAR2, domain IN VARCHAR2) RETURN NUMBER; Parameters Table 116-2 CONTAINS_HOST Function Parameters Parameter Description host Network host domain Network host, domain, or subnet Return Values Returns a non- NULL value if the given host is equal to or contained in the related host, domain, or subnet: If domain is a hostname, returns the level of its domain + 1 If domain is a domain name, returns the domain level If domain is an IP address or subnet, return the number of significant address bits of the IP address or subnet If domain is the wildcard "*", returns 0 The non- NULL value returned indicates the precedence of the domain or subnet for ACL assignment. The higher the value, the higher is the precedence. NULL will be returned if the host is not equal to or contained in the given host, domain or subnet. Examples SELECT host, acl, precedence FROM (select host, acl, DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST('192.0.2.3', host) precedence FROM dba_network_acls) WHERE precedence > 0 ORDER BY precedence DESC; HOST ACL PRECEDENCE ---------------------- -------------------------- ---------- 192.0.2.3 /sys/acls/hr-www.xml 32 ::ffff:192.0.2.0/120 /sys/acls/hr-domain.xml 24 ::ffff:192.0.0.0/104 /sys/acls/corp-domain.xml 8