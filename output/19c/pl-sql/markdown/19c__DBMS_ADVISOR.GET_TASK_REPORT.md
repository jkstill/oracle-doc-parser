---
id: 19c__DBMS_ADVISOR.GET_TASK_REPORT
name: DBMS_ADVISOR.GET_TASK_REPORT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.GET_TASK_REPORT

This function creates and returns a report for the specified task.

## Syntax

```sql
DBMS_ADVISOR.GET_TASK_REPORT (
   task_name      IN VARCHAR2,
   type           IN VARCHAR2 := 'TEXT',
   level          IN VARCHAR2 := 'TYPICAL',
   section        IN VARCHAR2 := 'ALL',
   owner_name     IN VARCHAR2 := NULL,
   execution_name IN VARCHAR2 := NULL,
   object_id      IN NUMBER   := NULL)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The name of the task from which the script will be created. |
| type | VARCHAR2 | IN | The only valid value is TEXT . |
| level | VARCHAR2 | IN | The possible values are BASIC , TYPICAL , and ALL . |
| section | VARCHAR2 | IN | Advisor-specific report sections. |
| owner_name | VARCHAR2 | IN | Owner of the task. If specified, the system will check to see if the current user has read privileges to the task data. |
| execution_name | VARCHAR2 | IN | An identifier of a specific execution of the task. It is needed only for advisors that allow their tasks to be executed multiple times. |
| object_id | NUMBER | IN | An identifier of an advisor object that can be targeted by the script. |

**Returns:** `CLOB`

## Usage Notes

Syntax DBMS_ADVISOR.GET_TASK_REPORT ( task_name IN VARCHAR2, type IN VARCHAR2 := 'TEXT', level IN VARCHAR2 := 'TYPICAL', section IN VARCHAR2 := 'ALL', owner_name IN VARCHAR2 := NULL, execution_name IN VARCHAR2 := NULL, object_id IN NUMBER := NULL) RETURN CLOB; Parameters Table 16-18 GET_TASK_REPORT Function Parameters Parameter Description task_name The name of the task from which the script will be created. type The only valid value is TEXT . level The possible values are BASIC , TYPICAL , and ALL . section Advisor-specific report sections. owner_name Owner of the task. If specified, the system will check to see if the current user has read privileges to the task data. execution_name An identifier of a specific execution of the task. It is needed only for advisors that allow their tasks to be executed multiple times. object_id An identifier of an advisor object that can be targeted by the script. Return Values Returns the buffer receiving the script.