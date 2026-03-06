---
id: 19c__DBMS_MGWADM.REMOVE_AGENT
name: DBMS_MGWADM.REMOVE_AGENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MGWADM
tags: [dbms_mgwadm]
source_file: DBMS_MGWADM.html
---

# DBMS_MGWADM.REMOVE_AGENT

This procedure removes a Messaging Gateway agent.

## Syntax

```sql
DBMS_MGWADM.REMOVE_AGENT(
   agent_name   IN   VARCHAR2 );
```

## Usage Notes

Syntax DBMS_MGWADM.REMOVE_AGENT( agent_name IN VARCHAR2 ); Parameters Table 110-38 REMOVE_AGENT Procedure Parameters Parameters Description agent_name Identifies the Messaging Gateway agent Usage Notes All messaging system links associated with this Messaging Gateway agent must be removed and the agent must be stopped before it can be removed. The Messaging Gateway default agent cannot be removed.