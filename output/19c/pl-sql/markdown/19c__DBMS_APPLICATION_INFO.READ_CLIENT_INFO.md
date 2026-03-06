---
id: 19c__DBMS_APPLICATION_INFO.READ_CLIENT_INFO
name: DBMS_APPLICATION_INFO.READ_CLIENT_INFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLICATION_INFO
tags: [dbms_application_info]
source_file: DBMS_APPLICATION_INFO.html
---

# DBMS_APPLICATION_INFO.READ_CLIENT_INFO

This procedure reads the value of the client_info field of the current session.

## Syntax

```sql
DBMS_APPLICATION_INFO.READ_CLIENT_INFO (
   client_info OUT VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_info | VARCHAR2) | OUT | Last client information value supplied to the SET_CLIENT_INFO procedure. |

## Usage Notes

Syntax DBMS_APPLICATION_INFO.READ_CLIENT_INFO ( client_info OUT VARCHAR2); Parameters Table 20-2 READ_CLIENT_INFO Procedure Parameters Parameter Description client_info Last client information value supplied to the SET_CLIENT_INFO procedure.