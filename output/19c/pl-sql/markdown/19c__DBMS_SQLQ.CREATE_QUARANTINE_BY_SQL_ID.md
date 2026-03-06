---
id: 19c__DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_ID
name: DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_ID
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQLQ
tags: [dbms_sqlq]
source_file: DBMS_SQLQ.html
---

# DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_ID

This function creates a quarantine configuration for execution plans of a SQL statement based on SQL ID.

## Syntax

```sql
DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_ID (
   sql_id           IN VARCHAR2,
   plan_hash_value  IN NUMBER DEFAULT NULL)
RETURN VARCHAR2;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_id | VARCHAR2 | IN | SQL ID of the SQL statement. |
| plan_hash_value | NUMBER | IN | Hash value of the execution plan of the SQL statement. Default value is NULL . When it is NULL , the quarantine configuration applies to all the execution plans of the SQL statement. |

**Returns:** `VARCHAR2`

## Usage Notes

Syntax DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_ID ( sql_id IN VARCHAR2, plan_hash_value IN NUMBER DEFAULT NULL) RETURN VARCHAR2; Parameters Table 167-3 CREATE_QUARANTINE_BY_SQL_ID Function Parameters Parameter Description sql_id SQL ID of the SQL statement. plan_hash_value Hash value of the execution plan of the SQL statement. Default value is NULL . When it is NULL , the quarantine configuration applies to all the execution plans of the SQL statement. Return Value Name of the quarantine configuration. Examples The following example creates a quarantine configuration for the SQL statement having the SQL ID of 8vu7s907prbgr . The quarantine configuration applies to all the execution plans of the SQL statement. DECLARE quarantine_config VARCHAR2(30); BEGIN quarantine_config := DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_ID(SQL_ID => '8vu7s907prbgr'); END; / The following example creates a quarantine configuration for the execution plan having the hash value of 3488063716 for the SQL statement having the SQL ID of 8vu7s907prbgr . DECLARE quarantine_config VARCHAR2(30); BEGIN quarantine_config := DBMS_SQLQ.CREATE_QUARANTINE_BY_SQL_ID(SQL_ID => '8vu7s907prbgr', PLAN_HASH_VALUE => '3488063716'); END; /