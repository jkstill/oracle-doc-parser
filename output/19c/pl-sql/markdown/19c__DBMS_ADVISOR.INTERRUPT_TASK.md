---
id: 19c__DBMS_ADVISOR.INTERRUPT_TASK
name: DBMS_ADVISOR.INTERRUPT_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.INTERRUPT_TASK

This procedure stops a currently executing task.

## Syntax

```sql
DBMS_ADVISOR.INTERRUPT_TASK (
   task_name          IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | A single Advisor task name that will be interrupted. |

## Usage Notes

The task will end its operations as it would at a normal exit. The user will be able to access any recommendations that exist to this point. Syntax DBMS_ADVISOR.INTERRUPT_TASK ( task_name IN VARCHAR2); Parameters Table 16-26 INTERRUPT_TASK Procedure Parameters Parameter Description task_name A single Advisor task name that will be interrupted. Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); BEGIN task_name := 'My Task'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.EXECUTE_TASK(task_name); END; / While this session is executing its task, you can interrupt the task from a second session using the following statement: BEGIN DBMS_ADVISOR.INTERRUPT_TASK('My Task'); END; /