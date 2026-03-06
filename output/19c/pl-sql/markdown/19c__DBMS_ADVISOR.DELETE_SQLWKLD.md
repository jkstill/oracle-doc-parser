---
id: 19c__DBMS_ADVISOR.DELETE_SQLWKLD
name: DBMS_ADVISOR.DELETE_SQLWKLD
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.DELETE_SQLWKLD

This procedure deletes an existing SQL Workload object from the repository.

## Syntax

```sql
DBMS_ADVISOR.DELETE_SQLWKLD (
   workload_name        IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2) | IN | The workload object name that uniquely identifies an existing workload. The wildcard % is supported as a WORKLOAD_NAME . The rules of use are identical to the LIKE operator. For example, to delete all tasks for the current user, use the wildcard % as the WORKLOAD_NAME . If a wildcard is provided, the DELETE_SQLWKLD operation will not delete any workloads marked as READ_ONLY or TEMPLATE . |

## Usage Notes

Note: This procedure is deprecated starting in Oracle Database 11 g . Note: This procedure is deprecated starting in Oracle Database 11 g . Syntax DBMS_ADVISOR.DELETE_SQLWKLD ( workload_name IN VARCHAR2); Parameters Table 16-11 DELETE_SQLWKLD Procedure Parameters Parameter Description workload_name The workload object name that uniquely identifies an existing workload. The wildcard % is supported as a WORKLOAD_NAME . The rules of use are identical to the LIKE operator. For example, to delete all tasks for the current user, use the wildcard % as the WORKLOAD_NAME . If a wildcard is provided, the DELETE_SQLWKLD operation will not delete any workloads marked as READ_ONLY or TEMPLATE . Usage Notes A workload cannot be modified or deleted if it is currently referenced by an active task. A task is considered active if it is not in its initial state. See the RESET_TASK Procedure to set a task to its initial state.