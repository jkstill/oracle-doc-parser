---
id: 19c__DBMS_MGWADM.SHUTDOWN
name: DBMS_MGWADM.SHUTDOWN
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.SHUTDOWN

This procedure shuts down the Messaging Gateway agent. No propagation activity occurs until Messaging Gateway is restarted.

## Syntax

```sql
DBMS_MGWADM.SHUTDOWN (
   sdmode      IN BINARY_INTEGER DEFAULT DBMS_MGWADM.SHUTDOWN_NORMAL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sdmode | BINARY_INTEGER | IN | The shutdown mode. The only value currently supported is DBMS_MGWADM.SHUTDOWN_NORMAL for normal shutdown. The Messaging Gateway agent may attempt to complete any propagation work currently in progress. |
| agent_name |  |  | Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. |

## Usage Notes

Syntax DBMS_MGWADM.SHUTDOWN ( sdmode IN BINARY_INTEGER DEFAULT DBMS_MGWADM.SHUTDOWN_NORMAL); DBMS_MGWADM.SHUTDOWN ( agent_name IN VARCHAR2); Parameters Table 110-48 SHUTDOWN Procedure Parameters Parameter Description sdmode The shutdown mode. The only value currently supported is DBMS_MGWADM.SHUTDOWN_NORMAL for normal shutdown. The Messaging Gateway agent may attempt to complete any propagation work currently in progress. agent_name Identifies the Messaging Gateway agent. DBMS_MGWADM . DEFAULT_AGENT specifies the default agent. Usage Notes The Messaging Gateway default agent is shut down if no agent name is specified.