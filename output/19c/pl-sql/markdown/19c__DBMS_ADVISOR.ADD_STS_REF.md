---
id: 19c__DBMS_ADVISOR.ADD_STS_REF
name: DBMS_ADVISOR.ADD_STS_REF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.ADD_STS_REF

This procedure establishes a link between the current SQL Access Advisor task and a SQL tuning set.

## Syntax

```sql
DBMS_ADVISOR.ADD_STS_REF(
  task_name       IN VARCHAR2 NOT NULL,
  sts_owner       IN VARCHAR2,
  workload_name   IN VARCHAR2 NOT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The SQL Access Advisor task name that uniquely identifies an existing task. |
| sts_owner | VARCHAR2 | IN | The owner of the SQL tuning set. The value of this parameter may be NULL , in which case the advisor assumes the SQL tuning set to be owned by the currently logged-in user. |
| workload_name | VARCHAR2 | IN | The name of the workload to be linked. A workload consists of one or more SQL statements, plus statistics and attributes that fully describe each statement. The database stores a workload as a SQL tuning set. After a workload has been linked to a task, it becomes read-only and cannot be deleted. There is no limit to the number of links to workloads. To remove the link to the workload, use the procedure DBMS_ADVISOR.DELETE_STS_REF . |

## Usage Notes

The link enables an advisor task to access data for the purpose of doing an analysis. The link also provides a stable view of the data. Once a connection between a SQL Access Advisor task and a SQL tuning set is made, the STS is protected from removal or modification. Use ADD_STS_REF for any STS-based advisor runs. The older method of using ADD_SQLWKLD_REF with parameter IS_STS=1 is only supported for backward compatibility. Furthermore, the ADD_STS_REF function accepts a SQL tuning set owner name, whereas ADD_SQLWKLD_REF does not. Syntax DBMS_ADVISOR.ADD_STS_REF( task_name IN VARCHAR2 NOT NULL, sts_owner IN VARCHAR2, workload_name IN VARCHAR2 NOT NULL); Parameters Table 16-4 ADD_STS_REF Procedure Parameters Parameter Description task_name The SQL Access Advisor task name that uniquely identifies an existing task. sts_owner The owner of the SQL tuning set. The value of this parameter may be NULL , in which case the advisor assumes the SQL tuning set to be owned by the currently logged-in user. workload_name The name of the workload to be linked. A workload consists of one or more SQL statements, plus statistics and attributes that fully describe each statement. The database stores a workload as a SQL tuning set. After a workload has been linked to a task, it becomes read-only and cannot be deleted. There is no limit to the number of links to workloads. To remove the link to the workload, use the procedure DBMS_ADVISOR.DELETE_STS_REF . Examples DBMS_ADVISOR.ADD_STS_REF ('My Task', 'SCOTT', 'My Workload');