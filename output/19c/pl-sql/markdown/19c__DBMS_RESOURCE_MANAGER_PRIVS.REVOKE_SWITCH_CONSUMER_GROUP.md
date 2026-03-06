---
id: 19c__DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SWITCH_CONSUMER_GROUP
name: DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SWITCH_CONSUMER_GROUP
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER_PRIVS
tags: [dbms_resource_manager_privs]
source_file: DBMS_RESOURCE_MANAGER_PRIVS.html
---

# DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SWITCH_CONSUMER_GROUP

This procedure revokes the privilege to switch to a resource consumer group.

## Syntax

```sql
DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SWITCH_CONSUMER_GROUP (
   revokee_name   IN VARCHAR2, 
   consumer_group IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| revokee_name | VARCHAR2 | IN | Name of user/role from which to revoke access. |
| consumer_group | VARCHAR2) | IN | Name of consumer group. |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SWITCH_CONSUMER_GROUP ( revokee_name IN VARCHAR2, consumer_group IN VARCHAR2); Parameters Table 143-4 REVOKE_SWITCH_CONSUMER_GROUP Procedure Parameter Parameter Description revokee_name Name of user/role from which to revoke access. consumer_group Name of consumer group. Usage Notes If you revoke a user's switch privilege for a particular consumer group, then any subsequent attempts by that user to switch to that consumer group will fail. If you revoke the initial consumer group from a user, then that user will automatically be part of the DEFAULT_CONSUMER_GROUP consumer group when logging in. If you revoke the switch privilege for a consumer group from a role, then any users who only had switch privilege for the consumer group through that role will not be able to switch to that consumer group. If you revoke the switch privilege for a consumer group from PUBLIC , then any users who could previously only use the consumer group through PUBLIC will not be able to switch to that consumer group. Examples The following example revokes the privileges to switch to mail_maintenance_group from Scott: BEGIN DBMS_RESOURCE_MANAGER_PRIVS.REVOKE_SWITCH_CONSUMER_GROUP ( 'scott', 'mail_maintenance_group'); END; /