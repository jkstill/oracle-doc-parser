---
id: 19c__DBMS_PARALLEL_EXECUTE.GENERATE_TASK_NAME
name: DBMS_PARALLEL_EXECUTE.GENERATE_TASK_NAME
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_PARALLEL_EXECUTE
tags: [dbms_parallel_execute]
source_file: DBMS_PARALLEL_EXECUTE.html
---

# DBMS_PARALLEL_EXECUTE.GENERATE_TASK_NAME

This function returns a unique name for a task.

## Syntax

```sql
DBMS_PARALLEL_EXECUTE.GENERATE_TASK_NAME (
   prefix      IN      VARCHAR2 DEFAULT 'TASK$_') 
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| prefix | VARCHAR2 | IN | The prefix to use when generating the task name |

**Returns:** `VARCHAR2`

## Usage Notes

The name is of the form prefix N where N is a number from a sequence. If no prefix is specified, the generated name is, by default, TASK$_1 , TASK$_2 , TASK$_3 , and so on. If ' SCOTT ' is specified as the prefix, the name is SCOTT1 , SCOTT2 , and so on. Syntax DBMS_PARALLEL_EXECUTE.GENERATE_TASK_NAME ( prefix IN VARCHAR2 DEFAULT 'TASK$_') RETURN VARCHAR2; Parameters Table 121-15 GENERATE_TASK_NAME Function Parameters Parameter Description prefix The prefix to use when generating the task name