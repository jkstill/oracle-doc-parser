---
id: 19c__DBMS_ADVISOR.GET_TASK_SCRIPT
name: DBMS_ADVISOR.GET_TASK_SCRIPT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.GET_TASK_SCRIPT

This function creates a SQL*Plus-compatible SQL script and sends the output to a file.

## Syntax

```sql
DBMS_ADVISOR.GET_TASK_SCRIPT (
   task_name          IN VARCHAR2
   type               IN VARCHAR2 := 'IMPLEMENTATION',
   rec_id             IN NUMBER   := NULL,
   act_id             IN NUMBER   := NULL,
   owner_name         IN VARCHAR2 := NULL,
   execution_name     IN VARCHAR2 := NULL,
   object_id          IN NUMBER   := NULL)
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The task name that uniquely identifies an existing task. |
| type | VARCHAR2 | IN | Specifies the type of script to generate. The possible values are IMPLEMENTATION and UNDO . |
| rec_id | NUMBER | IN | An optional recommendation identifier number that can be used to extract a subset of the implementation script. A zero or the value DBMS_ADVISOR.ADVISOR_ALL indicates all accepted recommendations would be included. The default is to include all accepted recommendations for the task. |
| act_id | NUMBER | IN | Optional action identifier number that can be used to extract a single action as a DDL command. A zero or the value DBMS_ADVISOR.ADVISOR_ALL indicates all actions for the recommendation would be included. The default is to include all actions for a recommendation. |
| owner_name | VARCHAR2 | IN | An optional task owner name. |
| execution_name | VARCHAR2 | IN | An identifier of a specific execution of the task. It is needed only for advisors that allow their tasks to be executed multiple times. |
| object_id | NUMBER | IN | An identifier of an advisor object that can be targeted by the script. |

**Returns:** `CLOB`

## Usage Notes

The output script contains all of the accepted recommendations from the specified task. Syntax DBMS_ADVISOR.GET_TASK_SCRIPT ( task_name IN VARCHAR2 type IN VARCHAR2 := 'IMPLEMENTATION', rec_id IN NUMBER := NULL, act_id IN NUMBER := NULL, owner_name IN VARCHAR2 := NULL, execution_name IN VARCHAR2 := NULL, object_id IN NUMBER := NULL) RETURN CLOB; Parameters Table 16-19 GET_TASK_SCRIPT Function Parameters Parameter Description task_name The task name that uniquely identifies an existing task. type Specifies the type of script to generate. The possible values are IMPLEMENTATION and UNDO . rec_id An optional recommendation identifier number that can be used to extract a subset of the implementation script. A zero or the value DBMS_ADVISOR.ADVISOR_ALL indicates all accepted recommendations would be included. The default is to include all accepted recommendations for the task. act_id Optional action identifier number that can be used to extract a single action as a DDL command. A zero or the value DBMS_ADVISOR.ADVISOR_ALL indicates all actions for the recommendation would be included. The default is to include all actions for a recommendation. owner_name An optional task owner name. execution_name An identifier of a specific execution of the task. It is needed only for advisors that allow their tasks to be executed multiple times. object_id An identifier of an advisor object that can be targeted by the script. Return Values Returns the script as a CLOB buffer. Usage Notes Though the script is ready to execute, Oracle recommends that the user review the script for acceptable locations for new materialized views and indexes. For a recommendation to appear in a generated script, it must be marked as accepted.