---
id: 19c__DBMS_ADVISOR.CANCEL_TASK
name: DBMS_ADVISOR.CANCEL_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.CANCEL_TASK

This procedure causes a currently executing operation to terminate.

## Syntax

```sql
DBMS_ADVISOR.CANCEL_TASK (
   task_name      IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | A valid Advisor task name that uniquely identifies an existing task. |

## Usage Notes

This call performs a soft interrupt. It will not break into a low-level database access call like a hard interrupt such as Ctrl-C . The SQL Access Advisor periodically checks for soft interrupts and acts appropriately. As a result, this operation may take a few seconds to respond to a call. Syntax DBMS_ADVISOR.CANCEL_TASK ( task_name IN VARCHAR2); Parameters Table 16-5 CANCEL_TASK Procedure Parameter Parameter Description task_name A valid Advisor task name that uniquely identifies an existing task. Usage Notes A cancel command restores the task to its condition prior to the start of the canceled operation. Therefore, a canceled task or data object cannot be resumed. Because all Advisor task procedures are synchronous, to cancel an operation, you must use a separate database session. Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); workload_name VARCHAR2(30); BEGIN task_name := 'My Task'; workload_name := 'My Workload'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.CANCEL_TASK('My Task'); END; /