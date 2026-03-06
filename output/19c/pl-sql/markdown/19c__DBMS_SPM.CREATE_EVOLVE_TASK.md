---
id: 19c__DBMS_SPM.CREATE_EVOLVE_TASK
name: DBMS_SPM.CREATE_EVOLVE_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SPM
tags: [dbms_spm]
source_file: DBMS_SPM.html
---

# DBMS_SPM.CREATE_EVOLVE_TASK

The function has two overloads, both of which create an advisor task and sets its parameters. This version which takes a SQL handle creates an evolve task in order to evolve one or more plans for a given SQL statement.

## Syntax

```sql
DBMS_SPM.CREATE_EVOLVE_TASK (
   sql_handle    IN  VARCHAR2  := NULL,
   plan_name     IN  VARCHAR2  := NULL,
   time_limit    IN  NUMBER    := DBMS_SPM.AUTO_LIMIT,
   task_name     IN  VARCHAR2  := NULL,
   description   IN  VARCHAR2  := NULL)
  RETURN VARCHAR2;

DBMS_SPM.CREATE_EVOLVE_TASK (
   plan_list     IN  DBMS_SPM.NAME_LIST,
   time_limit    IN  NUMBER    := DBMS_SPM.AUTO_LIMIT,
   task_name     IN  VARCHAR2  := NULL,
   description   IN  VARCHAR2  := NULL)
  RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_handle | VARCHAR2 | IN | Handle of a SQL statement. The default NULL considers all SQL statements with non-accepted plans. |
| plan_list | DBMS_SPM.NAME_LIST | IN | List of plan names. The plans may belong to different SQL statements. |
| plan_name | VARCHAR2 | IN | Plan identifier. The default NULL considers all non-accepted plans of the specified SQL handle or all SQL statements if the SQL handle is NULL . |
| time_limit | NUMBER | IN | Time limit in number of minutes. The time limit is global and it is used in the following manner. The time limit for first non-accepted plan is equal to the input value. The time limit for the second non-accepted plan is equal to (input value - time spent in first plan verification) and so on. The default DBMS_SPM . AUTO_LIMIT means let the system choose an appropriate time limit based on the number of plan verifications required to be done. The value DBMS_SPM . NO_LIMIT means no time limit. |
| task_name | VARCHAR2 | IN | Evolve task name |
| description | VARCHAR2 | IN | Description of the task (maximum 256 characters) |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SPM.CREATE_EVOLVE_TASK ( sql_handle IN VARCHAR2 := NULL, plan_name IN VARCHAR2 := NULL, time_limit IN NUMBER := DBMS_SPM.AUTO_LIMIT, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL) RETURN VARCHAR2; DBMS_SPM.CREATE_EVOLVE_TASK ( plan_list IN DBMS_SPM.NAME_LIST, time_limit IN NUMBER := DBMS_SPM.AUTO_LIMIT, task_name IN VARCHAR2 := NULL, description IN VARCHAR2 := NULL) RETURN VARCHAR2; Parameters Table 161-10 CREATE_EVOLVE_TASK Function Parameters Parameter Description sql_handle Handle of a SQL statement. The default NULL considers all SQL statements with non-accepted plans. plan_list List of plan names. The plans may belong to different SQL statements. plan_name Plan identifier. The default NULL considers all non-accepted plans of the specified SQL handle or all SQL statements if the SQL handle is NULL . time_limit Time limit in number of minutes. The time limit is global and it is used in the following manner. The time limit for first non-accepted plan is equal to the input value. The time limit for the second non-accepted plan is equal to (input value - time spent in first plan verification) and so on. The default DBMS_SPM . AUTO_LIMIT means let the system choose an appropriate time limit based on the number of plan verifications required to be done. The value DBMS_SPM . NO_LIMIT means no time limit. task_name Evolve task name description Description of the task (maximum 256 characters) Return Values SQL evolve task unique name