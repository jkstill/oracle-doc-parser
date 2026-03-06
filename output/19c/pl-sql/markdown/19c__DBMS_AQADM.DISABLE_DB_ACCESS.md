---
id: 19c__DBMS_AQADM.DISABLE_DB_ACCESS
name: DBMS_AQADM.DISABLE_DB_ACCESS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.DISABLE_DB_ACCESS

This procedure revokes the privileges of a specific database user from an Oracle Database Advanced Queuing Internet agent.

## Syntax

```sql
DBMS_AQADM.DISABLE_DB_ACCESS (
  agent_name                IN VARCHAR2,
  db_username               IN VARCHAR2)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent_name | VARCHAR2 | IN | Specifies the username of the Oracle Database Advanced Queuing Internet agent. |
| db_username | VARCHAR2) | IN | Specifies the database user whose privileges are to be revoked from the Oracle Database Advanced Queuing Internet agent. |

## Usage Notes

Syntax DBMS_AQADM.DISABLE_DB_ACCESS ( agent_name IN VARCHAR2, db_username IN VARCHAR2) Parameters Table 23-26 DISABLE_DB_ACCESS Procedure Parameters Parameter Description agent_name Specifies the username of the Oracle Database Advanced Queuing Internet agent. db_username Specifies the database user whose privileges are to be revoked from the Oracle Database Advanced Queuing Internet agent. Usage Notes The Oracle Database Advanced Queuing Internet agent should have been previously granted those privileges using the ENABLE_DB_ACCESS Procedure .