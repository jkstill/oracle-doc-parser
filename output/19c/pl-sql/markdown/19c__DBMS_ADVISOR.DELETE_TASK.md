---
id: 19c__DBMS_ADVISOR.DELETE_TASK
name: DBMS_ADVISOR.DELETE_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.DELETE_TASK

This procedure deletes an existing task from the repository.

## Syntax

```sql
DBMS_ADVISOR.DELETE_TASK (
   task_name          IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | A single Advisor task name that will be deleted from the repository. The wildcard % is supported as a TASK_NAME . The rules of use are identical to the LIKE operator. For example, to delete all tasks for the current user, use the wildcard % as the TASK_NAME . If a wildcard is provided, the DELETE_TASK operation will not delete any tasks marked as READ_ONLY or TEMPLATE . |

## Usage Notes

Syntax DBMS_ADVISOR.DELETE_TASK ( task_name IN VARCHAR2); Parameters Table 16-15 DELETE_TASK Procedure Parameters Parameter Description task_name A single Advisor task name that will be deleted from the repository. The wildcard % is supported as a TASK_NAME . The rules of use are identical to the LIKE operator. For example, to delete all tasks for the current user, use the wildcard % as the TASK_NAME . If a wildcard is provided, the DELETE_TASK operation will not delete any tasks marked as READ_ONLY or TEMPLATE . Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); BEGIN task_name := 'My Task'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.DELETE_TASK(task_name); END; /