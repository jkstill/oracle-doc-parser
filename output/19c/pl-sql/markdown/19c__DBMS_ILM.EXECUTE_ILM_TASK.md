---
id: 19c__DBMS_ILM.EXECUTE_ILM_TASK
name: DBMS_ILM.EXECUTE_ILM_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ILM
tags: [dbms_ilm]
source_file: DBMS_ILM.html
---

# DBMS_ILM.EXECUTE_ILM_TASK

This procedure executes an ADO task that has been evaluated previously and moves it to an active state.

## Syntax

```sql
DBMS_ILM.EXECUTE_ILM_TASK (
   task_id             IN     NUMBER,
   execution_mode      IN     NUMBER DEFAULT ILM_EXECUTION_ONLINE);
   execution_schedule  IN     NUMBER DEFAULT SCHEDULE_IMMEDIATE);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_id | NUMBER | IN | Identifies a particular ADO task |
| execution_mode | NUMBER | IN | Whether the ADO task be executed online ( ILM_EXECUTION_ONLINE ) or offline ( ILM_EXECUTION_OFFLINE ) |
| execution_schedule | NUMBER | IN | Identifies when the ADO task should be executed.Currently, the only choice available is immediate scheduling of ADO jobs |

## Usage Notes

Syntax DBMS_ILM.EXECUTE_ILM_TASK ( task_id IN NUMBER, execution_mode IN NUMBER DEFAULT ILM_EXECUTION_ONLINE); execution_schedule IN NUMBER DEFAULT SCHEDULE_IMMEDIATE); Parameters Table 86-7 EXECUTE_ILM_TASK Procedure Parameters Parameter Description task_id Identifies a particular ADO task execution_mode Whether the ADO task be executed online ( ILM_EXECUTION_ONLINE ) or offline ( ILM_EXECUTION_OFFLINE ) execution_schedule Identifies when the ADO task should be executed.Currently, the only choice available is immediate scheduling of ADO jobs