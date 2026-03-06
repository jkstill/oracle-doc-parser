---
id: 19c__DBMS_NETWORK_ACL_UTILITY
name: DBMS_NETWORK_ACL_UTILITY
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_UTILITY
tags: [dbms_network_acl_utility]
source_file: DBMS_NETWORK_ACL_UTILITY.html
---

# DBMS_NETWORK_ACL_UTILITY

The CONTAINS_HOST Function in this package indicates if a domain or subnet contains a given host or IP address.

## Syntax

```sql
SELECT host, lower_port, upper_port, acl,
     DECODE(
         DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID(aclid, 'SCOTT', 'connect'),
            1, 'GRANTED', 0, 'DENIED', NULL) privilege
     FROM (SELECT host, acl, aclid, lower_port, upper_port,
               DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST('www.hr.example.com', host)
                 precedence
          FROM dba_network_acls)
 WHERE precedence > 0
 ORDER BY precedence DESC, lower_port nulls LAST;


   HOST                 LOWER_PORT UPPER_PORT  ACL                 PRIVILEGE
   -------------------- ---------- ---------- -------------------- ---------
   www.hr.example.com          80         80  /sys/acls/www.xml    GRANTED
   www.hr.example.com        3000       3999  /sys/acls/www.xml    GRANTED
   www.hr.example.com                         /sys/acls/www.xml    GRANTED
   *.hr.example.com                           /sys/acls/all.xml
   *.example.com                              /sys/acls/all.xml
```

## Usage Notes

It can be used in conjunction with the CHECK_PRIVILEGE_ACLID Function in the DBMS_NETWORK_ACL_ADMIN package to determine the privilege assignments affecting a user's permission to access a network host. The return value of the CONTAINS_HOST Function in can also be used to order the ACL assignments by their precedence. For example, for SCOTT's permission to connect to www.hr.example.com : SELECT host, lower_port, upper_port, acl, DECODE( DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID(aclid, 'SCOTT', 'connect'), 1, 'GRANTED', 0, 'DENIED', NULL) privilege FROM (SELECT host, acl, aclid, lower_port, upper_port, DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST('www.hr.example.com', host) precedence FROM dba_network_acls) WHERE precedence > 0 ORDER BY precedence DESC, lower_port nulls LAST; HOST LOWER_PORT UPPER_PORT ACL PRIVILEGE -------------------- ---------- ---------- -------------------- --------- www.hr.example.com 80 80 /sys/acls/www.xml GRANTED www.hr.example.com 3000 3999 /sys/acls/www.xml GRANTED www.hr.example.com /sys/acls/www.xml GRANTED *.hr.example.com /sys/acls/all.xml *.example.com /sys/acls/all.xml For example, for SCOTT 's permission to do domain name resolution for www.hr.example.com: SELECT host, acl, DECODE( DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID(aclid, 'SCOTT', 'resolve'), 1, 'GRANTED', 0, 'DENIED', null) privilege FROM (SELECT host, acl, aclid, DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST('www.hr.example.com', host) precedence FROM dba_network_acls WHERE lower_port IS NULL AND upper_port IS NULL) WHERE precedence > 0 ORDER BY precedence DESC; HOST ACL PRIVILEGE ---------------------- ---------------------------- --------- www.hr.example.com /sys/acls/hr-www.xml GRANTED *.hr.example.com /sys/acls/hr-domain.xml *.example.com /sys/acls/corp-domain.xml Note that the "resolve" privilege takes effect only in ACLs assigned without any port range (when lower_port and upper_port are NULL ). For this reason, the example does not include lower_port and upper_port columns in the query.