---
id: 19c__DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE
name: DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE

This function checks if a privilege is granted or denied the user in an ACL.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE (
   acl             IN VARCHAR2,
   user            IN VARCHAR2,
   privilege       IN VARCHAR2)
  RETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2 | IN | Name of the ACL. Relative path will be relative to "/sys/acls". |
| user | VARCHAR2 | IN | User to check against. If the user is NULL , the invoker is assumed. The username is case-sensitive as in the USERNAME column of the ALL_USERS view. |
| privilege | VARCHAR2) | IN | Network privilege to check |

**Returns:** `NUMBER`

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . The procedure remains available in the package only for reasons of backward compatibility. Note: This procedure is deprecated in Oracle Database 12 c . The procedure remains available in the package only for reasons of backward compatibility. Syntax DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE ( acl IN VARCHAR2, user IN VARCHAR2, privilege IN VARCHAR2) RETURN NUMBER; Parameters Table 115-11 CHECK_PRIVILEGE Function Parameters Parameter Description acl Name of the ACL. Relative path will be relative to "/sys/acls". user User to check against. If the user is NULL , the invoker is assumed. The username is case-sensitive as in the USERNAME column of the ALL_USERS view. privilege Network privilege to check Return Values Returns 1 when the privilege is granted; 0 when the privilege is denied; NULL when the privilege is neither granted or denied.