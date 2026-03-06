---
id: 19c__DBMS_AQELM.SET_MAILHOST
name: DBMS_AQELM.SET_MAILHOST
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQELM
tags: [dbms_aqelm]
source_file: DBMS_AQELM.html
---

# DBMS_AQELM.SET_MAILHOST

This procedure sets the host name for the SMTP server. The database uses this SMTP server host name to send out e-mail notifications.

## Syntax

```sql
DBMS_AQELM.SET_MAILHOST (
   mailhost  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mailhost | VARCHAR2) | IN | SMTP server host name. |

## Usage Notes

Syntax DBMS_AQELM.SET_MAILHOST ( mailhost IN VARCHAR2); Parameters Table 24-2 SET_MAILHOST Procedure Parameters Parameter Description mailhost SMTP server host name. Usage Notes As part of the configuration for e-mail notifications, a user with AQ_ADMINISTRATOR_ROLE or with EXECUTE permissions on the DBMS_AQELM package needs to set the host name before registering for e-mail notifications.