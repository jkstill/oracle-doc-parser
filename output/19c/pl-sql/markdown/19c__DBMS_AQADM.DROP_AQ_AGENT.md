---
id: 19c__DBMS_AQADM.DROP_AQ_AGENT
name: DBMS_AQADM.DROP_AQ_AGENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQADM
tags: [dbms_aqadm]
source_file: DBMS_AQADM.html
---

# DBMS_AQADM.DROP_AQ_AGENT

This procedure drops an agent that was previously registered for Oracle Database Advanced Queuing Internet access.

## Syntax

```sql
DBMS_AQADM.DROP_AQ_AGENT (
  agent_name                IN VARCHAR2)
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent_name | VARCHAR2) | IN | Specifies the username of the Oracle Database Advanced Queuing Internet agent |

## Usage Notes

Syntax DBMS_AQADM.DROP_AQ_AGENT ( agent_name IN VARCHAR2) Parameters Table 23-28 DROP_AQ_AGENT Procedure Parameters Parameter Description agent_name Specifies the username of the Oracle Database Advanced Queuing Internet agent