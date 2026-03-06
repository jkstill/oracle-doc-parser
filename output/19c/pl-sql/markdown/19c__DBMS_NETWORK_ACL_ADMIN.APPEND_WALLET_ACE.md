---
id: 19c__DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACE
name: DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACE

This procedure appends an access control entry (ACE) to the access control list (ACL) of a wallet. The ACL controls access to the given wallet from the database and the ACE specifies the privileges granted to or denied from the specified principal.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACE (
   wallet_path    IN VARCHAR2,
   ace            IN XS$ACE_TYPE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| wallet_path | VARCHAR2 | IN | Directory path of the wallet. The path is case-sensitive of the format file: directory-path . |
| ace | XS$ACE_TYPE) | IN | The ACE |

## Usage Notes

Syntax DBMS_NETWORK_ACL_ADMIN.APPEND_WALLET_ACE ( wallet_path IN VARCHAR2, ace IN XS$ACE_TYPE); Parameters Table 115-7 APPEND_WALLET_ACE Function Parameters Parameter Description wallet_path Directory path of the wallet. The path is case-sensitive of the format file: directory-path . ace The ACE Usage Notes Duplicate privileges in the matching ACE in the host ACL will be skipped. To remove the ACE, use the REMOVE_WALLET_ACE Procedure . If the ACL is shared with another host or wallet, a copy of the ACL is made before the ACL is modified. See Also: Oracle Database Real Application Security Administrator's and Developer's Guide for more information about the XS$ACE_TYPE object type See Also: Oracle Database Real Application Security Administrator's and Developer's Guide for more information about the XS$ACE_TYPE object type