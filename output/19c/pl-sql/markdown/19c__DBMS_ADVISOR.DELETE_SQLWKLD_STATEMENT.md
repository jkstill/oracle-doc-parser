---
id: 19c__DBMS_ADVISOR.DELETE_SQLWKLD_STATEMENT
name: DBMS_ADVISOR.DELETE_SQLWKLD_STATEMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.DELETE_SQLWKLD_STATEMENT

This procedure deletes one or more statements from a workload.

## Syntax

```sql
DBMS_ADVISOR.DELETE_SQLWKLD_STATEMENT (
   workload_name        IN VARCHAR2,
   sql_id               IN NUMBER);

DBMS_ADVISOR.DELETE_SQLWKLD_STATEMENT (
   workload_name        IN VARCHAR2,
   search               IN VARCHAR2,
   deleted              OUT NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| workload_name | VARCHAR2 | IN | The workload object name that uniquely identifies an existing workload. |
| sql_id | NUMBER) | IN | The Advisor-generated identifier number that is assigned to the statement. To specify all workload statements, use the constant ADVISOR_ALL . |
| search | VARCHAR2 | IN | Disabled. |
| deleted | NUMBER) | OUT | Returns the number of statements deleted by the searched deleted operation. |

## Usage Notes

Note: This procedure has been deprecated. Note: This procedure has been deprecated. Syntax DBMS_ADVISOR.DELETE_SQLWKLD_STATEMENT ( workload_name IN VARCHAR2, sql_id IN NUMBER); DBMS_ADVISOR.DELETE_SQLWKLD_STATEMENT ( workload_name IN VARCHAR2, search IN VARCHAR2, deleted OUT NUMBER); Parameters Table 16-13 DELETE_SQLWKLD_STATEMENT Procedure Parameters Parameter Description workload_name The workload object name that uniquely identifies an existing workload. sql_id The Advisor-generated identifier number that is assigned to the statement. To specify all workload statements, use the constant ADVISOR_ALL . search Disabled. deleted Returns the number of statements deleted by the searched deleted operation. Usage Notes A workload cannot be modified or deleted if it is currently referenced by an active task. A task is considered active if it is not in its initial state. See the RESET_TASK Procedure to set a task to its initial state.