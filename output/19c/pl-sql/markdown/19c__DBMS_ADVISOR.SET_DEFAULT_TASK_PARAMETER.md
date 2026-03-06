---
id: 19c__DBMS_ADVISOR.SET_DEFAULT_TASK_PARAMETER
name: DBMS_ADVISOR.SET_DEFAULT_TASK_PARAMETER
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADVISOR
tags: [dbms_advisor]
source_file: DBMS_ADVISOR.html
---

# DBMS_ADVISOR.SET_DEFAULT_TASK_PARAMETER

This procedure modifies the default value for a user parameter within a task or a template.

## Syntax

```sql
DBMS_ADVISOR.SET_DEFAULT_TASK_PARAMETER (
   advisor_name        IN VARCHAR2
   parameter           IN VARCHAR2,
   value               IN VARCHAR2);

DBMS_ADVISOR.SET_DEFAULT_TASK_PARAMETER (
   advisor_name        IN VARCHAR2
   parameter           IN VARCHAR2,
   value               IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| advisor_name | VARCHAR2 | IN | Specifies the unique advisor name as defined in the view DBA_ADVISOR_DEFINITIONS . |
| parameter | VARCHAR2 | IN | The name of the task parameter to be modified. Parameter names are not case sensitive. Parameter names are unique to the task type, but not necessarily unique to all task types. Various task types may use the same parameter name for different purposes. |
| value | VARCHAR2) | IN | The value of the specified task parameter. The value can be specified as a string or a number. |

## Usage Notes

A user parameter is a simple variable that stores various attributes that affect various Advisor operations. When a default value is changed for a parameter, tasks will inherit the new value when they are created. A default task is different from a regular task. The default value is the initial value that will be inserted into a newly created task, while setting a task parameter with SET_TASK_PARAMETER sets the local value only. Thus, SET_DEFAULT_TASK_PARAMETER has no effect on an existing task. Syntax DBMS_ADVISOR.SET_DEFAULT_TASK_PARAMETER ( advisor_name IN VARCHAR2 parameter IN VARCHAR2, value IN VARCHAR2); DBMS_ADVISOR.SET_DEFAULT_TASK_PARAMETER ( advisor_name IN VARCHAR2 parameter IN VARCHAR2, value IN NUMBER); Parameters Table 16-32 SET_DEFAULT_TASK_PARAMETER Procedure Parameters Parameter Description advisor_name Specifies the unique advisor name as defined in the view DBA_ADVISOR_DEFINITIONS . parameter The name of the task parameter to be modified. Parameter names are not case sensitive. Parameter names are unique to the task type, but not necessarily unique to all task types. Various task types may use the same parameter name for different purposes. value The value of the specified task parameter. The value can be specified as a string or a number. Examples BEGIN DBMS_ADVISOR.SET_DEFAULT_TASK_PARAMETER(DBMS_ADVISOR.SQLACCESS_ADVISOR, 'VALID_TABLE_LIST', 'SH.%'); END; /