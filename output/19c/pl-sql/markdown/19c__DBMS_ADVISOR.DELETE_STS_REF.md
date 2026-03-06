---
id: 19c__DBMS_ADVISOR.DELETE_STS_REF
name: DBMS_ADVISOR.DELETE_STS_REF
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.DELETE_STS_REF

This procedure removes a link between the current SQL Access Advisor task and a SQL tuning set.

## Syntax

```sql
DBMS_ADVISOR.DELETE_STS_REF (
  task_name      IN VARCHAR2 NOT NULL,
  sts_owner      IN VARCHAR2,
  workload_name  IN VARCHAR2 NOT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The SQL Access Advisor task name that uniquely identifies an existing task. |
| sts_owner | VARCHAR2 | IN | The owner of the SQL tuning set. The value of this parameter may be NULL , in which case the advisor assumes the SQL tuning set to be owned by the currently logged-in user. |
| workload_name | VARCHAR2 | IN | The name of the workload to be unlinked. A workload consists of one or more SQL statements, plus statistics and attributes that fully describe each statement. The database stores a workload as a SQL tuning set. The wildcard % is supported as a workload name. The rules of use are identical to the SQL LIKE operator. For example, to remove all links to SQL tuning set objects, use the wildcard % as the STS_NAME . |

## Usage Notes

Use DELETE_STS_REF for any STS-based advisor runs. The older method of using DELETE_SQLWKLD_REF with parameter IS_STS=1 is only supported for backward compatibility. Furthermore, the DELETE_STS_REF function accepts an STS owner name, whereas DELETE_SQLWKLD_REF does not. Syntax DBMS_ADVISOR.DELETE_STS_REF ( task_name IN VARCHAR2 NOT NULL, sts_owner IN VARCHAR2, workload_name IN VARCHAR2 NOT NULL); Parameters Table 16-14 DELETE_STS_REF Procedure Parameters Parameter Description task_name The SQL Access Advisor task name that uniquely identifies an existing task. sts_owner The owner of the SQL tuning set. The value of this parameter may be NULL , in which case the advisor assumes the SQL tuning set to be owned by the currently logged-in user. workload_name The name of the workload to be unlinked. A workload consists of one or more SQL statements, plus statistics and attributes that fully describe each statement. The database stores a workload as a SQL tuning set. The wildcard % is supported as a workload name. The rules of use are identical to the SQL LIKE operator. For example, to remove all links to SQL tuning set objects, use the wildcard % as the STS_NAME . Examples DBMS_ADVISOR.DELETE_STS_REF ('My task', 'SCOTT', 'My workload');