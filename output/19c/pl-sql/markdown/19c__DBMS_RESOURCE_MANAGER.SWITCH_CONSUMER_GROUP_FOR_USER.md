---
id: 19c__DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_USER
name: DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_USER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_USER

This procedure changes the resource consumer group for all sessions with a given user ID. It also changes the consumer group of any parallel execution servers that are related to the top user session.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_USER (
   user            IN VARCHAR2, 
   consumer_group  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| user | VARCHAR2 | IN | Name of the user |
| consumer_group | VARCHAR2) | IN | Name of the consumer group to which to switch |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_USER ( user IN VARCHAR2, consumer_group IN VARCHAR2); Parameters Table 142-25 SWITCH_CONSUMER_GROUP_FOR_USER Procedure Parameters Parameter Description user Name of the user consumer_group Name of the consumer group to which to switch Usage Notes The SWITCH_CONSUMER_GROUP_FOR_SESS Procedure and the SWITCH_CONSUMER_GROUP_FOR_USER procedures let you raise or lower the allocation of CPU resources of certain sessions or users. This provides a functionality similar to the nice command on UNIX. These procedures cause the session to be moved into the newly specified consumer group immediately.