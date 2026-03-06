---
id: 19c__DBMS_RESOURCE_MANAGER.DEQUEUE_PARALLEL_STATEMENT
name: DBMS_RESOURCE_MANAGER.DEQUEUE_PARALLEL_STATEMENT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_RESOURCE_MANAGER
tags: [dbms_resource_manager]
source_file: DBMS_RESOURCE_MANAGER.html
---

# DBMS_RESOURCE_MANAGER.DEQUEUE_PARALLEL_STATEMENT

This procedure dequeues a parallel statement from the parallel statement queue.

## Syntax

```sql
DBMS_RESOURCE_MANAGER.DEQUEUE_PARALLEL_STATEMENT (
   session_id      IN  PLS_INTEGER,
   session_serial  IN  PLS_INTEGER,
   inst_id         IN  PLS_INTEGER  DEFAULT NULL,
   sql_id          IN  VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| session_id | PLS_INTEGER | IN | The session id of the session running the parallel statement to be dequeued. |
| session_serial | PLS_INTEGER | IN | The serial number of the session. |
| inst_id | PLS_INTEGER | IN | Instance ID where the session is running. If NULL , then the current instance is used. |
| sql_id | VARCHAR2 | IN | The SQL ID of the session's statement to dequeue. If the session is running SQL with a different SQL ID, then the statement is not dequeued. |

## Usage Notes

If the PARALLEL_DEGREE_POLICY initialization parameter is set to AUTO or ADAPTIVE , then parallel statement queuing is enabled. If a parallel statement is in the parallel statement queue, then you can use this procedure to dequeue the parallel statement so that it runs immediately. Syntax DBMS_RESOURCE_MANAGER.DEQUEUE_PARALLEL_STATEMENT ( session_id IN PLS_INTEGER, session_serial IN PLS_INTEGER, inst_id IN PLS_INTEGER DEFAULT NULL, sql_id IN VARCHAR2 DEFAULT NULL); Parameters Table 142-20 DEQUEUE_PARALLEL_STATEMENT Procedure Parameters Parameter Description session_id The session id of the session running the parallel statement to be dequeued. session_serial The serial number of the session. inst_id Instance ID where the session is running. If NULL , then the current instance is used. sql_id The SQL ID of the session's statement to dequeue. If the session is running SQL with a different SQL ID, then the statement is not dequeued.