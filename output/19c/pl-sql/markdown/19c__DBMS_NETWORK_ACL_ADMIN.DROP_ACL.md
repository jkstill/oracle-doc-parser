---
id: 19c__DBMS_NETWORK_ACL_ADMIN.DROP_ACL
name: DBMS_NETWORK_ACL_ADMIN.DROP_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.DROP_ACL

This deprecated procedure drops an access control list (ACL).

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.DROP_ACL (
   acl           IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2) | IN | Name of the ACL. Relative path will be relative to "/sys/acls". |

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . The procedure remains available in the package only for reasons of backward compatibility. Note: This procedure is deprecated in Oracle Database 12 c . The procedure remains available in the package only for reasons of backward compatibility. Syntax DBMS_NETWORK_ACL_ADMIN.DROP_ACL ( acl IN VARCHAR2); Parameters Table 115-15 DROP_ACL Procedure Parameters Parameter Description acl Name of the ACL. Relative path will be relative to "/sys/acls". Examples BEGIN DBMS_NETWORK_ACL_ADMIN.DROP_ACL( acl => 'us-example-com-permissions.xml'); END;