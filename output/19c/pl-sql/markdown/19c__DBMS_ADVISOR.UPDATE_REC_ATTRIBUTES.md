---
id: 19c__DBMS_ADVISOR.UPDATE_REC_ATTRIBUTES
name: DBMS_ADVISOR.UPDATE_REC_ATTRIBUTES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.UPDATE_REC_ATTRIBUTES

This procedure updates the owner, name, and tablespace for a recommendation.

## Syntax

```sql
DBMS_ADVISOR.UPDATE_REC_ATTRIBUTES (
   task_name            IN VARCHAR2
   rec_id               IN NUMBER,
   action_id            IN NUMBER,
   attribute_name       IN VARCHAR2,
   value                IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The task name that uniquely identifies an existing task. |
| rec_id | NUMBER | IN | The Advisor-generated identifier number that is assigned to the recommendation. |
| action_id | NUMBER | IN | The Advisor-generated action identifier that is assigned to the particular command. |
| attribute_name | VARCHAR2 | IN | Name of the attribute to be changed. The valid values are: owner The new owner of the object. name The new name of the object. tablespace The new tablespace for the object. |
| value | VARCHAR2) | IN | Specifies the new value for the recommendation attribute. |

## Usage Notes

Syntax DBMS_ADVISOR.UPDATE_REC_ATTRIBUTES ( task_name IN VARCHAR2 rec_id IN NUMBER, action_id IN NUMBER, attribute_name IN VARCHAR2, value IN VARCHAR2); Parameters Table 16-42 UPDATE_REC_ATTRIBUTES Procedure Parameters Parameter Description task_name The task name that uniquely identifies an existing task. rec_id The Advisor-generated identifier number that is assigned to the recommendation. action_id The Advisor-generated action identifier that is assigned to the particular command. attribute_name Name of the attribute to be changed. The valid values are: owner The new owner of the object. name The new name of the object. tablespace The new tablespace for the object. value Specifies the new value for the recommendation attribute. Usage Notes Recommendation attributes cannot be modified unless the task has successfully executed. Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); workload_name VARCHAR2(30); attribute VARCHAR2(100); BEGIN task_name := 'My Task'; workload_name := 'My Workload'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.CREATE_SQLWKLD(workload_name, 'My Workload'); DBMS_ADVISOR.ADD_SQLWKLD_REF(task_name, workload_name); DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT(workload_name, 'MONTHLY', 'ROLLUP', 100,400,5041,103,640445,680000,2, 1,SYSDATE,1,'SH','SELECT AVG(amount_sold) FROM sh.sales WHERE promo_id = 10'); DBMS_ADVISOR.EXECUTE_TASK(task_name); attribute := 'SH'; DBMS_ADVISOR.UPDATE_REC_ATTRIBUTES(task_name, 1, 3, 'OWNER', attribute); END; /