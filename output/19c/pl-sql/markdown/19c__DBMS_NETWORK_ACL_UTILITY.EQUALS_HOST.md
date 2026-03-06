---
id: 19c__DBMS_NETWORK_ACL_UTILITY.EQUALS_HOST
name: DBMS_NETWORK_ACL_UTILITY.EQUALS_HOST
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_UTILITY
tags: [dbms_network_acl_utility]
source_file: DBMS_NETWORK_ACL_UTILITY.html
---

# DBMS_NETWORK_ACL_UTILITY.EQUALS_HOST

This function determines if the two given hosts, domains, or subnets are equal. It handles different representation of the same IP address or subnet. For example, an IPv4-mapped IPv6 address is considered equal to the IPv4- native address it represents. It does not perform domain name resolution when comparing the two hosts or domains.

## Syntax

```sql
DBMS_NETWORK_ACL_UTILITY.EQUALS_HOST (
   host1    IN    VARCHAR2,
   host2    IN    VARCHAR2)
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| host 1 |  |  | Network host, domain, or subnet to compare |
| host 2 |  |  | Network host, domain, or subnet to compare |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_NETWORK_ACL_UTILITY.EQUALS_HOST ( host1 IN VARCHAR2, host2 IN VARCHAR2) RETURN NUMBER; Parameters Table 116-5 EQUALS_HOST Function Parameters Parameter Description host 1 Network host, domain, or subnet to compare host 2 Network host, domain, or subnet to compare Return Values 1 if the two hosts, domains, or subnets are equal. 0 otherwise. Examples SELECT host, acl FROM dba_network_acls WHERE DBMS_NETWORK_ACL_UTILITY.EQUALS_HOST('192.0.2.*', host) = 1; HOST ACL ---------------------- ---------------------------- ::ffff:192.0.2.0/120 /sys/acls/hr-domain.xml