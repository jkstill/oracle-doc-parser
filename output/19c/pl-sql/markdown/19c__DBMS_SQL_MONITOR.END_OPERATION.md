---
id: 19c__DBMS_SQL_MONITOR.END_OPERATION
name: DBMS_SQL_MONITOR.END_OPERATION
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_MONITOR
tags: [dbms_sql_monitor]
source_file: DBMS_SQL_MONITOR.html
---

# DBMS_SQL_MONITOR.END_OPERATION

This procedure ends a database operation in the current session. If the specified database operation does not exist, then this function has no effect.

## Syntax

```sql
DBMS_SQL_MONITOR.END_OPERATION(
   dbop_name       IN VARCHAR2,
   dbop_eid        IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dbop_name | VARCHAR2 | IN | Name of a composite database operation |
| dbop_eid | NUMBER) | IN | Unique identifier for the current execution of the composite database operation |

## Usage Notes

Syntax DBMS_SQL_MONITOR.END_OPERATION( dbop_name IN VARCHAR2, dbop_eid IN NUMBER); Parameters Table 163-4 END_OPERATION Procedure Parameters Parameter Description dbop_name Name of a composite database operation dbop_eid Unique identifier for the current execution of the composite database operation