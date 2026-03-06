---
id: 19c__DBMS_NETWORK_ACL_ADMIN.REMOVE_WALLET_ACE
name: DBMS_NETWORK_ACL_ADMIN.REMOVE_WALLET_ACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.REMOVE_WALLET_ACE

This procedure removes privileges from access control entries (ACE) in the access control list (ACL) of a wallet matching the given ACE.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.REMOVE_WALLET_ACE (
   wallet_path        IN VARCHAR2,
   ace                IN XS$ACE_TYPE,
   remove_empty_acl   IN BOOLEAN DEFAULT FALSE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| wallet_path | VARCHAR2 | IN | Directory path of the wallet. The path is case-sensitive of the format file: directory-path . |
| ace | XS$ACE_TYPE | IN | The ACE |
| remove_empty_acl | BOOLEAN | IN | Whether to remove the ACL when it becomes empty when the ACE is removed |

## Usage Notes

Syntax DBMS_NETWORK_ACL_ADMIN.REMOVE_WALLET_ACE ( wallet_path IN VARCHAR2, ace IN XS$ACE_TYPE, remove_empty_acl IN BOOLEAN DEFAULT FALSE); Parameters Table 115-17 REMOVE_WALLET_ACE Function Parameters Parameter Description wallet_path Directory path of the wallet. The path is case-sensitive of the format file: directory-path . ace The ACE remove_empty_acl Whether to remove the ACL when it becomes empty when the ACE is removed Usage Notes If the ACL is shared with another host or wallet, a copy of the ACL is made before the ACL is modified.