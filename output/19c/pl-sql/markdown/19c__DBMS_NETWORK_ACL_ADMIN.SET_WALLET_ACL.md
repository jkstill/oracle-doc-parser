---
id: 19c__DBMS_NETWORK_ACL_ADMIN.SET_WALLET_ACL
name: DBMS_NETWORK_ACL_ADMIN.SET_WALLET_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.SET_WALLET_ACL

This procedure sets the access control list (ACL) of a wallet which controls access to the wallet from the database.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.SET_WALLET_ACL (
   wallet_path    IN VARCHAR2,
   acl            IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| wallet_path | VARCHAR2 | IN | Directory path of the wallet. The path is case-sensitive of the format file: directory-path . |
| acl | VARCHAR2) | IN | The ACL. NULL to unset the host's ACL. |

## Usage Notes

Syntax DBMS_NETWORK_ACL_ADMIN.SET_WALLET_ACL ( wallet_path IN VARCHAR2, acl IN VARCHAR2); Parameters Table 115-19 SET_WALLET_ACL Function Parameters Parameter Description wallet_path Directory path of the wallet. The path is case-sensitive of the format file: directory-path . acl The ACL. NULL to unset the host's ACL. Usage Notes A wallet's ACL is created and set on-demand when an access control entry (ACE) is appended to the wallet's ACL. Users are discouraged from setting a wallet's ACL manually.