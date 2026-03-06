---
id: 19c__DBMS_SQLDIAG.CREATE_DIAGNOSIS_TASK
name: DBMS_SQLDIAG.CREATE_DIAGNOSIS_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLDIAG
tags: [dbms_sqldiag]
source_file: DBMS_SQLDIAG.html
---

# DBMS_SQLDIAG.CREATE_DIAGNOSIS_TASK

This function creates a diagnostic task in order to diagnose a single SQL statement. It returns a SQL diagnosis task unique name

## Syntax

```sql
DBMS_SQLDIAG.CREATE_DIAGNOSIS_TASK (
    sql_text           IN   CLOB,
    bind_list          IN   sql_binds := NULL,
    user_name          IN   VARCHAR2  := NULL,
    scope              IN   VARCHAR2  := SCOPE_COMPREHENSIVE,
    time_limit         IN   NUMBER    := TIME_LIMIT_DEFAULT,
    task_name          IN   VARCHAR2  := NULL,
    description        IN   VARCHAR2  := NULL,
    problem_type       IN   NUMBER    := PROBLEM_TYPE_PERFORMANCE)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_text | CLOB | IN | Text of a SQL statement |
| bind_list | sql_binds | IN | Set of bind values |
| user_name | VARCHAR2 | IN | Username for who the statement/sqlset will be diagnosed |
| scope | VARCHAR2 | IN | Diagnosis scope (limited/comprehensive) |
| time_limit | NUMBER | IN | Maximum duration in seconds for the diagnosis session |
| task_name | VARCHAR2 | IN | Optional diagnosis task name |
| description | VARCHAR2 | IN | Maximum of 256 SQL diagnosis session description |
| problem_type | NUMBER | IN | Determines the goal of the task. Possible values are: PROBLEM_TYPE_WRONG_RESULTS PROBLEM_TYPE_COMPILATION_ERROR PROBLEM_TYPE_EXECUTION_ERROR |
| sql_id |  |  | Identifier of the statement |
| plan_hash_value |  |  | Hash value of the SQL execution plan |
| sqlset_name |  |  | Sqlset name |
| basic_filter |  |  | SQL predicate to filter the SQL from the SQL tuning set (STS) |
| object_filter |  |  | Object filter |
| rank(i) |  |  | Order-by clause on the selected SQL |
| result_percentage |  |  | Percentage on the sum of a ranking measure |
| result_limit |  |  | Top L(imit) SQL from (filtered/ranked) SQL |
| plan_filter |  |  | Plan filter. It is applicable in case there are multiple plans ( plan_hash_value ). This filter allows selecting one plan (plan_hash_value) only. Possible values are: LAST_GENERATED : plan with most recent timestamp FIRST_GENERATED : opposite to LAST_GENERATED LAST_LOADED : plan with most recent first_load_time stat info FIRST_LOADED : opposite to LAST_LOADED MAX_ELAPSED_TIME : plan with maximum elapsed time MAX_BUFFER_GETS : plan with maximum buffer gets MAX_DISK_READS : plan with maximum disk reads MAX_DIRECT_WRITES : plan with maximum direct writes MAX_OPTIMIZER_COST : plan with maximum optimum cost |
| sqlset_owner |  |  | Owner of the sqlset, or null for current schema owner |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax Prepares the diagnosis of a single statement given its text: DBMS_SQLDIAG.CREATE_DIAGNOSIS_TASK ( sql_text IN CLOB, bind_list IN sql_binds := NULL, user_name IN VARCHAR2 := NULL, scope IN VARCHAR2 := SCOPE_COMPREHENSIVE, time_limit IN NUMBER := TIME_LIMIT_DEFAULT, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, problem_type IN NUMBER := PROBLEM_TYPE_PERFORMANCE) RETURN VARCHAR2; Prepares the diagnosis of a single statement from the Cursor Cache given its identifier: DBMS_SQLDIAG.CREATE_DIAGNOSIS_TASK ( sql_id IN VARCHAR2, plan_hash_value IN NUMBER := NULL, scope IN VARCHAR2 := SCOPE_COMPREHENSIVE, time_limit IN NUMBER := TIME_LIMIT_DEFAULT, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, problem_type IN NUMBER := PROBLEM_TYPE_PERFORMANCE) RETURN VARCHAR2; Prepares the diagnosis of a Sqlset: DBMS_SQLDIAG.CREATE_DIAGNOSIS_TASK ( sqlset_name IN VARCHAR2, basic_filter IN VARCHAR2 := NULL, object_filter IN VARCHAR2 := NULL, rank1 IN VARCHAR2 := NULL, rank2 IN VARCHAR2 := NULL, rank3 IN VARCHAR2 := NULL, result_percentage IN NUMBER := NULL, result_limit IN NUMBER := NULL, scope IN VARCHAR2 := SCOPE_COMPREHENSIVE, time_limit IN NUMBER := TIME_LIMIT_DEFAULT, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL, plan_filter IN VARCHAR2 := 'MAX_ELAPSED_TIME', sqlset_owner IN VARCHAR2 := NULL, problem_type IN NUMBER := PROBLEM_TYPE_PERFORMANCE) RETURN VARCHAR2; Parameters Table 165-13 CREATE_DIAGNOSIS_TASK Function Parameters Parameter Description sql_text Text of a SQL statement bind_list Set of bind values user_name Username for who the statement/sqlset will be diagnosed scope Diagnosis scope (limited/comprehensive) time_limit Maximum duration in seconds for the diagnosis session task_name Optional diagnosis task name description Maximum of 256 SQL diagnosis session description problem_type Determines the goal of the task. Possible values are: PROBLEM_TYPE_WRONG_RESULTS PROBLEM_TYPE_COMPILATION_ERROR PROBLEM_TYPE_EXECUTION_ERROR sql_id Identifier of the statement plan_hash_value Hash value of the SQL execution plan sqlset_name Sqlset name basic_filter SQL predicate to filter the SQL from the SQL tuning set (STS) object_filter Object filter rank(i) Order-by clause on the selected SQL result_percentage Percentage on the sum of a ranking measure result_limit Top L(imit) SQL from (filtered/ranked) SQL plan_filter Plan filter. It is applicable in case there are multiple plans ( plan_hash_value ). This filter allows selecting one plan (plan_hash_value) only. Possible values are: LAST_GENERATED : plan with most recent timestamp FIRST_GENERATED : opposite to LAST_GENERATED LAST_LOADED : plan with most recent first_load_time stat info FIRST_LOADED : opposite to LAST_LOADED MAX_ELAPSED_TIME : plan with maximum elapsed time MAX_BUFFER_GETS : plan with maximum buffer gets MAX_DISK_READS : plan with maximum disk reads MAX_DIRECT_WRITES : plan with maximum direct writes MAX_OPTIMIZER_COST : plan with maximum optimum cost sqlset_owner Owner of the sqlset, or null for current schema owner