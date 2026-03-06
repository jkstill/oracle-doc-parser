---
id: 19c__DBMS_MONITOR.CLIENT_ID_TRACE_ENABLE
name: DBMS_MONITOR.CLIENT_ID_TRACE_ENABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.CLIENT_ID_TRACE_ENABLE

This procedure will enable the trace for a given client identifier globally for the database.

## Syntax

```sql
DBMS_MONITOR.CLIENT_ID_TRACE_ENABLE(
 client_id    IN  VARCHAR2,
 waits        IN  BOOLEAN DEFAULT TRUE,
 binds        IN  BOOLEAN DEFAULT FALSE,
 plan_stat    IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_id | VARCHAR2 | IN | Database Session Identifier for which SQL tracing is enabled |
| waits | BOOLEAN | IN | If TRUE , wait information is present in the trace |
| binds | BOOLEAN | IN | If TRUE , bind information is present in the trace |
| plan_stat | VARCHAR2 | IN | Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '. |

## Usage Notes

Syntax DBMS_MONITOR.CLIENT_ID_TRACE_ENABLE( client_id IN VARCHAR2, waits IN BOOLEAN DEFAULT TRUE, binds IN BOOLEAN DEFAULT FALSE, plan_stat IN VARCHAR2 DEFAULT NULL); Parameters Table 112-5 CLIENT_ID_TRACE_ENABLE Procedure Parameters Parameter Description client_id Database Session Identifier for which SQL tracing is enabled waits If TRUE , wait information is present in the trace binds If TRUE , bind information is present in the trace plan_stat Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '. Usage Notes The trace will be written to multiple trace files because more than one Oracle shadow process can work on behalf of a given client identifier. The tracing is enabled for all instances and persistent across restarts. Examples EXECUTE DBMS_MONITOR.CLIENT_ID_TRACE_ENABLE('janedoe', TRUE, FALSE);