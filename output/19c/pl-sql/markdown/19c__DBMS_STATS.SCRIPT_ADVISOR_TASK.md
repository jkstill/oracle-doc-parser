---
id: 19c__DBMS_STATS.SCRIPT_ADVISOR_TASK
name: DBMS_STATS.SCRIPT_ADVISOR_TASK
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_STATS
tags: [dbms_stats]
source_file: DBMS_STATS.html
---

# DBMS_STATS.SCRIPT_ADVISOR_TASK

Retrieves the script that implements the recommended actions for the problems found by Optimizer Statistics Advisor.

## Syntax

```sql
DBMS_STATS.SCRIPT_ADVISOR_TASK (
  task_name          IN   VARCHAR2,
  execution_name     IN   VARCHAR2    := NULL,
  dir_name           IN   VARCHAR2    := NULL,
  level              IN   VARCHAR2    := 'TYPICAL')
RETURN CLOB;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | The name of the Optimizer Statistics Advisor task. |
| execution_name | VARCHAR2 | IN | A name that qualifies and identifies an advisor execution. If not specified, then the advisor automatically generates it. If the specified execution conflicts with the name of an existing execution, then the function returns an error. |
| dir_name | VARCHAR2 | IN | Directory name to which to write the generated script. If the name is not specified (NULL), then the function includes the script in the returned CLOB. If the name is specified, then the function returns the script as a CLOB and as a new file in the specified directory. |
| level | VARCHAR2 | IN | The level of the script to generate. Possible values are ALL : Ignores the filter and generates a script for all findings TYPICAL : Generates a script according to the filters in place |

**Returns:** `CLOB`

## Usage Notes

The generated script contains PL/SQL statements that you can choose to execute. Preceding the commands for each action are comments that list the potential side effects. You can review the comments, and choose to execute only the desired sections. Syntax DBMS_STATS.SCRIPT_ADVISOR_TASK ( task_name IN VARCHAR2, execution_name IN VARCHAR2 := NULL, dir_name IN VARCHAR2 := NULL, level IN VARCHAR2 := 'TYPICAL') RETURN CLOB; Parameters Table 171-117 SCRIPT_ADVISOR_TASK Function Parameters Parameter Description task_name The name of the Optimizer Statistics Advisor task. execution_name A name that qualifies and identifies an advisor execution. If not specified, then the advisor automatically generates it. If the specified execution conflicts with the name of an existing execution, then the function returns an error. dir_name Directory name to which to write the generated script. If the name is not specified (NULL), then the function includes the script in the returned CLOB. If the name is specified, then the function returns the script as a CLOB and as a new file in the specified directory. level The level of the script to generate. Possible values are ALL : Ignores the filter and generates a script for all findings TYPICAL : Generates a script according to the filters in place Security Model Note the following: To execute this subprogram, you must have the ADVISOR privilege. You must be the owner of the task. You can execute this subprogram for AUTO_STATS_ADVISOR_TASK , which is predefined. This subprogram executes using invoker's rights. The results of performing this task depend on the privileges of the executing user: SYSTEM level Only users with both the ANALYZE ANY and ANALYZE ANY DICTIONARY privileges can perform this task on system-level rules. Operation level The results depend on the following privileges: Users with both the ANALYZE ANY and ANALYZE ANY DICTIONARY privileges can perform this task for all statistics operations. Users with the ANALYZE ANY privilege but not the ANALYZE ANY DICTIONARY privilege can perform this task for statistics operations related to any schema except SYS . Users with the ANALYZE ANY DICTIONARY privilege but not the ANALYZE ANY privilege can perform this task for statistics operations related to their own schema and the SYS schema. Users with neither the ANALYZE ANY nor the ANALYZE ANY DICTIONARY privilege can only perform this operation for statistics operations relating to their own schema. Object level Users can perform this task for any object for which they have statistics collection privileges. Return Values This function returns a CLOB that contains the script.