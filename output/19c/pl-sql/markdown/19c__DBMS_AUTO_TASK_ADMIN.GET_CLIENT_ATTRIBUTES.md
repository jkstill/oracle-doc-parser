---
id: 19c__DBMS_AUTO_TASK_ADMIN.GET_CLIENT_ATTRIBUTES
name: DBMS_AUTO_TASK_ADMIN.GET_CLIENT_ATTRIBUTES
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_TASK_ADMIN
tags: [dbms_auto_task_admin]
source_file: DBMS_AUTO_TASK_ADMIN.html
---

# DBMS_AUTO_TASK_ADMIN.GET_CLIENT_ATTRIBUTES

This procedure returns values of select client attributes.

## Syntax

```sql
DBMS_AUTO_TASK_ADMIN.GET_CLIENT_ATTRIBUTES(
   client_name        IN    VARCHAR2,   service_name       OUT   VARCHAR2,   window_group       OUT   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_name | VARCHAR2 | IN | Name of the client, as found in DBA_AUTOTASK_CLIENT View |
| service_name | VARCHAR2 | OUT | Service name for client, may be NULL |
| window_group | VARCHAR2) | OUT | Name of the window group in which the client is active |

## Usage Notes

Syntax DBMS_AUTO_TASK_ADMIN.GET_CLIENT_ATTRIBUTES( client_name IN VARCHAR2, service_name OUT VARCHAR2, window_group OUT VARCHAR2); Parameters Table 32-5 GET_CLIENT_ATTRIBUTES Procedure Parameters Parameter Description client_name Name of the client, as found in DBA_AUTOTASK_CLIENT View service_name Service name for client, may be NULL window_group Name of the window group in which the client is active