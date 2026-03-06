---
id: 19c__DBMS_MONITOR.DATABASE_TRACE_ENABLE
name: DBMS_MONITOR.DATABASE_TRACE_ENABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.DATABASE_TRACE_ENABLE

This procedure enables SQL trace for the whole database or a specific instance.

## Syntax

```sql
DBMS_MONITOR.DATABASE_TRACE_ENABLE(
   waits          IN BOOLEAN DEFAULT TRUE,
   binds          IN BOOLEAN DEFAULT FALSE,
   instance_name  IN VARCHAR2 DEFAULT NULL,
   plan_stat      IN VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| waits | BOOLEAN | IN | If TRUE , wait information will be present in the trace |
| binds | BOOLEAN | IN | If TRUE , bind information will be present in the trace |
| instance_name | VARCHAR2 | IN | If set, restricts tracing to the named instance |
| plan_stat | VARCHAR2 | IN | Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '. |

## Usage Notes

Syntax DBMS_MONITOR.DATABASE_TRACE_ENABLE( waits IN BOOLEAN DEFAULT TRUE, binds IN BOOLEAN DEFAULT FALSE, instance_name IN VARCHAR2 DEFAULT NULL, plan_stat IN VARCHAR2 DEFAULT NULL); Parameters Table 112-7 DATABASE_TRACE_ENABLE Procedure Parameters Parameter Description waits If TRUE , wait information will be present in the trace binds If TRUE , bind information will be present in the trace instance_name If set, restricts tracing to the named instance plan_stat Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '.