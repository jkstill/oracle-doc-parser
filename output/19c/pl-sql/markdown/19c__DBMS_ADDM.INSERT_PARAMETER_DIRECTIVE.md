---
id: 19c__DBMS_ADDM.INSERT_PARAMETER_DIRECTIVE
name: DBMS_ADDM.INSERT_PARAMETER_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.INSERT_PARAMETER_DIRECTIVE

This procedure creates a directive to prevent ADDM from creating actions to alter the value of a specific system parameter. The directive can be created for a specific task (only when the task is in INITIAL status), or for all subsequently created ADDM tasks (such as a system directive).

## Syntax

```sql
DBMS_ADDM.INSERT_PARAMETER_DIRECTIVE (
   task_name             IN VARCHAR2,
   dir_name              IN VARCHAR2,
   parameter_name        IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task this directive applies to. If the value is NULL , it applies to all subsequently created ADDM Tasks. |
| dir_name | VARCHAR2 | IN | Name of the directive. All directives must be given unique names. |
| parameter_name | VARCHAR2) | IN | Specifies the parameter to use. Valid parameter names appear in V$PARAMETER. |

## Usage Notes

Syntax DBMS_ADDM.INSERT_PARAMETER_DIRECTIVE ( task_name IN VARCHAR2, dir_name IN VARCHAR2, parameter_name IN VARCHAR2); Parameters Table 14-17 INSERT_PARAMETER_DIRECTIVE Procedure Parameters Parameter Description task_name Name of the task this directive applies to. If the value is NULL , it applies to all subsequently created ADDM Tasks. dir_name Name of the directive. All directives must be given unique names. parameter_name Specifies the parameter to use. Valid parameter names appear in V$PARAMETER. Examples A new ADDM task is created to analyze a local instance. However, it has special treatment for all actions that recommend modifying the parameter ' sga_target '. The result of GET_REPORT does not show these actions. var tname varchar2(60); BEGIN DBMS_ADDM.INSERT_PARAMETER_DIRECTIVE( NULL, 'my Parameter directive', 'sga_target'); :tname := 'my_instance_analysis_mode_task'; DBMS_ADDM.ANALYZE_INST(:tname, 1, 2); END; To see a report containing all actions regardless of the directive: SELECT DBMS_ADVISOR.GET_TASK_REPORT(:tname, 'TEXT', 'ALL') FROM DUAL;