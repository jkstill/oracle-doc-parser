---
id: 19c__DBMS_ADVISOR.IMPLEMENT_TASK
name: DBMS_ADVISOR.IMPLEMENT_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.IMPLEMENT_TASK

This procedure implements the recommendations of the specified Advisor task.

## Syntax

```sql
DBMS_ADVISOR.IMPLEMENT_TASK (
   task_name          IN VARCHAR2,
   rec_id             IN NUMBER := NULL,
   exit_on_error      IN BOOLEAN := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The name of the task. |
| rec_id | NUMBER | IN | An optional recommendation ID. |
| exit_on_error | BOOLEAN | IN | An optional Boolean to exit on the first error. |

## Usage Notes

Syntax DBMS_ADVISOR.IMPLEMENT_TASK ( task_name IN VARCHAR2, rec_id IN NUMBER := NULL, exit_on_error IN BOOLEAN := NULL); Parameters Table 16-20 IMPLEMENT_TASK Procedure Parameters Parameter Description task_name The name of the task. rec_id An optional recommendation ID. exit_on_error An optional Boolean to exit on the first error.