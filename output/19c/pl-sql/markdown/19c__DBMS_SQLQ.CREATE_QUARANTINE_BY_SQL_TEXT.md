---
id: 19c__DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_TEXT
name: DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_TEXT
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLQ
tags: [dbms_sqlq]
source_file: DBMS_SQLQ.html
---

# DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_TEXT

This function creates a quarantine configuration for execution plans of a SQL statement based on SQL text.

## Syntax

```sql
DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_TEXT (
   sql_text         IN CLOB,
   plan_hash_value  IN NUMBER DEFAULT NULL)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_text | CLOB | IN | SQL statement. |
| plan_hash_value | NUMBER | IN | Hash value of the execution plan of the SQL statement. Default value is NULL . When it is NULL , the quarantine configuration applies to all the execution plans of the SQL statement. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_TEXT ( sql_text IN CLOB, plan_hash_value IN NUMBER DEFAULT NULL) RETURN VARCHAR2; Parameters Table 167-4 CREATE_QUARANTINE_BY_SQL_TEXT Function Parameters Parameter Description sql_text SQL statement. plan_hash_value Hash value of the execution plan of the SQL statement. Default value is NULL . When it is NULL , the quarantine configuration applies to all the execution plans of the SQL statement. Return Value Name of the quarantine configuration. Examples The following example creates a quarantine configuration that applies to all the execution plans of the SQL statement 'select count(*) from emp' . DECLARE quarantine_config VARCHAR2(30); BEGIN quarantine_config := DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_TEXT(SQL_TEXT => to_clob('select count(*) from emp')); END; / The following example creates a quarantine configuration for the execution plan having the hash value of 3488063716 for the SQL statement having the SQL text of 'select count(*) from emp' . DECLARE quarantine_config VARCHAR2(30); BEGIN quarantine_config := DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_TEXT(SQL_TEXT => to_clob('select count(*) from emp'), PLAN_HASH_VALUE => '3488063716'); END; /