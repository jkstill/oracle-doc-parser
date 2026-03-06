---
id: 19c__DBMS_APPLICATION_INFO.SET_CLIENT_INFO
name: DBMS_APPLICATION_INFO.SET_CLIENT_INFO
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_APPLICATION_INFO
tags: [dbms_application_info]
source_file: DBMS_APPLICATION_INFO.html
---

# DBMS_APPLICATION_INFO.SET_CLIENT_INFO

This procedure supplies additional information about the client application.

## Syntax

```sql
DBMS_APPLICATION_INFO.SET_CLIENT_INFO (
   client_info IN VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_info | VARCHAR2) | IN | Supplies any additional information about the client application. This information is stored in the V$SESSION view. Information exceeding 64 bytes is truncated. |

## Usage Notes

Syntax DBMS_APPLICATION_INFO.SET_CLIENT_INFO ( client_info IN VARCHAR2); Parameters Table 20-5 SET_CLIENT_INFO Procedure Parameters Parameter Description client_info Supplies any additional information about the client application. This information is stored in the V$SESSION view. Information exceeding 64 bytes is truncated. Note: CLIENT_INFO is readable and writable by any user. For storing secured application attributes, you can use the application context feature. Note: CLIENT_INFO is readable and writable by any user. For storing secured application attributes, you can use the application context feature.