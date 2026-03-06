---
id: 19c__DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SWITCH_CONSUMER_GROUP
name: DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SWITCH_CONSUMER_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER_PRIVS
tags: [dbms_resource_manager_privs]
source_file: DBMS_RESOURCE_MANAGER_PRIVS.html
---

# DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SWITCH_CONSUMER_GROUP

This procedure grants the privilege to switch to a resource consumer group.

## Syntax

```sql
DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SWITCH_CONSUMER_GROUP (
   grantee_name   IN VARCHAR2, 
   consumer_group IN VARCHAR2, 
   grant_option   IN BOOLEAN);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| grantee_name | VARCHAR2 | IN | Name of the user or role to whom privilege is to be granted. |
| consumer_group | VARCHAR2 | IN | Name of consumer group. |
| grant_option | BOOLEAN) | IN | TRUE if grantee should be allowed to grant access, FALSE otherwise. |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SWITCH_CONSUMER_GROUP ( grantee_name IN VARCHAR2, consumer_group IN VARCHAR2, grant_option IN BOOLEAN); Parameters Table 143-2 GRANT_SWITCH_CONSUMER_GROUP Procedure Parameters Parameter Description grantee_name Name of the user or role to whom privilege is to be granted. consumer_group Name of consumer group. grant_option TRUE if grantee should be allowed to grant access, FALSE otherwise. Usage Notes If you grant permission to switch to a particular consumer group to a user, then that user can immediately switch their current consumer group to the new consumer group. If you grant permission to switch to a particular consumer group to a role, then any users who have been granted that role and have enabled that role can immediately switch their current consumer group to the new consumer group. If you grant permission to switch to a particular consumer group to PUBLIC , then any user can switch to that consumer group. If the grant_option parameter is TRUE , then users granted switch privilege for the consumer group may also grant switch privileges for that consumer group to others. In order to set the initial consumer group of a user, you must grant the switch privilege for that group to the user. See Also: DBMS_RESOURCE_MANAGER See Also: DBMS_RESOURCE_MANAGER Examples BEGIN DBMS_RESOURCE_MANAGER_PRIVS.GRANT_SWITCH_CONSUMER_GROUP ( 'scott', 'mail_maintenance_group', true); DBMS_RESOURCE_MANAGER.CREATE_PENDING_AREA(); DBMS_RESOURCE_MANAGER.set_consumer_group_mapping( dbms_resource_manager.oracle_user, 'scott','mail_maintenance_group'); DBMS_RESOURCE_MANAGER.SUBMIT_PENDING_AREA(); END; /