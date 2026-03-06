---
id: 19c__DBMS_SCHEDULER.GET_AGENT_INFO
name: DBMS_SCHEDULER.GET_AGENT_INFO
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SCHEDULER
tags: [dbms_scheduler]
source_file: DBMS_SCHEDULER.html
---

# DBMS_SCHEDULER.GET_AGENT_INFO

This function can return job information specific to an agent, such as how many are running and so on, depending on the attribute selected.

## Syntax

```sql
DBMS_SCHEDULER.GET_AGENT_INFO (
   agent_name        IN VARCHAR2,
   attribute         IN VARCHAR2) RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| agent_name | VARCHAR2 | IN | The name of an external destination where the agent is running |
| attribute | VARCHAR2) | IN | Possible Attributes values VERSION :. Returns the agent version number. Requires the CREATE JOB system privilege. UPTIME : Returns the time the agent has been up and running. Requires the CREATE JOB system privilege. NUMBER_OF_RUNNING_JOBS : Returns the number of jobs that the agent is currently running. Requires the CREATE JOB system privilege. TOTAL_JOBS_RUN : Returns the number of jobs run by the agent since it was started. Requires the CREATE JOB system privilege. RUNNING_JOBS : Returns a comma-separated list of the names of the jobs running currently. Requires the MANAGE SCHEDULER system privilege. ALL : Returns all the information the previous options return. It requires the MANAGE SCHEDULER system privilege. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SCHEDULER.GET_AGENT_INFO ( agent_name IN VARCHAR2, attribute IN VARCHAR2) RETURN VARCHAR2; Parameters Table 151-64 GET_AGENT_INFO Function Parameter Parameter Description agent_name The name of an external destination where the agent is running attribute Possible Attributes values VERSION :. Returns the agent version number. Requires the CREATE JOB system privilege. UPTIME : Returns the time the agent has been up and running. Requires the CREATE JOB system privilege. NUMBER_OF_RUNNING_JOBS : Returns the number of jobs that the agent is currently running. Requires the CREATE JOB system privilege. TOTAL_JOBS_RUN : Returns the number of jobs run by the agent since it was started. Requires the CREATE JOB system privilege. RUNNING_JOBS : Returns a comma-separated list of the names of the jobs running currently. Requires the MANAGE SCHEDULER system privilege. ALL : Returns all the information the previous options return. It requires the MANAGE SCHEDULER system privilege. Usage Notes This function returns the same information as the schagent utility status option. See Oracle Database Administrator's Guide .