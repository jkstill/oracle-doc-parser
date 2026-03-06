---
id: 19c__DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACL
name: DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACL

This procedure appends access control entries (ACE) of an access control list (ACL) to the ACL of a wallet.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACL (
   wallet_path    IN VARCHAR2,
   acl            IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| wallet_path | VARCHAR2 | IN | Directory path of the wallet. The path is case-sensitive of the format file: directory-path . |
| ace |  |  | The ACL from which to append |

## Usage Notes

Syntax DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACL ( wallet_path IN VARCHAR2, acl IN VARCHAR2); Parameters Table 115-8 APPEND_WALLET_ACL Function Parameters Parameter Description wallet_path Directory path of the wallet. The path is case-sensitive of the format file: directory-path . ace The ACL from which to append Usage Notes Duplicate privileges in the matching ACE in the host ACL will be skipped. To remove the ACE, use REMOVE_WALLET_ACE. If the ACL is shared with another host or wallet, a copy of the ACL is made before the ACL is modified.