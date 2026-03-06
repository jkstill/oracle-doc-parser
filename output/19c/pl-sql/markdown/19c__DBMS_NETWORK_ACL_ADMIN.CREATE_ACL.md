---
id: 19c__DBMS_NETWORK_ACL_ADMIN.CREATE_ACL
name: DBMS_NETWORK_ACL_ADMIN.CREATE_ACL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_NETWORK_ACL_ADMIN
tags: [dbms_network_acl_admin]
source_file: DBMS_NETWORK_ACL_ADMIN.html
---

# DBMS_NETWORK_ACL_ADMIN.CREATE_ACL

This deprecated procedure creates an access control list (ACL) with an initial privilege setting. An ACL must have at least one privilege setting. The ACL has no access control effect unless it is assigned to the network target.

## Syntax

```sql
DBMS_NETWORK_ACL_ADMIN.CREATE_ACL (
   acl             IN VARCHAR2,
   description     IN VARCHAR2,
   principal       IN VARCHAR2,
   is_grant        IN BOOLEAN,
   privilege       IN VARCHAR2,
   start_date      IN TIMESTAMP WITH TIMEZONE DEFAULT NULL,
   end_date        IN TIMESTAMP WITH TIMEZONE DEFAULT NULL );
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| acl | VARCHAR2 | IN | Name of the ACL. Relative path will be relative to "/sys/acls". |
| description | VARCHAR2 | IN | Description attribute in the ACL |
| principal | VARCHAR2 | IN | Principal (database user or role) to whom the privilege is granted or denied. Case sensitive. |
| is_grant | BOOLEAN | IN | Privilege is granted or not (denied) |
| privilege | VARCHAR2 | IN | Network privilege to be granted or denied - 'connect | resolve' (case sensitive). A database user needs the connect privilege to an external network host computer if he or she is connecting using the UTL_TCP , UTL_HTTP , UTL_SMTP , and UTL_MAIL utility packages. To resolve a host name that was given a host IP address, or the IP address that was given a host name, with the UTL_INADDR package, grant the database user the resolve privilege. |
| start_date | TIMESTAMP | IN | Start date of the access control entry (ACE). When specified, the ACE is valid only on and after the specified date. |
| end_date | TIMESTAMP | IN | End date of the access control entry (ACE). When specified, the ACE expires after the specified date. The end_date must be greater than or equal to the start_date . |

## Usage Notes

Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND_HOST_ACE Procedure and the APPEND_WALLET_ACE Procedure . Note: This procedure is deprecated in Oracle Database 12 c . While the procedure remains available in the package for reasons of backward compatibility, Oracle recommends using the APPEND_HOST_ACE Procedure and the APPEND_WALLET_ACE Procedure . Syntax DBMS_NETWORK_ACL_ADMIN.CREATE_ACL ( acl IN VARCHAR2, description IN VARCHAR2, principal IN VARCHAR2, is_grant IN BOOLEAN, privilege IN VARCHAR2, start_date IN TIMESTAMP WITH TIMEZONE DEFAULT NULL, end_date IN TIMESTAMP WITH TIMEZONE DEFAULT NULL ); Parameters Table 115-13 CREATE_ACL Procedure Parameters Parameter Description acl Name of the ACL. Relative path will be relative to "/sys/acls". description Description attribute in the ACL principal Principal (database user or role) to whom the privilege is granted or denied. Case sensitive. is_grant Privilege is granted or not (denied) privilege Network privilege to be granted or denied - 'connect | resolve' (case sensitive). A database user needs the connect privilege to an external network host computer if he or she is connecting using the UTL_TCP , UTL_HTTP , UTL_SMTP , and UTL_MAIL utility packages. To resolve a host name that was given a host IP address, or the IP address that was given a host name, with the UTL_INADDR package, grant the database user the resolve privilege. start_date Start date of the access control entry (ACE). When specified, the ACE is valid only on and after the specified date. end_date End date of the access control entry (ACE). When specified, the ACE expires after the specified date. The end_date must be greater than or equal to the start_date . Usage Notes To drop the access control list, use the DROP_ACL Procedure .