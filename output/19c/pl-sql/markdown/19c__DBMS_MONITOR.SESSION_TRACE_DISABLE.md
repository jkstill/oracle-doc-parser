---
id: 19c__DBMS_MONITOR.SESSION_TRACE_DISABLE
name: DBMS_MONITOR.SESSION_TRACE_DISABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.SESSION_TRACE_DISABLE

This procedure will disable the trace for a given database session at the local instance.

## Syntax

```sql
DBMS_MONITOR.SESSION_TRACE_DISABLE(
   session_id      IN     BINARY_INTEGER DEFAULT NULL,
   serial_num      IN     BINARY_INTEGER DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| session_id | BINARY_INTEGER | IN | Database Session Identifier for which SQL trace is disabled |
| serial_num | BINARY_INTEGER | IN | Serial number for this session |

## Usage Notes

Syntax DBMS_MONITOR.SESSION_TRACE_DISABLE( session_id IN BINARY_INTEGER DEFAULT NULL, serial_num IN BINARY_INTEGER DEFAULT NULL); Parameters Table 112-12 SESSION_TRACE_DISABLE Procedure Parameters Parameter Description session_id Database Session Identifier for which SQL trace is disabled serial_num Serial number for this session Usage Notes If serial_num is NULL but session_id is specified, a session with a given session_id is no longer traced irrespective of its serial number. If both session_id and serial_num are NULL , the current user session is no longer traced. It is illegal to specify NULL session_id and non- NULL serial_num . In addition, the NULL values are default and can be omitted. Examples To enable tracing for a client with a given client session ID: EXECUTE DBMS_MONITOR.SESSION_TRACE_ENABLE(7,4634, TRUE, FALSE); To disable tracing specified in the previous step: EXECUTE DBMS_MONITOR.SESSION_TRACE_DISABLE(7,4634);;