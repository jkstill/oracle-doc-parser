---
id: 19c__DBMS_AUTO_TASK_ADMIN.DISABLE
name: DBMS_AUTO_TASK_ADMIN.DISABLE
object_type: plsql_subprogram
oracle_version: 19c
doc_type: plsql_packages
parent: DBMS_AUTO_TASK_ADMIN
tags: [dbms_auto_task_admin]
source_file: DBMS_AUTO_TASK_ADMIN.html
---

# DBMS_AUTO_TASK_ADMIN.DISABLE

This procedure prevents AUTOTASK from executing any requests from a specified client or operation.

## Syntax

```sql
DBMS_AUTO_TASK_ADMIN.DISABLE;
```

## Parameters

| Parameter | Type | Mode | Description |
|-----------|------|------|-------------|
| client_name |  |  | Name of the client, as found in DBA_AUTOTASK_CLIENT View |
| operation |  |  | Name of the operation as specified in DBA_AUTOTASK_OPERATION View |
| window_name |  |  | Optional name of the window in which client is to be disabled |

## Usage Notes

Syntax Disables all AUTOTASK functionality. DBMS_AUTO_TASK_ADMIN.DISABLE; Disables all tasks for the client or operation. DBMS_AUTO_TASK_ADMIN.DISABLE ( client_name IN VARCHAR2, operation IN VARCHAR2, window_name IN VARCHAR2); Parameters Table 32-3 DISABLE Procedure Parameters Parameter Description client_name Name of the client, as found in DBA_AUTOTASK_CLIENT View operation Name of the operation as specified in DBA_AUTOTASK_OPERATION View window_name Optional name of the window in which client is to be disabled Usage Notes If operation and window_name are both NULL , the client is disabled. If operation is not NULL , window_name is ignored and the operation is disabled If operation is NULL and window_name is not NULL , the client is disabled in the specified window.