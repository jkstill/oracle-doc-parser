---
id: 19c__DBMS_NETWORK_ACL_ADMIN
name: DBMS_NETWORK_ACL_ADMIN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN

Grant the connect and resolve privileges for host www.us.example.com to SCOTT .

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE(
  host => 'www.us.example.com',
  ace  =>  xs$ace_type(privilege_list => xs$name_list('connect', 'resolve'),
                       principal_name => 'scott',
                       principal_type => xs_acl.ptype_db));
```

## Usage Notes

DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE( host => 'www.us.example.com', ace => xs$ace_type(privilege_list => xs$name_list('connect', 'resolve'), principal_name => 'scott', principal_type => xs_acl.ptype_db)); Revoke the resolve privilege for host www.us.example.com from SCOTT . dbms_network_acl_admin.remove_host_ace( host => 'www.us.example.com', ace => xs$ace_type(privilege_list => xs$name_list('resolve'), principal_name => 'scott', principal_type => xs_acl.ptype_db)); Grant the use_client_certificates and use_passwords privileges for wallet file:/example/wallets/hr_wallet to SCOTT . dbms_network_acl_admin.append_wallet_ace( wallet_path => 'file:/example/wallets/hr_wallet', ace => xs$ace_type(privilege_list => xs$name_list('use_client_certificates', 'use_passwords'), principal_name => 'scott', principal_type => xs_acl.ptype_db)); Revoke the use_passwords privilege for wallet file:/example/wallets/hr_wallet from SCOTT . dbms_network_acl_admin.remove_wallet_ace( wallet_path => 'file:/example/wallets/hr_wallet', ace => xs$ace_type(privilege_list => xs$name_list('use_passwords'), principal_name => 'scott', principal_type => xs_acl.ptype_db)); The CONTAINS_HOST in the DBMS_NETWORK_ACL_UTLILITY package determines if a host is contained in a domain. It can be used in conjunction with the DBA_HOST_ACE view to determine the users and their privilege assignments to access a network host.For example, for access to www.us.example.com : SELECT HOST, LOWER_PORT, UPPER_PORT, ACE_ORDER, PRINCIPAL, PRINCIPAL_TYPE, GRANT_TYPE, INVERTED_PRINCIPAL, PRIVILEGE, START_DATE, END_DATE FROM (SELECT ACES.*, DBMS_NETWORK_ACL_UTILITY.CONTAINS_HOST('www.us.example.com', HOST) PRECEDENCE FROM DBA_HOST_ACES ACES) WHERE PRECEDENCE IS NOT NULL ORDER BY PRECEDENCE DESC, LOWER_PORT NULLS LAST, UPPER_PORT NULLS LAST, ACE_ORDER; HOST LOWER_PORT UPPER_PORT ACE_ORDER PRINCIPAL PRINCIPAL_TYPE GRANT_TYPE INVERTED_PRINCIPAL PRIVILEGE START_DATE END_DATE ------------------ ---------- ---------- --------- --------- ---------------- ---------- ------------------ ---------- ---------- -------- www.us.example.com 80 80 1 SCOTT DATABASE USER GRANT NO HTTP www.us.example.com 80 80 2 ADAMS DATABASE USER GRANT NO HTTP * 1 HQ_DBA DATABASE USER GRANT NO CONNECT * 1 HQ_DBA DATABASE USER GRANT NO RESOLVE