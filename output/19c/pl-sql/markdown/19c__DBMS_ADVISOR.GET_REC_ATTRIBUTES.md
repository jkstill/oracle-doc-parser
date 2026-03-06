---
id: 19c__DBMS_ADVISOR.GET_REC_ATTRIBUTES
name: DBMS_ADVISOR.GET_REC_ATTRIBUTES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.GET_REC_ATTRIBUTES

This procedure retrieves a specified attribute of a new object as recommended by Advisor analysis.

## Syntax

```sql
DBMS_ADVISOR.GET_REC_ATTRIBUTES (
   workload_name         IN VARCHAR2,
   rec_id                IN NUMBER,
   action_id             IN NUMBER,
   attribute_name        IN VARCHAR2,
   value                 OUT VARCHAR2,
   owner_name            IN VARCHAR2 := NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name |  |  | The task name that uniquely identifies an existing task. |
| rec_id | NUMBER | IN | The Advisor-generated identifier number that is assigned to the recommendation. |
| action_id | NUMBER | IN | The Advisor-generated action identifier that is assigned to the particular command. |
| attribute_name | VARCHAR2 | IN | Specifies the attribute to change. |
| value | VARCHAR2 | OUT | The buffer to receive the requested attribute value. |
| owner_name | VARCHAR2 | IN | Optional owner name of the target task. This permits access to task data not owned by the current user. |

## Usage Notes

Syntax DBMS_ADVISOR.GET_REC_ATTRIBUTES ( workload_name IN VARCHAR2, rec_id IN NUMBER, action_id IN NUMBER, attribute_name IN VARCHAR2, value OUT VARCHAR2, owner_name IN VARCHAR2 := NULL); Parameters Table 16-17 GET_REC_ATTRIBUTES Procedure Parameters Parameter Description task_name The task name that uniquely identifies an existing task. rec_id The Advisor-generated identifier number that is assigned to the recommendation. action_id The Advisor-generated action identifier that is assigned to the particular command. attribute_name Specifies the attribute to change. value The buffer to receive the requested attribute value. owner_name Optional owner name of the target task. This permits access to task data not owned by the current user. Return Values The requested attribute value is returned in the VALUE argument. Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); workload_name VARCHAR2(30); attribute VARCHAR2(100); BEGIN task_name := 'My Task'; workload_name := 'My Workload'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.CREATE_SQLWKLD(workload_name, 'My Workload'); DBMS_ADVISOR.ADD_SQLWKLD_REF(task_name, workload_name); DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT(workload_name, 'MONTHLY', 'ROLLUP', 100,400,5041,103,640445,680000,2, 1,SYSDATE,1,'SH','SELECT AVG(amount_sold) FROM sh.sales WHERE promo_id = 10'); DBMS_ADVISOR.EXECUTE_TASK(task_name); DBMS_ADVISOR.GET_REC_ATTRIBUTES(task_name, 1, 1, 'NAME', attribute); END; /