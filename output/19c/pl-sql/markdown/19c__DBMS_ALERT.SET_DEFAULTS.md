---
id: 19c__DBMS_ALERT.SET_DEFAULTS
name: DBMS_ALERT.SET_DEFAULTS
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_ALERT
tags: [dbms_alert]
source_file: DBMS_ALERT.html
---

# DBMS_ALERT.SET_DEFAULTS

In case a polling loop is required, use the SET_DEFAULTS procedure to set the polling interval.

## Syntax

```sql
DBMS_ALERT.SET_DEFAULTS (
   sensitivity  IN  NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sensitivity | NUMBER) | IN | Polling interval, in seconds, to sleep between polls. The default interval is five seconds. |

## Usage Notes

Syntax DBMS_ALERT.SET_DEFAULTS ( sensitivity IN NUMBER); Parameters Table 17-6 SET_DEFAULTS Procedure Parameters Parameter Description sensitivity Polling interval, in seconds, to sleep between polls. The default interval is five seconds.