---
id: 19c__DBMS_ADDM.DELETE_SQL_DIRECTIVE
name: DBMS_ADDM.DELETE_SQL_DIRECTIVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ADDM
tags: [dbms_addm]
source_file: DBMS_ADDM.html
---

# DBMS_ADDM.DELETE_SQL_DIRECTIVE

This procedure deletes a SQL directive.

## Syntax

```sql
DBMS_ADDM.DELETE_SQL_DIRECTIVE (
   task_name           IN VARCHAR2,
   dir_name            IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| task_name | VARCHAR2 | IN | Name of the task this directive applies to. If the value is NULL , it is a system directive. |
| dir_name | VARCHAR2) | IN | Name of the directive. All directives must be given unique names. |

## Usage Notes

Syntax DBMS_ADDM.DELETE_SQL_DIRECTIVE ( task_name IN VARCHAR2, dir_name IN VARCHAR2); Parameters Table 14-13 DELETE_SQL_DIRECTIVE Procedure Parameters Parameter Description task_name Name of the task this directive applies to. If the value is NULL , it is a system directive. dir_name Name of the directive. All directives must be given unique names.