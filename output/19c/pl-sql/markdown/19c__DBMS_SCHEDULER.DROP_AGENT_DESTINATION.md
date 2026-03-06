---
id: 19c__DBMS_SCHEDULER.DROP_AGENT_DESTINATION
name: DBMS_SCHEDULER.DROP_AGENT_DESTINATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.DROP_AGENT_DESTINATION

This procedure drops one or more external destinations, also known as agent destinations. It should be used only when the preferred method of dropping an external destination, using the schagent utility to unregister a Scheduler agent with a database, is unavailable due to failures.

## Syntax

```sql
DBMS_SCHEDULER.DROP_AGENT_DESTINATION (
   destination_name        IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| destination_name | VARCHAR2) | IN | A comma-separated list of external destinations to drop. Because user SYS owns all external destinations, do not prefix them with a schema name. The procedure stops processing if it encounters an external destination that does not exist. All external destinations processed before the error are dropped. Cannot be NULL . |

## Usage Notes

This procedure can be called only by the SYS user or a user with the MANAGE SCHEDULER privilege. Note: External destinations are created on a source database only implicitly by registering an agent with the database. There is no user-callable CREATE_AGENT_DESTINATION procedure. Note: External destinations are created on a source database only implicitly by registering an agent with the database. There is no user-callable CREATE_AGENT_DESTINATION procedure. Syntax DBMS_SCHEDULER.DROP_AGENT_DESTINATION ( destination_name IN VARCHAR2); Parameters Table 151-43 DROP_AGENT_DESTINATION Procedure Parameters Parameter Description destination_name A comma-separated list of external destinations to drop. Because user SYS owns all external destinations, do not prefix them with a schema name. The procedure stops processing if it encounters an external destination that does not exist. All external destinations processed before the error are dropped. Cannot be NULL . Usage Notes When an external destination is dropped: All database destinations that refer to the external destination are disabled and their agent attribute is set to NULL . Members of external destination groups that refer to the destination are removed from the group. All job instances in the *_SCHEDULER_JOB_DESTS views that refer to the external destination are also dropped. Jobs running against the destination are stopped.