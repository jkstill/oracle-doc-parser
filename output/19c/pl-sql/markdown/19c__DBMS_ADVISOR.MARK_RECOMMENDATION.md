---
id: 19c__DBMS_ADVISOR.MARK_RECOMMENDATION
name: DBMS_ADVISOR.MARK_RECOMMENDATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.MARK_RECOMMENDATION

This procedure marks a recommendation for import or implementation.

## Syntax

```sql
DBMS_ADVISOR.MARK_RECOMMENDATION (
   task_name          IN VARCHAR2
   id                 IN NUMBER,
   action             IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task. |
| id | NUMBER | IN | The recommendation identifier number assigned by the Advisor. |
| action | VARCHAR2) | IN | The recommendation action setting. The possible actions are: ACCEPT Marks the recommendation as accepted. With this setting, the recommendation will appear in implementation and undo scripts. IGNORE Marks the recommendation as ignore. With this setting, the recommendation will not appear in an implementation or undo script. REJECT Marks the recommendation as rejected. With this setting, the recommendation will not appear in any implementation or undo scripts. |

## Usage Notes

Syntax DBMS_ADVISOR.MARK_RECOMMENDATION ( task_name IN VARCHAR2 id IN NUMBER, action IN VARCHAR2); Parameters Table 16-27 MARK_RECOMMENDATION Procedure Parameters Parameter Description task_name Name of the task. id The recommendation identifier number assigned by the Advisor. action The recommendation action setting. The possible actions are: ACCEPT Marks the recommendation as accepted. With this setting, the recommendation will appear in implementation and undo scripts. IGNORE Marks the recommendation as ignore. With this setting, the recommendation will not appear in an implementation or undo script. REJECT Marks the recommendation as rejected. With this setting, the recommendation will not appear in any implementation or undo scripts. Usage Notes For a recommendation to be implemented, it must be marked as accepted. By default, all recommendations are considered accepted and will appear in any generated scripts. Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); workload_name VARCHAR2(30); attribute VARCHAR2(100); rec_id NUMBER; BEGIN task_name := 'My Task'; workload_name := 'My Workload'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.CREATE_SQLWKLD(workload_name, 'My Workload'); DBMS_ADVISOR.ADD_SQLWKLD_REF(task_name, workload_name); DBMS_ADVISOR.ADD_SQLWKLD_STATEMENT(workload_name, 'MONTHLY', 'ROLLUP', 100,400,5041,103,640445,680000,2, 1,SYSDATE,1,'SH','SELECT AVG(amount_sold) FROM sh.sales WHERE promo_id = 10'); DBMS_ADVISOR.EXECUTE_TASK(task_name); rec_id := 1; DBMS_ADVISOR.MARK_RECOMMENDATION(task_name, rec_id, 'REJECT'); END; /