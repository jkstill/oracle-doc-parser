---
id: 19c__DBMS_NETWORK_ACL_ADMIN.DELETE_PRIVILEGE
name: DBMS_NETWORK_ACL_ADMIN.DELETE_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.DELETE_PRIVILEGE

This deprecated procedure deletes a privilege in an access control list.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.DELETE_PRIVILEGE (
   acl           IN VARCHAR2,
   principal     IN VARCHAR2,
   is_grant      IN BOOLEAN DEFAULT NULL,
   privilege     IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2 | IN | Name of the ACL. Relative path will be relative to "/sys/acls". |
| principal | VARCHAR2 | IN | Principal (database user or role) for whom all the ACE will be deleted |
| is_grant | BOOLEAN | IN | Privilege is granted or not (denied). If a NULL value is given, the deletion is applicable to both granted or denied privileges. |
| privilege | VARCHAR2 | IN | Network privilege to be deleted. If a NULL value is given, the deletion is applicable to all privileges. |

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the REMOVE_HOST_ACE Procedure and the REMOVE_WALLET_ACE Procedure . Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the REMOVE_HOST_ACE Procedure and the REMOVE_WALLET_ACE Procedure . Syntax DBMS_NETWORK_ACL_ADMIN.DELETE_PRIVILEGE ( acl IN VARCHAR2, principal IN VARCHAR2, is_grant IN BOOLEAN DEFAULT NULL, privilege IN VARCHAR2 DEFAULT NULL); Parameters Table 115-14 DELETE_PRIVILEGE Function Parameters Parameter Description acl Name of the ACL. Relative path will be relative to "/sys/acls". principal Principal (database user or role) for whom all the ACE will be deleted is_grant Privilege is granted or not (denied). If a NULL value is given, the deletion is applicable to both granted or denied privileges. privilege Network privilege to be deleted. If a NULL value is given, the deletion is applicable to all privileges. Examples BEGIN DBMS_NETWORK_ACL_ADMIN.DELETE_PRIVILEGE( acl => 'us-example-com-permissions.xml', principal => 'ST_USERS') END;