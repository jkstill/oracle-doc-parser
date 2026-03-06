---
id: 19c__DBMS_ADVISOR.RESET_TASK
name: DBMS_ADVISOR.RESET_TASK
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.RESET_TASK

This procedure re-initializes the metadata for the specified task. The task status will be set to INITIAL .

## Syntax

```sql
DBMS_ADVISOR.RESET_TASK (
   task_name          IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2) | IN | The task name that uniquely identifies an existing task. |

## Usage Notes

Syntax DBMS_ADVISOR.RESET_TASK ( task_name IN VARCHAR2); Parameters Table 16-30 RESET_TASK Procedure Parameters Parameter Description task_name The task name that uniquely identifies an existing task. Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); workload_name VARCHAR2(30); BEGIN task_name := 'My Task'; workload_name := 'My Workload'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.ADD_SQLWKLD_REF(task_name, workload_name); DBMS_ADVISOR.EXECUTE_TASK(task_name); DBMS_ADVISOR.RESET_TASK(task_name); END; /