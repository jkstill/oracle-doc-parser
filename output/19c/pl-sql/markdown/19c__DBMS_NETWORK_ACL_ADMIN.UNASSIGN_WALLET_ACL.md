---
id: 19c__DBMS_NETWORK_ACL_ADMIN.UNASSIGN_WALLET_ACL
name: DBMS_NETWORK_ACL_ADMIN.UNASSIGN_WALLET_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.UNASSIGN_WALLET_ACL

This deprecated procedure unassigns the access control list (ACL) currently assigned to a wallet.

## Syntax

```sql
UTL_HTTP.UNASSIGN_WALLET_ACL (
   acl          IN  VARCHAR2 DEFAULT NULL,
   wallet_path  IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2 | IN | Name of the ACL. Relative path will be relative to "/sys/acls" . If acl is NULL , any ACL assigned to the wallet is unassigned |
| wallet_path | VARCHAR2 | IN | Directory path of the wallet to which the ACL is assigned. The path is case-sensitive and of the format file : directory-path . If both acl and wallet_path are NULL , all ACLs assigned to any wallets are unassigned. |

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the REMOVE_HOST_ACE Procedure and the REMOVE_WALLET_ACE Procedure . Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the REMOVE_HOST_ACE Procedure and the REMOVE_WALLET_ACE Procedure . Syntax UTL_HTTP.UNASSIGN_WALLET_ACL ( acl IN VARCHAR2 DEFAULT NULL, wallet_path IN VARCHAR2 DEFAULT NULL); Parameters Table 115-21 UNASSIGN_WALLET_ACL Procedure Parameters Parameter Description acl Name of the ACL. Relative path will be relative to "/sys/acls" . If acl is NULL , any ACL assigned to the wallet is unassigned wallet_path Directory path of the wallet to which the ACL is assigned. The path is case-sensitive and of the format file : directory-path . If both acl and wallet_path are NULL , all ACLs assigned to any wallets are unassigned. Examples BEGIN DBMS_NETWORK_ACL_ADMIN.UNASSIGN_WALLET_ACL( acl => 'wallet-acl.xml', wallet_path => 'file:/example/wallets/test_wallet'); END;