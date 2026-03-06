---
id: 19c__DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_SESS
name: DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_SESS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_SESS

This procedure changes the resource consumer group of a specific session. It also changes the consumer group of any parallel execution servers that are related to the top user session. This procedure is RAC instance specific. You need to connect to the PDB in same RAC instance where the session to be switched is running, and then run this procedure.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_SESS (
   session_id      IN NUMBER, 
   session_serial  IN NUMBER, 
   consumer_group  IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| session_id | NUMBER | IN | SID column from the view V$SESSION |
| session_serial | NUMBER | IN | SERIAL# column from view V$SESSION . |
| consumer_group | VARCHAR2) | IN | Name of the consumer group to which to switch |

## Usage Notes

Syntax DBMS_RESOURCE_MANAGER.SWITCH_CONSUMER_GROUP_FOR_SESS ( session_id IN NUMBER, session_serial IN NUMBER, consumer_group IN VARCHAR2); Parameters Table 142-24 SWITCH_CONSUMER_GROUP_FOR_SESS Procedure Parameters Parameter Description session_id SID column from the view V$SESSION session_serial SERIAL# column from view V$SESSION . consumer_group Name of the consumer group to which to switch