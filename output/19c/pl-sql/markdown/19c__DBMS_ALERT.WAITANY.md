---
id: 19c__DBMS_ALERT.WAITANY
name: DBMS_ALERT.WAITANY
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ALERT
tags: [dbms_alert]
source_file: DBMS_ALERT.html
---

# DBMS_ALERT.WAITANY

Call this procedure to wait for an alert to occur for any of the alerts for which the current session is registered.

## Syntax

```sql
DBMS_ALERT.WAITANY (
   name      OUT  VARCHAR2,
   message   OUT  VARCHAR2,
   status    OUT  INTEGER,
   timeout   IN   NUMBER DEFAULT MAXWAIT);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | OUT | Returns the name of the alert that occurred. |
| message | VARCHAR2 | OUT | Returns the message associated with the alert. This is the message provided by the SIGNAL call. If multiple signals on this alert occurred before WAITANY , the message corresponds to the most recent SIGNAL call. Messages from prior SIGNAL calls are discarded. |
| status | INTEGER | OUT | Values returned: 0 - alert occurred 1 - timeout occurred |
| timeout | NUMBER | IN | Maximum time to wait for an alert. If no alert occurs before timeout seconds, this returns a status of 1. |

## Usage Notes

Syntax DBMS_ALERT.WAITANY ( name OUT VARCHAR2, message OUT VARCHAR2, status OUT INTEGER, timeout IN NUMBER DEFAULT MAXWAIT); Parameters Table 17-8 WAITANY Procedure Parameters Parameter Description name Returns the name of the alert that occurred. message Returns the message associated with the alert. This is the message provided by the SIGNAL call. If multiple signals on this alert occurred before WAITANY , the message corresponds to the most recent SIGNAL call. Messages from prior SIGNAL calls are discarded. status Values returned: 0 - alert occurred 1 - timeout occurred timeout Maximum time to wait for an alert. If no alert occurs before timeout seconds, this returns a status of 1. Usage Notes An implicit COMMIT is issued before this procedure is executed. The same session that waits for the alert may also first signal the alert. In this case remember to commit after the signal and before the wait; otherwise, DBMS_LOCK . REQUEST (which is called by DBMS_ALERT ) returns status 4. Exceptions -20000, ORU-10024: there are no alerts registered.