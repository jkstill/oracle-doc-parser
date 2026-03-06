---
id: 19c__DBMS_AUTO_TASK_ADMIN.SET_CLIENT_SERVICE
name: DBMS_AUTO_TASK_ADMIN.SET_CLIENT_SERVICE
object_type: plsql_procedure
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_TASK_ADMIN
tags: [dbms_auto_task_admin]
source_file: DBMS_AUTO_TASK_ADMIN.html
---

# DBMS_AUTO_TASK_ADMIN.SET_CLIENT_SERVICE

This procedure associates an AUTOTASK Client with a specified Service.

## Syntax

```sql
DBMS_AUTO_TASK_ADMIN.SET_CLIENT_SERVICE(
   client_name        IN    VARCHAR2,
   service_name       IN   VARCHAR2);
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_name | VARCHAR2 | IN | Name of the client, as found in DBA_AUTOTASK_CLIENT View |
| service_name | VARCHAR2) | IN | Service name for client, may be NULL |

## Usage Notes

Syntax DBMS_AUTO_TASK_ADMIN.SET_CLIENT_SERVICE( client_name IN VARCHAR2, service_name IN VARCHAR2); Parameters Table 32-8 SET_CLIENT_SERVICE Procedure Parameters Parameter Description client_name Name of the client, as found in DBA_AUTOTASK_CLIENT View service_name Service name for client, may be NULL Usage Notes All work performed on behalf of the Client takes place only on instances where the service is enabled.