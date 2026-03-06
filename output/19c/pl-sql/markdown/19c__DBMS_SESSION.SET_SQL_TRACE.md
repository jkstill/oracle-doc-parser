---
id: 19c__DBMS_SESSION.SET_SQL_TRACE
name: DBMS_SESSION.SET_SQL_TRACE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SESSION
tags: [dbms_session]
source_file: DBMS_SESSION.html
---

# DBMS_SESSION.SET_SQL_TRACE

This procedure turns tracing on or off. It is equivalent to the SQL statement ALTER SESSION SET SQL_TRACE ... .

## Syntax

```sql
DBMS_SESSION.SET_SQL_TRACE (
   sql_trace boolean);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sql_trace | boolean) | IN | TRUE turns tracing on, FALSE turns tracing off |

## Usage Notes

Syntax DBMS_SESSION.SET_SQL_TRACE ( sql_trace boolean); Parameters Table 154-23 SET_SQL_TRACE Procedure Parameters Parameter Description sql_trace TRUE turns tracing on, FALSE turns tracing off