---
id: 19c__DBMS_WORKLOAD_CAPTURE.FINISH_CAPTURE
name: DBMS_WORKLOAD_CAPTURE.FINISH_CAPTURE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_WORKLOAD_CAPTURE
tags: [dbms_workload_capture]
source_file: DBMS_WORKLOAD_CAPTURE.html
---

# DBMS_WORKLOAD_CAPTURE.FINISH_CAPTURE

This procedure signals all connected sessions to stop the workload capture and stops future requests to the database from being captured.

## Syntax

```sql
DBMS_WORKLOAD_CAPTURE.FINISH_CAPTURE
   timeout     IN   NUMBER  DEFAULT 30
   reason       IN   VARCHAR2 DEFAULT NULL);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| timeout | NUMBER | IN | Specifies in seconds for how long the procedure should wait before it times out. Pass 0 if you want to cancel the current workload capture and not wait for any sessions to flush it's capture buffers. Default value: 30 seconds |
| reason | VARCHAR2 | IN | Specifies a reason for calling the procedure. The reason appears in the column ERROR_MESSAGE of the view DBA_WORKLOAD_CAPTURES . |

## Usage Notes

Syntax DBMS_WORKLOAD_CAPTURE.FINISH_CAPTURE timeout IN NUMBER DEFAULT 30 reason IN VARCHAR2 DEFAULT NULL); Parameters Table 190-8 FINISH_CAPTURE Procedure Parameters Parameter Description timeout Specifies in seconds for how long the procedure should wait before it times out. Pass 0 if you want to cancel the current workload capture and not wait for any sessions to flush it's capture buffers. Default value: 30 seconds reason Specifies a reason for calling the procedure. The reason appears in the column ERROR_MESSAGE of the view DBA_WORKLOAD_CAPTURES . Usage Notes By default, FINISH_CAPTURE waits for 30 seconds to receive a successful acknowledgement from all sessions in the database cluster before timing out. All sessions that either were in the middle of executing a user request or received a new user request, while FINISH_CAPTURE was waiting for acknowledgements, flush their buffers and send back their acknowledgement to FINISH_CAPTURE . If a database session remains idle (waiting for the next user request) throughout the duration of FINISH_CAPTURE , the session might have unflushed capture buffers and does not send it's acknowledgement to FINISH_CAPTURE . To avoid this, do not have sessions that remain idle (waiting for the next user request) while invoking FINISH_CAPTURE . Either close the database session(s) before running FINISH_CAPTURE or send new database requests to those sessions during FINISH_CAPTURE .