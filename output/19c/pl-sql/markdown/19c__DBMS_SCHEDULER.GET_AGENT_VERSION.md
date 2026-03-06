---
id: 19c__DBMS_SCHEDULER.GET_AGENT_VERSION
name: DBMS_SCHEDULER.GET_AGENT_VERSION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.GET_AGENT_VERSION

This function returns the version string of a Scheduler agent that is registered with the database and is currently running. GET_AGENT_VERSION throws an error if the agent is not registered with the database or if the agent is not currently running.

## Syntax

```sql
DBMS_SCHEDULER.GET_AGENT_VERSION (
   agent_host        IN VARCHAR2) RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent_host | VARCHAR2) | IN | Either the hostname and port on which the agent is running in the form hostname:port or the name of the agent as shown in the destination_name column of the ALL_SCHEDULER_EXTERNAL_DESTS view which lists all Scheduler agents registered with the database. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SCHEDULER.GET_AGENT_VERSION ( agent_host IN VARCHAR2) RETURN VARCHAR2; Parameters Table 151-65 GET_AGENT_VERSION Function Parameter Parameter Description agent_host Either the hostname and port on which the agent is running in the form hostname:port or the name of the agent as shown in the destination_name column of the ALL_SCHEDULER_EXTERNAL_DESTS view which lists all Scheduler agents registered with the database. Usage Notes This function requires the CREATE EXTERNAL JOB system privilege.