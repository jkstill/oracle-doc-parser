---
id: 19c__OWA_SEC.GET_CLIENT_IP
name: OWA_SEC.GET_CLIENT_IP
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: OWA_SEC
tags: [owa_sec]
source_file: OWA_SEC.html
---

# OWA_SEC.GET_CLIENT_IP

This function returns the IP address of the client.

## Syntax

```sql
OWA_SEC.GET_CLIENT_IP 
  RETURN OWA_UTIL.IP_ADDRESS;
```

**Returns:** `OWA_UTIL.IP_ADDRESS`

## Usage Notes

Syntax OWA_SEC.GET_CLIENT_IP RETURN OWA_UTIL.IP_ADDRESS; Return Values The IP address. The owa_util.ip_address datatype is a PL/SQL table where the first four elements contain the four numbers of the IP address. For example, if the IP address is 123.45.67.89 and the variable ipaddr is of the owa_util.ip_address datatype, the variable would contain the following values: ipaddr(1) = 123 ipaddr(2) = 45 ipaddr(3) = 67 ipaddr(4) = 89