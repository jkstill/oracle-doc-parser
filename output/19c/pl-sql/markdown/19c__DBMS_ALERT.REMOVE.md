---
id: 19c__DBMS_ALERT.REMOVE
name: DBMS_ALERT.REMOVE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ALERT
tags: [dbms_alert]
source_file: DBMS_ALERT.html
---

# DBMS_ALERT.REMOVE

This procedure enables a session that is no longer interested in an alert to remove that alert from its registration list. Removing an alert reduces the amount of work done by signalers of the alert.

## Syntax

```sql
DBMS_ALERT.REMOVE (
   name  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| name | VARCHAR2) | IN | Name of the alert (case-insensitive) to be removed from registration list. |

## Usage Notes

Syntax DBMS_ALERT.REMOVE ( name IN VARCHAR2); Parameters Table 17-5 REMOVE Procedure Parameters Parameter Description name Name of the alert (case-insensitive) to be removed from registration list. Usage Notes Removing alerts is important because it reduces the amount of work done by signalers of the alert. If a session dies without removing the alert, that alert is eventually (but not immediately) cleaned up.