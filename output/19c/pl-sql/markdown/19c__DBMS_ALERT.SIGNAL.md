---
id: 19c__DBMS_ALERT.SIGNAL
name: DBMS_ALERT.SIGNAL
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ALERT
tags: [dbms_alert]
source_file: DBMS_ALERT.html
---

# DBMS_ALERT.SIGNAL

This procedure signals an alert. The effect of the SIGNAL call only occurs when the transaction in which it is made commits. If the transaction rolls back, SIGNAL has no effect.

## Syntax

```sql
DBMS_ALERT.SIGNAL (
   name     IN  VARCHAR2,
   message  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2 | IN | Name of the alert to signal. |
| message | VARCHAR2) | IN | Message, of 1800 bytes or less, to associate with this alert. This message is passed to the waiting session. The waiting session might be able to avoid reading the database after the alert occurs by using the information in the message. |

## Usage Notes

All sessions that have registered interest in this alert are notified. If the interested sessions are currently waiting, they are awakened. If the interested sessions are not currently waiting, they are notified the next time they do a wait call. Multiple sessions can concurrently perform signals on the same alert. Each session, as it signals the alert, blocks all other concurrent sessions until it commits. This has the effect of serializing the transactions. Syntax DBMS_ALERT.SIGNAL ( name IN VARCHAR2, message IN VARCHAR2); Parameters Table 17-7 SIGNAL Procedure Parameters Parameter Description name Name of the alert to signal. message Message, of 1800 bytes or less, to associate with this alert. This message is passed to the waiting session. The waiting session might be able to avoid reading the database after the alert occurs by using the information in the message.