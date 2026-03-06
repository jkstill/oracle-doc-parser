---
id: 19c__DBMS_ALERT.WAITONE
name: DBMS_ALERT.WAITONE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ALERT
tags: [dbms_alert]
source_file: DBMS_ALERT.html
---

# DBMS_ALERT.WAITONE

This procedure waits for a specific alert to occur.

## Syntax

```sql
DBMS_ALERT.WAITONE (
   name      IN   VARCHAR2,
   message   OUT  VARCHAR2,
   status    OUT  INTEGER,
   timeout   IN   NUMBER DEFAULT MAXWAIT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the alert to wait for. |
| message | VARCHAR2 | OUT | Returns the message associated with the alert. This is the message provided by the SIGNAL call. If multiple signals on this alert occurred before WAITONE , the message corresponds to the most recent SIGNAL call. Messages from prior SIGNAL calls are discarded. |
| status | INTEGER | OUT | Values returned: 0 - alert occurred 1 - timeout occurred |
| timeout | NUMBER | IN | Maximum time to wait for an alert. If the named alert does not occurs before timeout seconds, this returns a status of 1. |

## Usage Notes

An implicit COMMIT is issued before this procedure is executed. A session that is the first to signal an alert can also wait for the alert in a subsequent transaction. In this case, remember to commit after the signal and before the wait; otherwise, DBMS_LOCK . REQUEST (which is called by DBMS_ALERT ) returns status 4. Syntax DBMS_ALERT.WAITONE ( name IN VARCHAR2, message OUT VARCHAR2, status OUT INTEGER, timeout IN NUMBER DEFAULT MAXWAIT); Parameters Table 17-9 WAITONE Procedure Parameters Parameter Description name Name of the alert to wait for. message Returns the message associated with the alert. This is the message provided by the SIGNAL call. If multiple signals on this alert occurred before WAITONE , the message corresponds to the most recent SIGNAL call. Messages from prior SIGNAL calls are discarded. status Values returned: 0 - alert occurred 1 - timeout occurred timeout Maximum time to wait for an alert. If the named alert does not occurs before timeout seconds, this returns a status of 1.