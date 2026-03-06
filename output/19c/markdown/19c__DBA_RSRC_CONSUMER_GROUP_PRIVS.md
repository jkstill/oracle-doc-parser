---
id: 19c__DBA_RSRC_CONSUMER_GROUP_PRIVS
name: DBA_RSRC_CONSUMER_GROUP_PRIVS
object_type: data_dictionary_view
oracle_version: 19c
doc_type: database_reference
category: security
tags: [dba]
source_file: DBA_RSRC_CONSUMER_GROUP_PRIVS.html
---

# DBA_RSRC_CONSUMER_GROUP_PRIVS

DBA_RSRC_CONSUMER_GROUP_PRIVS displays information about all resource consumer groups and the users and roles assigned to them.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| GRANTEE | VARCHAR2(128) | User or role receiving the grant |
| GRANTED_GROUP | VARCHAR2(128) | Granted consumer group name |
| GRANT_OPTION | VARCHAR2(3) | Indicates whether the grant was with the GRANT option ( YES ) or not ( NO ) |
| INITIAL_GROUP | VARCHAR2(3) | Indicates whether the consumer group is designated as the default for this user or role ( YES ) or not ( NO ) |

## Usage Notes

The grant referred to in this view and the related view is the grant of the SWITCH_CONSUMER_GROUP object privilege, which is granted using the DBMS_RESOURCE_MANAGER_PRIVS package. This privilege is not granted through the GRANT SQL statement. Related View USER_RSRC_CONSUMER_GROUP_PRIVS displays information about the resource consumer groups to which the current user is assigned. This view does not display the GRANTEE column. See Also: " USER_RSRC_CONSUMER_GROUP_PRIVS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_RESOURCE_MANAGER_PRIVS package See Also: " USER_RSRC_CONSUMER_GROUP_PRIVS " Oracle Database PL/SQL Packages and Types Reference for more information about the DBMS_RESOURCE_MANAGER_PRIVS package