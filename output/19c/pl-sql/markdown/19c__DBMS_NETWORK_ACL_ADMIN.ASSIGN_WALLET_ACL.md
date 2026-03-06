---
id: 19c__DBMS_NETWORK_ACL_ADMIN.ASSIGN_WALLET_ACL
name: DBMS_NETWORK_ACL_ADMIN.ASSIGN_WALLET_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.ASSIGN_WALLET_ACL

This procedure assigns an access control list (ACL) to a wallet.

## Syntax

```sql
UTL_HTTP.ASSIGN_WALLET_ACL (
   acl          IN  VARCHAR2,
   wallet_path  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2 | IN | Name of the ACL. Relative path will be relative to "/sys/acls " |
| wallet_path | VARCHAR2) | IN | Directory path of the wallet to which the ACL is to be assigned. The path is case-sensitive and of the format file: directory-path . |

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND_HOST_ACE Procedure and the APPEND_WALLET_ACE Procedure . Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND_HOST_ACE Procedure and the APPEND_WALLET_ACE Procedure . Syntax UTL_HTTP.ASSIGN_WALLET_ACL ( acl IN VARCHAR2, wallet_path IN VARCHAR2); Parameters Table 115-10 ASSIGN_WALLET_ACL Procedure Parameters Parameter Description acl Name of the ACL. Relative path will be relative to "/sys/acls " wallet_path Directory path of the wallet to which the ACL is to be assigned. The path is case-sensitive and of the format file: directory-path . Usage Notes To remove the assignment, use the UNASSIGN_WALLET_ACL Procedure .