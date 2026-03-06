---
id: 19c__DBMS_XPLAN.DIFF_PLAN
name: DBMS_XPLAN.DIFF_PLAN
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_XPLAN
tags: [dbms_xplan]
source_file: DBMS_XPLAN.html
---

# DBMS_XPLAN.DIFF_PLAN

This function compares two sql plans, the reference plan and the target plan. This function returns a task_id that can be used to retrieve the report of findings.

## Syntax

```sql
DBMS_XPLAN.DIFF_PLAN(
   sql_text    IN   CLOB,
   outline     IN   CLOB,
   user_name   IN   VARCHAR2 := 'NULL')
 RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_text | CLOB | IN | The text of the SQL statement. |
| outline | CLOB | IN | Used to generate the target plan. |
| user_name | VARCHAR2 | IN | The parsing schema name default to current user. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_XPLAN.DIFF_PLAN( sql_text IN CLOB, outline IN CLOB, user_name IN VARCHAR2 := 'NULL') RETURN VARCHAR2; Parameters Table 215-4 DIFF_PLAN Function Parameters Parameter Description sql_text The text of the SQL statement. outline Used to generate the target plan. user_name The parsing schema name default to current user.