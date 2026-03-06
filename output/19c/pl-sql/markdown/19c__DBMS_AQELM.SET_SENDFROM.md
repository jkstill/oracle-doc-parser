---
id: 19c__DBMS_AQELM.SET_SENDFROM
name: DBMS_AQELM.SET_SENDFROM
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AQELM
tags: [dbms_aqelm]
source_file: DBMS_AQELM.html
---

# DBMS_AQELM.SET_SENDFROM

This procedure sets the sent-from e-mail address. This e-mail address is used in the sent-from field in all the e-mail notifications sent out by the database to the registered e-mail addresses.

## Syntax

```sql
DBMS_AQELM.SET_SENDFROM (
   sendfrom  IN  VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| sendfrom | VARCHAR2) | IN | The sent-from e-mail address. |

## Usage Notes

Syntax DBMS_AQELM.SET_SENDFROM ( sendfrom IN VARCHAR2); Parameters Table 24-4 SET_SENDFROM Procedure Parameters Parameter Description sendfrom The sent-from e-mail address. Usage Notes As part of the configuration for e-mail notifications, a user with AQ_ADMINISTRATOR_ROLE or with EXECUTE permissions on the DBMS_AQELM package should set the sent-from address before registering for e-mail notifications