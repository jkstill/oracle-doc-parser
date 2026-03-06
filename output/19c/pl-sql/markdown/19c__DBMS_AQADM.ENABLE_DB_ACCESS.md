---
id: 19c__DBMS_AQADM.ENABLE_DB_ACCESS
name: DBMS_AQADM.ENABLE_DB_ACCESS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.ENABLE_DB_ACCESS

This procedure grants an Oracle Database Advanced Queuing Internet agent the privileges of a specific database user.

## Syntax

```sql
DBMS_AQADM.ENABLE_DB_ACCESS (
  agent_name                IN VARCHAR2,
  db_username               IN VARCHAR2)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent_name | VARCHAR2 | IN | Specifies the username of the Oracle Database Advanced Queuing Internet agent. |
| db_username | VARCHAR2) | IN | Specified the database user whose privileges are to be granted to the Oracle Database Advanced Queuing Internet agent. |

## Usage Notes

Syntax DBMS_AQADM.ENABLE_DB_ACCESS ( agent_name IN VARCHAR2, db_username IN VARCHAR2) Parameters Table 23-32 ENABLE_DB_ACCESS Procedure Parameters Parameter Description agent_name Specifies the username of the Oracle Database Advanced Queuing Internet agent. db_username Specified the database user whose privileges are to be granted to the Oracle Database Advanced Queuing Internet agent. Usage Notes The Oracle Database Advanced Queuing Internet agent should have been previously created using the CREATE_AQ_AGENT Procedure . For secure queues, the sender and receiver agent of the message must be mapped to the database user performing the enqueue or dequeue operation. The SYS.AQ$INTERNET_USERS view has a list of all Oracle Database Advanced Queuing Internet agents and the names of the database users whose privileges are granted to them.