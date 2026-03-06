---
id: 19c__DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE
name: DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE

This procedure adds a privilege to grant or deny the network access to the user. The access control entry (ACE) is created if it does not exist.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE (
   acl             IN VARCHAR2,
   principal       IN VARCHAR2,
   is_grant        IN BOOLEAN,
   privilege       IN VARCHAR2,
   position        IN PLS_INTEGER DEFAULT NULL,
   start_date      IN TIMESTAMP WITH TIMESTAMP DEFAULT NULL,
   end_date        IN TIMESTAMP WITH TIMESTAMP DEFAULT NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2 | IN | Name of the ACL. Relative path will be relative to "/sys/acls" |
| principal | VARCHAR2 | IN | Principal (database user or role) to whom the privilege is granted or denied. Case sensitive. |
| is_grant | BOOLEAN | IN | Privilege is granted or denied. |
| privilege | VARCHAR2 | IN | Network privilege to be granted or denied |
| position | PLS_INTEGER | IN | Position (1-based) of the ACE. If a non- NULL value is given, the privilege will be added in a new ACE at the given position and there should not be another ACE for the principal with the same is_grant (grant or deny). If a NULL value is given, the privilege will be added to the ACE matching the principal and the is_grant if one exists, or to the end of the ACL if the matching ACE does not exist. |
| start_date | TIMESTAMP | IN | Start date of the access control entry (ACE). When specified, the ACE will be valid only on and after the specified date. The start_date will be ignored if the privilege is added to an existing ACE. |
| end_date | TIMESTAMP | IN | End date of the access control entry (ACE). When specified, the ACE expires after the specified date. The end_date must be greater than or equal to the start_date . The end_date will be ignored if the privilege is added to an existing ACE. |

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND_HOST_ACE Procedure and the APPEND_WALLET_ACE Procedure . Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND_HOST_ACE Procedure and the APPEND_WALLET_ACE Procedure . Syntax DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE ( acl IN VARCHAR2, principal IN VARCHAR2, is_grant IN BOOLEAN, privilege IN VARCHAR2, position IN PLS_INTEGER DEFAULT NULL, start_date IN TIMESTAMP WITH TIMESTAMP DEFAULT NULL, end_date IN TIMESTAMP WITH TIMESTAMP DEFAULT NULL ); Parameters Table 115-4 ADD_PRIVILEGE Function Parameters Parameter Description acl Name of the ACL. Relative path will be relative to "/sys/acls" principal Principal (database user or role) to whom the privilege is granted or denied. Case sensitive. is_grant Privilege is granted or denied. privilege Network privilege to be granted or denied position Position (1-based) of the ACE. If a non- NULL value is given, the privilege will be added in a new ACE at the given position and there should not be another ACE for the principal with the same is_grant (grant or deny). If a NULL value is given, the privilege will be added to the ACE matching the principal and the is_grant if one exists, or to the end of the ACL if the matching ACE does not exist. start_date Start date of the access control entry (ACE). When specified, the ACE will be valid only on and after the specified date. The start_date will be ignored if the privilege is added to an existing ACE. end_date End date of the access control entry (ACE). When specified, the ACE expires after the specified date. The end_date must be greater than or equal to the start_date . The end_date will be ignored if the privilege is added to an existing ACE. Usage Notes To remove the permission, use the DELETE_PRIVILEGE Procedure .