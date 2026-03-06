---
id: 19c__DBMS_SQL_MONITOR.BEGIN_OPERATION
name: DBMS_SQL_MONITOR.BEGIN_OPERATION
object_type: plsql_function
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_SQL_MONITOR
tags: [dbms_sql_monitor]
source_file: DBMS_SQL_MONITOR.html
---

# DBMS_SQL_MONITOR.BEGIN_OPERATION

This function starts a database operation in the current session.

## Syntax

```sql
DBMS_SQL_MONITOR.BEGIN_OPERATION (
   dbop_name       IN VARCHAR2,
   dbop_eid        IN NUMBER   := NULL,
   forced_tracking IN VARCHAR2 := NO_FORCE_TRACKING,
   attribute_list  IN VARCHAR2 := NULL,
   session_id      IN NUMBER   := NULL,
   session_serial  IN NUMBER   := NULL)
  iRETURN NUMBER;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| dbop_name | VARCHAR2 | IN | Name for the composite database operation. |
| dbop_eid | NUMBER | IN | Unique identifier for the current execution of the composite database operation. |
| forced_tracking | VARCHAR2 | IN | Whether tracking is forced. Possible values are: FORCE_TRACKING - forces the composite database operation to be tracked when the operation starts. You can also use the string variable Y . NO_FORCE_TRACKING - tracks the operation only when it has consumed at least 5 seconds of CPU or I/O time. You can also use the string variable N . See " DBMS_SQL_MONITOR Constants " . |
| attribute_list | VARCHAR2 | IN | List of user-created attributes. It is a comma-separated list of name-value pairs (for example, 'table_name=emp, operation=load' ). |
| session_id | NUMBER | IN | Session ID of the session to be monitored. If omitted (or null), then the database monitors the current session. |
| session_serial | NUMBER | IN | Serial number of the session to be monitored. If omitted (or null), then the database uses only the session ID to determine the session. |

**Returns:** `NUMBER`

## Usage Notes

Syntax DBMS_SQL_MONITOR.BEGIN_OPERATION ( dbop_name IN VARCHAR2, dbop_eid IN NUMBER := NULL, forced_tracking IN VARCHAR2 := NO_FORCE_TRACKING, attribute_list IN VARCHAR2 := NULL, session_id IN NUMBER := NULL, session_serial IN NUMBER := NULL) iRETURN NUMBER; Parameters Table 163-3 BEGIN_OPERATION Procedure Parameters Parameter Description dbop_name Name for the composite database operation. dbop_eid Unique identifier for the current execution of the composite database operation. forced_tracking Whether tracking is forced. Possible values are: FORCE_TRACKING - forces the composite database operation to be tracked when the operation starts. You can also use the string variable Y . NO_FORCE_TRACKING - tracks the operation only when it has consumed at least 5 seconds of CPU or I/O time. You can also use the string variable N . See " DBMS_SQL_MONITOR Constants " . attribute_list List of user-created attributes. It is a comma-separated list of name-value pairs (for example, 'table_name=emp, operation=load' ). session_id Session ID of the session to be monitored. If omitted (or null), then the database monitors the current session. session_serial Serial number of the session to be monitored. If omitted (or null), then the database uses only the session ID to determine the session. Return Values This function returns the database operation execution ID. If the value is null for dbop_eid , then the database generates a unique value.