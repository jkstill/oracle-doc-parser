---
id: 19c__DBMS_ADVISOR.ADD_SQLWKLD_REF
name: DBMS_ADVISOR.ADD_SQLWKLD_REF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.ADD_SQLWKLD_REF

This procedure establishes a link between the current SQL Access Advisor task and a SQL Workload object.

## Syntax

```sql
DBMS_ADVISOR.ADD_SQLWKLD_REF (
   task_name              IN VARCHAR2,
   workload_name          IN VARCHAR2,
   is_sts                 IN NUMBER :=0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The SQL Access Advisor task name that uniquely identifies an existing task. |
| workload_name | VARCHAR2 | IN | The name of the workload object to be linked. Once a object has been linked to a task, it becomes read-only and cannot be deleted. There is no limit to the number of links to workload objects. To remove the link to the workload object, use the procedure DELETE_REFERENCE . |
| is_sts | NUMBER | IN | Indicates the type of workload source. Possible values are: 0 - SQL workload object 1 - SQL tuning set |

## Usage Notes

Note: This procedure is deprecated starting in Oracle Database 11 g . The link allows an advisor task to access interesting data for doing an analysis. The link also provides a stable view of the data. Once a connection between a SQL Access Advisor task and a SQL Workload object is made, the workload is protected from removal or modification. Users should use ADD_STS_REF instead of ADD_SQLWKLD_REF for all SQL tuning set-based advisor runs. This function is only provided for backward compatibility. Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.ADD_SQLWKLD_REF ( task_name IN VARCHAR2, workload_name IN VARCHAR2, is_sts IN NUMBER :=0); Parameters Table 16-2 ADD_SQLWKLD_REF Procedure Parameters Parameter Description task_name The SQL Access Advisor task name that uniquely identifies an existing task. workload_name The name of the workload object to be linked. Once a object has been linked to a task, it becomes read-only and cannot be deleted. There is no limit to the number of links to workload objects. To remove the link to the workload object, use the procedure DELETE_REFERENCE . is_sts Indicates the type of workload source. Possible values are: 0 - SQL workload object 1 - SQL tuning set Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); workload_name VARCHAR2(30); BEGIN task_name := 'My Task'; workload_name := 'My Workload'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.ADD_SQLWKLD_REF(task_name, workload_name, 1); END; /