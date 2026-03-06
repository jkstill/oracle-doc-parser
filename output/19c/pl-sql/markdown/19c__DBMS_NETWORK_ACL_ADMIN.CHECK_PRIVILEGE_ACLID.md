---
id: 19c__DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID
name: DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID

This function checks if a privilege is granted to or denied from the user in an ACL by specifying the object ID of the access control list.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID (
   aclid           IN RAW,
   user            IN VARCHAR2 DEFAULT NULL)
   privilege       IN VARCHAR2,
 RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| aclid | RAW | IN | Object ID of the ACL |
| user | VARCHAR2 | IN | User to check against. If the user is NULL , the invoker is assumed. The username is case-sensitive as in the USERNAME column of the ALL_USERS view. |
| privilege | VARCHAR2 | IN | Network privilege to check |

**Returns:** `NUMBER`

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . The procedure remains available in the package only for reasons of backward compatibility. Note: This procedure is deprecated in Oracle Database 12 c . The procedure remains available in the package only for reasons of backward compatibility. Syntax DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE_ACLID ( aclid IN RAW, user IN VARCHAR2 DEFAULT NULL) privilege IN VARCHAR2, RETURN NUMBER; Parameters Table 115-12 CHECK_PRIVILEGE_ACLID Function Parameters Parameter Description aclid Object ID of the ACL user User to check against. If the user is NULL , the invoker is assumed. The username is case-sensitive as in the USERNAME column of the ALL_USERS view. privilege Network privilege to check Return Values Returns 1 when the privilege is granted; 0 when the privilege is denied; NULL when the privilege is neither granted or denied.