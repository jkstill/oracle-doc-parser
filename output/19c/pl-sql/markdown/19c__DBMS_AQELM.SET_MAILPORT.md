---
id: 19c__DBMS_AQELM.SET_MAILPORT
name: DBMS_AQELM.SET_MAILPORT
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQELM
tags: [dbms_aqelm]
source_file: DBMS_AQELM.html
---

# DBMS_AQELM.SET_MAILPORT

This procedure sets the port number for the SMTP server.

## Syntax

```sql
DBMS_AQELM.SET_MAILPORT (
   mailport  IN NUMBER);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| mailport | NUMBER) | IN | SMTP server port number. |

## Usage Notes

Syntax DBMS_AQELM.SET_MAILPORT ( mailport IN NUMBER); Parameters Table 24-3 SET_MAILPORT Procedure Parameters Parameter Description mailport SMTP server port number. Usage Notes As part of the configuration for e-mail notifications, a user with AQ_ADMINISTRATOR_ROLE or with EXECUTE permissions on DBMS_AQELM package needs to set the port number before registering for e-mail notifications. The database uses this SMTP server port number to send out e-mail notifications. If not set, the SMTP mailport defaults to 25