---
id: 19c__DBMS_ADVISOR.DELETE_SQLWKLD_REF
name: DBMS_ADVISOR.DELETE_SQLWKLD_REF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.DELETE_SQLWKLD_REF

This procedure removes a link between the current SQL Access task and a SQL Workload data object.

## Syntax

```sql
DBMS_ADVISOR.DELETE_SQLWKLD_REF (
   task_name              IN VARCHAR2,
   workload_name          IN VARCHAR2,
   is_sts                 IN NUMBER :=0);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The SQL Access task name that uniquely identifies an existing task. |
| workload_name | VARCHAR2 | IN | The name of the workload object to be unlinked. The wildcard % is supported as a workload_name . The rules of use are identical to the LIKE operator. For example, to remove all links to workload objects, use the wildcard % as the workload_name . |
| is_sts | NUMBER | IN | Indicates the type of workload source. Possible values are: 0 - SQL workload object 1 - SQL tuning set |

## Usage Notes

Note: This procedure is deprecated starting in Oracle Database 11 g . Use DELETE_STS_REF instead of DELETE_SQLWKLD_REF for all SQL tuning set-based advisor runs. This function is only provided for backward compatibility. Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.DELETE_SQLWKLD_REF ( task_name IN VARCHAR2, workload_name IN VARCHAR2, is_sts IN NUMBER :=0); Parameters Table 16-12 DELETE_SQLWKLD_REF Procedure Parameters Parameter Description task_name The SQL Access task name that uniquely identifies an existing task. workload_name The name of the workload object to be unlinked. The wildcard % is supported as a workload_name . The rules of use are identical to the LIKE operator. For example, to remove all links to workload objects, use the wildcard % as the workload_name . is_sts Indicates the type of workload source. Possible values are: 0 - SQL workload object 1 - SQL tuning set Examples DECLARE task_id NUMBER; task_name VARCHAR2(30); workload_name VARCHAR2(30); BEGIN task_name := 'My Task'; workload_name := 'My Workload'; DBMS_ADVISOR.CREATE_TASK(DBMS_ADVISOR.SQLACCESS_ADVISOR, task_id, task_name); DBMS_ADVISOR.ADD_SQLWKLD_REF(task_name, workload_name); DBMS_ADVISOR.DELETE_SQLWKLD_REF(task_name, workload_name); END; /