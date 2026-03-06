---
id: 19c__DBMS_MONITOR.SESSION_TRACE_ENABLE
name: DBMS_MONITOR.SESSION_TRACE_ENABLE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_MONITOR
tags: [dbms_monitor]
source_file: DBMS_MONITOR.html
---

# DBMS_MONITOR.SESSION_TRACE_ENABLE

This procedure enables a SQL trace for the given Session ID on the local instance

## Syntax

```sql
DBMS_MONITOR.SESSION_TRACE_ENABLE(
    session_id   IN  BINARY_INTEGER DEFAULT NULL,
    serial_num   IN  BINARY_INTEGER DEFAULT NULL,
    waits        IN  BOOLEAN DEFAULT TRUE,
    binds        IN  BOOLEAN DEFAULT FALSE,
    plan_stat    IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| session_id | BINARY_INTEGER | IN | Client Identifier for which SQL trace is enabled. If omitted (or NULL ), the user's own session is assumed. |
| serial_num | BINARY_INTEGER | IN | Serial number for this session. If omitted (or NULL ), only the session ID is used to determine a session. |
| waits | BOOLEAN | IN | If TRUE , wait information is present in the trace |
| binds | BOOLEAN | IN | If TRUE , bind information is present in the trace |
| plan_stat | VARCHAR2 | IN | Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '. |

## Usage Notes

Syntax DBMS_MONITOR.SESSION_TRACE_ENABLE( session_id IN BINARY_INTEGER DEFAULT NULL, serial_num IN BINARY_INTEGER DEFAULT NULL, waits IN BOOLEAN DEFAULT TRUE, binds IN BOOLEAN DEFAULT FALSE, plan_stat IN VARCHAR2 DEFAULT NULL); Parameters Table 112-13 SESSION_TRACE_ENABLE Procedure Parameters Parameter Description session_id Client Identifier for which SQL trace is enabled. If omitted (or NULL ), the user's own session is assumed. serial_num Serial number for this session. If omitted (or NULL ), only the session ID is used to determine a session. waits If TRUE , wait information is present in the trace binds If TRUE , bind information is present in the trace plan_stat Frequency at which we dump row source statistics. Value should be ' NEVER ', ' FIRST_EXECUTION ' (equivalent to NULL ) or ' ALL_EXECUTIONS '. Usage Notes The procedure enables a trace for a given database session, and is still useful for client/server applications. The trace is enabled only on the instance to which the caller is connected, since database sessions do not span instances. This tracing is strictly local to an instance. If serial_num is NULL but session_id is specified, a session with a given session_id is traced irrespective of its serial number. If both session_id and serial_num are NULL , the current user session is traced. It is illegal to specify NULL session_id and non- NULL serial_num . In addition, the NULL values are default and can be omitted. Examples To enable tracing for a client with a given client session ID: EXECUTE DBMS_MONITOR.SESSION_TRACE_ENABLE(7,4634, TRUE, FALSE); To disable tracing specified in the previous step: EXECUTE DBMS_MONITOR.SESSION_TRACE_DISABLE(7,4634); Either EXECUTE DBMS_MONITOR.SESSION_TRACE_ENABLE(5); or EXECUTE DBMS_MONITOR.SESSION_TRACE_ENABLE(5, NULL); traces the session with session ID of 5, while either EXECUTE DBMS_MONITOR.SESSION_TRACE_ENABLE(); or EXECUTE DBMS_MONITOR.SESSION_TRACE_ENABLE(NULL, NULL); traces the current user session. Also, EXECUTE DBMS_MONITOR.SESSION_TRACE_ENABLE(NULL, NULL, TRUE, TRUE); traces the current user session including waits and binds. The same can be also expressed using keyword syntax: EXECUTE DBMS_MONITOR.SESSION_TRACE_ENABLE(binds=>TRUE);